from cataloger.models.book_profile import BookProfile
from cataloger.story.builder import BookStoryBuilder
from cataloger.story.formatter import StoryFormatter


profile = BookProfile()

profile.title = "The Dot"
profile.author = "Peter H. Reynolds"

profile.summary = (
    "A young girl discovers that creativity begins "
    "with the courage to make a single mark."
)

profile.why_this_book_matters = (
    "The Dot encourages readers to believe in themselves, "
    "embrace mistakes, and discover that confidence grows through trying."
)

profile.themes = [
    "Creativity",
    "Confidence",
    "Courage",
]

profile.subjects = [
    "Art",
    "School",
]

profile.great_for = [
    "Read Aloud",
    "Growth Mindset",
]

profile.curated_collections = [
    "Dream Big",
    "Books That Build Confidence",
]

profile.conversation_starter = (
    "Have you ever surprised yourself by trying something new?"
)

profile.library_tip = (
    "Look for other Peter H. Reynolds books nearby."
)

builder = BookStoryBuilder()

story = builder.build(profile)

formatter = StoryFormatter()

print(formatter.format(story))