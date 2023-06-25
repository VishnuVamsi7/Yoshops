#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a python program to displayed products count number by products main categories and sub categories.
#Enter 1 put value link = Yoshops.com
#Enter 2 put categories link=
#Output = create excel file with Name Category, Products count,Total products count.
#After completing task please convert your PY file to EXE file 


# In[3]:


from bs4 import BeautifulSoup
from urllib import request
import re
import openpyxl


# In[8]:


website = input("Enter the website: ")
workbook = openpyxl.Workbook()

worksheet = workbook.active
subcategories = ["organic","vegetable","non-veg","seafood","biryani"]
print("subcategories: ", len(subcategories))
for i in range(5):  #as there are 5 sub categories in food
	fp = request.urlopen("https://yoshops.com/t/"+subcategories[i].lower())
	mybytes = fp.read()
	mystr = mybytes.decode("utf8")
	fp.close()
	pattern = r'data-name="([^"]+)"'

	matches = re.findall(pattern, mystr)
	print(f"Count of products in each subcategory {subcategories[i]}: {len(matches)}", )
	matches.insert(0, subcategories[i])
	print("-----------------------------------------------------------------------------------------------")
	worksheet.append(matches)
workbook.save("final_excel.xlsx")
    

# In[ ]:




