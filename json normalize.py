import pandas as pd
# https://www.youtube.com/watch?v=LYh8ih2X5Oo&ab_channel=MrFuguDataScience

df1 = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in ex_one['entities'].items()]))

