import os
from multiprocessing import Pool
from sys import stdout
from urllib.error import HTTPError

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)


def request(method, url, **kwargs):
    try:
        return requests.request(method, url, **kwargs)
    except HTTPError as error:
        print('HTTPError:', error)
    except ConnectionError as error:
        print('ConnectionError:', error)


def download(url, file):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    response = request('get', url, headers=headers, stream=True, verify=False)
    if response.status_code == 200:
        content_length = int(response.headers['content-length'])
        stdout.write('文件大小: %0.2fMB\n' % (content_length / 1024 / 1024))
        with open(file, 'wb') as f:
            chunk_size = 1024
            size = 0
            for data in response.iter_content(chunk_size=chunk_size):
                f.write(data)
                f.flush()
                size += len(data)
                stdout.write('下载进度: %.2f%%\r' % float(size / content_length * 100))
                if size / content_length == 1:
                    print('\n')
    else:
        print('下载出错')


def batch_download(urls):
    if len(urls) > 0:
        path = os.path.join(os.getcwd(), 'tmp')
        if not os.path.exists(path):
            os.makedirs(path)
        pool = Pool(8)
        for index, url in enumerate(urls):
            file = os.path.join(path, '%d.ts' % (index + 1))
            pool.apply_async(download, args=(url, file))
        pool.close()
        pool.join()


def main():
    urls = []
    batch_download(urls)


if __name__ == '__main__':
    main()
