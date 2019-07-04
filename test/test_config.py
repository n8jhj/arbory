"""Test configuration use.
"""

from click.testing import CliRunner

from arbory import tree


def test_config():
    runner = CliRunner()
    result = runner.invoke(tree, ['tree'])
    assert result.output == '\n'.join([
        'tree/',
        '    f_tree.txt',
        '    sub1/',
        '        f_sub1.txt',
        '',
    ])
