import unittest
from pathlib import Path

from src.envutil import Config, EnvConst


class EnvUtilTest(unittest.TestCase):
	BASE_DIR = Path(__file__).parent.parent.resolve().joinpath('test_data').__str__()

	def setUp(self) -> None:
		Config.load(env_path=self.BASE_DIR, main_file='.env', local_file='.env.local')

	def test_load_env(self):
		self.assertTrue(Config.is_loaded())

	def test_get_config(self):
		self.assertEqual(Config.get(EnvConst.PYENV_LOAD_STATUS_KEY).as_str(), '1')
		self.assertEqual(Config.get(EnvConst.PYENV_LOAD_STATUS_KEY).as_int(), 1)
		self.assertEqual(Config.get(EnvConst.PYENV_LOAD_STATUS_KEY).as_bool(), True)
		self.assertEqual(Config.get(EnvConst.PYENV_LOAD_STATUS_KEY).as_float(), 1.0)
