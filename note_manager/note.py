
from datetime import datetime


class Note:
    def __init__(self, title, content, tags=None, timestamp=None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []
        self.timestamp = timestamp or datetime.now().isoformat()

    def save(self):
        return {
            "title": self.title,
            "content": self.content,
            "tags": self.tags,
            "timestamp": self.timestamp
        }

    def display(self):
        print(f"Title: {self.title}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Tags: {', '.join(self.tags)}")
        print(f"Content: {self.content}")
        print("-" * 27)

    def matches_search(self, term):
        term = term.lower()

        return (
            term in self.title.lower()
            or term in self.content.lower()
            or any(term in tag.lower() for tag in self.tags)
        )
