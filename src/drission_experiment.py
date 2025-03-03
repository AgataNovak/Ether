import time
from DrissionPage import ChromiumPage, ChromiumOptions, Chromium
from bs4 import BeautifulSoup
import re


pattern = r"^0x"


def connect():
    e_url = f'https://etherscan.io/search?q=deployer&ps=100&filter=address&p=1'
    browser = Chromium()
    tab = browser.latest_tab
    tab.get(e_url)
    for i in range(1, 2):
        try:
            eles = tab.eles('tag:span')
            with open('some_file', 'w') as file:
                for ele in eles:
                    if re.match(pattern, ele.text):
                        file.write(ele.text + '\n')
            tab.ele('text=Next').click()
        except Exception as ex:
            print(ex)
    browser.quit()


if __name__ == '__main__':
    connect()
