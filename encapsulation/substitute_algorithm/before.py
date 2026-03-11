class TagAnalyticsBefore:
    def normalize_tags(self, tags: list[str]) -> list[str]:
        normalized = []

        for tag in tags:
            value = tag.strip().lower()
            if value == "":
                continue

            exists = False
            for current in normalized:
                if current == value:
                    exists = True
                    break

            if not exists:
                normalized.append(value)

        return normalized

    def top_tag(self, tags: list[str]) -> str | None:
        normalized = self.normalize_tags(tags)
        if not normalized:
            return None

        best_tag = normalized[0]
        best_count = 0

        for candidate in normalized:
            count = 0
            for original in tags:
                value = original.strip().lower()
                if value == candidate:
                    count += 1

            if count > best_count:
                best_count = count
                best_tag = candidate
            elif count == best_count and candidate < best_tag:
                best_tag = candidate

        return best_tag

    def summary(self, tags: list[str]) -> str:
        normalized = self.normalize_tags(tags)
        top = self.top_tag(tags)

        if top is None:
            return "Tags: 0 | Top: none"

        return f"Tags: {len(normalized)} | Top: {top}"
