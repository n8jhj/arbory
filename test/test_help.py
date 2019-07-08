"""Test help for all functions.
"""

from click.testing import CliRunner
import pytest

from arbory import arb


@pytest.mark.parametrize('cmd', [
    # arbory base command.
    [],
    # tree subcommand.
    ['tree'],
    # config subcommand.
    ['config'],
])
def test_help(cmd):
    """Make sure help is available in both long and short forms."""
    runner = CliRunner()
    cmd.append('--help')
    result = runner.invoke(arb, cmd)
    assert result.exit_code == 0 and 'Usage: ' in result.output
    cmd[-1] = '-h'
    result = runner.invoke(arb, cmd)
    assert result.exit_code == 0 and 'Usage: ' in result.output
    del cmd[-1]
    result = runner.invoke(arb, cmd)
    assert result.exit_code == 0 and 'Usage: ' in result.output
