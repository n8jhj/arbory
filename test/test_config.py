"""Test configuration use.
"""

import pathlib
import shutil

from click.testing import CliRunner
import pytest

from arbory import arb


@pytest.fixture
def temp_config(tmpdir):
    cfg_perm = pathlib.Path('arbory') / 'config.ini'
    cfg_temp = pathlib.Path(tmpdir) / 'config.ini'
    shutil.copyfile(cfg_perm, cfg_temp)
    yield
    shutil.copyfile(cfg_temp, cfg_perm)


def test_show_config():
    runner = CliRunner()
    result = runner.invoke(arb, ['config'])
    assert result.output == 'Configuration: DEFAULT\n'


@pytest.mark.usefixtures('temp_config')
def test_use_option():
    runner = CliRunner()
    result = runner.invoke(arb, ['config', '--use', 'yo'])
    assert result.output == "'yo' does not exist.\n"
    result = runner.invoke(arb, ['config', '--use', 'cobalt'])
    assert result.output == 'Configuration selected: cobalt\n'
