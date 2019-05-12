#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from pathlib import Path

AUTHOR = "Julian Berman"
SITENAME = "Julian"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [
    ("GitHub", "https://github.com/Julian/"),
]

# Social widget
SOCIAL = [
    ("@JulianWasTaken", "https://twitter.com/JulianWasTaken"),
    ("@julianberman", "https://instagram.com/julianberman"),
]

DEFAULT_PAGINATION = 10

THEME = Path(__file__).parent / "martin-pelican"

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
