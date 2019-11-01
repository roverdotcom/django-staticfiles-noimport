import os

from .apps import *
from .static import *

try:
    os.environ["DB_ACCESS_URL"]
except KeyError:
    print("Unable to find required environment varible.")
    raise
