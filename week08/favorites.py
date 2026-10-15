"""Persistent, case-insensitive storage for favorite weather locations."""

import json


class FavoritesManager:
    """Manage named favorite locations saved to a JSON file."""

    def __init__(self, filename):
        self.filename = filename
        self.favorites = self._load()

    def _load(self):
        """Load favorites from disk, returning an empty dict if missing or corrupted."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        if not isinstance(data, dict):
            return {}
        return {str(name).lower(): location for name, location in data.items()}

    def _save(self):
        """Write the current favorites to disk."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.favorites, f, indent=2)

    def add(self, name, location):
        """Add a favorite. Return False if the name already exists."""
        key = name.lower()
        if key in self.favorites:
            return False
        self.favorites[key] = location
        self._save()
        return True

    def remove(self, name):
        """Remove a favorite. Return False if the name does not exist."""
        key = name.lower()
        if key not in self.favorites:
            return False
        del self.favorites[key]
        self._save()
        return True

    def list_all(self):
        """Return a copy of all favorites as a name -> location dict."""
        return dict(self.favorites)

    def get_location(self, name):
        """Return the location saved under name, or None."""
        return self.favorites.get(name.lower())
