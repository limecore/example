from injector import inject
from limecore.database.api import Database
from limecore.messaging.api import Handler, Publisher

from example.governance import commands, enterprise_events


class AddTodo(Handler):
    handles = [commands.AddTodo]
    queue = "example.command.add_todo"

    @inject
    def __init__(self, database: Database, publisher: Publisher):
        self._database = database
        self._publisher = publisher

    def handle_message(self, msg: commands.AddTodo):
        with self._database as d:
            d.execute(
                "insert into todo (id, title) values (%s, %s)",
                msg.message_id,
                msg.title,
            )

            d.commit()

        with self._publisher as publisher:
            publisher.publish(
                enterprise_events.TodoAdded.obtain(title=msg.title), mandatory=True
            )
