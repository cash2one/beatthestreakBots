from bot import Bot
import unittest

class TestBot(unittest.TestCase):
    pass
    def setUp(self):
        self.bot = Bot('frahman305@gmail.com', 'fymze812')

    def tearDown(self):
        self.bot.quit_browser()

    def test_get_login_page(self):
        loginTitle = 'Account Management - Login/Register | MLB.com: Account'
        self.bot.get_login_page()
        self.assertTrue(loginTitle in self.bot.get_browser().title)