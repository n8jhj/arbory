"""Test the core tree functionality of arbory.
"""

from click.testing import CliRunner

from arbory import tree


def test_tree():
    runner = CliRunner()
    result = runner.invoke(tree, ['arbory'])
    assert result.output == '\n'.join([
        'arbory/',
        '    core.py',
        '    __init__.py',
        '    __version__.py',
        '    __pycache__/',
        '        core.cpython-37.pyc',
        '        __init__.cpython-37.pyc',
        '        __version__.cpython-37.pyc',
        '',
    ])
