#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
filepath = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchasedata = pd.read_csv(filepath)
data=pd.DataFrame(purchasedata)
data.head()


# ## Player Count

# * Display the total number of players
# 

# In[2]:


playercount=len(data["SN"].unique())
totalplayer= pd.DataFrame({"Total Player":[playercount]}) 
totalplayer


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:


itemcount=len(data["Item Name"].unique())
avgprice="$"+str(round(data["Price"].mean(),2))
purchasecount=len(data["Purchase ID"])
totalrevenue="$"+str(data["Price"].sum())
purchaseanalysis=pd.DataFrame({"Number of Unique Items":[itemcount],"Average Price":[avgprice],"Number of Purchases":[purchasecount],"Total Revenue":[totalrevenue]})
purchaseanalysis


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[4]:


genderdata=data.groupby(data["Gender"])
uniquedata=genderdata["SN"].unique()
femalecount=len(uniquedata[0])
malecount=len(uniquedata[1])
othercount=len(uniquedata[2])
totalcount=malecount+femalecount+othercount
malepct=str(round(malecount/totalcount*100,2))+"%"
femalepct=str(round(femalecount/totalcount*100,2))+"%"
otherpct=str(round(othercount/totalcount*100,2))+"%"
genderdemographic=pd.DataFrame({"":["Female","Male","Other / Non-Disclosed"],"Total Count":[femalecount,malecount,othercount],"Percentage of Players":[femalepct,malepct,otherpct]})
genderdemographic


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[5]:


genderpurchasecount=genderdata["Purchase ID"].count()
genderavgprice=round(genderdata["Price"].mean(),2)
genderpurchasevalue=round(genderdata["Price"].sum(),2)
avgvalueperperson=["$"+str(round(genderpurchasevalue[0]/femalecount,2)),"$"+str(round(genderpurchasevalue[1]/malecount,2)),"$"+str(round(genderpurchasevalue[2]/othercount,2))]
genderpurchaseanalysis=pd.DataFrame({"Gender":["Female","Male","Other / Non-Disclosed"],"Purchase Count":[genderpurchasecount[0],genderpurchasecount[1],genderpurchasecount[2]],"Average Purchase Price":[genderavgprice[0],genderavgprice[1],genderavgprice[2]],"Total Purchase Value":[genderpurchasevalue[0],genderpurchasevalue[1],genderpurchasevalue[2]],"Avg Total Purchase per Person":[avgvalueperperson[0],avgvalueperperson[1],avgvalueperperson[2]]})
genderpurchaseanalysis


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[6]:


agedata=data.groupby(data["SN"])
agecountdata=agedata.mean()
bins=(min(agecountdata["Age"]),10,15,20,25,30,35,40,max(agecountdata["Age"]))
agegroup=("<10","11-14","15-19","20-24","25-29","30-34","35-39","40+")
agecountdata[""]=pd.cut(agecountdata["Age"],bins,labels=agegroup,include_lowest=True,duplicates='drop')
agegroupdata=agecountdata.groupby("")
agegroupcountdata=agegroupdata.count()
agegroupcountdata=agegroupcountdata.rename(columns={"Age":"Total Count"})
agegroupcountdata["Percentage of Players"]=round(agegroupcountdata["Total Count"]/sum(agegroupcountdata["Total Count"]),2)
agegroupcountdata["Percentage of Players"]=agegroupcountdata["Percentage of Players"].map('{:,.2%}'.format)
agedemographic=agegroupcountdata[["Total Count","Percentage of Players"]]
agedemographic


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[7]:


agepurchasecount=agegroupdata["Purchase ID"].count()
ageavgprice=round(agegroupdata["Price"].mean(),2)
agepurchasevalue=round(agegroupdata["Price"].sum(),2)
avgvalueperperson=round(agepurchasevalue/agepurchasecount,2)
agepurchaseanalysis=pd.DataFrame({"Age Ranges":agegroup,"Purchase Count":agepurchasecount,"Average Purchase Price":ageavgprice.map('${:,}'.format),"Total Purchase Value":agepurchasevalue.map('${:,}'.format),"Avg Total Purchase per Person":avgvalueperperson.map('${:,}'.format)})
agepurchaseanalysis.set_index("Age Ranges",drop=True)


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[8]:


spenderdata=data.groupby("SN")
spenderpurchasecount=spenderdata["Purchase ID"].count()
spenderavgprice=round(spenderdata["Price"].mean(),2)
spenderpurchasevalue=round(spenderdata["Price"].sum(),2)
topspender=pd.DataFrame({"Purchase Count":spenderpurchasecount,"Average Purchase Price":spenderavgprice.map('${:,}'.format),"Total Purchase Value":spenderpurchasevalue.map('${:,}'.format)})
topspender.sort_values(by="Total Purchase Value",ascending=False)


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[9]:


itemdata=data.groupby(["Item ID","Item Name"])
itempurchasecount=itemdata["Purchase ID"].count()
itemavgprice=round(itemdata["Price"].mean(),2)
itempurchasevalue=round(itemdata["Price"].sum(),2)
mostpopular=pd.DataFrame({"Purchase Count":itempurchasecount,"Item Price":itemavgprice.map('${:,}'.format),"Total Purchase Value":itempurchasevalue.map('${:,}'.format)})
mostpopular.sort_values(by="Purchase Count",ascending=False)


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[11]:


mostpopular=pd.DataFrame({"Purchase Count":itempurchasecount,"Item Price":itemavgprice.map('${:,}'.format),"Total Purchase Value":itempurchasevalue})
mostpopular.sort_values(by="Total Purchase Value",ascending=False)


# In[ ]:




