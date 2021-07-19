"""
"""
from irahorecka.python.api.craigslist.utils import open_json, write_json, NEIGHBORHOOD_PATH


def write_neighborhoods(session, model):
    """Gets all naturally lowercase neighborhoods (avoid scammy titles) and bind them
    to its parent Area."""
    neighborhood_json = open_json(NEIGHBORHOOD_PATH)
    for post in session.query(model).distinct(model.neighborhood):
        if post.neighborhood.lower() != post.neighborhood or post.neighborhood == "":
            continue
        neighborhood_json[post.neighborhood.title()] = post.area
    write_json(neighborhood_json, NEIGHBORHOOD_PATH)
