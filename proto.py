import requests
from zipfile import ZipFile
import argparse
from bs4 import BeautifulSoup
import pandas as pd


# parser = argparse.ArgumentParser()
# parser.add_argument('dataDir', type=str, default='./solution/', help='path to data dir')

# args = parser.parse_args()

# dataDir = args.dataDir
# print("File will be extracted to "+dataDir)

# url = "https://vicroadsopendatastorehouse.vicroads.vic.gov.au/opendata/Road/Assets/Electrical/Traffic_Signal_Configuration_Data_Sheets/Sheets%204000-4999.zip"

# print("Downloading .... ")
# res = requests.get(url)

# open("Sheets%204000-4999.zip", "wb").write(res.content)
# print("Downloaded!")
# print("Extracting .... ")

# with ZipFile("Sheets%204000-4999.zip",'r') as zb:
#     zb.extractall(
#         path='solution')
# print("Extraction Completed") 
# 



# HTMLFileToBeOpened = open("solution/4000-4999/4011_files/sheet007.htm", "r")

# contents = HTMLFileToBeOpened.read()

# SoupText = BeautifulSoup(contents, "html.parser")
# tr = SoupText.select('tr:-soup-contains("YELLOW","RED")')
# data=[]
# all_d = []
# for te in tr:
#     t = te.text.replace('\xa0', '')
#     data = t.split("\n")
    
#     data.pop(0)
#     data.pop()
#     data.pop()
#     all_d.append(data)
#     if(data[0]=="YELLOW" or data[0]=="RED"):
#        print(data)

# print('writing to excel')

# rs = pd.DataFrame(all_d, columns=["DESCRIPTION","TIME SETTING NO.","A(1)","B(2)","C(3)","D(4)","E(5)","F(6)","G(7)"])
# print(rs)

# writer = pd.ExcelWriter('4011.xlsx') 


# rs.to_excel(writer, sheet_name='Intersection', index=False, na_rep='NaN')
# writer.save()


datafr1 = pd.read_excel('../TCS0196/196 Phase statistics.xlsx')

datafr1['End'] = datafr1['End'].str.replace(r"(\s*\[.*?\]\s*)", "").str.strip()




print(datafr1['End'])

