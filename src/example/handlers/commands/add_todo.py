from injector import inject
from limecore.messaging.api import Handler, Publisher

from example.governance import commands, enterprise_events


class AddTodo(Handler):
    handles = [commands.AddTodo]
    queue = "example.command.add_todo"

    @inject
    def __init__(self, publisher: Publisher):
        self._publisher = publisher

    def handle_message(self, msg: commands.AddTodo):
        with self._publisher as publisher:
            publisher.publish(
                enterprise_events.TodoAdded.obtain(title=msg.title), mandatory=True
            )
