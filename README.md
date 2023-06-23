# Python
Find record from df
        df.loc[df['Current Owner Address'].str.contains(r'ROCKY MT',regex=True,na=False)]

regex code for replace dictionary 
                (.*?):(.*)
replace as 
                "$1":"$2",
