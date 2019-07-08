"""Test help for all functions.
"""

from click.testing import CliRunner

from arbory import arb


def test_help():
    """Make sure help is available in both long and short forms."""
    runner = CliRunner()
    result = runner.invoke(arb, ['--help'])
    assert result.exit_code == 0 and 'Usage: ' in result.output
    result = runner.invoke(arb, ['-h'])
    assert result.exit_code == 0 and 'Usage: ' in result.output
    result = runner.invoke(arb, [])
    assert result.exit_code == 0 and 'Usage: ' in result.output
