from typing import Any, Dict

import requests
from requests import Response

from botbeings import SuperBotBeing

BLAGUESAPI_BASE_URL = "https://www.blagues-api.fr"


class BlaguesBotBeing(SuperBotBeing):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        blagues_api_config: Dict[str, Any] = config.get("blaguesapi", dict)
        self.blagues_api_token = blagues_api_config.get("access_token")
        self.excluded_categories = blagues_api_config.get("excluded_categories")

    def run(self, action: str = "default") -> None:
        blague = self.fetch_random_blague()
        _, joke, answer = blague["type"], blague["joke"], blague["answer"]
        content = f"{joke}\n\n{answer}"
        self.mastodon.status_post(content, spoiler_text=joke)
        self.logger.info(f"Tooted: {joke} {answer} (length: {len(content)})")

    def fetch_random_blague(self) -> Dict[str, Any]:
        # fetches a random blague through Blagues API
        r: Response = requests.get(
            f"{BLAGUESAPI_BASE_URL}/api/random",
            params={"disallow": self.excluded_categories},
            headers={
                "Authorization": f"Bearer {self.blagues_api_token}",
            },
        )
        assert r.status_code == 200
        return r.json()
