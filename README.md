This is code I wrote for the [video](https://www.youtube.com/watch?v=Z2EUDerNkOY&t)
# Python
Find record from df
```df.loc[df['Current Owner Address'].str.contains(r'ROCKY MT',regex=True,na=False)]```

* regex code for replace dictionary 
```(.*?):(.*)```
replace as 
```"$1":"$2",```


* pandas filter
```
no_info_records = df.query("GIS_PIN != '000000' & TAX_PIN.isnull() & GIS_PARID.notnull()", engine='python')
```
no_info_records


https://curl.iculture.cc

### Create a virtual environment
This can be done with 
``` python -m venv env ```

activate the virtual environment with 

``` 
env/bin/activate
```

or 

```
env\Scripts\activate
```


## Save as requirements.txt
```
pip freeze > requirements.txt
```
## Install dependencies
```
pip install -r requirements.txt
```

# Anaconda
### Create env
```
conda create --myenv python=3.8
```
### List env
```
conda env list
```
### Activate env
```
activate myenv
```
### Run jupyter notebook
```
jupyter-notebook
```

