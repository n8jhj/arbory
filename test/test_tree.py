"""Test the core tree functionality of arbory.
"""

from click.testing import CliRunner

from arbory import tree


def test_tree(fs):
    # Set up fake directory.
    fs.create_file('tree/f_tree.txt')
    fs.create_file('tree/sub1/f_sub1.txt')
    # Run test.
    runner = CliRunner()
    result = runner.invoke(tree, ['tree'])
    assert result.output == '\n'.join([
        'tree/',
        '    f_tree.txt',
        '    sub1/',
        '        f_sub1.txt',
        '',
    ])
