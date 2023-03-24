import logging
from abc import ABC, abstractmethod
from typing import Any, Dict

from mastodon import Mastodon

TIMELINE_LIMIT = 20


class SuperBotBeing(ABC):
    """
    Abstract BotBeing class
    All implemented bot beings should extend this class
    """

    mastodon: Mastodon
    interact_with_human: bool
    interact_with_bots: bool
    fetch_timeline_limit: int
    config: Dict[str, Any]
    logger = logging.getLogger()

    def __init__(self, config: Dict[str, Any]):
        self.mastodon = Mastodon(**config.get("api"))
        self.interact_with_human = config.get("interact_with_human", False)
        self.interact_with_bots = config.get("interact_with_bots", True)
        self.fetch_timeline_limit = config.get("fetch_timeline_limit", TIMELINE_LIMIT)
        self.config = config

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} (power: {self.power()})>"

    @abstractmethod
    def power(self) -> str:
        """
        Gives a simple string declaring the bot's power
        Used as a key to parse YAML configuration file
        :return: bot's power
        """
        pass

    @abstractmethod
    def action(self, action: str = "default") -> None:
        """
        Run bot's action: this is teh main function that perform's bot's power
        :param action: bot's action to trigger
        :return: nothing but a G thang
        """
        # run actions
        pass

    def can_interact_with_toot(self, toot: Dict[str, Any]) -> bool:
        """
        # check if the bot can interact with a toot, based on toot's author and bot's config
        :param toot: Dict representation of a mastodon toot, using API format:
        https://mastodonpy.readthedocs.io/en/stable/02_return_values.html#status-dicts
        :return: True if the bot can interract with the provided toot
        """

        bot_user = toot["account"]["bot"]
        return (self.interact_with_human and not bot_user) or (self.interact_with_bots and bot_user)
