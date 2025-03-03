import time
from DrissionPage import ChromiumPage, ChromiumOptions
from bs4 import BeautifulSoup

options = ChromiumOptions()
options.set_argument("--remote-debugging-port=9222")


driver = ChromiumPage(addr_or_opts=options)


def connect():
    e_url = f'https://etherscan.io/search?q=deployer&ps=100&filter=address&p=1'
    try:
        driver.get(e_url)
        content = driver.html
        
    except Exception as ex:
        print(ex)
    finally:
        driver.quit()


if __name__ == '__main__':
    for i in range(1, 5):
        connect()
        time.sleep(10)




