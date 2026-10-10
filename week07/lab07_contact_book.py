"""A simple contact book backed by a JSON file."""

import json


def save_contacts_to_json(contacts, filename):
    """Write the contacts list to filename as indented JSON."""
    with open(filename, "w") as f:
        json.dump(contacts, f, indent=4)


def load_contacts_from_json(filename):
    """Return contacts from filename, or an empty list if it does not exist."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
