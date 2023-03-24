from botbeings import SuperBotBeing


class FavouriteBotBeing(SuperBotBeing):
    def power(self) -> str:
        return "favourite"

    def action(self, action: str = "default") -> None:
        # fetch some toots
        timeline = self.mastodon.timeline_public(limit=self.fetch_timeline_limit)

        nb_favourites = 0
        for toot in timeline:
            if not self.can_interact_with_toot(toot):
                continue

            self.mastodon.status_favourite(toot)
            nb_favourites += 1
            self.logger.debug(f"Favourited toot #{toot.id} by {toot.account.username}")

        self.logger.info(f"Done: favourited {nb_favourites} toots")
