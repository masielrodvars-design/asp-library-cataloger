"""
Fake enrichment service.

This implementation allows us to build and test the
Living Library without connecting to any AI service.
"""

from cataloger.enrichment.base import EnrichmentService


class FakeEnrichmentService(EnrichmentService):

    def generate_summary(self, book, metadata):

        if metadata and metadata.description:
            return metadata.description

        return "No summary available."

    def generate_themes(self, book, metadata):

        text = ""

        if metadata:

            if metadata.title:
                text += metadata.title + " "

            if metadata.description:
                text += metadata.description

        text = text.lower()

        themes = []

        if "friend" in text:
            themes.append("Friendship")

        if "family" in text:
            themes.append("Family")

        if "dog" in text or "cat" in text:
            themes.append("Animals")

        if not themes:
            themes.append("General")

        return themes