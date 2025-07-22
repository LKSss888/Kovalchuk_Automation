import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# 1 ----------------------------------------------------------------------------

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# 2 ----------------------------------------------------------------------------

@pytest.mark.positive
@pytest.mark.parametrize("word, liter, expected", [
    ("Good", "O", True),
    ("Beer", "B", True),
    ("Night", "H", True),
])
def test_contains_positive(word, liter, expected):
    assert string_utils.capitalize(word, liter) == expected


@pytest.mark.negative
@pytest.mark.parametrize("word, liter, expected", [
    ("Good", "A", False),
    ("Beer", "+", False),
    ("Night", "   ", False),
])
def test_contains_negative(word, liter, expected):
    assert string_utils.capitalize(word, liter) == expected

# 3 ----------------------------------------------------------------------------

@pytest.mark.positive
@pytest.mark.parametrize("text, expected", [
    ("    skypro", "skypro"),
    ("    hello", "hello"),
    ("     04 апреля", "04 апреля"),
])
def test_trim_positive(text, expected):
    assert string_utils.capitalize(text) == expected


@pytest.mark.negative
@pytest.mark.parametrize("text, expected", [
    ("123abc     ", "123abc     "),
    ("     ", ""),
    ("04 апреля", "04 апреля"),
])
def test_trim_negative(text, expected):
    assert string_utils.capitalize(text) == expected

# 4 ----------------------------------------------------------------------------

@pytest.mark.positive
@pytest.mark.parametrize("text, liter, expected", [
    ("skypro", "k", "sypro"),
    ("world", "orld", "w"),
    ("python", "on", "pyth"),
])
def test_delete_symbol_positive(text, liter, expected):
    assert string_utils.capitalize(text, liter) == expected


@pytest.mark.negative
@pytest.mark.parametrize("text, liter, expected", [
    ("123abc", "123456", Error),  # я не понимаю какой тут ОР
    (None, None, Error),   # я не понимаю какой тут ОР
    ("world", "world", None),  # я не понимаю какой тут ОР
])
def test_delete_symbol_negative(text, liter, expected):
    assert string_utils.capitalize(text, liter) == expected