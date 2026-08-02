from cataloger.ai.summary_generator import SummaryGenerator
from cataloger.intelligence import rules
from cataloger.models.book_profile import BookProfile
from cataloger.models.recommendation import Recommendation


class IntelligenceEngine:

    def __init__(self):
        self.summary_generator = SummaryGenerator()

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
        Build a Living Library BookProfile from a book and its metadata.
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
        # Summary
        #

        profile.summary = self.summary_generator.generate(
            book,
            metadata,
        )

        #
        # Library
        #

        profile.collection = recommendation.collection_code

        #
        # Future AI fields
        #

        # profile.call_number = ...
        # profile.language = ...
        # profile.subjects = ...
        # profile.themes = ...
        # profile.instructional_supports = ...
        # profile.representation = ...
        # profile.community_notes = ...

        return profile