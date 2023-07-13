import random
from typing import Tuple

import wikiquote
from lirecouleur.text import phonemes
from wikiquote.constants import DEFAULT_MAX_QUOTES

from botbeings import SuperBotBeing
from botbeings.jobs_bot import MAX_TOOT_LENGTH

DEFAULT_LANGUAGE = "fr"

# TODO: implement https://fr.wikipedia.org/wiki/Orthographe_d%27apparat
OA_PHONEMS = {"phonem": "écriture du phonème en orthographe d'apparat"}


class PataphysicsBotBeing(SuperBotBeing):
    def run(self, action: str = "default") -> None:
        if action == "orthoapp_quote":
            toot = self.generate_oa_random_quote_toot()
            while len(toot) >= MAX_TOOT_LENGTH:
                toot = self.generate_oa_random_quote_toot()
            self.mastodon.status_post(toot)
            self.logger.info(f'Tooted: "{toot}" (length: {len(toot)})')

        if action == "orthoapp_stream":
            # TODO: open stream and wait for mentions
            # on mention: get toot content and encode it to orthographe d'apparat
            # post toot in reply to toot with mention
            pass

    def generate_oa_random_quote_toot(self) -> str:
        quote, title = self.random_quote()
        encoded = self.encode_orthographe_d_apparat(quote)
        return f"{title}: '{encoded}'"

    def encode_orthographe_d_apparat(self, text: str) -> str:
        phonems = phonemes(text)
        # TODO: read words and convert to orthographe d'apparat using OA_PHONEMS dict
        return text

    @staticmethod
    def quote_of_the_day(lang: str = DEFAULT_LANGUAGE) -> str:
        return wikiquote.qotd(lang=lang)

    @staticmethod
    def random_quote_from(
        title: str, max_quotes: int = DEFAULT_MAX_QUOTES, lang: str = DEFAULT_LANGUAGE
    ) -> str:
        quotes = wikiquote.quotes(title, max_quotes=max_quotes, lang=lang)
        return random.choice(quotes)

    @staticmethod
    def random_quote(
        max: int = DEFAULT_MAX_QUOTES, lang: str = DEFAULT_LANGUAGE
    ) -> Tuple[str, str]:
        titles = wikiquote.random_titles(max_titles=max, lang=lang)
        title = random.choice(titles)
        quotes = wikiquote.quotes(title, max_quotes=max, lang=lang)
        return random.choice(quotes), title
