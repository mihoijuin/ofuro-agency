import random
import sched
import time


import tweepy


from .crypturl import AESCipher


# ?本当はTweetBotで基本的なリプライやBot情報読み込みのメソッドを定義して、OfuroBotクラスで継承した上でカスタマイズするのが良いのだと思う
# ?だがまずは完成するのが先決なのでこのままやる
class TweetBot():
    # // TODO __init__で書き換えられないか試す（クラス変数は外部から上書きできてしまってあんまよくないため）
    def __init__(self):
        self.CK = 'cQJQwfbViw7F4wiKwnayEnNZG'
        self.CS = 'fPgufYNM41qTrXA7nFRgGZLxG8V0nqZewKSbtyyVtnPnBn21gW'
        self.AT = '953117369609568257-X9GsNc0kSIdGaUBaVtLqJyYWYoGNolE'
        self.ATS = 'Ssw5hIi7pfkeWKpJVjQrzN3ylsGnVQosiGX3STaRswiIM'

    def encrypt_path(self, path):    # urls.pyでも使い回せるようにURL全部でなくパスを暗号化
        key = 'poriporiporiofuroporipori'
        aes = AESCipher(key)
        enc_path = aes.encrypt(aes.key, path)
        return enc_path

    def auth_tweepy(self):
        auth = tweepy.OAuthHandler(self.CK, self.CS)
        auth.set_access_token(self.AT, self.ATS)
        api = tweepy.API(auth)
        return api

    def reply_result(self, twit_name):
        # URLを暗号化
        root_url = 'https://ofuro-agency.herokuapp.com/'
        result_monkey = [root_url + self.encrypt_path('result-monkey')]
        result_dog = [root_url + self.encrypt_path('result-dog')]
        result_duck = [root_url + self.encrypt_path('result-duck')]
        result_nananana = [root_url + self.encrypt_path('result-nananana')]
        result_money = [root_url + 'LofG1lC3uIf7XnD6awGDw==']
        result_oyaji = [root_url + self.encrypt_path('result-oyaji')]
        # resultページのURLをネタ枠が多くなるようにランダムに選ぶ
        result_urls = result_monkey * 1 + result_dog * 1 + result_duck * 1 + result_nananana * 1 + result_money * 5 + result_oyaji * 5
        # 連投エラーの保険のためにフレーズを複数用意しランダムに選ぶ
        phrases = [
            'お風呂代わりに入ってきました♨️ええお湯でした♨️',
            'お待たせいたしました！お風呂代わりに入ってきました♨️ええお湯でした♨️',
            'おふろ代わりに入ってきました〜🛀お風呂さいこう〜♨️',
            'おまたせいたしました！おふろ代わりに入ってきました♨️お風呂最高🛀',
            'ふぅ〜〜〜♨️いいお湯いただきました🛀'
            ]
        phrase = '{text}\n#お風呂めんどいときはお風呂代理店へ\n\n代行内容をご確認ください↓\n{url}'.format(
            text=random.choice(phrases),
            url=random.choice(result_urls)
        )
        image = './ofuro/static/images/ofuro-silhouette.png'
        # reply
        api = self.auth_tweepy()    # TweepyでBotの情報を読み込む
        api.update_with_media(image, status='@' + twit_name + '\n\n' + phrase)

    def reply_after_10min(self, twit_name):
        '''10分後にreply'''
        scheduler = sched.scheduler(time.time, time.sleep)
        scheduler.enter(600, 1, self.reply_result, argument=[twit_name])
        scheduler.run()

    def reply_error(self, twit_name):
        # TweepyでBot情報を読み込む
        api = self.auth_tweepy()
        phrase = '申し訳ございません🙇‍ただいま代行スタッフが全員入浴中です🙇‍\n時間を置いてお試しいただくか、頑張って自分で入浴いただけますと幸いです🐤\n'
        url = 'https://ofuro-agency.herokuapp.com/wait'
        api.update_status('@' + twit_name + '\n\n' + phrase + '\n' + url)
