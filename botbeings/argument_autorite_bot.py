import random

from botbeings import MAX_TOOT_LENGTH, SuperBotBeing

AUTORITIES = [
    "84% des dermatologues",
    "Un panel représentatif de français",
    "Une majorité de français",
    "93% des français",
    "Un consensus au sein de la rédaction CNEWS",
    "Un groupement d'éditorialistes de BFMTV",
    "Christophe Barbier",
    "Un article paru récemment",
    "Un récent sondage",
    "Un panel d'experts",
]

VERBS = [
    "estime que",
    "considère que",
    "affirme que",
    "préconise que",
    "met le doigt sur le fait que",
    "met l'accent sur le fait que",
    "envisage que",
    "souligne le fait que",
    "s'indigne que",
    "soulève le fait que",
    "dresse le constat que",
    "s'alarme du fait que",
]

SUBJECTS = [
    "la situation",
    "le contexte",
    "l'évolution de la situation",
    "la mise en perspective du contexte",
    "l'état actuel de la situation",
    "les choses à l'heure actuelle",
    "les contraintes actuelles",
    "tout porte à croire que la situation",
    "tout porte à croire que le contexte",
]

ACTION = [
    "tend à s'aggraver",
    "s'améliore lentement mais sûrement",
    "est plutôt stable",
    "tend à évoluer à la marge",
    "tend à évoluer de manière modérée",
    "est au statu-quo",
    "pour n'être pas pire qu'hier, ne se dirige pas non plus vers une amélioration marquée",
    "évolue raisonnablement",
    "avance à sa propre vitesse",
    "n'a pas vocation à changer du tout-au-tout",
]

TOOT_TEMPLATE = "️☝️ {autority} {verb} {subject} {action}."


class ArgumentDAutoriteBotBeing(SuperBotBeing):
    def run(self, action: str = "default") -> None:
        toot = self.generate_toot()
        while len(toot) > MAX_TOOT_LENGTH:
            toot = self.generate_toot()
        self.mastodon.status_post(toot)
        self.logger.info(f'Tooted: "{toot}" (length: {len(toot)})')

    def generate_toot(self) -> str:
        return TOOT_TEMPLATE.format(
            autority=random.choice(AUTORITIES),
            verb=random.choice(VERBS),
            subject=random.choice(SUBJECTS),
            action=random.choice(ACTION),
        )
