from cataloger.metadata.metadata_record import MetadataRecord
from cataloger.metadata.providers.open_library import OpenLibraryProvider
from cataloger.metadata.providers.google_books import GoogleBooksProvider
from cataloger.storage.metadata_cache import MetadataCache


class MetadataEngine:

    def __init__(self):
        self.providers = [
            OpenLibraryProvider(),
            GoogleBooksProvider(),
        ]

        self.cache = MetadataCache()

    def lookup(self, isbn):
        isbn = (isbn or "").strip()

        if not isbn:
            return MetadataRecord(
                isbn="",
                source="No ISBN",
                confidence=0.0,
            )

        # We'll turn this back on later
        # cached = self.cache.get(isbn)
        # if cached:
        #     print(f"Cache hit: {isbn}")
        #     return cached

        print(f"Fetching: {isbn}")

        for provider in self.providers:

            metadata = provider.lookup(isbn)

            if metadata.title:
                self.cache.save(metadata)
                return metadata

        return MetadataRecord(
            isbn=isbn,
            source="No Metadata Found",
            confidence=0.0,
        )