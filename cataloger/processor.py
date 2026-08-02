from pathlib import Path

from cataloger.analysis.quality import print_quality_report
from cataloger.excel.reader import load_books
from cataloger.excel.writer import ExcelWriter
from cataloger.intelligence.engine import IntelligenceEngine
from cataloger.metadata.engine import MetadataEngine


class CatalogProcessor:

    def __init__(self):
        self.metadata_engine = MetadataEngine()
        self.intelligence_engine = IntelligenceEngine()
        self.writer = ExcelWriter(
            "sample_data/ASP Library Catalog Project.xlsx"
        )

    def run(self):
        books = self.load_books()

        if not books:
            print("No books found.")
            return

        self.writer.write_headers()

        for row, book in enumerate(books[:10], start=2):

            metadata = self.metadata_engine.lookup(book.isbn)

            recommendation = self.intelligence_engine.analyze(
                book,
                metadata,
            )

            self.writer.write_recommendation(
                row,
                recommendation,
            )

            print()
            print(f"{row - 1}. {book.title}")
            print(
                f"Suggested collection: "
                f"{recommendation.collection_code}"
            )

    def load_books(self):
        books = load_books(
            Path("sample_data/ASP Library Catalog Project.xlsx")
        )

        print_quality_report(books)

        print(f"Loaded {len(books)} books.")

        return books