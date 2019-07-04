"""Defines test configurations.
"""

import pytest


@pytest.fixture(autouse=True)
def fake_filesys(fs):
    """Set up fake file system."""
    fs.create_file('tree/f_tree.txt')
    fs.create_file('tree/sub1/f_sub1.txt')
