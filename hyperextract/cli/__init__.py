"""Hyper-Extract CLI - A command-line tool for knowledge extraction."""

import utils.net
import utils.clients
import utils.http_session
import utils.transport
import utils.session
from importlib.metadata import version

__version__ = version("hyperextract")
__author__ = "Yifan Feng"

from .cli import app

__all__ = ["app"]
