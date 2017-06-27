from setuptools import setup

setup(
    name='youtube_mp3_downloader',
    version='1.0.1',
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
        'Programming Language :: Python :: 3.5'
    ],
    keywords="Youtube mp3 downloader",
    author_email='aggarwals5411@gmail.com',
    url='https://github.com/shubhamaggarwal/youtube-mp3-downloader',
    packages=['youtube_mp3_downloader'],
    scripts=['bin/youtube_mp3_downloader'],
    install_requires=[
        "requests >= 2.18.1",
        "beautifulsoup4 >= 4.6.0",
        "PrettyTable",
        "fake_useragent"
    ]
)