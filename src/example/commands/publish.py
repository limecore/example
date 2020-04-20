import inspect

from argparse import ArgumentParser, Namespace
from injector import inject
from limecore import util
from limecore.cli import Command
from limecore.messaging.api import Publisher

from example.governance import commands


class Publish(Command):
    @inject
    def __init__(self, publisher: Publisher):
        self._publisher = publisher

    @classmethod
    def create_argument_parser(cls, parser: ArgumentParser):
        subparsers = parser.add_subparsers(dest="message_type")

        for message in commands.__all__:
            impl = getattr(commands, message)

            subparser = subparsers.add_parser(util.to_snakecase(message, "-"))

            for parameter in cls._get_parameters(impl):
                subparser.add_argument(
                    "--%s" % parameter.name.replace("_", "-"),
                    type=parameter.annotation,
                    default=parameter.default if parameter.default else None,
                    required=True,
                )

    def run(self, argv: Namespace):
        impl = self._find_impl(argv.message_type)
        parameters = dict(
            (p.name, getattr(argv, p.name)) for p in self._get_parameters(impl)
        )

        with self._publisher as p:
            p.publish(impl.obtain(**parameters), mandatory=True)

    @classmethod
    def _get_parameters(cls, callable):
        for parameter in inspect.signature(callable).parameters.values():
            if parameter.kind != inspect.Parameter.POSITIONAL_OR_KEYWORD:
                # We cannot process **kwargs here.
                continue

            yield parameter

    def _find_impl(self, message_type):
        for message in commands.__all__:
            if message_type == util.to_snakecase(message, "-"):
                return getattr(commands, message)
