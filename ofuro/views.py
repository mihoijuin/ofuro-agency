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
result_yukariko = [root_url + encrypt_path('result-yukariko')]
result_sorami = [root_url + encrypt_path('result-sorami')]
result_mokyu = [root_url + encrypt_path('result-mokyu')]
result_haijoi = [root_url + 'zRdifYIsoUzKIBWCyz8vA==']
result_amanatu = [root_url + 'Hplos4rCjLihwEng3Ow==']
result_mam = [root_url + 'gunY0ZDCpndh1PkTaRRNw==']
result_beryl = [root_url + 'Gqpi2dVPDOVSBVdB6qRg==']
# resultページのURLをネタ枠が多くなるようにランダムに選ぶ
result_urls = result_monkey * 11 + result_dog * 13 + result_duck * 3\
    + result_money * 15 + result_oyaji * 15 + result_nananana\
    + result_seabiscuit + result_momu + result_mam + result_sana\
    + result_chihiro + result_muscle_nananana * 3 + result_higuma\
    + result_amanatu + result_yukariko + result_sorami + result_beryl\
    + result_haijoi + result_mokyu


def page_transition(request):
    time.sleep(2)
    return render(
        request, 'page_transition.html',
        {'result_urls': result_urls}
        )


def top(request):
    return render(request, 'top.html')


def wait(request):
    return render(request, 'wait.html')


# TODO できたら各ビューで画像数種類をランダムに表示できるようにしたい...
# TODO 画像を管理画面から投稿してどんどんページを作成できるようにするのが理想
# resultへすんなり遷移させたくなかったのでsleep挟む
def result_monkey(request):
    try:
        return render(request, 'result_monkey.html')
    except:
        return redirect('/wait')


def result_dog(request):
    try:
        return render(request, 'result_dog.html')
    except:
        return redirect('/wait')


def result_duck(request):
    try:
        return render(request, 'result_duck.html')
    except:
        return redirect('/wait')


def result_nananana(request):
    try:
        return render(request, 'result_nananana.html')
    except:
        return redirect('/wait')


def result_muscle_nananana(request):
    try:
        return render(request, 'result_muscle_nananana.html')
    except:
        return redirect('/wait')


def result_money(request):
    try:
        return render(request, 'result_money.html')
    except:
        return redirect('/wait')


def result_oyaji(request):
    try:
        return render(request, 'result_oyaji.html')
    except:
        return redirect('/wait')


def result_seabiscuit(request):
    try:
        return render(request, 'result_seabiscuit.html')
    except:
        return redirect('/wait')


def result_momu(request):
    try:
        return render(request, 'result_momu.html')
    except:
        return redirect('/wait')


def result_mam(request):
    try:
        return render(request, 'result_mam.html')
    except:
        return redirect('/wait')


def result_sana(request):
    try:
        return render(request, 'result_sana.html')
    except:
        return redirect('/wait')


def result_chihiro(request):
    try:
        return render(request, 'result_chihiro.html')
    except:
        return redirect('/wait')


def result_higuma(request):
    try:
        return render(request, 'result_higuma.html')
    except:
        return redirect('/wait')


def result_amanatu(request):
    try:
        return render(request, 'result_amanatu.html')
    except:
        return redirect('/wait')


def result_sorami(request):
    try:
        return render(request, 'result_sorami.html')
    except:
        return redirect('/wait')


def result_yukariko(request):
    try:
        return render(request, 'result_yukariko.html')
    except:
        return redirect('/wait')


def result_beryl(request):
    try:
        return render(request, 'result_beryl.html')
    except:
        return redirect('/wait')


def result_haijoi(request):
    try:
        return render(request, 'result_haijoi.html')
    except:
        return redirect('/wait')


def result_mokyu(request):
    try:
        return render(request, 'result_mokyu.html')
    except:
        return redirect('/wait')
