from concurrent.futures import ThreadPoolExecutor
import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404

from .models import OfuroResult, GuestIntroduce
from .crypturl import AESCipher

# def encrypt_path(path):    # urls.pyでも使い回せるようにURL全部でなくパスを暗号化
#     '''結果ページのURLをパッと見てわからなくするために暗号化'''
#     aes = AESCipher()
#     enc_path = aes.encrypt(path)
#     return enc_path


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


def result_detail(request, pk):
    result = get_object_or_404(OfuroResult, pk=pk)
    # ゲストの場合はゲスト紹介文をテンプレートに渡す
    try:
        guest_introduces = GuestIntroduce.objects.get(result=pk)
        return render(
            request,
            'result_detail.html',
            {
                'result': result,
                'guest_introduces': guest_introduces,
                'path': pk
            }
        )
    except:
        return render(
            request,
            'result_detail.html',
            {
                'result': result,
                'path': pk
            }
        )
    # aes = AESCipher()
    # result_id = aes.decrypt(encrypt_pk)
    # result = get_object_or_404(OfuroResult, pk=pk)
    # guest_introduces = get_list_or_404(GuestIntroduce, result=result_id)
