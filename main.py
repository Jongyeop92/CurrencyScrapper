# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import requests


def test():
    url = "http://finance.daum.net/exchange/exchangeMain.daum?DA=TMZ"
    
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    exInfoList = soup.find("ul", attrs={"id" : "exInfoList"})
    for exInfo in exInfoList.find_all("div", "exDetailBox"):
        country = exInfo.dl.dt.text
        infoList = exInfo.dl.find_all("dd")

        price = infoList[0].text
        change = infoList[1].text
        per = infoList[2].text
        

        print "-" * 30
        print country
        print price
        print change
        print per
        print


def main():
    pass


if __name__ == "__main__":
    test()
    #main()
