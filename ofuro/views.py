import random

from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)

from .crypturl import AESCipher
from .models import GuestIntroduce, OfuroResult


def page_transition(request):
    if request.method == 'GET':
        # idを暗号化したものをURLにしているため全idを取得
        result_id_list = list(
            OfuroResult.objects.values_list('result_id', flat=True))
        # 暗号化
        aes = AESCipher()
        result_paths = [aes.encrypt(result_id) for result_id in result_id_list]
        # ネタ枠が多くなるようにする
        regular_staff = [aes.encrypt('monkey'), aes.encrypt('dog'), aes.encrypt('duck'), aes.encrypt('money'), aes.encrypt('oyaji')]
        for regular in regular_staff:
            for i in range(0, 9):
                result_paths.append(regular)
        result_path = random.choice(result_paths)
    elif request.method == 'POST':
        # 指名代行のとき
        try:
            order = request.POST['order']
            result_id_list = list(
                OfuroResult.objects.values_list('result_id', flat=True))
            if order not in result_id_list:
                raise Exception
            else:
                # 暗号化
                aes = AESCipher()
                result_path = aes.encrypt(order)
        except:
            return redirect('/wait')
    return render(
            request,
            'page_transition.html',
            {'result_path': result_path}
        )


def top(request):
    return render(request, 'top.html')


def staffs(request):
    # スタッフ名一覧をランダムな順番で取得
    staff_list = OfuroResult.objects.order_by('?')
    guest = OfuroResult.guestintroduce_set
    return render(
        request,
        'staffs.html',
        {
            'staffs': staff_list
        }
    )


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
                'path': enc
            }
        )
