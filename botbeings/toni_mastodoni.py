import random
from random import randint

from botbeings import SuperBotBeing

RECIPIENTS = [
    "Jimmy",
    "Paulie",
    "Tommy",
    "Vinny",
    "Billy",
    "Nicky",
    "Charlie",
    "Frankie",
    "Salvie",
    "Angie",
    "Richie",
    "Sonny",
]

APOSTROPHES = [
    "Hey {name} !",
    "You know, {name}.",
    "You hear what I said, {name} ?",
    "Listen to your friend here, {name}.",
    "Listen to me {name}, will ya ?",
    "What did ya say {name} ?",
    "What's the fuckin' matter wit ya, {name} ?",
    "Come on {name}.",
    "You talkin' to me {name} ?",
    "Come over here {name}, will ya ?",
    "What the fuck ya looking at {name} ?",
    "You know {name}, it’s a multiple-choice thing with you.",
    "Do you believe that, {name} ?",
    "Hey, {name}, hurry up, will ya ?",
    "I'll make this short and sweet, {name}.",
    "Well {name}, I've been busy.",
    "Yeah {name}, you're always fuckin' late.",
    "No more shines, {name}.",
    "Relax {name}, will ya ?",
    "I wanna tell ya one thing, {name}",
    "Hey {name}, I'm talkin to {mobster} right now.",
    "Hey {name}, stop being a prick, will ya ?",
]

QUESTIONS = [
    "You don't say hello ? Show the respect, will ya ?",
    "You talkin' to me ?",
    "I'm just some lunatic macaroni mushroom, is that it ?",
    "I'm funny how ? I mean funny like I'm a clown ? I amuse you ? I make you laugh? I'm here to fuckin' amuse you ? What do you mean, funny? Funny how ? How am I funny ?",
    "Do I amuse you ?",
    "Am I here to fuckin' amuse you ?",
    "You know why you hate me so much, {name} ? Because I look the way you feel.",
    "Did Mad freakin' Max just call me irritating ?",
    "What the fuck are you doing ? You're hanging around my fuckin' neck like a vulture, like impending danger.",
    "What the fuck is wrong with that ?",
    "Who the fuck cares ?",
    "What you mean, you're kidding ?",
    "What ? Do you got me on a fuckin' pay-no-mind list ?",
    "Who the fuck asked you anything ?",
    "Did {mobster} ever tell you about my painting ?",
    "They say everyday's a gift, but does it have to be a pair of socks ?",
    'I wonder what\'s french canadian for "I grew up without a mother" ?',
    "I was born, grew up, spent a few years in the army, couple more in the can, and here I am, half a wise guy, so what ?",
    "What did you say {name} ? Are you being a fuckin' wiseguy with me ?",
    "Do you believe that ? In this day and age ? What the fuck is the world coming to ?",
    "What am I ? A mirage ?",
    "What are you staring at you prick ?",
    "What the fuck you looking at ?",
    "Don't make a scene, all right ?",
    "What the fuck do I know ?",
    "How the fuck could I know ?",
    "Why is that you have twenty-four different kinds of pork rinds and you only have one kind of peanut butter ?",
    "What about these pants I got on, you think they're ok ?",
    "What is that ? Mozart ?",
    "Where you going ? Where you going, you dizzy motherfucker, you ?",
    "Who the fuck asked you anything ?",
    "We know what you do, don't we {name} ?",
    "What happened to Gary Cooper ? The strong silent type.",
    "You havin' a good time ?",
    "What is it ? A big fuckin' deal ?",
    "Who the fack told you that ?",
]

AFFIRMATIONS = [
    "You win, you win. You lose, you still win.",
    "You're a fuckin' mumbling stuttering little fuck. You know that ?",
    "That fuckin' bandage on your foot is bigger than your fuckin' head.",
    "What the fuck you looking at ? Come on. Make that coffee to go. Let's go.",
    "I can't tomorrow night, I gotta meet {mobster}.",
    "If it's not good for you, it's not good for me.",
    "I haven't been able to tell anybody this. I'm fuckin' relieved.",
    "My father was in it. My uncle was in it. Maybe I was too lazy to think for myself.",
    "I don't know what it's about, but the T.V. stays here.",
    "The guy gives him the works: MRIs, CAT scans, DOG scans, you name it. He says there's not a thing wrong with his back.",
    "When I was a kid, you two were old ladies. Now I’m old. And you two are still old.",
    "It's like an ad for a Weight Loss Center. Before, and way before.",
    "If I wanna talk private, I gotta go to a fuckin' bus stop.",
    "Listen to your friend here. He knows what he's talking about.",
    "I'm not gonna answer that. It's stupid. It's a sick question and you're a sick fuck and I'm not that sick that I'm gonna answer it.",
    "I never made it to the sixth grade, kid.",
    "My mother's gonna make some fried peppers and sausage for us.",
    "I've been trying to reach you {name}. You're tougher to get than the president.",
    "They fuck you with cell phones. That's what it is. They're fuckin' you with the cell phone. They love it when you get cut off. Y'know why, huh? You know why? 'Cause when you call back, which they know you're gonna do, they charge you for that fuckin' first minute again at that high rate.",
    "I'm gonna make him an offer he can't refuse.",
    "Monday, Tuesday, Thursday, Wednesday, Friday, Sunday, Saturday.",
    "Now we’re talking business, let’s talk business.",
    "You think too much of me, kid. I am not that clever.",
    "I'm a Waste Management Consultant.",
    "Just when I thought I was out, they pull me back in.",
    "A grown man made a wager. He lost. He made another one – he lost again. End of story.",
    "You can’t learn about it in school, and you can’t have a late start.",
    "There are three ways of doing things around here: the right way, the wrong way, and the way I do it.",
    "You don't make up for your sins in church. You do it in the streets. You do it at home. The rest is bullshit and you know it.",
    "I asked God for a bike, but I know God doesn’t work that way. So, I stole a bike and asked him for forgiveness.",
    "You've fucked with the wrong person here {name}.",
    "I couldn't get any jobs, and when that happens, you get so humble it's disgusting.",
    "I was bumping into walls and saying, Excuse me.",
    "You can't talk to me like that.",
    "He said, 'No, you're gonna tell me something today, tough guy.'",
    "I said, 'All right, I'll tell you something: go fuck your mother.'",
    "When I ask somebody to take care of something for me, I expect them to take care of it themselves. I don't need two roads coming back to me.",
    "Maybe you didn't hear about it, {name}. You've been away a long time.",
    "Sometimes you don't sound like you're kidding, you know, there's a lotta people around...",
    "I just came home and I haven't seen you in a long time, {name}.",
]

ENDS = [
    "I'm fuckin' relieved.",
    "I got to admit the truth.",
    "You can’t fuckin' do this like this !",
    "Say hello to my little friend !",
    "Fack it. I’m gonna go get the papers.",
    "I’m an average nobody.",
    "Show the respect, will ya ?",
    "Come on. Let's go, come an.",
    "Listen to your friend here, {name}.",
    "I told ya, {name}.",
    "End of story.",
    "Come on let's go, you motherfucker, you.",
    "Forget about it.",
    "First you get the sugar.",
    "See, ya are what ya are in this world.",
    "It’s not personal, {name}, it's strictly business.",
    "Nothing personal here, {name}, just business, that's all.",
    "That’s the way it is now, {name}.",
    "Makes me very angry.",
    "I'm wit ya, {name}, all the way to the finish.",
    "What is that ? Mozart ?",
    "Better hear what {mobster} has to say.",
    "Glad to be here. Come an, let's go.",
    "You try too hard, {name}.",
    "Don't be late next time {name}, will ya ?",
    "Come on. Make that coffee to go. Let's go.",
    "I'm sorry {name}, I didn't mean to offend you.",
    "I'm only kidding with you, we're having a party.",
    "I'm kidding, {name}",
    "You, you fucking piece of shit !",
    "Yeah, yeah, come an, come an !",
    "Come an.",
    "Fack it, let's go.",
    "Don't be a prick, {name}.",
    "That fake old tough guy !",
    "Let's have a talk with {lobster}, tonight.",
]


class ToniMastodoni(SuperBotBeing):
    def run(self, action: str = "default") -> None:
        if action == "default":
            self.toot()

    @staticmethod
    def generate_toot(recipient: str, nbq: int, nba: int) -> str:
        if recipient in RECIPIENTS:
            RECIPIENTS.remove(recipient)
        mobster = random.choice(RECIPIENTS)
        apostrophe = random.choice(APOSTROPHES)
        questions = random.sample(QUESTIONS, k=nbq)
        affirmations = random.sample(AFFIRMATIONS, k=nba)
        end = random.choice(ENDS)
        content = f"{apostrophe} {' '.join(questions)} {' '.join(affirmations)} {end}"
        return content.format(name=recipient, mobster=mobster)

    def toot(self) -> None:
        recipient = random.choice(RECIPIENTS)
        nb_elements = random.randint(2, 4)
        nb_questions = random.randint(1, nb_elements - 1)
        nb_affirmations = nb_elements - nb_questions

        self.logger.debug(
            f"Generating toot with {nb_questions} questions and {nb_affirmations} affirmations"
        )
        toot = self.generate_toot(recipient, nb_questions, nb_affirmations)
        self.mastodon.status_post(toot)
        self.logger.info(f'Tooted: "{toot}" (length: {len(toot)})')
