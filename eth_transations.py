import requests
import parsel
import csv
import os

try:
    os.remove('eth.csv')
except OSError:
    pass

eth_wallet = '0x9FBd9B6c69aAd68c221a7C4E2fEB4B3B6a7fA32d'

def get_transations(eth_wallet):
    url = f"https://www.blockchain.com/eth/address/{eth_wallet}"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    r = requests.get(url=url, headers=headers)
    selector = parsel.Selector(r.text)

    f = open('eth.csv', mode='a', encoding='utf-8', newline='')
    csv_writer = csv.DictWriter(f, fieldnames=[
                                                'hash',
                                                'date',
                                                'eth_from',
                                                'eth_to',
                                                'amount'
                                            ])
    csv_writer.writeheader()

    blocks = selector.css('div.sc-1fp9csv-0.ifDzmR')
    # print(len(blocks))
    for b in blocks:
        hash = b.css('div > div >div:nth-child(2) > a::text').get()
        date = b.css('div > div:nth-child(2) > div:nth-child(2) > div > span::text').get()
        eth_from = b.css(' div:nth-child(2) > div > div:nth-child(2) > a::text').get()
        eth_to = b.css( 'div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > a::text').get()
        amount = b.css('div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div > span::text').get().replace(' ETH','')

        transations = {
            'hash': hash,
            'date': date,
            'eth_from': eth_from,
            'eth_to':eth_to,
            'amount':float(amount),
        }
        csv_writer.writerow(transations)
    print(f'{len(blocks)} in total')

get_transations(eth_wallet)
