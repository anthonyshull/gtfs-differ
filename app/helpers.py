"""
Reusable helper functions for the GTFS differ application.
"""

from datetime import datetime
from dateutil import parser
from os import environ
from sys import exit

def maybe_continue(should_continue: bool) -> None:
    """Writes to GITHUB_OUTPUT to short-circuit subsequent steps in GitHub Actions."""
    if not should_continue:
        with open(environ["GITHUB_OUTPUT"], "a") as f:
            f.write("should_continue=false\n")
        exit(78)

def parse_last_modified(last_modified: str) -> datetime:
    """Parses the Last-Modified header into a datetime object."""
    return parser.parse(last_modified)