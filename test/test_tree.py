"""Test the core tree functionality of arbory.
"""

from click.testing import CliRunner
import pytest

from arbory import tree


@pytest.mark.parametrize('cmd, args, output', [
    (tree, ['tree'], '\n'.join([
        'tree/',
        '    f_tree.txt',
        '    sub1/',
        '        f_sub1.txt',
        '',
    ])),
    (tree, ['tree', '-f', 'False'], '\n'.join([
        'tree/',
        '    sub1/',
        '',
    ])),
])
def test_tree(fs, cmd, args, output):
    # Set up fake directory.
    fs.create_file('tree/f_tree.txt')
    fs.create_file('tree/sub1/f_sub1.txt')
    # Run test.
    runner = CliRunner()
    result = runner.invoke(cmd, args)
    assert result.output == output
