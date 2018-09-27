import tweepy


class TweetBot():
    # TODO __init__で書き換えられないか試す（クラス変数は外部から上書きできてしまってあんまよくないため）
    consumer_key = 'cQJQwfbViw7F4wiKwnayEnNZG'
    consumer_secret = 'fPgufYNM41qTrXA7nFRgGZLxG8V0nqZewKSbtyyVtnPnBn21gW'
    access_token = '953117369609568257-X9GsNc0kSIdGaUBaVtLqJyYWYoGNolE'
    access_token_secret = 'Ssw5hIi7pfkeWKpJVjQrzN3ylsGnVQosiGX3STaRswiIM'

    def reply_result(self, twit_name):
        # TweepyでBot情報を読み込む
        # ? Bot情報を読み込むのは別メソッドを定義した方がいいかも？
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        # reply用の情報
        user_name = twit_name
        result_url = '<result画面のURL>'
        phrase = '{name}様の代わりにお風呂代行しました♡\n{url}'.format(
            name=user_name,
            url=result_url
            )
        # reply
        api.update_status('@' + user_name + '\n' + phrase)
