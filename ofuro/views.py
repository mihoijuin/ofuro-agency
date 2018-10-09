from concurrent.futures import ThreadPoolExecutor
import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from social_django.models import UserSocialAuth

from .twitbot import TweetBot
from .crypturl import AESCipher


def encrypt_path(path):    # urls.pyでも使い回せるようにURL全部でなくパスを暗号化
    key = 'poriporiporiofuroporipori'
    aes = AESCipher(key)
    enc_path = aes.encrypt(aes.key, path)
    return enc_path


def top(request):
    # URLを暗号化
    try:
        root_url = 'https://ofuro-agency.herokuapp.com/'
        result_monkey = [root_url + 'LofG1lC3uIf7XnD6awGDw==']
        result_dog = [root_url + encrypt_path('result-dog')]
        result_duck = [root_url + encrypt_path('result-duck')]
        result_nananana = [root_url + encrypt_path('result-nananana')]
        result_money = [root_url + encrypt_path('result-money')]
        result_oyaji = [root_url + encrypt_path('result-oyaji')]
        result_seabiscuit = [root_url + 'mmDtzcWuWnC0pYkMBEugKgR5rXLRQRKv02WLfTIvzM=']
        # resultページのURLをネタ枠が多くなるようにランダムに選ぶ
        result_urls = result_monkey * 2 + result_dog * 1 + result_duck * 1 + result_nananana * 1 + result_money * 5 + result_oyaji * 5 + result_seabiscuit * 1
        return render(request, 'top.html', {'result_urls': result_urls})
    except:
        return redirect('/wait')


def wait(request):
    return render(request, 'wait.html')


# TODO できたら各ビューで画像数種類をランダムに表示できるようにしたい...
# TODO 画像を管理画面から投稿してどんどんページを作成できるようにするのが理想
# resultへすんなり遷移させたくなかったのでsleep挟む
def result_monkey(request):
    time.sleep(2)
    return render(request, 'result_monkey.html')


def result_dog(request):
    time.sleep(2)
    return render(request, 'result_dog.html')


def result_duck(request):
    time.sleep(2)
    return render(request, 'result_duck.html')


def result_nananana(request):
    time.sleep(2)
    return render(request, 'result_nananana.html')


def result_money(request):
    time.sleep(2)
    return render(request, 'result_money.html')


def result_oyaji(request):
    time.sleep(2)
    return render(request, 'result_oyaji.html')


def result_seabiscuit(request):
    time.sleep(2)
    return render(request, 'result_seabiscuit.html')



def result_momu(request):
    time.sleep(2)
    return render(request, 'result_momu.html')

# @login_required
# def ordered(request):
#     user = UserSocialAuth.objects.get(user_id=request.user.id)
#     # Twitter認証後、ordered.htmlを表示させつつ裏でBotを動かし10分後にリプライさせる
#     # // TODO 例外発生した時にはすでにorderedに飛んでしまってるので例外処理を考え直す
#     try:
#         bot = TweetBot()
#         executor = ThreadPoolExecutor(max_workers=2)
#         executor.submit(
#             bot.reply_after_10min,
#             user.access_token['screen_name']
#             )
#     except:
#         bot = TweetBot()
#         bot.reply_error(user.access_token['screen_name'])
#         return redirect('/wait')
#     return render(request, 'ordered.html')
