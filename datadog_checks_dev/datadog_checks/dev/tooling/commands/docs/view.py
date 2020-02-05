# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import webbrowser

import click

from ....utils import dir_exists, path_join
from ...constants import get_root
from ..console import CONTEXT_SETTINGS, abort


@click.command(context_settings=CONTEXT_SETTINGS, short_help='View documentation in a web browser')
def view():
    """View documentation in a web browser."""
    site_dir = path_join(get_root(), 'site')
    if not dir_exists(site_dir):
        abort('Site directory does not exist, build docs by running `ddev docs build`')

    webbrowser.open_new_tab(f"file:///{path_join(site_dir, 'index.html').lstrip('/')}")
