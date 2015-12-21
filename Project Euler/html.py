from bs4 import BeautifulSoup, Comment
from urllib2 import urlopen
import sys
import time

def get_page(url):
    try:
        raw = urlopen(url).read()
        return raw
    except:
        print "Wrong url!"
        exit()
        
def test_link(link):
    if 'http://' in link or '@' in link or '#' in link:
        return False
    else:
        return True

def set_file(path):
    try:
        wordlist = open(path, 'a+')
    except:
        wordlist = open(path, 'w+')
    finally:
        return wordlist

class HtmlToPass:
    def __init__(self, url, path="wordlist.txt"):
        self.base_url = url
        self.links = []
        self.words = []
        self.wordlist = set_file(path)

    def spider(self):
        raw = get_page(self.base_url)
        soup = BeautifulSoup(raw)
        self.links.append("/")
        for link in soup.find_all('a'):
            if test_link(link.get('href')):
                self.links.append(link.get('href'))
        self.links = list(set(self.links))
        return self.links

    def get_content(self, url):
        soup = BeautifulSoup(urlopen(url).read())
        [s.extract() for s in soup('script')]
        [s.extract() for s in soup('style')]
        [c.extract() for c in soup.findAll(text=lambda text:isinstance(text, Comment))]
        try:        #this is against a NoneType error: "AttributeError: 'NoneType' object has no attribute 'stripped_strings'"
            for string in soup.body.stripped_strings:
                for word in string.split(' '):
                    word = ''.join(e for e in word if e.isalnum())  #remove special characters
                    if word not in self.words:      #remove duplicates
                        self.words.append(word)
        finally:
            return self.words

    def main(self):
        for link in self.spider():
            print "stripping: " + link
            for word in self.get_content(self.base_url + link):
                try:
                    self.wordlist.write(word + "\n")
                except:
                    pass
        return self.wordlist

if __name__ == '__main__':
    t = time.time()
    try:
        url = sys.argv[1]
    except:
        url = "http://sintlodewijk-lokeren.be/"
    blub = HtmlToPass(url)
    blub.main()
    time = str(time.time() - t) + " seconds"
    blub.wordlist.close()
    lines = 0
    blanklines = 0
    textf = open("wordlist.txt", "r")
    for line in textf:
        lines += 1
        if line.startswith('\n'):
            blanklines += 1
    print str(lines) + " words" + " in " + time
    print blanklines
