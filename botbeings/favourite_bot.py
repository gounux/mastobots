from botbeings import SuperBotBeing


class FavouriteBotBeing(SuperBotBeing):
    def power(self) -> str:
        return "favourite"

    def action(self) -> None:
        timeline = self.mastodon.timeline_public(limit=self.fetch_timeline_limit)
        for toot in timeline:
            if not self.can_interact_with_toot(toot):
                continue

            self.mastodon.status_favourite(toot)
