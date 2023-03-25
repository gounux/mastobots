from typing import Tuple

import requests
from requests import Response

from botbeings import SuperBotBeing

QUOTABLE_API_BASE_URL = "https://api.quotable.io"


class QuoteBotBeing(SuperBotBeing):
    def run(self, action: str = "default") -> None:
        if action == "default":
            quote, author = self.random_quote()
            content = f'"{quote}"\n\n- {author} -'
            self.mastodon.status_post(content)
            self.logger.info(
                f'Random quote tooted: "{quote}" -{author}- (length: {len(content)})'
            )

    def random_quote(self) -> Tuple[str, str]:
        # fetch a quote through quotable API
        r: Response = requests.get(f"{QUOTABLE_API_BASE_URL}/random")
        assert r.status_code == 200
        quote = r.json()
        return quote["content"], quote["author"]
