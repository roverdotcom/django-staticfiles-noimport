import os

SECRET_KEY = os.environ["SECRET_KEY"]

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.sitemaps",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.flatpages",
    "django.contrib.gis",
    "django.contrib.humanize",
    "django.contrib.redirects",
    "projectapp",
)

