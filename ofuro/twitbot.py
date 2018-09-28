import random
import time
from datetime import datetime, timedelta
import sched


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

    # // TODO phraseをランダムに変えるようにする（Twitterのエラー対処のため）
    def reply_result(self, twit_name):
        # TweepyでBot情報を読み込む
        # ? Bot情報を読み込むのは別メソッドを定義した方がいいかも？
        auth = tweepy.OAuthHandler(self.CK, self.CS)
        auth.set_access_token(self.AT, self.ATS)
        api = tweepy.API(auth)
        # reply用の情報
        # // TODO phraseの内容は連投エラーの保険のためにランダムにした方が良さそう
        user_name = twit_name
        # resultページのURLをネタ枠が多くなるようにランダムに選ぶ
        result_url1 = ['https://ofuro-agency.herokuapp.com/result1']    # ネタ枠
        result_url2 = ['https://ofuro-agency.herokuapp.com/result2']    # ゲスト枠
        result_url3 = ['https://ofuro-agency.herokuapp.com/result3']    # 犬枠
        result_urls = result_url1 * 20 + result_url2 * 5 + result_url3 * 2
        # 連投エラーの保険のためにフレーズを複数用意しランダムに選ぶ
        phrases = [
            'お風呂代わりに入ってきました♡',
            'お待たせいたしました♡お風呂代わりに入ってきました♡',
            'おふろ代わりに入ってきました♡',
            'おまたせいたしました♡おふろ代わりに入ってきました♡'
            ]
        phrase = '{text}\n{url}'.format(
            text=random.choice(phrases),
            url=random.choice(result_urls)
        )
        # reply
        api.update_status('@' + user_name + '\n\n' + phrase)

    # 10分後に実行するスクリプト頑張って考えたのに...
    # これをTwitter認証後に呼び出されるビュー関数のなかで実行したら600秒間次の画面行くまでステイさせられるクソ仕様になったので一旦使用しない
    def reply_after_10min(self, twit_name):
        # 10分後にreply
        scheduler = sched.scheduler(time.time, time.sleep)
        scheduler.enter(600, 1, self.reply_result, argument=[twit_name])
        scheduler.run()
