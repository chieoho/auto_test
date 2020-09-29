import requests


class HttpPosterException(Exception):
    def __str__(self):
        return 'url null; fill or set url'


class HttpPoster(object):
    """
    http publisher base class
    """
    url = ''

    def __init__(self):
        pass

    @classmethod
    def set_url(cls, url):
        cls.url = url

    @classmethod
    def get(cls, url=None, param=None, verify=False, **kwargs):
        # 2020/9/29 以传过来的参数为主
        if url or cls.url:
            url = url or cls.url
        else:
            raise HttpPosterException
        return requests.get(url, param, verify=verify, **kwargs)

    @classmethod
    def post(cls, url=None, data=None, json=None, verify=False, **kwargs):
        if url or cls.url:
            url = url or cls.url
        else:
            raise HttpPosterException
        return requests.post(url, data, json, verify=verify, **kwargs)

    @classmethod
    def options(cls, url, verify=False, **kwargs):
        if url or cls.url:
            url = url or cls.url
        else:
            raise HttpPosterException
        return requests.options(url, verify=verify, **kwargs)
