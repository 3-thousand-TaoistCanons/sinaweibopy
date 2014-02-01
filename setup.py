from distutils.core import setup
import weibo3

kw = dict(
    name = 'sinaweibopy3',
    version = weibo3.__version__,
    description = 'Sina Weibo OAuth 2 API Python SDK',
    long_description = open('README', 'r').read(),
    author = 'Michael Liao',
    author_email = 'askxuefeng@gmail.com',
    url = 'https://github.com/WeCase/sinaweibopy',
    download_url = 'https://github.com/WeCase/sinaweibopy',
    py_modules = ['weibo3'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python 3',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])

setup(**kw)
