
from src.utils.helpers import normalize_name

def test_normalize_name():
    assert normalize_name(" Hello World ") == "hello-world"
    assert normalize_name(None) == ""
    assert normalize_name("Hello") == "hello"
