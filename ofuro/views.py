from concurrent.futures import ThreadPoolExecutor
import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from social_django.models import UserSocialAuth

from .twitbot import TweetBot
from .crypturl import AESCipher


def encrypt_path(path):    # urls.pyでも使い回せるようにURL全部でなくパスを暗号化
    '''結果ページのURLをパッと見てわからなくするために暗号化'''
    aes = AESCipher()
    enc_path = aes.encrypt(path)
    return enc_path


def page_transition(request):
    # ランダム表示する結果URLリストを作成（URLは暗号化）
    result_monkey = [encrypt_path('result-monkey')]
    result_dog = [encrypt_path('result-dog')]
    result_duck = [encrypt_path('result-duck')]
    result_nananana = [encrypt_path('result-nananana')]
    result_muscle_nananana = [encrypt_path('result-muscle_nananana')]
    result_money = [encrypt_path('result-money')]
    result_oyaji = [encrypt_path('result-oyaji')]
    result_seabiscuit = [encrypt_path('result-seabiscuit')]
    result_momu = [encrypt_path('result-momu')]
    result_sana = [encrypt_path('result-sana')]
    result_chihiro = [encrypt_path('result-chihiro')]
    result_higuma = [encrypt_path('result-higuma')]
    result_yukariko = [encrypt_path('result-yukariko')]
    result_sorami = [encrypt_path('result-sorami')]
    result_mokyu = [encrypt_path('result-mokyu')]
    result_momiji = [encrypt_path('result-momiji')]
    result_imari = [encrypt_path('result-imari')]
    result_ain = [encrypt_path('result-ain')]
    result_mareru = [encrypt_path('result-mareru')]
    result_haijoi = [encrypt_path('result-haijoi')]
    result_amanatu = [encrypt_path('result-amanatu')]
    result_mam = [encrypt_path('result-mam')]
    result_beryl = [encrypt_path('result-beryl')]
    # resultページのURLをネタ枠が多くなるようにランダムに選ぶ
    result_paths = result_monkey * 5 + result_dog * 5 + result_duck\
        + result_money * 5 + result_oyaji * 5 + result_nananana\
        + result_seabiscuit + result_momu * 3 + result_mam + result_sana\
        + result_chihiro + result_muscle_nananana * 3 + result_higuma\
        + result_amanatu + result_yukariko + result_sorami + result_beryl\
        + result_haijoi + result_mokyu + result_mareru + result_ain\
        + result_momiji + result_imari
    return render(
        request, 'page_transition.html',
        {'result_paths': result_paths}
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


def result_mareru(request):
    try:
        return render(request, 'result_mareru.html')
    except:
        return redirect('/wait')


def result_ain(request):
    try:
        return render(request, 'result_ain.html')
    except:
        return redirect('/wait')


def result_momiji(request):
    try:
        return render(request, 'result_momiji.html')
    except:
        return redirect('/wait')


def result_imari(request):
    try:
        return render(request, 'result_imari.html')
    except:
        return redirect('/wait')
