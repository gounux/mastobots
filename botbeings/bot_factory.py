from typing import Any, Dict, Mapping, Type

from botbeings import SuperBotBeing
from botbeings.boost_bot import BoostBotBeing
from botbeings.favourite_bot import FavouriteBotBeing
from botbeings.follow_bot import FollowBotBeing
from botbeings.toni_mastodoni import ToniMastodoni

available_bots: Mapping[str, Type[SuperBotBeing]] = {
    "favourite": FavouriteBotBeing,
    "boost": BoostBotBeing,
    "follow": FollowBotBeing,
    "tonimastodoni": ToniMastodoni,
}


def bots_factory(power: str, configs: Dict[str, Dict[str, Any]]) -> SuperBotBeing:
    config = configs[power]
    return available_bots[power](config)
