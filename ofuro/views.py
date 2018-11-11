from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)

from .models import GuestIntroduce, OfuroResult
from .crypturl import AESCipher


def page_transition(request):
    aes = AESCipher()
    monkey = [aes.encrypt('monkey')]
    dog = [aes.encrypt('dog')]
    duck = [aes.encrypt('duck')]
    money = [aes.encrypt('money')]
    oyaji = [aes.encrypt('oyaji')]
    nananana = [aes.encrypt('nananana')]
    seabiscuit = [aes.encrypt('seabiscuit')]
    momu = [aes.encrypt('momu')]
    mam = [aes.encrypt('mam')]
    sana = [aes.encrypt('sana')]
    chihiro = [aes.encrypt('chihiro')]
    kintanikuo = [aes.encrypt('kintanikuo')]
    higuma = [aes.encrypt('higuma')]
    amanatu = [aes.encrypt('amanatu')]
    yukariko = [aes.encrypt('yukariko')]
    sorami = [aes.encrypt('sorami')]
    beryl = [aes.encrypt('beryl')]
    haijoi = [aes.encrypt('haijoi')]
    mokyu = [aes.encrypt('mokyu')]
    mareru = [aes.encrypt('mareru')]
    ain = [aes.encrypt('ain')]
    momiji = [aes.encrypt('momiji')]
    imari = [aes.encrypt('imari')]
    # resultページのURLをネタ枠が多くなるようにランダムに選ぶ
    result_paths = monkey * 5 + dog * 5 + duck\
        + money * 5 + oyaji * 5 + nananana\
        + seabiscuit + momu * 3 + mam + sana\
        + chihiro + kintanikuo * 3 + higuma\
        + amanatu + yukariko + sorami + beryl\
        + haijoi + mokyu + mareru + ain\
        + momiji + imari
    return render(
        request, 'page_transition.html',
        {'result_paths': result_paths}
        )


def top(request):
    return render(request, 'top.html')


def wait(request):
    return render(request, 'wait.html')


def result_detail(request, enc):
    # ゲストの場合はゲスト紹介文をテンプレートに渡す
    try:
        aes = AESCipher()
        pk = aes.decrypt(enc)
        result = get_object_or_404(OfuroResult, result_id=pk)
        guest_introduces = get_list_or_404(GuestIntroduce, result=pk)
        return render(
            request,
            'result_detail.html',
            {
                'result': result,
                'guest_introduces': guest_introduces,
                'path': enc,
            }
        )
    except ValueError:
        return redirect('/wait')
    except:
        return render(
            request,
            'result_detail.html',
            {
                'result': result,
                'path': pk
            }
        )
