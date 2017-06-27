#!/usr/bin/python3
from setuptools import setup

setup(
    name='youtube-mp3-downloader',
    version='1.1',
    description='Download mp3 from youtube',
    long_description='This python package lets you mp3 from download youtube videos to your local machine.',
    author='Shubham Aggarwal',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    platform="any",
    keywords="Youtube mp3 downloader offline local computer",
    author_email='aggarwals5411@gmail.com',
    url='https://github.com/shubhamaggarwal/youtube-mp3-downloader',
    packages=['mp3'],
    scripts=['bin/mp3'],
    install_requires=[
        "requests >= 2.18.1",
        "beautifulsoup4 >= 4.6.0",
        "PrettyTable",
        "fake_useragent"
    ]
)
