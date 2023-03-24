import logging
import sys
from argparse import ArgumentParser, Namespace

import colorlog
import yaml
from mastodon import MastodonError
from yaml import SafeLoader

from botbeings.bot_factory import available_bots, bots_factory

# configure logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = colorlog.ColoredFormatter(
    "%(yellow)s%(asctime)s %(log_color)s[%(levelname)s]%(reset)s %(purple)s[%(name)s]%(reset)s %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)


def arguments() -> Namespace:
    """
    Creates CLI arguments needed by the program
    :return: Namespace for CLI arg's definition
    """
    parser = ArgumentParser(description="BotBeings superpower trigger")
    parser.add_argument("power", help=f"Power of the botbeing to invoke (available: {','.join(available_bots.keys())})")
    parser.add_argument("config", help="Config file to use (path to the YAML file)")
    parser.add_argument("-a", "--action", default="default", help="Bot's action to trigger")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Verbose output")
    return parser.parse_args()


if __name__ == "__main__":
    args = arguments()

    if args.verbose:
        logger.setLevel(logging.DEBUG)
        for h in logger.handlers:
            h.setLevel(logging.DEBUG)

    logging.info(f"Parsing bots configuration YAML file at {args.config}")
    with open(args.config) as f:
        config = yaml.load(f, Loader=SafeLoader)

        try:
            logging.info(f"Creating botbeing with power '{args.power}'")
            bot = bots_factory(args.power, config["bots"])
            logging.info(f"Invoking action of bot {bot}")
            bot.action(args.action)
        except MastodonError as e:
            logging.error(e)
