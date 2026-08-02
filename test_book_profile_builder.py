from pathlib import Path

from cataloger.excel.reader import load_books
from cataloger.intelligence.engine import IntelligenceEngine
from cataloger.metadata.engine import MetadataEngine


def main():
    books = load_books(
        Path("sample_data/ASP Library Catalog Project.xlsx")
    )

    book = books[0]

    metadata_engine = MetadataEngine()
    metadata = metadata_engine.lookup(book.isbn)

    engine = IntelligenceEngine()

    profile = engine.build_book_profile(
        book,
        metadata,
    )

    print()
    print(profile)


if __name__ == "__main__":
    main()