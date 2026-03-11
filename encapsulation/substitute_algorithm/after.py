class TagAnalyticsAfter:
    def format_tags(self, tags: list[str]):
        return [tag.strip().lower() for tag in tags if tag.strip().lower()]

    def normalize_tags(self, tags: list[str]) -> list[str]:
        return list(dict.fromkeys(self.format_tags(tags)))

    def top_tag(self, tags: list[str]) -> str | None:
        normalized = self.normalize_tags(tags)
        if not normalized:
            return None

        best_tag = normalized[0]
        best_count = 0

        tags_formatted = self.format_tags(tags)
        for candidate in normalized:
            count = tags_formatted.count(candidate)
            if count > best_count or (count == best_count and candidate < best_tag):
                best_count = count
                best_tag = candidate

        return best_tag

    def summary(self, tags: list[str]) -> str:
        normalized = self.normalize_tags(tags)
        if not normalized:
            return "Tags: 0 | Top: none"
        top = self.top_tag(tags)

        return f"Tags: {len(normalized)} | Top: {top}"
