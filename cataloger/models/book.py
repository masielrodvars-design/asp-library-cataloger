from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
    """Represents a single book in the catalog."""

    book_id: Optional[str] = None

    title: str = ""
    author: str = ""
    additional_authors: str = ""

    isbn: str = ""
    isbn13: str = ""

    publisher: str = ""

    year_published: Optional[int] = None
    original_publication_year: Optional[int] = None

    language: str = ""

    fiction_type: str = ""

    collection: str = ""
    call_number: str = ""

    genre: str = ""

    review_status: str = "Not Started"