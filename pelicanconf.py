#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from pathlib import Path

AUTHOR = "Julian Berman"
SITENAME = "Julian"
TAGLINE ="All the Good Names Were Already Taken, Including This One."
SITEURL = ""

PATH = "content"

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

TYPOGRIFY = True

# Disable feed generation for development only.
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = [
    ("GitHub", "https://github.com/Julian/"),
]

SOCIAL = [
    ("@JulianWasTaken", "https://twitter.com/JulianWasTaken"),
    ("@julianberman", "https://instagram.com/julianberman"),
]
GITHUB_URL = "https://github.com/Julian"
TWITTER_USERNAME = "JulianWasTaken"

DEFAULT_PAGINATION = 10

THEME = Path(__file__).parent / "martin-pelican"

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

DRAFT_URL = "drafts/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
DRAFT_SAVE_AS = "drafts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

AUTHOR_URL = 'authors/{slug}/'
AUTHOR_SAVE_AS = 'authors/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors/index.html'

CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_SAVE_AS = 'tags/index.html'
