# Python
Find record from df
```df.loc[df['Current Owner Address'].str.contains(r'ROCKY MT',regex=True,na=False)]```

* regex code for replace dictionary 
```(.*?):(.*)```
replace as 
```"$1":"$2",```


* pandas filter
```no_info_records = df.query("GIS_PIN != '000000' & TAX_PIN.isnull() & GIS_PARID.notnull()", engine='python')```
no_info_records


https://curl.iculture.cc

## Save as requirements.txt
```pip freeze > requirements.txt```
## Install dependencies
```pip install -r requirements.txt```


