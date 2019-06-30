"""Test help for all functions.
"""

from click.testing import CliRunner

from arbory import basic


def test_help():
    runner = CliRunner()
    result = runner.invoke(basic, ['--help'])
    assert result.exit_code == 0
