
import requests
from io import BytesIO
from pyzbar import pyzbar
from PIL import Image,ImageEnhance


def decode_qr(img_adds):

    # 从网络下载并加载二维码图片
    rq_img = requests.get(img_adds).content
    img = Image.open(BytesIO(rq_img))

    # img.show()  # 显示图片，测试用

    txt_list = pyzbar.decode(img)

    for txt in txt_list:
        barcodeData = txt.data.decode("utf-8")
        return barcodeData

if __name__ == '__main__':


    # 解析网络二维码
    print(decode_qr('http://47.56.193.188:80/nginx_upload/qrcode/df844564c507c11caee4a8ee9d92d21d_00000003.jpeg'))
