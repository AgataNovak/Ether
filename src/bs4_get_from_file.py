from bs4 import BeautifulSoup


def get_addresses():
    with open('my_html.html', 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    elements = soup.find_all("span", class_='text-muted text-break')
    for element in elements:
        print(element.text)


if __name__ == '__main__':
    get_addresses()
