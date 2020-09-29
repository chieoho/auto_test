from auto_test.test_tools.communication.poster import HttpPoster


def test_http_url():
    # 2020/9/29 pytest只执行test_下面内容所以要是想忽略warning 需要在下面写
    import urllib3
    urllib3.disable_warnings()
    # 2020/9/29 优先级 self.options(url) > cls.url
    h = HttpPoster()
    h.url = 'https://192.168.73.109:8002/keylist'   # 错误的接口
    op = h.options('https://192.168.73.109:8003/api/exclude/keylist')
    assert op.ok is True
    print('<<<< test_http_url success ')


def test_http_set_url():
    import urllib3
    urllib3.disable_warnings()
    h = HttpPoster()
    h.set_url('https://192.168.73.109:8003/api/exclude/keylist')
    assert h.url == 'https://192.168.73.109:8003/api/exclude/keylist'
    print('<<<< test_http_set_url success ')


if __name__ == '__main__':
    # m = MonitorPoster()
    # m.set_url('a')
    # u = m.url
    # print(u)
    test_http_url()
    test_http_set_url()
