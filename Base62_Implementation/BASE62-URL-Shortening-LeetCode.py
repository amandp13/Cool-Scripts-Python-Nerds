import os
import random
import sys
import time


class Codec:

    shortlong: dict = dict()

    def encode(self, longUrl: str):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        # we need a list of all characters in 0-9A-Za-z
        chars: tuple = tuple('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
        length: int = 6  # a length of tinyurl you would like, can be determined
        ans: str = ""  # this is what we will reply

        for i in range(length):  #get 6 random characters from "chars"
            ans += chars[random.randint(0, 61)]
        #we can setup a while loop here to see if the short url exists in map/database

        #add url to dictionary or insert into database--if not exists
        self.shortlong[ans] = longUrl
        #print "ans =",ans," long =",longUrl
        return "https://tinyurl/" + ans

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        last = shortUrl.split("/")[-1]
        #print "   short=",shortUrl,"  last=",last
        #print "   long",self.shortlong[last]
        return self.shortlong[last]


def main():
    UrlShortener = Codec()
    URL: str = "https://leetcode.com/problems/design-tinyurl"
    print("URL: " + URL)
    x: str = UrlShortener.encode(URL)
    print("Encode: " + x)
    print("Decode: " + UrlShortener.decode(x))


if __name__ == '__main__':
    os.system('clear')
    main()
