import random


def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    # f-string drops the three words straight into the template text.
    # The story itself is arbitrary; only the presence of all three words matters.
    story = (
        f"Once upon a time, a {adjective} {noun} decided to {verb} "
        f"across the yard. Everyone who saw the {adjective} {noun} "
        f"agreed it was the best {verb} they had ever seen."
    )
    return story


def guessing_game():
    """Run an interactive number-guessing game."""
    # Secret number the player is trying to guess. Called as random.randint
    # (not "from random import randint") so tests can patch lab03.random.randint.
    secret_number = random.randint(1, 100)

    while True:
        # Ask the player for a guess and convert the text input to an integer
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            # Correct guess: congratulate the player and end the loop
            print(f"Correct! Congratulations, you guessed {secret_number}!")
            break


def main():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")

    print(generate_mad_lib(adjective, noun, verb))
    print()
    guessing_game()


if __name__ == "__main__":
    main()
