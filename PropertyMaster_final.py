import threading
import time
import requests
from bs4 import BeautifulSoup
# from parsel import Selector
import pandas as pd
import usaddress

# url = 'https://taxpa.edgecombecountync.gov/paas/?DEST=download&action=Search'
# export_url = 'https://taxpa.edgecombecountync.gov/paas/?DEST=download&action=Export'





export_url = 'https://taxpa.edgecombecountync.gov/paas/'




headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'referer': 'https://taxpa.edgecombecountync.gov/paas/?DEST=download&action=Export',
    'cookie': 'ASPSESSIONIDQERCDDSB=POFPHGJCONDIDPNDJJAOHGHF',
    'authority': 'taxpa.edgecombecountync.gov',
    'path': '/paas/?DEST=download&action=Export'
}
query_para = {
    'DEST': 'download',
    'action': 'export'
}





def get_parsed_address(s):
    
    if s == '' or type(s) != str:
        d_full_address = {
            'AddressNumber': '',
            'PlaceName': '',
            'StateName': '',
            'ZipCode': '',
            'other': ''
        }
    else:
        d = {}
        
        tagged_str = usaddress.parse(s)




       for i in tagged_str:




           if i[1] in d:
                d[i[1]] = d[i[1]] + ' ' + i[0]




           else:
                d[i[1]] = i[0]




       street_info = [(k, v) for k, v in d.items() if k != 'AddressNumber' and k != 'PlaceName' and k != 'StateName' and  k != 'ZipCode']




       delete_extra_keys = [k for k in d if k != 'AddressNumber' and k != 'PlaceName' and k != 'StateName' and  k != 'ZipCode']




       for k in delete_extra_keys:
            del d[k]




       d_street_info = {'other':''}




       for i in street_info:




           if d_street_info['other'] != '':




               d_street_info['other'] = d_street_info['other'] + ' ' +  i[1]




           else:
                d_street_info['other'] = i[1]
        
        d_merged = d | d_street_info




       d_full_address = {
            'AddressNumber': '',
            'PlaceName': '',
            'StateName': '',
            'ZipCode': '',
            'other': ''
        }




       for k in d_full_address:
            if k in d_merged:
                d_full_address[k] = d_merged[k]
            else:
                d_full_address[k] = ''




           
        
    return d_full_address





def get_data(page):
    page_no = page
   




   data1 = [
        ('OWNER',''),
        ('MAP', ''),
        ('lACRE', ''),
        ('uACRE', ''),
        ('SUB', ''),
        ('TWP', ''),
        ('TAX','G01'),
        ('col', 'Parcel ID'),
        ('col', 'Property Address'),
        ('col', 'Property Description'),
        ('col', 'Current Owner 1'),
        ('col', 'Current Owner 2'),
        ('col', 'Deed Book/Page'),
        ('col', 'Current Owner Address'),
        ('col','Date Recorded'),
        # ('col','Deferred Amount'),
        # ('col','Building Value'),
        # ('col','Tax Codes'),
        # ('col','Land Value'),
        # ('col','Township Codes'),
        # ('col','Subdivision Codes'),
        # ('col','Account Number'),
        # ('col','Map Sheet'),
        # ('col','Sale Price'),
        # ('col', 'Total Tax Value'),
        ('page_no', page_no)
        ]
    




   r = requests.post(url=export_url, headers=headers, data=data1,params=query_para)




   soup = BeautifulSoup(r.text, 'html.parser')
    tb = soup.find_all("table")[6]
    trs = tb.find_all("tr")[1:]




   info = []




   for tr in trs:
        tds = tr.find_all("td")




       parcelID = tds[0].text.strip().replace('-','')
        property_address = tds[1].text.strip()
        property_desc = tds[2].text.strip()
        current_owner1 = tds[3].text.strip()
        current_owner2 = tds[4].text.strip()
        deed_book_page = tds[5].text.strip()
        current_owner_address = tds[6].text.strip()
        date_recorded = tds[7].text.strip()




       ad_number = get_parsed_address(current_owner_address)['AddressNumber']    
        city = get_parsed_address(current_owner_address)['PlaceName']
        state = get_parsed_address(current_owner_address)['StateName']
        zip = get_parsed_address(current_owner_address)['ZipCode']
        street = get_parsed_address(current_owner_address)['other']




       d = {
            'parcelID' : parcelID,
            'property_address' : property_address,
            'property_desc': property_desc,
            'current_owner1': current_owner1,
            'current_owner2': current_owner2,
            'deed_book_page': deed_book_page,
            'current_owner_address': current_owner_address,
            'date_recorded': date_recorded,        
            'current_owner_address_no':ad_number,
            'current_owner_street':street,
            'curent_owner_city':city,
            'curent_owner_state':state,
            'zip': zip
            }
      
        
        info.append(d)
        
    df = pd.DataFrame(info)
        
    return df




   
get_data(1)
