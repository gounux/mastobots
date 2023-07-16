import random

from botbeings import MAX_TOOT_LENGTH, SuperBotBeing

AUTORITIES = [
    "84% des dermatologues",
    "Un panel représentatif de français",
    "Une majorité de français",
    "93% des français",
    "Un consensus au sein d'une rédaction journalistique",
    "Un groupement d'éditorialistes de chaînes de la TNT",
    "Une présentatrice d'une émission de grande écoute",
    "Une dirigeante de chaîne d'info en continu",
    "Christophe Barbier",
    "Un article paru récemment",
    "Une étude récemment parue",
    "Un récent sondage",
    "Un panel d'experts",
    "Un groupement d'experts sur le sujet",
    "Le Grand Rabbin de la Mecque",
    "Une nièce de milliardaire",
    "Une membre du gouvernement",
    "Une membre du gouvernement souhaitant garder l'anonymat",
    "Une membre de l'opposition",
    "Une membre de l'opposition souhaitant garder l'anonymat",
    "Une lanceuse d'alerte",
]

VERBS = [
    "estime que",
    "considère que",
    "pense que",
    "affirme que",
    "préconise que",
    "conçoit que",
    "juge que",
    "envisage que",
    "rappelle que",
    "rappelle le fait que",
    "doute du fait que",
    "pointe du doigt le fait que",
    "met le doigt sur le fait que",
    "met l'accent sur le fait que",
    "spécule sur le fait que",
    "souligne le fait que",
    "soulève le fait que",
    "tempère le fait que",
    "dresse le constat que",
]

SUBJECTS = [
    "la situation",
    "le contexte",
    "la conjecture",
    "l'évolution de la situation",
    "la situation contextuelle",
    "le contexte de la situation",
    "le contexte situationnel",
    "le contexte circonstanciel",
    "le contexte en l'état",
    "la situation en l'état",
    "la conjecture en l'état",
    "la situation circonstancielle",
    "la circonstance contextuelle et situationnelle",
    "la mise en perspective du contexte",
    "l'état actuel",
    "l'état à l'heure d'aujourd'hui",
    "l'état actuel à l'heure d'aujourd'hui",
    "l'état actuel de la situation",
    "l'état des choses à l'heure actuelle",
    "la conjoncture actuelle",
    "la conjoncture projetée",
    "la conjoncture du contexte à l'heure actuelle",
    "la complexité de la situation",
    "tout porte à croire que la situation",
    "tout porte à croire que le contexte",
    "de nombreux éléments portent à croire que la situation",
    "de nombreux éléments portent à croire que le contexte",
]

ACTION = [
    "est plutôt stable",
    "tend à évoluer à la marge",
    "tend à évoluer de manière modérée",
    "est au statu-quo",
    "pour n'être pas pire qu'hier, ne se dirige pas non plus vers une amélioration marquée",
    "évolue modérément",
    "avance à sa propre vitesse",
    "s'améliore lentement, même si des efforts restent à accomplir",
    "n'a pas vocation à changer du tout-au-tout",
    "évolue convenablement, mais pas non plus de manière drastique",
    "a plutôt vocation à stagner",
    "stagne de manière spectaculaire",
    "reste à définir selon ce qu'en pense tout un chacun",
    "commence à devenir préoccupante, sans toutefois tirer la sonnette d'alarme",
    "est au beau-fixe, même si quelques changements modérés sont à prévoir",
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
