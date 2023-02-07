import random

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == "past":
        words = [ "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        elif quantity != 1:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # Randomly choose and return a verb.
    word = random.choice(words)
    return word

def get_Adjective ():
    # Randomly choose and return a adjective .
    words = ["good","short","large","little","new, old",
        "right","special","strong","red","smart", "tall",
        "yound","crazy", "dead"]

    word = random.choice(words)
    return word

def get_preposition():
    # Randomly choose and return a preposition.
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):

    word_1 = get_preposition()
    word_2 = get_determiner(quantity)
    word_3 = get_noun(quantity)

    # Randomly choose and return a verb.
    phrase = f"{word_1} {word_2} {word_3}"
    return phrase

def main(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    phrase = get_prepositional_phrase(quantity)
    adjective =  get_Adjective()

    print(f"{determiner} {adjective} {noun} {verb} {phrase}")

main(1, "past")
main(1, "present")
main(1, "future")
main(2, "past")
main(2, "present")
main(2, "future")

