"""Command-line weather application."""

import argparse
import os
import sys
from pathlib import Path

try:
    from week08.favorites import FavoritesManager
    from week08.weather_api import WeatherAPI, format_current_weather, format_forecast
except ImportError:
    from favorites import FavoritesManager
    from weather_api import WeatherAPI, format_current_weather, format_forecast

FAVORITES_FILE = Path(__file__).parent / "favorites.json"
PLACEHOLDER_KEY = "YOUR_API_KEY_HERE"


def load_api_key():
    """Return the API key from WEATHER_API_KEY, then config.py, or None."""
    key = os.environ.get("WEATHER_API_KEY")
    if key:
        return key
    try:
        from week08 import config
    except ImportError:
        try:
            import config
        except ImportError:
            return None
    key = getattr(config, "WEATHER_API_KEY", None)
    if not key or key == PLACEHOLDER_KEY:
        return None
    return key


def build_parser():
    """Build the argument parser for all weather commands."""
    parser = argparse.ArgumentParser(description="Weather CLI application")
    subparsers = parser.add_subparsers(dest="command", required=True)

    current = subparsers.add_parser("current", help="Show current weather")
    current.add_argument("location", help="Location or favorite name")

    forecast = subparsers.add_parser("forecast", help="Show a 1-3 day forecast")
    forecast.add_argument("location", help="Location or favorite name")
    forecast.add_argument("--days", type=int, default=3, help="Days (1-3)")

    favorites = subparsers.add_parser("favorites", help="Manage favorite locations")
    fav_sub = favorites.add_subparsers(dest="favorites_command", required=True)
    add = fav_sub.add_parser("add", help="Add a favorite")
    add.add_argument("name")
    add.add_argument("location")
    fav_sub.add_parser("list", help="List favorites")
    remove = fav_sub.add_parser("remove", help="Remove a favorite")
    remove.add_argument("name")

    return parser


def handle_favorites(args, manager):
    """Run a favorites subcommand and return an exit status."""
    if args.favorites_command == "add":
        if not manager.add(args.name, args.location):
            print(f"Error: favorite '{args.name}' already exists.", file=sys.stderr)
            return 1
        print(f"Added favorite '{args.name}': {args.location}")
        return 0

    if args.favorites_command == "list":
        favorites = manager.list_all()
        if not favorites:
            print("No favorites saved.")
        for name, location in favorites.items():
            print(f"{name}: {location}")
        return 0

    if not manager.remove(args.name):
        print(f"Error: favorite '{args.name}' not found.", file=sys.stderr)
        return 1
    print(f"Removed favorite '{args.name}'.")
    return 0


def main(argv=None) -> int:
    """Parse arguments, run the requested command, and return an exit status."""
    args = build_parser().parse_args(argv)
    manager = FavoritesManager(FAVORITES_FILE)

    if args.command == "favorites":
        return handle_favorites(args, manager)

    api_key = load_api_key()
    if not api_key:
        print(
            "Error: no API key found. Set WEATHER_API_KEY or create week08/config.py.",
            file=sys.stderr,
        )
        return 1

    location = manager.get_location(args.location) or args.location
    client = WeatherAPI(api_key)

    if args.command == "current":
        data = client.get_current_weather(location)
        formatter = format_current_weather
    else:
        try:
            data = client.get_forecast(location, days=args.days)
        except ValueError as error:
            print(f"Error: {error}", file=sys.stderr)
            return 1
        formatter = format_forecast

    if data is None:
        print(f"Error: could not get weather for '{location}'.", file=sys.stderr)
        return 1

    print(formatter(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
