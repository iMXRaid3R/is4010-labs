def make_greeting(name: str) -> str:
    """Returns a greeting string formatted as 'Hello, <name>!'."""
    return f"Hello, {name}!"


def is_even(number: int) -> bool:
    """Returns True if the number is even, False otherwise."""
    return number % 2 == 0


def count_vowels(text: str) -> int:
    """Counts vowels (a, e, i, o, u), ignoring case and excluding y."""
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)
