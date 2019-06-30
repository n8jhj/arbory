"""Test help for all functions.
"""

from click.testing import CliRunner

from arbory import basic


def test_help():
    """Make sure help is available in both long and short forms."""
    runner = CliRunner()
    result = runner.invoke(basic, ['--help'])
    assert result.exit_code == 0
    result = runner.invoke(basic, ['-h'])
    assert result.exit_code == 0
