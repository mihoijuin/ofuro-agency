from concurrent.futures import ThreadPoolExecutor

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from social_django.models import UserSocialAuth

from .twitbot import TweetBot


@login_required
def wait(request):
    return render(request, 'wait.html')


@login_required
def ordered(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    # Twitter認証後、ordered.htmlを表示させつつ裏でBotを動かし10分後にリプライさせる
    # // TODO 例外発生した時にはすでにorderedに飛んでしまってるので例外処理を考え直す
    try:
        bot = TweetBot()
        executor = ThreadPoolExecutor(max_workers=2)
        executor.submit(
            bot.reply_after_10min,
            user.access_token['screen_name']
            )
    except:
        bot = TweetBot()
        bot.reply_error(user.access_token['screen_name'])
        return redirect('/wait')
    return render(request, 'ordered.html')


# TODO できたら各ビューで画像数種類をランダムに表示できるようにしたい...
# TODO 画像を管理画面から投稿してどんどんページを作成できるようにするのが理想

def result-monkey(request):
    return render(request, 'result-monkey.html')


def result-dog(request):
    return render(request, 'result-dog.html')


def result-duck(request):
    return render(request, 'result-duck.html')


def result-nananana(request):
    return render(request, 'result-nananana.html')


def result-money(request):
    return render(request, 'result-money.html')


def result-oyaji(request):
    return render(request, 'result-oyaji.html')
