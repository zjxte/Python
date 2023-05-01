import threading
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import csv
import os

def page_number():
    url = 'https://taxpa.edgecombecountync.gov/paas/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'referer': 'https://taxpa.edgecombecountync.gov/paas/?DEST=download&action=Search',
        'cookie': 'ASPSESSIONIDQERCDDSB=POFPHGJCONDIDPNDJJAOHGHF',
        'authority': 'taxpa.edgecombecountync.gov',
        'path': '/paas/?DEST=download&action=Search'
    }
    query_para = {
        'DEST': 'download',
        'action': 'search'
    }

    data1 = [
        ('OWNER', ''),
        ('MAP', ''),
        ('lACRE', ''),
        ('uACRE', ''),
        ('SUB', ''),
        ('TWP', ''),
        ('TAX', 'G01'),
        ('col', 'Parcel ID'),
        ('col', 'Property Address'),
        ('col', 'Property Description'),
        ('col', 'Current Owner 1'),
        ('col', 'Current Owner 2'),
        ('col', 'Deed Book/Page'),
        ('col', 'Current Owner Address'),
        ('col', 'Date Recorded'),
        ('col', 'Deferred Amount'),
        ('col', 'Building Value'),
        ('col', 'Tax Codes'),
        ('col', 'Land Value'),
        ('col', 'Township Codes'),
        ('col', 'Subdivision Codes'),
        ('col', 'Account Number'),
        ('col', 'Map Sheet'),
        ('col', 'Sale Price'),
        ('col', 'Total Tax Value'),
        ('page_no', 1)
    ]

    r = requests.post(url=url, headers=headers, data=data1, params=query_para)
    page = re.findall("jsSubmit\(\'Page\'\,\'(.*?)\'\)",r.text)
    page_num = int(page[-1])
    return page_num

def get_data(page):
    url = 'https://taxpa.edgecombecountync.gov/paas/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'referer': 'https://taxpa.edgecombecountync.gov/paas/?DEST=download&action=Search',
        'cookie': 'ASPSESSIONIDQERCDDSB=POFPHGJCONDIDPNDJJAOHGHF',
        'authority': 'taxpa.edgecombecountync.gov',
        'path': '/paas/?DEST=download&action=Search'
    }
    query_para = {
        'DEST': 'download',
        'action': 'search'
    }

    data1 = [
        ('OWNER', ''),
        ('MAP', ''),
        ('lACRE', ''),
        ('uACRE', ''),
        ('SUB', ''),
        ('TWP', ''),
        ('TAX', 'G01'),
        ('col', 'Parcel ID'),
        ('col', 'Property Address'),
        ('col', 'Property Description'),
        ('col', 'Current Owner 1'),
        ('col', 'Current Owner 2'),
        ('col', 'Deed Book/Page'),
        ('col', 'Current Owner Address'),
        ('col', 'Date Recorded'),
        ('col', 'Deferred Amount'),
        ('col', 'Building Value'),
        ('col', 'Tax Codes'),
        ('col', 'Land Value'),
        ('col', 'Township Codes'),
        ('col', 'Subdivision Codes'),
        ('col', 'Account Number'),
        ('col', 'Map Sheet'),
        ('col', 'Sale Price'),
        ('col', 'Total Tax Value'),
        ('page_no', page)
    ]

    r = requests.post(url=url, headers=headers, data=data1, params=query_para)
    # print(r.text)
    #
    # with open('edge.html', 'w', encoding='utf-8') as f:
    #     f.write(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')
    tb = soup.find_all("table")[6]
    trs = tb.find_all("tr")[1:]
    # print(trs[4])

    data = []

    for tr in trs:
        tds = tr.find_all("td")
        #     print(tds[0].text)

        parcelID = tds[0].text.strip()
        property_address = tds[1].text.strip()
        property_desc = tds[2].text.strip()
        current_owner1 = tds[3].text.strip()
        current_owner2 = tds[4].text.strip()
        deed_book_page = tds[5].text.strip()
        current_owner_address = tds[6].text.strip()
        date_recorded = tds[7].text.strip()
        a8 = tds[8].text.strip()
        a9 = tds[9].text.strip()
        a10 = tds[10].text.strip()
        a11 = tds[11].text.strip()
        a12 = tds[12].text.strip()
        a13 = tds[13].text.strip()
        a14 = tds[14].text.strip()
        a15 = tds[15].text.strip()
        a16 = tds[16].text.strip()
        a17 = tds[17].text.strip()

        d = {
            'parcelID': parcelID,
            'property_address': property_address,
            'property_desc': property_desc,
            'current_owner1': current_owner1,
            'current_owner2': current_owner2,
            'deed_book_page': deed_book_page,
            'current_owner_address': current_owner_address,
            'date_recorded': date_recorded,
            'deferred_amount': a8,
            'building_value': a9,
            'tax_codes': a10,
            'land_value': a11,
            'township_codes': a12,
            'SUBDIVISION_CODES': a13,
            'account_number': a14,
            'map_sheet': a15,
            'sale_price': a16,
            'Total_tax_value': a17,

        }

        data.append(d)
        csv_writer.writerow(d)
    return data

if __name__ == '__main__':

    try:
        os.remove("Edgecombe tax.csv")
    except OSError:
        pass

    f = open("Edgecombe tax.csv", mode="a", encoding="utf-8", newline="")
    csv_writer = csv.DictWriter(
                                f, fieldnames= [
                                                'parcelID',
                                                'property_address',
                                                'property_desc',
                                                'current_owner1',
                                                'current_owner2',
                                                'deed_book_page',
                                                'current_owner_address',
                                                'date_recorded',
                                                'deferred_amount',
                                                'building_value',
                                                'tax_codes',
                                                'land_value',
                                                'township_codes',
                                                'SUBDIVISION_CODES',
                                                'account_number',
                                                'map_sheet',
                                                'sale_price',
                                                'Total_tax_value'])
    csv_writer.writeheader()

    total_page = page_number() + 1

    for p in range(1, 5):
        ds = get_data(p)
        print(ds)
