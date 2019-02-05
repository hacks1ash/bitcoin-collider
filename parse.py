from bs4 import BeautifulSoup
import requests
import utils


def parse_home_page():
    home_page = 'https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html'
    r = requests.get(home_page)
    html_content = r.text
    final_bitcoin_address_list = list()
    soup = BeautifulSoup(html_content, 'html.parser')
    table1 = soup.find('table', attrs={'id': 'tblOne'})
    table2 = soup.find('table', attrs={'id': 'tblOne2'})
    trs1 = table1.find_all('a')
    trs2 = table2.find_all('a')
    for tr in trs1:
        if tr.text[0] != 'w':
            final_bitcoin_address_list.append(tr.text)

    for tr in trs2:
        if tr.text[0] != 'w':
            final_bitcoin_address_list.append(tr.text)

    utils.write_text_to_file('bitcoin_addresses', '\n'.join(final_bitcoin_address_list))


def parse_bitcoin_addresses(page_count):
    parse_home_page()
    for page_number in range(2, page_count + 1):

        bitcoin_website = f'https://bitinfocharts.com/top-100-richest-bitcoin-addresses-{page_number}.html'
        r = requests.get(bitcoin_website)
        html_content = r.text
        final_bitcoin_address_list = list()
        soup = BeautifulSoup(html_content, 'html.parser')
        table1 = soup.find('table', attrs={'id': 'tblOne'})
        table2 = soup.find('table', attrs={'id': 'tblOne2'})
        trs1 = table1.find_all('a')
        trs2 = table2.find_all('a')

        for tr in trs1:
            if tr.text[0] != 'w':
                final_bitcoin_address_list.append(tr.text)

        for tr in trs2:
            if tr.text[0] != 'w':
                final_bitcoin_address_list.append(tr.text)

        utils.write_text_to_file('bitcoin_addresses', '\n'.join(final_bitcoin_address_list))
