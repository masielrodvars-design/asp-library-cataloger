import requests

from cataloger.metadata.metadata_record import MetadataRecord
from cataloger.metadata.providers.base import MetadataProvider


class OpenLibraryProvider(MetadataProvider):
    """
    Retrieves book metadata from the Open Library Books API.
    """

    BASE_URL = "https://openlibrary.org/api/books"

    def lookup(self, isbn: str) -> MetadataRecord:
        params = {
            "bibkeys": f"ISBN:{isbn}",
            "format": "json",
            "jscmd": "data",
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        key = f"ISBN:{isbn}"

        if key not in data:
            return MetadataRecord(
                isbn=isbn,
                source="Open Library",
                confidence=0.0,
            )

        book = data[key]

        subjects = [
             subject["name"]
             for subject in book.get("subjects", [])
         ]

        description = book.get("description")

        if isinstance(description, dict):
             description = description.get("value")


        return MetadataRecord(
            isbn=isbn,
            title=book.get("title"),
            subtitle=book.get("subtitle"),
            authors=[
                author.get("name")
                for author in book.get("authors", [])
                if author.get("name")
            ],
            publisher=(
                book.get("publishers", [{}])[0].get("name")
                if book.get("publishers")
                else None
            ),
            publication_year=(
                int(book["publish_date"][-4:])
                if book.get("publish_date")
                and book["publish_date"][-4:].isdigit()
                else None
            ),
            page_count=book.get("number_of_pages"),

            subjects=subjects,
            description=description,

            cover_image_url=(
                book.get("cover", {}).get("large")
                or book.get("cover", {}).get("medium")
                or book.get("cover", {}).get("small")
            ),
            source="Open Library",
        )