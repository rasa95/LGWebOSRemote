"""
Publish a new version:
$ git tag X.Y.Z -m "Release X.Y.Z"
$ git push --tags
$ pip install --upgrade twine wheel
$ python setup.py sdist bdist_wheel
$ twine upload dist/*
"""
import codecs
from setuptools import setup


LGTV_VERSION = '1.1.0'
LGTV_DOWNLOAD_URL = (
    'https://github.com/rasa95/LGWebOSRemote/tarball/' + LGTV_VERSION
)


def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, 'r', 'utf8') as f:
        return f.read()

setup(
    name='LGTV',
    packages=['LGTV'],
    version=LGTV_VERSION,
    description='LG WebOS TV Controller.',
    long_description=read_file('README.md'),
    license='MIT',
    author='Playground',
    author_email='office@playground.rs',
    url='https://github.com/rasa95/LGWebOSRemote',
    download_url=LGTV_DOWNLOAD_URL,
    keywords=[
        'smarthome', 'smarttv', 'lg', 'tv', 'webos', 'remote'
    ],
    install_requires=[
        'wakeonlan',
        'ws4py'
    ],
    entry_points={'console_scripts': ['lgtv = LGTV.main:main']},
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
    ],
)
