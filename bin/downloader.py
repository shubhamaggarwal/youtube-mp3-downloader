import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import urllib.request
from fake_useragent import UserAgent
import sys
import os
import time

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def input_query():
    try:
        search_query = sys.argv[1:]
        if len(sys.argv) <= 1:
            raise IndexError
        name = ' '.join(search_query)
        return name
    except IndexError:
        print("Enter at least one search query.")
        sys.exit()


def scrape():
    search_query = input_query()
    youtube_url = "https://www.youtube.com/results?search_query="+search_query
    ua = UserAgent()
    header = {'User-Agent': ua.random}
    try:
        response = requests.get(youtube_url, headers=header)
        if response.status_code == 200:
            print(color.BOLD + color.BLUE + "\nBreathe in..Breathe out.. : " + color.END)
    except requests.exceptions.ConnectionError:
        print("Connection Error. Check your internet connection or try again after sometime.")
        sys.exit()

    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    title = []
    ref = []
    all_title_tags = soup.find_all("h3", attrs={"class": "yt-lockup-title"})
    for h3 in all_title_tags:
        title.append(h3.find('a').contents[0])
        ref.append(h3.find('a')['href'])
    sequence = ["S.No", "Title"]
    t = PrettyTable(sequence)
    sz = len(title)
    print("Results found = "+str(sz))
    sys.setrecursionlimit(100000)
    for i in range(sz):
        t.add_row([i + 1, title[i]])
    if len(title) != 0:
        print(color.BOLD + color.CYAN + "\nResults : " + color.END)
        print(t)

        choice = input(color.CYAN + color.BOLD + "\nEnter your choice (numerical) : " + color.END)
        if 1 <= int(choice) <= len(title):
            filename = title[int(choice) - 1]
            video_url = "https://www.youtube.com" + str(ref[int(choice) - 1])
            return filename, video_url
        else:
            print("Invalid entry.")
            sys.exit()
    else:
        print(color.BOLD + color.CYAN + "Sorry, no results found." + color.END)


def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize: # near the end
            sys.stderr.write("\n")
    else: # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))


def mp3downloader():
    filename, video_url = scrape()
    print(video_url)
    redirect_url = "http://youtubeinmp3.com/download/?video="+video_url
    print(redirect_url)
    ua = UserAgent()
    header = {'User-Agent': ua.random}
    try:
        response = requests.get(redirect_url, headers=header)
    except requests.exceptions.ConnectionError as e:
        print("Connection Error. Check your internet connection or try again after sometime.")
        sys.exit()
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    tag = soup.find_all('a', attrs={'id': "download"})
    print(tag)
    download_url = "http://www.youtubeinmp3.com/"+tag[0]['href']
    print(download_url)
    print("Downloading..")
    urllib.request.urlretrieve(download_url, "/home/canoodle/Desktop/"+filename, reporthook)
    print("Done")


if __name__ == "__main__":
    mp3downloader()