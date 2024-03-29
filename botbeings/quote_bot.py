from typing import Tuple

import requests
from requests import Response

from botbeings import SuperBotBeing
from botbeings.pataphysics_bot import random_wikiquote

QUOTABLE_API_BASE_URL = "https://api.quotable.io"


class QuoteBotBeing(SuperBotBeing):
    def run(self, action: str = "default") -> None:
        if action == "quotable":
            quote, author = self.fetch_random_quotable()
            content = f'"{quote}"\n\n- {author} -'
            if not self.dryrun:
                self.mastodon.status_post(content)
            self.logger.info(f'Tooted: "{quote}" -{author}- (length: {len(content)})')
        elif action == "wikiquote":
            quote, title, content = self.fetch_random_wikiquote("en")
            if not self.dryrun:
                self.mastodon.status_post(content)
            self.logger.info(f'Tooted: "{quote}" -{title}- (length: {len(content)})')

    @staticmethod
    def fetch_random_quotable() -> Tuple[str, str]:
        # fetches a quote through quotable API
        r: Response = requests.get(f"{QUOTABLE_API_BASE_URL}/random")
        assert r.status_code == 200
        quote = r.json()
        return quote["content"], quote["author"]

    def fetch_random_wikiquote(self, lang: str) -> Tuple[str, str, str]:
        quote, title = random_wikiquote(lang=lang)
        content = f'"{quote}"\n\n- {title} -'
        if len(content) >= self.max_toot_length:
            return self.fetch_random_wikiquote(lang)
        return quote, title, content
