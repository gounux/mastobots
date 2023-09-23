from mastodon import MastodonAPIError

from botbeings import SuperBotBeing


class FollowBotBeing(SuperBotBeing):
    nb_follows: int = 0

    def run(self, action: str = "default") -> None:
        if self.dryrun:
            self.logger.warning("Can not run in dryrun mode")
            return

        # fetch some toots
        timeline = self.mastodon.timeline_public(limit=self.fetch_timeline_limit)

        for toot in timeline:
            if not self.can_interact_with_toot(toot):
                continue
            if self.mastodon.ratelimit_remaining < 2:
                self.logger.debug("Stop: API ratelimit reached")
                continue

            user = toot.account
            self.follow_user(user)
            followers = self.mastodon.account_followers(
                user, limit=self.config.get("fetch_followers_limit")
            )
            for follower in followers:
                if follower.id == self.me.id:
                    continue
                self.follow_user(follower)

        self.logger.info(f"Done: followed {self.nb_follows} users")

    def follow_user(self, user) -> None:
        """
        Follows a mastodon user
        :param user: representation of a mastodon user, using API format:
        https://mastodonpy.readthedocs.io/en/stable/02_return_values.html#user-account-dicts
        """
        if user.locked:
            return

        if self.mastodon.ratelimit_remaining < 2:
            self.logger.debug("Stop: API ratelimit reached")
            return

        try:
            self.mastodon.account_follow(user)
            self.nb_follows += 1
            self.logger.info(f"Following user {user.acct}")
        except MastodonAPIError as e:
            self.logger.error(f"{e}: user {user.acct}")
