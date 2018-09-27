import tweepy


class TweetBot():
    # //d TODO __init__で書き換えられないか試す（クラス変数は外部から上書きできてしまってあんまよくないため）
    def __init__(self):
        self.CK = 'cQJQwfbViw7F4wiKwnayEnNZG'
        self.CS = 'fPgufYNM41qTrXA7nFRgGZLxG8V0nqZewKSbtyyVtnPnBn21gW'
        self.AT = '953117369609568257-X9GsNc0kSIdGaUBaVtLqJyYWYoGNolE'
        self.ATS = 'Ssw5hIi7pfkeWKpJVjQrzN3ylsGnVQosiGX3STaRswiIM'

    def reply_result(self, twit_name):
        # TweepyでBot情報を読み込む
        # ? Bot情報を読み込むのは別メソッドを定義した方がいいかも？
        auth = tweepy.OAuthHandler(self.CK, self.CS)
        auth.set_access_token(self.AT, self.ATS)
        api = tweepy.API(auth)
        # reply用の情報
        user_name = twit_name
        result_url = '<result画面のURL>'
        phrase = '{name}さまの代わりにお風呂代行しました♡\n{url}'.format(
            name=user_name,
            url=result_url
            )
        # reply
        api.update_status('@' + user_name + '\n' + phrase)
