from django.test import TestCase

from twitbot import TweetBot

# Create your tests here.
if __name__ == '__main__':
    bot = TweetBot()
    bot.reply_result('iju_miho')
