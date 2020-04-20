from limecore.cli import App as CLIApp, AppFactory
from limecore.core.cli import ArgumentParser
from limecore.core.configuration import Module as ConfigurationModule
from limecore.core.di import LimecoreApplication
from limecore.logging import Module as LoggingModule
from limecore.messaging.rabbitmq import Module as RabbitMQModule
from pathlib import Path

from . import commands


app_factory = AppFactory().add(commands)
arg_parser = app_factory.create_argument_parser(ArgumentParser())
args = arg_parser.parse_args()

LimecoreApplication(Path("."), args).using(ConfigurationModule("example")).using(
    LoggingModule()
).using(RabbitMQModule()).using(app_factory).run(CLIApp)
