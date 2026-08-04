from cataloger.models.book_profile import BookProfile


class BookStoryBuilder:
    """
    Converts a BookProfile into a Living Library Story.
    """

    def build(self, profile: BookProfile) -> dict:

        return {
            "title": profile.title,
            "author": profile.author,
            "summary": profile.summary,
            "why_this_book_matters": profile.why_this_book_matters,
            "themes": profile.themes,
            "subjects": profile.subjects,
            "collection": profile.collection,
            "conversation_starter": profile.conversation_starter,
            "library_tip": profile.library_tip,
            "great_for": profile.great_for,
            "curated_collections": profile.curated_collections,
        }