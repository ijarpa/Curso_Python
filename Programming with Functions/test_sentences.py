from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_Adjective
import pytest

def test_determier():
    single_determiners = ["a", "one", "the"]
    
    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners

    plural_determiners = ["some", "many", "the"]

    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners

def test_noun():
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
        word = get_noun(1)
        assert word in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(4):
        word = get_noun(2)
        assert word in plural_nouns

def test_verb():
    verbs_past = [ "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        word = get_verb(1, "past")
        assert word in verbs_past

    single_verbs_present = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        word = get_verb(1, "present")
        assert word in single_verbs_present

    plural_verbs_present = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        word = get_verb(2, "present")
        assert word in plural_verbs_present
    
    verbs_future = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(4):
        word = get_verb(3, "future")
        assert word in verbs_future

def test_get_preposition ():
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    word = get_preposition()
    assert word in words

def test_get_Adjective():
    words = ["good","short","large","little","new, old",
        "right","special","strong","red","smart", "tall",
        "yound","crazy", "dead"]

    word = get_Adjective()
    assert word in words

def test_get_prepositional_phrase ():
    phrase = get_prepositional_phrase(1).split()
    assert len(phrase) == 3



pytest.main(["-v", "--tb=line", "-rN", __file__])