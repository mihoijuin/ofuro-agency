from concurrent.futures import ThreadPoolExecutor
import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from social_django.models import UserSocialAuth

from .twitbot import TweetBot
from .crypturl import AESCipher


def encrypt_path(path):    # urls.pyでも使い回せるようにURL全部でなくパスを暗号化
    '''結果ページのURLをパッと見てわからなくするために暗号化'''
    key = 'poriporiporiofuroporipori'
    aes = AESCipher(key)
    enc_path = aes.encrypt(aes.key, path)
    return enc_path


# ランダム表示する結果URLリストを作成（URLは暗号化）
# 複数のビューで呼び出すため、グローバル変数に代入
root_url = 'https://ofuro-agency.herokuapp.com/'
result_monkey = [root_url + 'LofG1lC3uIf7XnD6awGDw==']
result_dog = [root_url + encrypt_path('result-dog')]
result_duck = [root_url + encrypt_path('result-duck')]
result_nananana = [root_url + encrypt_path('result-nananana')]
result_muscle_nananana = [root_url + encrypt_path('result-muscle_nananana')]
result_money = [root_url + encrypt_path('result-money')]
result_oyaji = [root_url + encrypt_path('result-oyaji')]
result_seabiscuit = [root_url + 'mmDtzcWuWnC0pYkMBEugKgR5rXLRQRKv02WLfTIvzM=']
result_momu = [root_url + encrypt_path('result-momu')]
result_sana = [root_url + encrypt_path('result-sana')]
result_chihiro = [root_url + encrypt_path('result-chihiro')]
result_higuma = [root_url + encrypt_path('result-higuma')]
result_amanatu = [root_url + 'Hplos4rCjLihwEng3Ow==']
result_mam = [root_url + 'gunY0ZDCpndh1PkTaRRNw==']
# resultページのURLをネタ枠が多くなるようにランダムに選ぶ
result_urls = result_monkey + result_dog + result_duck + result_money * 8\
    + result_oyaji * 8 + result_nananana + result_seabiscuit + result_momu\
    + result_mam + result_sana + result_chihiro + result_muscle_nananana * 3\
    + result_higuma + result_amanatu


def top(request):
    return render(request, 'top.html', {'result_urls': result_urls})


def wait(request):
    return render(request, 'wait.html')


# TODO できたら各ビューで画像数種類をランダムに表示できるようにしたい...
# TODO 画像を管理画面から投稿してどんどんページを作成できるようにするのが理想
# resultへすんなり遷移させたくなかったのでsleep挟む
def result_monkey(request):
    time.sleep(2)
    try:
        return render(request, 'result_monkey.html', {'result_urls': result_urls})
    except:
        return redirect('/wait')


def result_dog(request):
    time.sleep(2)
    try:
        return render(request, 'result_dog.html', {'result_urls': result_urls})
    except:
        return redirect('/wait')


def result_duck(request):
    time.sleep(2)
    try:
        return render(request, 'result_duck.html', {'result_urls': result_urls})
    except:
        return redirect('/wait')


def result_nananana(request):
    time.sleep(2)
    try:
        return render(
            request, 'result_nananana.html', {'result_urls': result_urls}
            )
    except:
        return redirect('/wait')


def result_muscle_nananana(request):
    time.sleep(2)
    try:
        return render(
            request, 'result_muscle_nananana.html',
            {'result_urls': result_urls}
            )
    except:
        return redirect('/wait')


def result_money(request):
    time.sleep(2)
    try:
        return render(
            request, 'result_money.html', {'result_urls': result_urls}
            )
    except:
        return redirect('/wait')


def result_oyaji(request):
    time.sleep(2)
    try:
        return render(
            request, 'result_oyaji.html', {'result_urls': result_urls}
            )
    except:
        return redirect('/wait')


def result_seabiscuit(request):
    time.sleep(2)
    try:
        return render(
            request, 'result_seabiscuit.html', {'result_urls': result_urls}
            )
    except:
        return redirect('/wait')


def result_momu(request):
    time.sleep(2)
    try:
        return render(
            request, 'result_momu.html', {'result_urls': result_urls}
            )
    except:
        return redirect('/wait')


def result_mam(request):
    time.sleep(2)
    try:
        return render(
            request, 'result_mam.html', {'result_urls': result_urls}
            )
    except:
        return redirect('/wait')


def result_sana(request):
    time.sleep(2)
    try:
        return render(
            request, 'result_sana.html', {'result_urls': result_urls}
            )
    except:
        return redirect('/wait')


def result_chihiro(request):
    time.sleep(2)
    try:
        return render(
            request, 'result_chihiro.html', {'result_urls': result_urls}
            )
    except:
        return redirect('/wait')


def result_higuma(request):
    time.sleep(2)
    try:
        return render(
            request, 'result_higuma.html', {'result_urls': result_urls}
            )
    except:
        return redirect('/wait')


def result_amanatu(request):
    time.sleep(2)
    try:
        return render(
            request, 'result_amanatu.html', {'result_urls': result_urls}
            )
    except:
        return redirect('/wait')
