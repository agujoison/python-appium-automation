import unittest

from screens import log_text_box, api_demo, text_demo
from config import config


class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        self.driver = config.Config.get_driver()

        self.log_text_box_screen = log_text_box.LogTextBox(self.driver)
        self.api_demo_screen = api_demo.ApiDemo(self.driver)
        self.text_demo_screen = text_demo.TextDemo(self.driver)

    def test_log_text_box(self):
        self.api_demo_screen.open_text_option()
        self.text_demo_screen.open_log_text_box_option()
        self.log_text_box_screen.add_text_log()

        self.assertEqual(self.log_text_box_screen.get_text_log(), 'This is a test')

    def tearDown(self):
        # end the session
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
