import unittest
import time
from alttester import *


class MyFirstTest(unittest.TestCase):

    altdriver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = AltDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.stop()

    def test_start_game_exit(self):
        try:
            self.driver.load_scene('Menu')
            escp_button = self.driver.find_object(By.NAME, "MoreGamesButton")
            self.assertTrue(escp_button.enabled)
            escp_button.tap()
            time.sleep(2)
            self.driver.load_scene('Menu')
            exit_button = self.driver.find_object(By.NAME, "ExitButton")
            self.assertTrue(exit_button.enabled)
            time.sleep(1)
            exit_button.tap()

        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

        finally:
            self.driver.stop()
