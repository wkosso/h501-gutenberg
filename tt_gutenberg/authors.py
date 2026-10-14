
import pandas as pd
from tt_gutenberg.data import load_authors, load_metadata, load_languages
from tt_gutenberg.transform import get_data


def list_authors(by_languages=True, alias=True):
    # Load the three tables
    authors = load_authors()
    metadata = load_metadata()
    languages = load_languages()

    full = get_data()

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