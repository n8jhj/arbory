"""Test the core tree functionality of arbory.
"""

from click.testing import CliRunner
import pytest

from arbory import tree


@pytest.mark.parametrize('cmd, args, output', [
    # All defaults for a given directory.
    (tree, ['tree'], '\n'.join([
        'tree/',
        '    f_tree.txt',
        '    sub1/',
        '        f_sub1.txt',
        '',
    ])),
    # Without files.
    (tree, ['tree', '-f', 'False'], '\n'.join([
        'tree/',
        '    sub1/',
        '',
    ])),
])
def test_tree(cmd, args, output):
    runner = CliRunner()
    result = runner.invoke(cmd, args)
    assert result.output == output
