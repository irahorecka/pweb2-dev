"""
Clean db of junk data
Criteria:
- Posts older than a week of cleaning
- Repeated titles per given neighborhood in database
"""

import datetime

from irahorecka.models import db, CraigslistHousing


def clean_craigslist_housing():
    """ENTRY POINT: Cleans Craigslist Housing database."""
    # Tack on more functions as you see fit.
    rm_old_posts(CraigslistHousing)
    rm_duplicate_posts(CraigslistHousing)


def rm_old_posts(model, days=7):
    """Remove posts where `model.last_updated` is over `days` old."""
    lower_dttm_threshold = datetime.datetime.now() - datetime.timedelta(days=days)
    model.query.filter(model.last_updated < lower_dttm_threshold).delete()
    db.session.commit()


def rm_duplicate_posts(model):
    """Filter id's where `model._title_neighborhood` is unique."""
    unique_posts = model.query.with_entities(model.id).distinct(model._title_neighborhood)
    duplicate_posts = model.__table__.delete().where(model.id.not_in(unique_posts))
    # Remove duplicate posts
    db.session.execute(duplicate_posts)
    db.session.commit()
