from cataloger.enrichment import FakeEnrichmentService
from cataloger.intelligence import rules
from cataloger.models.book_profile import BookProfile
from cataloger.models.recommendation import Recommendation


class IntelligenceEngine:

    def __init__(self):
        self.enrichment = FakeEnrichmentService()

    def analyze(self, book, metadata):
        """
        Analyze a catalog record and return recommendations.
        """

        recommendation = Recommendation()

        rules.recommend_collection(
            book,
            metadata,
            recommendation,
        )

        return recommendation

    def build_book_profile(self, book, metadata):
        """
        Build a Living Library BookProfile.
        """

        recommendation = self.analyze(
            book,
            metadata,
        )

        profile = BookProfile()

        #
        # Identity
        #

        profile.title = book.title
        profile.author = book.author
        profile.isbn = book.isbn

        #
        # Enrichment
        #

        profile.summary = self.enrichment.generate_summary(
            book,
            metadata,
        )

        profile.themes = self.enrichment.generate_themes(
            book,
            metadata,
        )

        #
        # Library
        #

        profile.collection = recommendation.collection_code

        return profile