import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, "src")
TESTS_PATH = os.path.join(PROJECT_PATH, "tests")
sys.path.extend([SOURCE_PATH, TESTS_PATH])
