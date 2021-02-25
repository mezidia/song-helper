"""Main file of test system"""
import os
import unittest

import requests


class Parent:
    """Parent class with need variables"""
    token = os.getenv('TOKEN')
    url = f'https://api.telegram.org/bot{token}/'
    ok_status_code = 200
    bot_name = 'Telegram Keep'
    test_text = 'test'
    chat_id = os.getenv('CHAT_ID')


class TelegramTest(unittest.TestCase, Parent):
    """Class for testing connecting with Telegram API"""

    def setUp(self):
        """Make requests"""
        self.getMe = requests.get(self.url + 'getMe')
        self.sendMessage = requests.get(
            self.url + f'sendMessage?chat_id={self.chat_id}&text={self.test_text}')

    def test_conn(self):
        """Test connection with different methods"""
        self.assertEqual(self.getMe.status_code, self.ok_status_code)
        self.assertEqual(self.sendMessage.status_code, self.ok_status_code)

    def test_fields(self):
        """Test fields from different request methods"""
        self.assertTrue(self.getMe.json()["ok"])
        self.assertTrue(self.sendMessage.json()["ok"])
        self.assertTrue(self.getMe.json()["result"]["is_bot"])
        self.assertFalse(
            self.getMe.json()["result"]["can_read_all_group_messages"])
        self.assertFalse(
            self.getMe.json()["result"]["supports_inline_queries"])
        self.assertEqual(
            self.getMe.json()["result"]["first_name"],
            self.bot_name)
        self.assertEqual(
            self.sendMessage.json()["result"]["text"],
            self.test_text)