from tt_gutenberg.data import load_authors, load_metadata, load_languages
import pandas as pd


def get_data():
    authors = load_authors()
    metadata = load_metadata()
    languages = load_languages()
    books = pd.merge(authors, metadata, on='gutenberg_author_id')
    full = pd.merge(books, languages, on='gutenberg_id')
    return full