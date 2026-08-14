import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "campus_data.json")


with open(DATA_FILE, "r", encoding="utf-8") as file:
    campus_data = json.load(file)


def get_location(location_name):
    """Return information about a specific campus location."""
    return campus_data.get(location_name)


def get_all_locations():
    """Return all available campus locations."""
    return list(campus_data.keys())


def get_campus_data():
    """Return the complete campus knowledge base."""
    return campus_data