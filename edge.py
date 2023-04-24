import requests

url = 'https://taxpa.edgecombecountync.gov/paas/?DEST=download&action=Search'

# export_url = 'https://taxpa.edgecombecountync.gov/paas/?DEST=download&action=Export'
export_url = 'https://taxpa.edgecombecountync.gov/paas/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'referer': 'https://taxpa.edgecombecountync.gov/paas/?DEST=download&action=Search',
    'cookie': 'ASPSESSIONIDQERCDDSB=POFPHGJCONDIDPNDJJAOHGHF',
    'authority': 'taxpa.edgecombecountync.gov',
    'path': '/paas/?DEST=download&action=Search'
}
query_para = {
    'DEST': 'download',
    'action': 'Search'
}
data = {
    'OWNER': '',
    'MAP': '',
    'lACRE': '',
    'uACRE': '',
    'SUB': '',
    'TWP': '',
    'TAX': 'G01', # edgecome county tax

    # 'col':  'Parcel ID',
    # 'col_1':  'Property Address',
    # 'col_2':  'Land Value',
    # 'col_4':  'Account Number',
    # 'col_5':  'Property Description',
    # 'col_8':  'Current Owner 1',
    # 'col_12':  'Current Owner 2',
    # 'col_13':  'Deed Book/Page',
    # 'col_14':  'Total Tax Value',
    'col':  'Current Owner Address',
    'page_no': 3

    # 'col_0': True, # 'Parcel ID',
    # 'col_1': True, # 'Property Address',
    # 'col_2': True, # 'Land Value',
    # 'col_4': True, # 'Account Number',
    # 'col_5': True, # 'Property Description',
    # 'col_8': True, # 'Current Owner 1',
    # 'col_12': True, # 'Current Owner 2',
    # 'col_13': True, # 'Deed Book/Page',
    # 'col_14': True, # 'Total Tax Value',
    # 'col_16': True, #  'Current Owner Address'
    # 'page_no': 3
}
r = requests.post(url=export_url, headers=headers, data=data,params=query_para)
print(r.text)

with open('edge.html','w',encoding='utf-8')as f:
    f.write(r.text)
