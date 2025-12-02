"""Task 4 — Movie Reviews Data Cleaning

Produces `movie_reviews_cleaned.csv` and a before-vs-after summary report.

Steps:
- Standardize text: lowercase and remove HTML tags
- Tokenize and offer TF-IDF encoding (uses sklearn's TfidfVectorizer)
- Handle missing ratings by filling with median
- Normalize ratings from 0-10 to 0-1
- Save cleaned CSV and a small summary report

Run:
    python task4.py

This script also exposes small helper functions used by tests.
"""

import os
import re
import pandas as pd
import numpy as np
from typing import Tuple

# TF-IDF import (use dynamic import to avoid static analyzer errors if sklearn is not installed)
import importlib
try:
    _sklearn_text = importlib.import_module('sklearn.feature_extraction.text')
    TfidfVectorizer = getattr(_sklearn_text, 'TfidfVectorizer', None)
except (ImportError, AttributeError):
    TfidfVectorizer = None

INPUT = 'movie_reviews-1.csv'
OUTPUT = 'movie_reviews_cleaned.csv'
TFIDF_OUTPUT = 'movie_reviews_tfidf.npz'  # optional save (if sklearn available)
REPORT = 'movie_reviews_report.txt'

# ---------------------- Helpers ----------------------

def remove_html_tags(text: str) -> str:
    if pd.isna(text):
        return text
    return re.sub(r'<[^>]+>', '', str(text))

def standardize_text(text: str) -> str:
    """Lowercase and remove HTML tags and extra whitespace."""
    if pd.isna(text):
        return ''
    t = remove_html_tags(text)
    t = t.lower()
    t = re.sub(r"[^\w\s']", '', t)  # remove punctuation but keep apostrophes
    t = ' '.join(t.split())
    return t

# ---------------------- Main processing ----------------------

if __name__ == '__main__':
    if not os.path.exists(INPUT):
        raise FileNotFoundError(f"Input file '{INPUT}' not found.")

    df = pd.read_csv(INPUT)

    # Save pre-clean summary
    pre_shape = df.shape
    pre_missing_ratings = df['rating'].isnull().sum()

    # Standardize text
    df['review_text_raw'] = df['review_text']
    df['review_text'] = df['review_text'].apply(standardize_text)

    # Handle missing ratings: fill with median
    median_rating = df['rating'].median()
    df['rating_filled'] = df['rating'].fillna(median_rating)

    # Normalize ratings 0-10 to 0-1
    df['rating_normalized'] = df['rating_filled'] / 10.0

    # Tokenization / TF-IDF
    # If sklearn is available, compute TF-IDF matrix; otherwise, create placeholder
    tfidf_status = 'sklearn_not_available'
    tfidf_shape = None
    if TfidfVectorizer is not None:
        vect = TfidfVectorizer(ngram_range=(1,2), max_features=100)
        tfidf = vect.fit_transform(df['review_text'].fillna(''))
        tfidf_status = 'ok'
        tfidf_shape = tfidf.shape
        # optional save (requires scipy.sparse save) — skip to keep dependencies minimal
    else:
        vect = None

    # Prepare final dataframe
    cleaned = df[['review_id', 'review_text', 'review_text_raw', 'rating', 'rating_filled', 'rating_normalized']].copy()
    cleaned.to_csv(OUTPUT, index=False)

    # Build a small before-vs-after summary
    with open(REPORT, 'w', encoding='utf-8') as f:
        f.write('Movie Reviews Cleaning Report\n')
        f.write('=================================\n')
        f.write(f'Input file: {INPUT}\n')
        f.write(f'Output file: {OUTPUT}\n')
        f.write('\n-- Data Summary BEFORE --\n')
        f.write(f'Shape: {pre_shape}\n')
        f.write(f'Missing ratings: {pre_missing_ratings}\n')
        f.write('\n-- Data Summary AFTER --\n')
        f.write(f'Shape: {cleaned.shape}\n')
        f.write(f'Missing ratings filled with median: {median_rating}\n')
        f.write(f'TF-IDF status: {tfidf_status}\n')
        if tfidf_shape:
            f.write(f'TF-IDF matrix shape: {tfidf_shape}\n')

    print('Saved cleaned data to', OUTPUT)
    print('Saved report to', REPORT)
    if tfidf_shape:
        print('TF-IDF computed. Matrix shape:', tfidf_shape)
    else:
        print('TF-IDF not computed (sklearn not available).')

# Expose functions for tests
__all__ = ['standardize_text', 'remove_html_tags']
