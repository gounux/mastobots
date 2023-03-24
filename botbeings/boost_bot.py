from botbeings import SuperBotBeing


class BoostBotBeing(SuperBotBeing):
    def action(self, action: str = "default") -> None:
        # fetch some toots
        timeline = self.mastodon.timeline_public(limit=self.fetch_timeline_limit)

        nb_boosts = 0
        for toot in timeline:
            if not self.can_interact_with_toot(toot):
                continue

            self.mastodon.status_reblog(toot)
            nb_boosts += 1
            self.logger.debug(f"Boosted toot #{toot.id} by {toot.account.username}")

        self.logger.info(f"Done: boosted {nb_boosts} toots")
