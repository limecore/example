from limecore.messaging.api import Message


class TodoAdded(Message):
    routing_key = "example.ee.todo_added"

    def __init__(self, title: str, **kwargs):
        super().__init__(title=title, **kwargs)

    @property
    def title(self):
        return self._body["title"]
