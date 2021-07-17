"""
"""
import json
from pathlib import Path

# Delete this file when pushing to production
# This file is intended to provide development utilities for api/craigslisthousing

JSON_PATH = Path(__file__).absolute().parent.joinpath("neighborhoods.json")


def read_neighborhoods():
    return open_json(JSON_PATH)


def write_neighborhoods(session, model):
    """Gets all naturally lowercase neighborhoods (avoid scammy titles) and bind them
    to found region."""
    neighborhood_json = open_json(JSON_PATH)
    for post in session.query(model).distinct(model.neighborhood):
        if post.neighborhood.lower() != post.neighborhood or post.neighborhood == "":
            continue
        neighborhood_json[post.neighborhood.title()] = post.area
    write_json(neighborhood_json, JSON_PATH)


def open_json(input_path):
    with open(input_path) as file:
        data = json.load(file)
    return data


def write_json(data, output_path):
    with open(output_path, "w") as file:
        json.dump(data, file)