from cataloger.models.book import Book


def print_quality_report(books: list[Book]) -> None:

    total = len(books)

    missing_isbn = sum(1 for b in books if not b.isbn)
    missing_author = sum(1 for b in books if not b.author)
    missing_collection = sum(1 for b in books if not b.collection)
    missing_call_number = sum(1 for b in books if not b.call_number)
    missing_language = sum(1 for b in books if not b.language)

    print()
    print("=" * 60)
    print("ASP Library Catalog Data Quality Report")
    print("=" * 60)

    print(f"Books:                 {total}")
    print(f"Missing ISBN:          {missing_isbn}")
    print(f"Missing Author:        {missing_author}")
    print(f"Missing Collection:    {missing_collection}")
    print(f"Missing Call Number:   {missing_call_number}")
    print(f"Missing Language:      {missing_language}")