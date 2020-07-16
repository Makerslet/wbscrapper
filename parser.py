
import requests
import bs4
import collections

ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'brand_name',
        'goods_name',
        'url'
    )
)

class Client:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
            'Accept-Language': 'ru'
        }

    def load_page(self, page: int = None):
        url = 'https://www.wildberries.ru/catalog/obuv/zhenskaya'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('div.dtList.i-dtList.j-card-item')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        url_block = block.select_one('a.ref_goods_n_p.j-open-full-product-card')
        if not url_block:
            print('no url block')
            return
        
        url = url_block.get('href')
        if not url:
            print('no href')
            return

        print(relative_card_url)
        print('=' * 100)

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)