from cataloger.enrichment import FakeEnrichmentService
from cataloger.intelligence import rules
from cataloger.models.book_profile import BookProfile
from cataloger.models.recommendation import Recommendation


class IntelligenceEngine:

    def __init__(self):
        self.enrichment = FakeEnrichmentService()

    def analyze(self, book, metadata):

        recommendation = Recommendation()

        rules.recommend_collection(
            book,
            metadata,
            recommendation,
        )

        return recommendation

    def build_book_profile(self, book, metadata):

        recommendation = self.analyze(book, metadata)

        profile = BookProfile()

        #
        # Identity
        #

        profile.title = book.title
        profile.author = book.author
        profile.isbn = book.isbn

        #
        # AI Enrichment
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

        #
        # Reader Experience
        #

        profile.why_this_book_matters = (
            "This book helps readers discover meaningful ideas and experiences."
        )

        profile.conversation_starter = (
            "What part of this story stayed with you the most?"
        )

        profile.library_tip = (
            "Look for books nearby to discover similar stories."
        )

        #
        # Accessibility
        #

        profile.available_languages = [
            "English"
        ]

        profile.reading_levels = [
            "Independent Reader"
        ]

        #
        # Tutor Mode
        #

        profile.tutor_prompts = [
            "Ask the reader why they think this story matters."
        ]

        return profile