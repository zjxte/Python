import requests
import parsel
import csv, os, re

try:
    os.remove('eth.csv')
except OSError:
    pass

# write csv header
f = open('eth.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
                                        'date', # transfer date
                                        'eth_from', # transfer from
                                        'eth_to',
                                        'amount',
                                        'hash',
                                        'fee',
                                        'gas',
                                        'wei',
                                        'wallet_ref',
                                    ])
csv_writer.writeheader()

# get eth transations for each
def get_transations(wallet):
    url = f"https://www.blockchain.com/eth/address/{wallet}"
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    r = requests.get(url=url, headers=headers)
    selector = parsel.Selector(r.text)

    blocks = selector.css('div.sc-1fp9csv-0.ifDzmR')
    # print(len(blocks))
    for b in blocks:
        hash = b.css('div > div >div:nth-child(2) > a::text').get()
        date = b.css('div > div:nth-child(2) > div:nth-child(2) > div > span::text').get()
        eth_from = b.css(' div:nth-child(2) > div > div:nth-child(2) > a::text').get()
        eth_to = b.css( 'div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > a::text').get()
        amount = b.css('div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div > span::text').get().replace(' ETH','')
        fee = b.css('div:nth-child(3) > div > div:nth-child(2) > div > span::text').get().replace(' ETH','')
        gas = b.css('div:nth-child(3) > div > div:nth-child(2) > div > span:nth-child(2)::text').get().split(" - ")[0].replace('(','').replace(' GAS','')
        wei = b.css('div:nth-child(3) > div > div:nth-child(2) > div > span:nth-child(2)::text').get().split(" - ")[1].replace(')','').replace(' WEI','')


        transations = {
            'date': date,
            'eth_from': eth_from,
            'eth_to': eth_to,
            'amount': float(amount),
            'hash': hash,
            'fee': float(fee),
            'gas': float(gas),
            'wei': float(wei),
            'wallet_ref': wallet,
        }
        csv_writer.writerow(transations)
    print(f'{len(blocks)} in total')


# eth_wallet = '0x9FBd9B6c69aAd68c221a7C4E2fEB4B3B6a7fA32d' # 20221022
# eth_wallet = '0x2995FD0155171C2d2741FEFc79b881e98ECfD75F' # 20221023

eth_wallet = ['0x9FBd9B6c69aAd68c221a7C4E2fEB4B3B6a7fA32d', # 20221022
              '0x2995FD0155171C2d2741FEFc79b881e98ECfD75F', # 20221023
            ]
for wallet in eth_wallet:

    get_transations(wallet)
