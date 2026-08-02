"""
AI Summary Generator

Generates a short, reader-friendly summary for a book.
"""


class SummaryGenerator:

    def generate(self, book, metadata):
        """
        Return a short summary.

        Placeholder implementation.
        """

        if metadata and metadata.description:
            return metadata.description

        return "No summary available."