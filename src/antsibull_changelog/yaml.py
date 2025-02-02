# -*- coding: utf-8 -*-
# Author: Felix Fontein <felix@fontein.de>
# License: GPLv3+
# Copyright: Ansible Project, 2020

"""
YAML handling.
"""

from typing import Any

import yaml

_SafeLoader: Any
_SafeDumper: Any
try:
    # use C version if possible for speedup
    from yaml import CSafeLoader as _SafeLoader
    from yaml import CSafeDumper as _SafeDumper
except ImportError:
    from yaml import SafeLoader as _SafeLoader
    from yaml import SafeDumper as _SafeDumper


def load_yaml(path: str) -> Any:
    """
    Load and parse YAML file ``path``.
    """
    with open(path, 'rb') as stream:
        return yaml.load(stream, Loader=_SafeLoader)


def store_yaml(path: str, content: Any) -> None:
    """
    Store ``content`` as YAML file under ``path``.
    """
    with open(path, 'w', encoding='utf-8') as stream:
        dumper = _SafeDumper
        dumper.ignore_aliases = lambda *args: True
        yaml.dump(content, stream, default_flow_style=False, Dumper=dumper)
