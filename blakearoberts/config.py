import os

APP_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

FREEZER_DESTINATION = PROJECT_ROOT

FREEZER_REMOVE_EXTRA_FILES = False
