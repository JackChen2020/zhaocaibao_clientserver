import  requests, json


def decode_qr(qr_url):
    host = 'http://qrapi.market.alicloudapi.com'
    path = '/yunapi/qrdecode.html'
    appcode = 'b50239aa446f477d8e2738e1c2f31bde'
    bodys = {}
    url = host + path

    bodys['imgurl'] = qr_url
    bodys['version'] = '''1.1'''

    headers={
        'Authorization':'APPCODE ' + appcode,
        'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8"
    }

    try:
        html = requests.post(url=url,data=bodys,headers=headers)
        return json.loads(html.text)['data']['raw_text']
    except:
        return None

if __name__ == '__main__':


    # 解析网络二维码
    print(decode_qr('http://47.56.193.188:80/nginx_upload/qrcode/c5743b67c0e20849577203e604d38b25_00000050.jpeg'))