"""Defines test configurations.
"""

import pytest


@pytest.fixture(autouse=True)
def fake_filesys(fs):
    """Set up fake file system."""
    fs.create_file('tree/f_tree.txt')
    fs.create_file('tree/sub1/f_sub1.txt')
    fs.create_file('arbory/config.ini', contents='\n'.join([
        '[DEFAULT]',
        'selected = cobalt',
        'dir_color_fg = blue',
        'dir_color_bg = white',
        'file_color_fg = green',
        '',
        '[cobalt]',
        'dir_color_fg = red',
        'file_color_fg = bright_cyan',
    ]))
