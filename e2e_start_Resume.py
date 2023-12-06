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
            escp_button = self.driver.find_object(By.NAME, "EscapeButton")
            self.assertTrue(escp_button.enabled)
            escp_button.tap()
            self.driver.load_scene('Game')
            score_table = self.driver.wait_for_object(By.NAME, "ScoreLabel", timeout=10)
            self.assertIsNotNone(score_table)
            resume_button = self.driver.find_object(By.NAME, "ResumeButton")
            self.assertTrue(resume_button.enabled)
            resume_button.tap()
            score_table = self.driver.wait_for_object(By.NAME, "ScoreLabel", timeout=10)
            self.assertIsNotNone(score_table)
            menu_button = self.driver.find_object(By.NAME, "MenuButton")
            self.assertTrue(menu_button.enabled)
            menu_button.tap()
            time.sleep(1.5)
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