from logic import make_greeting


def test_default_name():
    assert make_greeting(None, "Hello") == "Hello, world!"


def test_trims_name():
    assert make_greeting("  Pawan  ", "Hi") == "Hi, Pawan!"