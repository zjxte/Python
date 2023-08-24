import glob
import pandas as pd
import os

path = "C:\\Users\\Li\\Desktop\\temp"

# get sheet name from xls folder
sheet_list = []
for filename in os.listdir(path):
    if filename.endswith('.xls'):
        sheet_list.append(filename.replace('_ADDRESSES_EXPORT.xls',''))
print(sheet_list)

# get file list from xls folder and read it to a list
file_list = glob.glob(path + "/*.xls")
excl_list = []
for file in file_list:
	excl_list.append(pd.read_excel(file))

# add a route colunmn into each dataset
final_list = []
for i in range(0, 4):
    excl_list[i]["Route"] = sheet_list[i]
    # excl_list[i]["Unique_Address"] = excl_list[i]["A_NUM"].astype(str) + ' ' + excl_list[i]["A_NAME"]
    excl_list[i].insert(0, "Unique_Add", excl_list[i]["A_NUM"].astype(str) + ' ' + excl_list[i]["A_NAME"])
    
    # excl_list[i]["Unique_Address"] = excl_list[i][['A_NUM','A_NAME']].apply(lambda x: ' '.join(x), axis=1)
    final_list.append(excl_list[i])

# print(excl_list[0]["Route"])
# merge dataset as a new xlsx file
excl_merged = pd.concat(final_list, ignore_index=True)
excl_merged.to_excel('merged.xlsx', index=False)





