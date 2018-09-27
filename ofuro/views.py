from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth

from .twitbot import TweetBot


def wait(request):
    return render(request, 'wait.html')


@login_required
def ordered(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    # TODO テンプレートを読み込む動作を止めずに、Botメソッドを起動するのを10分後にしたい
    # ? 並行処理かな？とは思っている
    try:
        reply_bot = TweetBot()
        # TODO ここでスクリーンネームでなくユーザ名を表示する方法がわからない...
        reply_bot.reply_result(user.access_token['screen_name'])
    except:
        return redirect('/wait')
    return render(request, 'ordered.html', {'user': user})

