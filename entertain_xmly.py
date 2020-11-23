import json
import random
import time
from concurrent import futures

import requests


class EntertainXMLY():
    user_agents = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        "UCWEB7.0.2.37/28/999",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        "Openwave/ UCWEB7.0.2.37/28/999",
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
        "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

    ]
    header = {
        'User-Agent': random.choice(user_agents),
        'Referer': 'https://www.ximalaya.com/category/',
        'Host': 'www.ximalaya.com',
        'Accept': 'application/json, */*',
        'Connection': 'close'
    }


    start_urls = [
        'https://www.ximalaya.com/revision/category/allCategoryInfo',
        'https://www.ximalaya.com/revision/category/queryCategoryPageAlbums?category={pinyin}&subcategory={code}',
        'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId={albumId}&pageNum={pageNum}'
    ]


    def get_category(self):
        content = self.request(self.start_urls[0])
        if content:
            data = content.get('data')
            for temp in data:
                categories = temp.get('categories')
                for category in categories:
                    category_type = category.get('displayName')
                    category_pinyin = category.get('pinyin')
                    sub_categories = category.get('subcategories')
                    thread_pool = futures.ProcessPoolExecutor(max_workers=5)
                    for sub in sub_categories:
                        sub_code = sub.get('code')
                        print('当前code为: {}'.format(sub_code))
                        category_url = self.start_urls[1].format(pinyin=category_pinyin, code=sub_code)
                        thread_pool.submit(self.get_sub_category, category_url, category_type)
                    thread_pool.shutdown()
        else:
            print('获取所有分类失败')

    def get_sub_category(self, url, content_type):
        content = self.request(url)
        if content:
            total = int(content.get('data').get('total'))
            page_size = int(content.get('data').get('pageSize'))
            if total % page_size != 0:
                page_num = 1 + int((total / page_size))
            else:
                page_num = int(total / page_size)
            for num in range(page_num):
                albums_url = url + '&sort=0&page={}&perPage={}'.format(num, page_size)
                print('处理专辑url：{}'.format(albums_url))
                self.get_albums(albums_url, content_type)
        else:
            print('content 内容为空')


    def get_albums(self, albums_url, content_type):
        content = self.request(albums_url)
        if str(content) != '{}':
            albums = content.get('data').get('albums')
            for album in albums:
                album_id = album.get('albumId')
                track_count = int(album.get('trackCount'))
                title = album.get('title')
                author = album.get('anchorName')
                if track_count / 30 != 0:
                    page_num = 1 + int(track_count / 30)
                else:
                    page_num = int(track_count / 30)
                for i in range(page_num):
                    content_url = self.start_urls[2].format(albumId=album_id, pageNum=page_num)
                    print('处理content_url为: {}'.format(content_url))
                    self.parse(content_url, content_type, title, author)
        else:
            print('获取专辑失败')

    def parse(self, url, content_type, title, author):
        response = self.request(url)
        if response:
            tracks = response.get('data').get('tracks')
            thread_pool = futures.ProcessPoolExecutor(max_workers=5)
            for track in tracks:
                thread_pool.submit(self.write, track, content_type, title, author)
            thread_pool.shutdown()
        else:
            print('解析内容失败')

    def write(self, track, content_type, name, author):
        title = track.get('title')
        tag = [content_type]
        artist = [author]
        data = json.dumps({'tag': tag, 'artist': artist, 'title': title, 'name': name})
        with open('xmly.list', 'a+', encoding='utf-8') as f:
            f.write(data)
            f.write('\n')

    def request(self, url):
        # self.header['xm-sign'] = self.get_sign()
        time.sleep(0.5)
        proxies = {'http':'http://{}'.format(self.get_proxy())}
        try:
            req = requests.get(url=url, headers=self.header, proxies=proxies, timeout=5)
            if req.status_code == 200:
                response = req.content.decode('utf-8')
                content = json.loads(response)
                req.close()
                return content
            else:
                req.close()
                return None
        except requests.ConnectionError:
            print('连接中断')
            return None


    # def get_timestamp(self):
    #     url = 'https://www.ximalaya.com/revision/time'
    #     response = self.session.get(url, headers=self.header, proxies={}, timeout=5)
    #     time.sleep(0.5)
    #     timestamp = response.text
    #     response.close()
    #     return timestamp

    # 喜马拉雅检验签名，爬取的时候没发现一定要用
    # def get_sign(self):
    #     timestamp = self.get_timestamp()
    #     with open('xmSign.js', encoding='utf-8') as f:
    #         script = f.read()
    #     jsexec = execjs.compile(script)
    #     res = jsexec.call('python', timestamp)
    #     return res

    def get_proxy(self):
        url = '代理IP获取地址'
        response = requests.get(url)
        if response.status_code == 200:
            proxy = response.text
            return proxy
        else:
            print('proxy failed')



if __name__ == '__main__':
    entertain = EntertainXMLY()
    entertain.get_category()
