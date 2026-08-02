from dataclasses import dataclass, field
from typing import List

@dataclass
class Recommendation:

    # Classification
    language: str = ""
    format: str = ""
    reading_audience: str = ""
    genre: str = ""

    # Keep these temporarily for compatibility
    fiction_type: str = ""
    audience: str = ""

    # Collection Assignment
    collection_code: str = ""
    collection_name: str = ""
    call_number: str = ""

    # Special Collections
    is_graphic: bool = False
    is_sel: bool = False

    # Discovery
    themes: List[str] = field(default_factory=list)
    format_tags: List[str] = field(default_factory=list)

    # Decision Support
    confidence: float = 0.0
    needs_review: bool = False
    notes: List[str] = field(default_factory=list)
    reasons: List[str] = field(default_factory=list)