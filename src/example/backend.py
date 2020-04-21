from argparse import ArgumentParser
from limecore.core.configuration import Module as ConfigurationModule
from limecore.core.di import LimecoreApplication
from limecore.database.postgresql import Module as PostgreSQLModule
from limecore.logging import Module as LoggingModule
from limecore.messaging.api import App, AppFactory
from limecore.messaging.rabbitmq import Module as RabbitMQModule
from pathlib import Path

from .handlers import commands

app_factory = AppFactory().add(commands)
arg_parser = app_factory.create_argument_parser(ArgumentParser())
args = arg_parser.parse_args()


LimecoreApplication(Path("."), None)\
    .using(ConfigurationModule("example", enable_commandline_arguments=False))\
    .using(LoggingModule())\
    .using(PostgreSQLModule())\
    .using(RabbitMQModule())\
    .using(app_factory)\
    .run(App)
