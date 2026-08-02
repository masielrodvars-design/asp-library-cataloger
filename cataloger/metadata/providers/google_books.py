import requests

from cataloger.metadata.metadata_record import MetadataRecord
from cataloger.metadata.providers.base import MetadataProvider


class GoogleBooksProvider(MetadataProvider):
    """
    Retrieves metadata from the Google Books API.
    """

    BASE_URL = "https://www.googleapis.com/books/v1/volumes"

    def lookup(self, isbn: str) -> MetadataRecord:

        response = requests.get(
            self.BASE_URL,
            params={
                "q": f"isbn:{isbn}",
            },
            timeout=10,
        )

        try:
            response.raise_for_status()
        except requests.HTTPError:
            return MetadataRecord(
                isbn=isbn,
                source="Google Books",
                confidence=0.0,
            )

        data = response.json()

        if data.get("totalItems", 0) == 0:
            return MetadataRecord(
                isbn=isbn,
                source="Google Books",
                confidence=0.0,
            )

        book = data["items"][0]["volumeInfo"]

        print(book)

        return MetadataRecord(
            isbn=isbn,
            source="Google Books",
            confidence=0.0,
        )  