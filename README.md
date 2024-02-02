$\color{green}{test}$
This is code I wrote for the [video](https://www.youtube.com/watch?v=Z2EUDerNkOY&t)
# Python
Find record from df
```
df.loc[df['Current Owner Address'].str.contains(r'ROCKY MT',regex=True,na=False)]
```

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

### activate the virtual environment with 

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
### Create env, $\color{red}{python=3.8 is optional}$
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

> **Note**
> Highlights information that users should take into account, even when skimming.

> [!IMPORTANT]  
> Crucial information necessary for users to succeed.

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.

> **Check**
> This is OK
>
## show more columns in pandas
```
pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)
```
## If you use Anaconda for environment management you most likely created requirements.txt file via:
```
conda list --explicit > requirements.txt
```
### To recreate the environment with all your listed packages use:
```
conda env create --file requirements.txt
```
