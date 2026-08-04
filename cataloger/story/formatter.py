class StoryFormatter:

    def format(self, story: dict) -> str:

        lines = []

        lines.append("=" * 60)
        lines.append(story["title"])
        lines.append("=" * 60)

        if story["author"]:
            lines.append(f"Author: {story['author']}")

        lines.append("")

        lines.append("WHY THIS BOOK MATTERS")
        lines.append("---------------------")
        lines.append(story["why_this_book_matters"])
        lines.append("")

        if story["summary"]:
            lines.append("SUMMARY")
            lines.append("-------")
            lines.append(story["summary"])
            lines.append("")

        if story["themes"]:
            lines.append("THEMES")
            lines.append("------")
            for item in story["themes"]:
                lines.append(f"• {item}")
            lines.append("")

        if story["subjects"]:
            lines.append("SUBJECTS")
            lines.append("--------")
            for item in story["subjects"]:
                lines.append(f"• {item}")
            lines.append("")

        if story["great_for"]:
            lines.append("GREAT FOR")
            lines.append("---------")
            for item in story["great_for"]:
                lines.append(f"• {item}")
            lines.append("")

        if story["curated_collections"]:
            lines.append("CURATED COLLECTIONS")
            lines.append("-------------------")
            for item in story["curated_collections"]:
                lines.append(f"• {item}")
            lines.append("")

        lines.append("CONVERSATION STARTER")
        lines.append("--------------------")
        lines.append(story["conversation_starter"])
        lines.append("")

        lines.append("LIBRARY TIP")
        lines.append("-----------")
        lines.append(story["library_tip"])
        lines.append("")

        return "\n".join(lines)