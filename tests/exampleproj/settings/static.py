from .apps import *

STATIC_URL = "/static/foo/"
# Allow tests to execute with
# short-lived tmp directories.
import os

STATIC_ROOT = os.environ["STATIC_ROOT"]

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = (os.path.join(BASE_PATH, "static"),)
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "staticfiles_noimport.finders.AppDirectoriesNoImportFinder",
)

STATICFILES_STORAGE = os.environ.get(
    "STATICFILES_STORAGE",
    "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
)
