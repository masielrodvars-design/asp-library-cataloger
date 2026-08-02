from dataclasses import dataclass, field


@dataclass
class BookProfile:
    """
    The complete Living Library profile for a single book.
    """

    # Identity
    title: str = ""
    author: str = ""
    isbn: str = ""
    summary: str = ""

    # Library
    collection: str = ""
    call_number: str = ""
    language: str = ""

    # Discovery
    subjects: list[str] = field(default_factory=list)
    themes: list[str] = field(default_factory=list)
    instructional_supports: list[str] = field(default_factory=list)
    representation: list[str] = field(default_factory=list)

    # Community
    community_notes: list[str] = field(default_factory=list)

    # AI
    confidence: float = 0.0