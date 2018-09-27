from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth

from .twitbot import TweetBot


@login_required
def ordered(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    # TODO テンプレートを読み込む動作を止めずに、Botメソッドを起動するのを10分後にしたい
    # ? 並行処理かな？とは思っている
    try:
        reply_bot = TweetBot()
        reply_bot.reply_result(user.access_token['screen_name'])
    except:
        return render(request, 'wait.html')
    return render(request, 'ordered.html', {'user': user})
