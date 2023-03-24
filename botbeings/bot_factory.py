from typing import Any, Dict

from botbeings import SuperBotBeing
from botbeings.boost_bot import BoostBotBeing
from botbeings.favourite_bot import FavouriteBotBeing

available_bots = {
    "favourite": FavouriteBotBeing,
    "boost": BoostBotBeing,
}


def bots_factory(power: str, configs: Dict[str, Any]) -> SuperBotBeing:
    config = configs[power]
    return available_bots[power](config)
