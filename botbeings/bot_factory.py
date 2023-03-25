from typing import Any, Dict, Mapping, Type

from botbeings import SuperBotBeing
from botbeings.blagues_bot import BlaguesBotBeing
from botbeings.boost_bot import BoostBotBeing
from botbeings.favourite_bot import FavouriteBotBeing
from botbeings.follow_bot import FollowBotBeing
from botbeings.quote_bot import QuoteBotBeing
from botbeings.toni_mastodoni import ToniMastodoni

available_bots: Mapping[str, Type[SuperBotBeing]] = {
    "favourite": FavouriteBotBeing,
    "boost": BoostBotBeing,
    "follow": FollowBotBeing,
    "quote": QuoteBotBeing,
    "blague": BlaguesBotBeing,
    "tonimastodoni": ToniMastodoni,
}


def bots_factory(power: str, configs: Dict[str, Dict[str, Any]]) -> SuperBotBeing:
    config = configs[power]
    return available_bots[power](config)
