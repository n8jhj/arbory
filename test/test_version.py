"""Test version option.
"""

from click.testing import CliRunner

from arbory import tree
from arbory.__version__ import __version__


def test_version():
    runner = CliRunner()
    result = runner.invoke(tree, ['--version'])
    assert result.exit_code == 0
    assert result.output == 'arbory, version {}\n'.format(__version__)
