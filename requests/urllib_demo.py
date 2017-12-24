# -*- coding= utf-8 -*-
import urllib
import urllib2

URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET = 'http://127.0.0.1:8000/get'


def use_simple_urllib2():
    response = urllib2.urlopen(URL_IP)
    print ">>>>>>Response.info"
    print response.info()
    print ">>>>>Response body"
    print ''.join([line for line in response.readlines()])


def use_params_urllib2():
    print "\n\n\nuse_params_urllib2"
    # 构建请求参数
    params = urllib.urlencode({'params1': 'hello', 'params2': 'world'})
    print params
    # 发送请求
    response = urllib2.urlopen('?'.join([URL_GET, '%s']) % params)
    # 处理相应
    print ">>>>>>>>Response_body"
    print response.info()
    print ">>>>>>>>Response_code"
    print response.getcode()
    print ''.join([line for line in response.readlines()])



if __name__ == '__main__':
    use_simple_urllib2()
    use_params_urllib2()
