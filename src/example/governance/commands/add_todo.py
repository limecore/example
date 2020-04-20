from limecore.messaging.api import Message


class AddTodo(Message):
    routing_key = "example.command.add_todo"

    def __init__(self, title: str, **kwargs):
        super().__init__(title=title, **kwargs)

    @property
    def title(self):
        return self._body["title"]
