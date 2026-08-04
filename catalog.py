from pathlib import Path

from cataloger.excel.reader import load_books
from cataloger.analysis.quality import print_quality_report
from cataloger.metadata.engine import MetadataEngine
from cataloger.intelligence.engine import IntelligenceEngine
from cataloger.excel.writer import ExcelWriter

from cataloger.story.builder import BookStoryBuilder
from cataloger.story.formatter import StoryFormatter
from cataloger.processor import CatalogProcessor

def main():
    # Load books from Excel
    books = load_books(Path("sample_data/ASP Library Catalog Project.xlsx"))

    # Print quality report
    print_quality_report(books)

    metadata_engine = MetadataEngine()
    intelligence_engine = IntelligenceEngine()
    story_builder = BookStoryBuilder()
    story_formatter = StoryFormatter()
    writer = ExcelWriter("sample_data/ASP Library Catalog Project.xlsx")
    writer.write_headers()


    # Show first 10 books while developing
    for row, book in enumerate(books[:10], start=2):

        print()
        print("=" * 60)
        print(f"Catalog Title : {book.title}")
        print(f"ISBN          : {book.isbn}")

        metadata = metadata_engine.lookup(book.isbn)

        profile = intelligence_engine.build_book_profile(
            book,
            metadata,
        )

        recommendation = intelligence_engine.analyze(
            book,
            metadata,
        )

        writer.write_recommendation(
            row,
            recommendation,
        )

        print(f"Open Library  : {metadata.title}")
        print(f"Language      : {metadata.language}")
        print(f"Format        : {recommendation.format}")
        print(f"Audience      : {recommendation.audience}")
        print(f"Needs Review  : {recommendation.needs_review}")
        print(f"Subjects      : {metadata.subjects}")
        print(f"Authors       : {', '.join(metadata.authors)}")
        print("*** INTELLIGENCE ENGINE RAN ***")

        story = story_builder.build(profile)
        print()
        print(story_formatter.format(story))

        print(
            f"Suggested Collection : "
            f"{recommendation.collection_code} - "
            f"{recommendation.collection_name}"
         )

        print(f"Confidence           : {recommendation.confidence:.0%}")

        if recommendation.reasons:
            for reason in recommendation.reasons:
                print(f"Reason               : {reason}")

    writer.save("sample_data/ASP Library Catalog Project AI.xlsx")

    print("\nAI catalog saved successfully!")
        
if __name__ == "__main__":
    main()