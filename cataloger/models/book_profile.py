from dataclasses import dataclass, field


@dataclass
class BookProfile:
    """
    Complete Living Library knowledge record for a single book.
    This model powers every reader experience.
    """

    #
    # Identity
    #

    title: str = ""
    author: str = ""
    isbn: str = ""
    summary: str = ""

    #
    # Library
    #

    collection: str = ""
    call_number: str = ""
    language: str = ""

    #
    # Discovery
    #

    subjects: list[str] = field(default_factory=list)
    themes: list[str] = field(default_factory=list)

    genre: list[str] = field(default_factory=list)

    curated_collections: list[str] = field(default_factory=list)

    great_for: list[str] = field(default_factory=list)

    instructional_supports: list[str] = field(default_factory=list)

    representation: list[str] = field(default_factory=list)

    #
    # Reader Experience
    #

    why_this_book_matters: str = ""

    conversation_starter: str = ""

    library_tip: str = ""

    #
    # Community

    community_notes: list[str] = field(default_factory=list)

    #
    # Accessibility

    available_languages: list[str] = field(default_factory=list)

    reading_levels: list[str] = field(default_factory=list)

    #
    # Tutor Mode

    tutor_prompts: list[str] = field(default_factory=list)

    extension_activities: list[str] = field(default_factory=list)

    vocabulary: list[str] = field(default_factory=list)

    related_books: list[str] = field(default_factory=list)

    #
    # AI

    confidence: float = 0.0