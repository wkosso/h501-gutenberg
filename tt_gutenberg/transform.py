import pandas as pd
from tt_gutenberg.data import load_authors, load_languages, load_metadata


def list_authors(by_languages=True, alias=True):
    # Load the three tables
    authors = load_authors()
    metadata = load_metadata()
    languages = load_languages()

    # Merge authors with books (metadata) using the author ID
    books = pd.merge(authors, metadata, on='gutenberg_author_id')

    # Merge that with languages using the book ID
    full = pd.merge(books, languages, on='gutenberg_id')

    # Choose which column to rank: alias or the author name
    name_col = 'alias' if alias else 'author_x'

    if by_languages:
        # Count how many different languages each author has
        counts = full.groupby(name_col)['language_y'].nunique()
    else:
        # Otherwise count the number of rows (books) for each author
        counts = full.groupby(name_col).size()

    # Sort from most to fewest, then return just the names as a list
    return counts.sort_values(ascending=False).index.tolist()