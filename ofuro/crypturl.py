from Crypto.Cipher import AES
import base64


class AESCipher:
    def __init__(self, key):
        self.key = key
        self.iv = 'L3n0G2m0iGvs9On7'     # 初期化ベクトル（16文字の適当な値を指定）
        self.mode = AES.MODE_CBC     # 暗号化モードを指定

    def mkpad(self, data, size):
        '''
        特定の文字数にするため空白を埋める
        '''
        # utf-8文字列をバイト列に変換
        data = data.encode('utf-8')
        # 特定の長さの倍数にするのにたりない分だけの空白を生成
        pad = b' ' * (size - len(data) % size)
        return data + pad

    def encrypt(self, key, data):
        '''暗号化する'''
        # 特定の長さに調整
        data = self.mkpad(data, 16)
        # キーが16文字以下の時の対策にmkpad()で16の倍数に整形
        key = self.mkpad(key, 16)
        # キーを16文字にスライス
        key = key[:16]
        # 暗号化
        aes = AES.new(key, self.mode, self.iv)
        data_cipher = aes.encrypt(data)
        return base64.b64encode(data_cipher).decode('utf-8')

    def decrypt(self, key, encdata):
        '''複合化する'''
        # キーの文字数を調節
        key = self.mkpad(key, 16)
        key = key[:16]
        # 複合化
        aes = AES.new(key, self.mode, self.iv)
        encdata = base64.b64decode(encdata)     # バイト列に
        data = aes.decrypt(encdata)
        return data.decode('utf-8')     # バイト列を文字列に


# 使用例
# from crypturl import AESCipher
# key = 'poriporiporiofuroporipori'
# aes = AESCipher(key)
# url = 'https://ofuro-agency.herokuapp.com/result-dog'
# enc = aes.encrypt(aes.key, url)
# dec = aes.decrypt(aes.key, enc)
