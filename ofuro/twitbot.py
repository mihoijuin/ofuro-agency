import random
import sched
import time
from datetime import datetime, timedelta

import tweepy


# ?本当はTweetBotで基本的なリプライやBot情報読み込みのメソッドを定義して、OfuroBotクラスで継承した上でカスタマイズするのが良いのだと思う
# ?だがまずは完成するのが先決なのでこのままやる
class TweetBot():
    # // TODO __init__で書き換えられないか試す（クラス変数は外部から上書きできてしまってあんまよくないため）
    def __init__(self):
        self.CK = 'cQJQwfbViw7F4wiKwnayEnNZG'
        self.CS = 'fPgufYNM41qTrXA7nFRgGZLxG8V0nqZewKSbtyyVtnPnBn21gW'
        self.AT = '953117369609568257-X9GsNc0kSIdGaUBaVtLqJyYWYoGNolE'
        self.ATS = 'Ssw5hIi7pfkeWKpJVjQrzN3ylsGnVQosiGX3STaRswiIM'

    def auth_tweepy(self):
        auth = tweepy.OAuthHandler(self.CK, self.CS)
        auth.set_access_token(self.AT, self.ATS)
        api = tweepy.API(auth)
        return api

    def reply_result(self, twit_name):
        # TweepyでBot情報を読み込む
        api = self.auth_tweepy()
        # // ? Bot情報を読み込むのは別メソッドを定義した方がいいかも？
        # reply用の情報
        user_name = twit_name
        # resultページのURLをネタ枠が多くなるようにランダムに選ぶ
        result_url1 = ['https://ofuro-agency.herokuapp.com/result1']    # ネタ枠
        result_url2 = ['https://ofuro-agency.herokuapp.com/result2']    # 犬枠
        result_url3 = ['https://ofuro-agency.herokuapp.com/result3']    # アヒル枠
        result_urls = result_url1 * 10 + result_url2 * 5 + result_url3 * 2
        # 連投エラーの保険のためにフレーズを複数用意しランダムに選ぶ
        phrases = [
            'お風呂代わりに入ってきました♡',
            'お待たせいたしました♡お風呂代わりに入ってきました♡',
            'おふろ代わりに入ってきました♡',
            'おまたせいたしました♡おふろ代わりに入ってきました♡'
            ]
        phrase = '{text}\n#お風呂めんどいときはお風呂代理店へ\n\n結果を見る↓\n{url}'.format(
            text=random.choice(phrases),
            url=random.choice(result_urls)
        )
        image = './ofuro/static/images/ofuro-silhouette.png'
        # reply
        api.update_with_media(image, status='@' + user_name + '\n\n' + phrase)

    def reply_after_10min(self, twit_name):
        '''10分後にreply'''
        scheduler = sched.scheduler(time.time, time.sleep)
        scheduler.enter(600, 1, self.reply_result, argument=[twit_name])
        scheduler.run()

    def reply_error(self, twit_name):
        # TweepyでBot情報を読み込む
        api = self.auth_tweepy()
        user_name = twit_name
        phrase = '申し訳ございません🙇‍ただいま代行スタッフが全員入浴中です🙇‍\n時間を置いてお試しいただくか、頑張って自分で入浴いただけますと幸いです🐤\n'
        url = 'https://ofuro-agency.herokuapp.com/wait'
        api.update_status('@' + user_name + '\n\n' + phrase + '\n' + url)
