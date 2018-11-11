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
    # resultページのURLをネタ枠が多くなるようにランダムに選ぶ
    result_paths = ['monkey'] * 5 + ['dog'] * 5 + ['duck']\
        + ['money'] * 5 + ['oyaji'] * 5 + ['nananana']\
        + ['seabiscuit'] + ['momu'] * 3 + ['mam'] + ['sana']\
        + ['chihiro'] + ['kintanikuo'] * 3 + ['higuma']\
        + ['amanatu'] + ['yukariko'] + ['sorami'] + ['beryl']\
        + ['haijoi'] + ['mokyu'] + ['mareru'] + ['ain']\
        + ['momiji'] + ['imari']
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
        guest_introduces = get_list_or_404(GuestIntroduce, result=pk)
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
