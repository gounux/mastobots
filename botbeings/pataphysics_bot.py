import logging
import random
from typing import Callable, Tuple

import lirecouleur.text as lt
import wikiquote
from mastodon import Mastodon, StreamListener
from wikiquote.constants import DEFAULT_MAX_QUOTES

from botbeings import SuperBotBeing
from botbeings.jobs_bot import MAX_TOOT_LENGTH

LOGGER = logging.getLogger()
DEFAULT_LANGUAGE = "fr"

# orthographe d'apparat phonems implementation
# see: https://fr.wikipedia.org/wiki/Orthographe_d%27apparat
OA_PHONEMS = {
    # voyelles
    "a": "igt",  # doigt
    "a~": "aon",  # paon
    "e^": "ë",  # noël
    "e^_comp": "ë",  # noël
    "e": "a",  # baby
    "e_comp": "a",  # baby
    "i": "u",  # business
    "j": "u",  # business ('travaIL')
    "e~": "ingt",  # vingt
    "x~": "ingt",  # vingt ('IMprimer')
    "q": "on",  # monsieur
    "o": "ü",  # capharnaüm
    "o_ouvert": "ü",  # capharnaüm
    "o_comp": "oa",  # goal
    "o~": "um",  # columbarium
    "u": "e",  # fuel
    "x": "i",  # flirt
    "x^": "e!",  # donne-le!
    "y": "eu",  # rue
    # consonnes
    "p": "b",  # obscène
    "t": "ght",  # sunlight
    "s_t": "ght",  # sunlight ('Tiens')
    "k": "x",  # excellent
    "k_qu": "x",  # excellent
    "b": "bes",  # lombes
    "d": "gd",  # amigdale
    "g": "c",  # second
    "g_u": "c",  # second
    "f": "ph",  # phamille
    "f_ph": "ph",  # phamille
    "v": "fh",  # neuf heures
    "s": "w",  # law
    "s_c": "w",  # law
    "s_x": "w",  # law ('siX')
    "z": "lsh",  # gentilshommes
    "z_s": "lsh",  # gentilshommes ('occaSion')
    "s^": "zsch",  # nietzschéen
    "z^": "sg",  # vosgien
    "z^_g": "sg",  # vosgien
    "l": "les",  # ailes
    "m": "hms",  # ohms
    "n": "mne",  # automne
    "r": "rrh",  # logorrhée
    # custom (phonems empiricly met)
    "gz": "cw",  # 'eXactement' -> 'seCond' + 'laW'
    "ks": "xw",  # 'eXcuser' -> 'eXcellent' + 'laW'
    "n~": "mneu",  # 'gaGNes'
    "g~": "mnec",  # 'hawkiNG' -> 'autoMNE' + 'seCond'
    "j_a": "uigt",  # 'vIA' -> 'bUsiness' + 'doIGT'
    "j_a~": "uaon",  # 'ambIANce'
    "j_e": "ua",  # 'qualifIÉ'
    "j_e_comp": "ua",  # 'remercIER' -> 'bUsiness' + 'bAby'
    "j_e^": "uë",  # 'entIÈre'
    "j_e^_comp": "uë",  # 'vIEtnam'
    "j_e~": "uingt",  # 'bIEN' -> 'bUsiness' + 'vINGT'
    "j_o": "uü",  # 'passIOnné'
    "j_o~": "uum",  # 'occasION' -> 'bUsiness' + 'colUMbarium'
    "j_o_comp": "uoa",  # 'socIAUx'
    "j_q": "u",  # 'spIEler'
    "j_q_caduc": "uon",  # 'oreILLE' -> 'bUsiness' + 'mONsieur' BIF BOF
    "j_x": "ue!",  # 'meILLEUr'
    "j_x^": "ue!",  # 'vIEUx'
    "w": "oa",  # 'haWking'
    "w_a": "oaigt",  # 'vOIlà' -> 'gOAl' + 'doIGT'
    "w_e": "ea",  # supposed
    "w_e_comp": "ea",  # 'jOUER' -> 'fuEl' + 'bAby'
    "w_e^_comp": "eë",  # 'silhOUEtte' -> 'fuEl' + 'noEl'
    "w_e~": "oaingt",  # 'lOIN' -> 'gOAl' + 'vINGT'
    "w_i": "eu",  # 'jOUIssance' -> 'fuEl' + 'bUsiness'
    "w_x": "ei",  # 'jOUEUr' -> 'fuEl' + 'flIrt'
    # misc
    "q_caduc": "",  # 'éprouvEnt'
    "verb_3p": "",  # 'éprouveNT'
    "#": "",
    "": "",
}


def encode_orthographe_d_apparat(text: str) -> str:
    oa, processed = "", ""
    phonems = lt.phonemes(text)
    for word in phonems:
        if isinstance(word, str):
            LOGGER.debug(f"Word is not a string and not a list of phonems: '{word}')")
            oa += word
            processed += word
            continue
        LOGGER.debug(f"word: {word}")
        for ph, char in word:
            LOGGER.debug(f"Processing phonem '{ph}' for '{char}'")
            if char in ["'"]:
                oa += " "
                processed += char
                continue
            oa_ph = OA_PHONEMS[ph].title() if char[0].isupper() else OA_PHONEMS[ph]
            oa += oa_ph
            processed += char
            LOGGER.debug(
                f"Phonem '{ph}' ('{char}') -> '{oa_ph}' (processed: '{processed}')"
            )
    return oa


def generate_oa_random_quote_toot() -> Tuple[str, str, str, str]:
    quote, title = random_quote()
    encoded = encode_orthographe_d_apparat(quote)
    toot = f"""💡 \"{encoded}\"

({title})"""
    return title, quote, encoded, toot


# region fetch quotes


def quote_of_the_day(lang: str = DEFAULT_LANGUAGE) -> str:
    return wikiquote.qotd(lang=lang)


def random_quote_from(
    title: str, max_quotes: int = DEFAULT_MAX_QUOTES, lang: str = DEFAULT_LANGUAGE
) -> str:
    quotes = wikiquote.quotes(title, max_quotes=max_quotes, lang=lang)
    return random.choice(quotes)


def random_quote(
    max: int = DEFAULT_MAX_QUOTES, lang: str = DEFAULT_LANGUAGE
) -> Tuple[str, str]:
    titles = wikiquote.random_titles(max_titles=max, lang=lang)
    if len(titles) == 0:
        return random_quote(max, lang)
    title = random.choice(titles)
    quotes = wikiquote.quotes(title, max_quotes=max, lang=lang)
    if len(quotes) == 0:
        return random_quote(max, lang)
    return random.choice(quotes), title


# endregion


class PataphysicsStreamListener(StreamListener):
    def __init__(
        self,
        mastodon: Mastodon,
        encoder: Callable[[str], str] = encode_orthographe_d_apparat,
        quote_fetcher: Callable[[int, str], Tuple[str, str]] = random_quote,
    ):
        self.mastodon = mastodon
        self.encoder = encoder
        self.quote_fetcher = quote_fetcher

    def on_update(self, status) -> None:
        sender = status.account
        LOGGER.info(f"Toot update from '{sender.acct}': '{status.content}'")

        _, quote, _, toot = generate_oa_random_quote_toot()
        while len(toot) >= MAX_TOOT_LENGTH or len(quote) >= MAX_TOOT_LENGTH - 4:
            _, quote, _, toot = generate_oa_random_quote_toot()

        reply_toot = self.mastodon.status_post(toot, in_reply_to_id=status.id)
        self.mastodon.status_post(f'👉 "{quote}"', in_reply_to_id=reply_toot.id)


class PataphysicsBotBeing(SuperBotBeing):
    def run(self, action: str = "default") -> None:
        if action == "oa_quote":
            # fetch a quote from wikiquote, encode it into orthographe d'apparat, toot it and reply with original
            title, quote, oa, toot = generate_oa_random_quote_toot()
            while len(toot) >= MAX_TOOT_LENGTH or len(quote) >= MAX_TOOT_LENGTH - 4:
                title, quote, oa, toot = generate_oa_random_quote_toot()
            oa_toot = self.mastodon.status_post(toot)
            self.logger.info(f'Tooted: "{oa}" ({title}, toot length: {len(toot)})')
            self.mastodon.status_post(f'👉 "{quote}"', in_reply_to_id=oa_toot["id"])
            self.logger.info(f'Replied: "{quote}" ({title}, toot length: {len(toot)})')

        elif action == "oa_stream_user":
            # open stream and wait for user event
            listener = PataphysicsStreamListener(self.mastodon)
            self.mastodon.stream_user(listener, run_async=False)

        elif action == "oa_stream_hash":
            # open stream and wait for hashtags event
            listener = PataphysicsStreamListener(self.mastodon)
            self.mastodon.stream_hashtag(
                "OrthographeApparat", listener, run_async=False
            )

        elif action == "autotest":
            # dummy method to launch many encodings and detects potential missing phonems
            self._autotest()

        else:
            # no specific action -> encode action text to orthographe d'apparat
            text = action
            oa_encoded = encode_orthographe_d_apparat(text)
            self.logger.info(text)
            self.logger.info(oa_encoded)

    def _autotest(self, total: int = 100) -> None:
        assert (
            encode_orthographe_d_apparat("Projet d'Orthographe d'apparat")
            == "Brrhüsgë gd Ürrhghtücrrhigtph gd igtbigtrrhigt"
        )

        self.logger.setLevel(logging.DEBUG)
        for h in self.logger.handlers:
            h.setLevel(logging.DEBUG)

        nb_ok, nb_err, exceptions = 0, 0, []
        for _ in range(total):
            try:
                generate_oa_random_quote_toot()
                nb_ok += 1
            except Exception as exc:
                nb_err += 1
                exceptions.append(exc)

        self.logger.info(f"NB OK: {nb_ok}/{total}")
        self.logger.info(f"NB ERRORS: {nb_err}/{total}")
        for e in exceptions:
            self.logger.info(e)
