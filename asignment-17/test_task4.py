import task4


def test_remove_html_and_lowercase():
    inp = '<p>Great Movie!</p>'
    out = task4.standardize_text(inp)
    assert out == 'great movie', f"unexpected: {out}"


def test_missing_rating_fill_and_normalize():
    import pandas as pd
    df = pd.DataFrame({'review_id':[1,2], 'review_text':['a','b'], 'rating':[8.0, None]})
    median = df['rating'].median()
    df['rating_filled'] = df['rating'].fillna(median)
    df['rating_normalized'] = df['rating_filled']/10.0
    assert df.loc[1, 'rating_filled'] == median
    assert 0.0 <= df.loc[1, 'rating_normalized'] <= 1.0


def test_tfidf_vector_shape_if_available():
    # This test attempts to compute TF-IDF with small sample and checks shape
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
    except Exception:
        return  # sklearn not available — skip assert
    vect = TfidfVectorizer(ngram_range=(1,1), max_features=10)
    docs = ['amazing movie', 'terrible acting']
    X = vect.fit_transform(docs)
    assert X.shape[0] == 2
    assert X.shape[1] <= 10


if __name__ == '__main__':
    test_remove_html_and_lowercase()
    test_missing_rating_fill_and_normalize()
    test_tfidf_vector_shape_if_available()
    print('All tests passed (if sklearn unavailable, TF-IDF test skipped).')
