from cataloger.models import book
from cataloger.models.recommendation import Recommendation


def detect_language(book, metadata, recommendation: Recommendation):
    """
    Detect the book's language.
    """

    title = f"{book.title} {metadata.title or ''}".lower()

    spanish_indicators = [
    "spanish",
    "spanish edition",
    "(spanish)",
    "en español",
    "español",
     ]

    is_spanish = any(
    indicator in title
    for indicator in spanish_indicators
     )

    if is_spanish:
        recommendation.language = "Spanish"
        recommendation.collection_code = "SP"
        recommendation.collection_name = "Spanish (Needs Classification)"
        recommendation.reasons.append(
            "Spanish language indicators found."
        )
    else:
        recommendation.language = "English"
        recommendation.collection_code = "EN"
        recommendation.collection_name = "English (Needs Classification)"
        recommendation.reasons.append(
            "No Spanish language indicators found."
        )

def detect_format(book, metadata, recommendation):
    """
    Detect the book's physical format.
    """

    subjects = [s.lower() for s in metadata.subjects]

    title = f"{book.title} {metadata.title or ''}".lower()

    #
    # Graphic Novel
    #

    graphic_subjects = [
        "graphic novels",
        "comic books",
        "comics",
        "manga",
    ]

    if any(s in subjects for s in graphic_subjects):
        recommendation.format = "Graphic Novel"
        recommendation.reasons.append(
            "Graphic Novel subjects detected."
        )
        return

    #
    # Early Reader
    #

    early_reader_subjects = [
        "readers (primary)",
        "phonetic method",
        "easy readers",
        "beginning readers",
    ]

    if any(s in subjects for s in early_reader_subjects):
        recommendation.format = "Early Reader"
        recommendation.reasons.append(
            "Early Reader subjects detected."
        )
        return

    #
    # Picture Book
    #

    picture_subjects = [
        "picture books",
        "board books",
        "stories in rhyme",
    ]

    if any(s in subjects for s in picture_subjects):
        recommendation.format = "Picture Book"
        recommendation.reasons.append(
            "Picture Book subjects detected."
        )
        return

    #
    # Unknown until we have enough evidence
    #

    recommendation.format = "Unknown"

    recommendation.reasons.append(
         "Format could not be determined."
     )

def detect_genre(book, metadata, recommendation):
    """
    Detect whether the book is fiction or nonfiction.
    """

    subjects = [s.lower() for s in metadata.subjects]

    nonfiction_keywords = [
        "biography",
        "history",
        "science",
        "animals",
        "nature",
        "geography",
        "reference",
        "encyclopedias",
    ]

    if any(keyword in " ".join(subjects) for keyword in nonfiction_keywords):
        recommendation.genre = "Nonfiction"
        recommendation.reasons.append("Nonfiction subjects detected.")
    else:
        recommendation.genre = "Fiction"

def detect_audience(book, metadata, recommendation):
    """
    Determine shelving audience based on format.
    """

    if recommendation.format == "Early Reader":
        recommendation.audience = "ER"
        return

    if recommendation.format == "Picture Book":
        recommendation.audience = "E"
        return

    recommendation.audience = ""


def recommend_collection(book, metadata, recommendation):

    detect_language(book, metadata, recommendation)
    detect_format(book, metadata, recommendation)
    detect_genre(book, metadata, recommendation)
    detect_audience(book, metadata, recommendation)

    #
    # Collection Assignment
    #

    if recommendation.language == "Spanish":

        if recommendation.audience == "ER":
            recommendation.collection_code = "SP ER"
            recommendation.collection_name = "Spanish Early Readers"

        elif recommendation.audience == "E":
            recommendation.collection_code = "SP E"
            recommendation.collection_name = "Spanish Picture Books"

        else:
            recommendation.collection_code = "SP J"
            recommendation.collection_name = "Spanish Juvenile"

    else:

        if recommendation.audience == "ER":
            recommendation.collection_code = "ER"
            recommendation.collection_name = "Early Readers"

        elif recommendation.audience == "E":
            recommendation.collection_code = "E"
            recommendation.collection_name = "Picture Books"

        else:
            recommendation.collection_code = "REVIEW"
            recommendation.collection_name = "Needs Manual Review"

            recommendation.needs_review = True

            recommendation.reasons.append(
                "Insufficient information to assign a collection."
            )

    #
    # Confidence
    #
    # 
    if recommendation.needs_review:
        recommendation.confidence = 0.0

    elif recommendation.audience == "ER":
          recommendation.confidence = 0.95

    else:
         recommendation.confidence = 0.80