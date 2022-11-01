# anydesk cn relay scan
from bs4 import BeautifulSoup
import httpx

url = 'https://domain.glass/net.anydesk.com.cn'
# anydesk 配置文件
anydesk_conf = 'C:\\Users\\WIN10\\AppData\\Roaming\\AnyDesk\\system.conf'
 
client = httpx.Client(http2=True, verify=False)
headers = {
    'authority': 'domain.glass',
    'method': 'GET',
    'path': '/net.anydesk.com.cn',
    'scheme': 'https',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'zh-CN,zh;q=0.9'
}

resp = client.get(url, headers=headers)
soup = BeautifulSoup(resp,"html.parser")

with open(anydesk_conf, mode='a') as conf:
    for a in soup.find_all('a'):
        if a.string != None and a.string.startswith('relay'):
           print(a.string)
           conf.write('\n')
           conf.write("ad.anynet.last_relay={}:80:443:6568".format(a.string))  

conf.close()           