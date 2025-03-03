import time
from DrissionPage import ChromiumPage, ChromiumOptions

# e_url = 'https://etherscan.io/search?q=deployer&filter=address'
e_url = 'https://etherscan.io/search?q=deployer&ps=100&filter=address&p=2'

options = ChromiumOptions()
options.set_argument("--remote-debugging-port=9222")


driver = ChromiumPage(addr_or_opts=options)


def connect():
    try:
        driver.get(e_url)
        time.sleep(2)
        # i = driver.get_frame('@src^https://challenges.cloudflare.com/cdn-cgi')
        # e = i('.mark')
        # time.sleep(5)
        # e.click()
        # elements = driver.ele('@class:text-muted text-break')
        all_content = driver.html
        # return elements
        return all_content
    except Exception as ex:
        print(ex)
    finally:
        driver.quit()


if __name__ == '__main__':
    # connect()
    all_content = connect()
    # print(elements)
    print(all_content)
    f = open('my_html.html', 'w')
    f.write(all_content)







