import pandas as pd
import numpy as np
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import warnings
warnings.filterwarnings('ignore')

# Download required NLTK data
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Load the data
df = pd.read_csv('social_media.csv')

print("=" * 80)
print("SOCIAL MEDIA DATA CLEANING PROCESS")
print("=" * 80)

print("\n1. INITIAL DATA OVERVIEW")
print("-" * 80)
print(f"Dataset shape: {df.shape}")
print(f"\nFirst few rows:\n{df.head()}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nMissing values:\n{df.isnull().sum()}")

# ============================================================================
# STEP 1: Remove HTML tags and special characters from post_text
# ============================================================================
print("\n2. REMOVING HTML TAGS AND CLEANING TEXT")
print("-" * 80)

def clean_text(text):
    """
    Remove HTML tags, punctuation, and special symbols from text
    """
    if pd.isna(text):
        return text
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove special symbols but keep # for hashtags initially
    text = re.sub(r'[^a-zA-Z0-9\s#]', '', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text.lower()

df['post_text_cleaned'] = df['post_text'].apply(clean_text)
print(f"Text cleaned. Sample:\n{df[['post_text', 'post_text_cleaned']].head()}")

# ============================================================================
# STEP 2: Remove stopwords and extract hashtags
# ============================================================================
print("\n3. REMOVING STOPWORDS AND EXTRACTING HASHTAGS")
print("-" * 80)

stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    """Remove stopwords from text"""
    if pd.isna(text):
        return text
    
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

def extract_hashtags(text):
    """Extract hashtags from original text"""
    if pd.isna(text):
        return ''
    
    hashtags = re.findall(r'#\w+', text)
    return ' '.join(hashtags)

df['hashtags'] = df['post_text'].apply(extract_hashtags)
df['post_text_cleaned'] = df['post_text_cleaned'].apply(remove_stopwords)

print(f"Stopwords removed. Sample:\n{df[['post_text_cleaned', 'hashtags']].head()}")

# ============================================================================
# STEP 3: Handle missing values in likes and shares
# ============================================================================
print("\n4. HANDLING MISSING VALUES")
print("-" * 80)

print(f"Missing values before imputation:\n{df[['likes', 'shares']].isnull().sum()}")

# Fill missing values with median
df['likes'].fillna(df['likes'].median(), inplace=True)
df['shares'].fillna(df['shares'].median(), inplace=True)

print(f"\nMissing values after imputation:\n{df[['likes', 'shares']].isnull().sum()}")
print(f"Likes filled with median: {df['likes'].median()}")
print(f"Shares filled with median: {df['shares'].median()}")

# ============================================================================
# STEP 4: Convert timestamp to datetime and extract features
# ============================================================================
print("\n5. CONVERTING TIMESTAMP AND EXTRACTING DATETIME FEATURES")
print("-" * 80)

df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['weekday'] = df['timestamp'].dt.day_name()
df['date'] = df['timestamp'].dt.date
df['day_of_week'] = df['timestamp'].dt.dayofweek  # 0=Monday, 6=Sunday

print(f"Timestamp converted. Sample:\n{df[['timestamp', 'hour', 'weekday', 'date']].head()}")

# ============================================================================
# STEP 5: Detect and remove duplicate posts
# ============================================================================
print("\n6. DETECTING AND REMOVING DUPLICATES")
print("-" * 80)

print(f"Total records before duplicate removal: {len(df)}")

# Identify exact duplicates based on post_text_cleaned
df_before_dedup = df.copy()
df = df.drop_duplicates(subset=['post_text_cleaned'], keep='first')

duplicates_removed = len(df_before_dedup) - len(df)
print(f"Exact duplicates removed: {duplicates_removed}")
print(f"Total records after duplicate removal: {len(df)}")

# Reset index
df = df.reset_index(drop=True)

# ============================================================================
# STEP 6: Detect spam (posts with very low engagement or suspicious patterns)
# ============================================================================
print("\n7. DETECTING AND REMOVING SPAM POSTS")
print("-" * 80)

# Consider posts as spam if:
# - Text is very short (less than 5 characters after cleaning) OR
# - Multiple consecutive punctuation marks in original text

def is_spam(row):
    """Detect spam posts based on heuristics"""
    # Check if cleaned text is too short
    if pd.notna(row['post_text_cleaned']) and len(row['post_text_cleaned']) < 5:
        return True
    
    # Check for excessive special characters in original text
    original = str(row['post_text'])
    special_count = sum(1 for c in original if c in '!@#$%^&*()')
    if special_count > 5:
        return True
    
    return False

df['is_spam'] = df.apply(is_spam, axis=1)
spam_count = df['is_spam'].sum()
print(f"Spam posts detected: {spam_count}")

# Remove spam posts
df = df[df['is_spam'] == False].reset_index(drop=True)
print(f"Records after spam removal: {len(df)}")

# ============================================================================
# STEP 7: Calculate engagement metrics
# ============================================================================
print("\n8. CALCULATING ENGAGEMENT METRICS")
print("-" * 80)

df['engagement_score'] = df['likes'] + (df['shares'] * 2)  # Shares weighted more
df['engagement_rate'] = df['shares'] / (df['likes'] + 1)  # Avoid division by zero

print(f"Engagement metrics calculated:")
print(f"Engagement score range: {df['engagement_score'].min()} - {df['engagement_score'].max()}")
print(f"Engagement rate range: {df['engagement_rate'].min():.2f} - {df['engagement_rate'].max():.2f}")

# ============================================================================
# STEP 8: Prepare final cleaned dataset
# ============================================================================
print("\n9. PREPARING FINAL CLEANED DATASET")
print("-" * 80)

# Select and reorder columns
cleaned_df = df[['post_id', 'user', 'post_text_cleaned', 'hashtags', 
                  'likes', 'shares', 'engagement_score', 'engagement_rate',
                  'timestamp', 'date', 'hour', 'weekday', 'day_of_week']]

# Rename column for clarity
cleaned_df = cleaned_df.rename(columns={'post_text_cleaned': 'post_text'})

print(f"Final dataset shape: {cleaned_df.shape}")
print(f"\nFinal cleaned data (first 10 rows):\n{cleaned_df.head(10)}")

# ============================================================================
# STEP 9: Summary statistics
# ============================================================================
print("\n10. SUMMARY STATISTICS")
print("-" * 80)
print(f"\nNumerical columns summary:\n{cleaned_df[['likes', 'shares', 'engagement_score', 'engagement_rate']].describe()}")

print(f"\nPosts by weekday:\n{cleaned_df['weekday'].value_counts()}")
print(f"\nPosts by hour distribution:\n{cleaned_df['hour'].value_counts().sort_index()}")

# ============================================================================
# STEP 10: Save cleaned dataset
# ============================================================================
output_file = 'social_media_cleaned.csv'
cleaned_df.to_csv(output_file, index=False)
print(f"\n{'=' * 80}")
print(f"Cleaned dataset saved to: {output_file}")
print(f"{'=' * 80}")

# ============================================================================
# DETAILED PROCESSING REPORT
# ============================================================================
print("\n11. DATA CLEANING SUMMARY REPORT")
print("-" * 80)
print(f"Original records: {len(df_before_dedup)}")
print(f"Duplicates removed: {duplicates_removed}")
print(f"Spam posts removed: {spam_count}")
print(f"Final records: {len(cleaned_df)}")
print(f"Retention rate: {(len(cleaned_df) / len(df_before_dedup) * 100):.2f}%")

print(f"\nMissing value handling:")
print(f"  - Likes: Filled with median ({df['likes'].median()})")
print(f"  - Shares: Filled with median ({df['shares'].median()})")

print(f"\nFeature engineering:")
print(f"  - Cleaned text (removed HTML, punctuation, stopwords)")
print(f"  - Extracted hashtags")
print(f"  - Temporal features: hour, weekday, date")
print(f"  - Engagement metrics: engagement_score, engagement_rate")

print(f"\nOutput file: {output_file}")
print(f"Output columns: {list(cleaned_df.columns)}")
print("=" * 80)
