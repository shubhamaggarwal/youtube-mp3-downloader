#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import sys
import time
import os

class color(object):
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
        return ' '.join(search_query)
    except IndexError:
        print(color.BOLD + color.YELLOW + "Enter at least one search query." + color.END)
        sys.exit()


def scrape():
    search_query = input_query()
    youtube_url = "https://www.youtube.com/results?search_query=" + search_query
    useragent = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    header = useragent
    try:
        response = requests.get(youtube_url, headers=header)
        if response.status_code == 200:
            print(color.BOLD + color.BLUE + "\nWe have got your stuff. " +
                  "Meanwhile you can practice breathing in and out: " +
                  color.END
                  )
            time.sleep(2)
    except requests.exceptions.ConnectionError:
        print(color.UNDERLINE + color.BOLD + color.RED + "\nConnection Error." +
              " Check your internet connection" +
              " or try again after sometime." +
              color.END
              )
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
    print("Results found = " + str(sz))
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



def mp3downloader():
    filename, video_url = scrape()
    redirect_url = "http://youtubeinmp3.com/download/?video=" + video_url
    userAgent = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    header = userAgent
    try:
        response = requests.get(redirect_url, headers=header)
    except requests.exceptions.ConnectionError as e:
        print(color.UNDERLINE + color.BOLD + color.RED + "\nConnection Error." +
              " Check your internet connection" +
              " or try again after sometime." +
              color.END
              )
        sys.exit()
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    tag = soup.find_all('a', attrs={'id': "download"})
    download_url = "http://www.youtubeinmp3.com" + tag[0]['href']
    print(color.BOLD + color.DARKCYAN + "Filling diesel in the engine" + color.END)
    file = filename+'.mp3'
    path = os.path.join(os.path.expanduser('~/Desktop'), file)
    try:

        res = requests.get(download_url, timeout=10, stream=True)
                
        res.raise_for_status()
                
        total_length = res.headers.get('content-length')
        if total_length is None:
            raise Exception
        downloaded_length = 0
        print(color.BOLD + color.GREEN + "Your file will be saved to "+ color.YELLOW + str(path)+color.END)
        with open(path, 'wb') as fd:
            for chunk in res.iter_content(chunk_size=100000):
                downloaded_length += len(chunk)
                fd.write(chunk)
                done = int(50 * int(downloaded_length) / int(total_length))
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()
        print(color.BOLD + color.GREEN + "\nDone" + color.END)
    except:
        print(color.BOLD + color.RED + "\nSorry, we tried but someone added water with diesel."+
                                       " You can try again." + color.END)


if __name__ == "__main__":
    mp3downloader()
