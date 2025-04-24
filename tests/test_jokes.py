from utils.random_jokes import get_joke

def test_get_joke_returns_string():
    joke = get_joke()
    assert isinstance(joke, str)
    assert len(joke) > 0

    

