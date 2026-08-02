from abc import ABC, abstractmethod

from cataloger.metadata.metadata_record import MetadataRecord


class MetadataProvider(ABC):
    """
    Base class for all metadata providers.
    """

    @abstractmethod
    def lookup(self, isbn: str) -> MetadataRecord:
        """
        Look up metadata for a book by ISBN.

        Returns a MetadataRecord.
        """
        pass