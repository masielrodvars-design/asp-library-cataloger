from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class MetadataRecord:
    """
    Represents authoritative metadata about a book retrieved from an
    external metadata provider.
    """

    isbn: Optional[str] = None
    isbn13: Optional[str] = None

    title: Optional[str] = None
    subtitle: Optional[str] = None

    authors: List[str] = field(default_factory=list)

    publisher: Optional[str] = None
    publication_year: Optional[int] = None

    language: Optional[str] = None

    page_count: Optional[int] = None

    description: Optional[str] = None

    subjects: List[str] = field(default_factory=list)

    audience: Optional[str] = None

    cover_image_url: Optional[str] = None

    source: Optional[str] = None

    confidence: float = 1.0