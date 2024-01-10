#!/usr/bin/env python
# coding: utf-8

# # Control Flow

# In[193]:


marks = 75


# In[194]:


if marks >= 90:
    print("pass")


# 
# - under if row there is a gap/space ->Indundation through which Python tries to understand the begining and end of the if.
# - second,this got executed but no result-> why ? because for condition holding false - no instructions.

# In[196]:


if marks >=90:
    print("pass")
else:
    print("parents need to be intimated")


# In[197]:


marks = 200


# In[198]:


if marks >=100:
    print("just passed")
elif marks >=150:
    print("Good")
elif:
    print("Excellent")


# - this is invalid why in if python checks the order,the moment first statement holds true,it doesn't execute the next.
# 
# - in the above code for marks greater than 100 lets say 151 ->the first condition holds true so it wont read any furthur to print Good

# In[199]:


marks = 24


# In[200]:


if 1<= marks <=49:
    print("Failed")
elif 50 <= marks <= 150:
    print("Passed")
elif 151 <= marks <=200:
    print("Passed with distinction")


# In[201]:


marks = 66


# In[202]:


if 1<= marks <=49:
    print("Failed")
elif 50 <= marks <= 150:
    print("Passed")
elif 151 <= marks <=200:
    print("Passed with distinction")
    
    


# In[203]:


marks_in_subjects = [100,95,65,75,35,30]


# In[204]:


for m in marks_in_subjects:
    if m >= 50:
        print("Pass")
    else:
        print("Fail")


# # USER DEFINED FUNCTION

# #writing code like above for marks is difficult for admin guys in a university to write this they ask for one liner comand ==  UDF

# In[205]:


li = [32,34,26,55,82,93,76,79,61,82]


# In[206]:


def result(marks):
    for m in marks:
        if m >= 50:
            print("Passed")
        else:
            print("fail")


# In[207]:


result(li)


# In[208]:


#lets make a udf to calculate the mean


# In[209]:


a = [22,23,24,24,36,72,84]


# In[217]:


def mean_function(data):
    total = sum(data)
    count = len(data)
    mean = total/count
    return mean


# In[218]:


print(mean_function(a))


# In[219]:


#let's reduce the number of decimals.

x = mean_function(a)
x = "{:.2f}".format(x)
print(x)


# In[ ]:





# In[ ]:





# # PANDAS

# Primarily used for Data Analysis and Data cleaning purposes

# In[3]:


pip install pandas


# In[5]:


import pandas as pd

- In Pandas there are 2 types of Datatypes. 

    1.Dataframe : Stores 2 diminesional data ex - exceldata. EX-Dict
    2.Series :1 D data ex : list, tupple, set
# In[9]:


help(pd.DataFrame)


# # LOADING FILE INTO PANDAS

# In[10]:


import pandas as pd


# In[11]:


heart = pd.read_csv('C:\Python Excel Files  BEPC\clevelanda.csv') #by copying the path 'path\file_name.csv'


# heart -> variable name  used to store the DataFrame created by reading a CSV file using the pandas library in Python.

# In[12]:


heart


# # head(n) - to check the first n reocords
# 

# In[15]:


heart.head(5)


# In[16]:


heart.head(10)


# # Tail()- to show the bottom n records

# In[17]:


heart.tail(4)


# # describe() - gives an overall analysis of the table

# In[18]:


heart.describe()


# # columns: to get names of columns
# 

# In[19]:


heart.columns


# # info() : to check details about columns are there any null values

# In[20]:


heart.info()


# # shape - gives me the details about number of rows and columns
# 

# In[21]:


heart.shape  #here shape is an attribute


# # accessing a particular column

# In[23]:


heart['age']


# In[24]:


heart['gender']


# In[58]:


heart['gender'].head(6) #you could select the first 6 rows this way


# # iloc - to select range of rows and range of  columns

# In[26]:


heart.iloc[:,:4] #selects allrows and 4 coumns


# In[32]:


heart.iloc[:4,:,]  #gives 4 rows and all columns


# In[35]:


heart.iloc[:2,:2]


# In[1]:





# In[38]:


heart.iloc[1,5]  #Row index 1 - note index starts from 0. actually it is second row ,
                 # 5 -> is actually 6th row


# # np.nan- it is null value

# In[39]:


#lets say we want to add null value to the above cell that is obtained from heart.iloc[1,5]= 0 we want to replace with Null(empty) value


# In[42]:


heart.iloc[1,5] = np.nan # why din't it get executed ? because np = numpy not yet called or installed


# In[43]:


pip install numpy


# In[45]:


import numpy as np


# In[46]:


heart.iloc[1,5] = np.nan


# In[47]:


heart.head(6)


# See in the cell it is already fed

# In[48]:


heart.info()


# see- initially 303 was the fps count but because of Nan it got reduced to 302

# # isnull() - checks for null value

# -  for null values either you could check with info()
# or
# -- you could use isnull and sum to see the number of nullvalues in aparticular column

# In[100]:


heart.isnull()


# In[50]:


heart.isnull().sum()


# fps- count 1 because we had set iloc[1,5] = np.nan above
# 
# 
# 

# In[51]:


heart.iloc[1,5]


# In[52]:


heart.iloc[1,6]


# # unique() - displays all unique values in a column

# In[54]:


heart.columns


# In[55]:


heart['ca'].unique()


# In[57]:


heart['ca'].head(5)


# In[60]:


heart['gender'].unique()


# In[61]:


heart['gender']


# # value_counts() - counts the unique elements of each columns
# 

# In[62]:


heart['ca'].unique()


# In[64]:


heart['ca'].value_counts()


# In[65]:


heart['gender'].unique()


# In[66]:


heart['gender'].value_counts()


# In[67]:


heart.columns


# In[68]:


heart['thal'].unique()


# In[69]:


heart['thal'].value_counts()


# Now why is it required before you treat the data, you analysed this and you swa some anomalies and outliers which you shoud be discussing with the client before treating the data.

# In[71]:


heart['thal'].unique()


# In[72]:


heart['thal'].value_counts()


# In[73]:


heart


# In[74]:


heart.head(5)


# Here : class -> is the category of heart disease -> 0 - no disease, 2- severe disease. now let's say I want to calculate the mean age of each of these.
# 

# In[75]:


heart['class'].unique()


# In[76]:


heart['class'].value_counts()


# # groupby()

# In[88]:


heart.groupby('class').mean()


# In[90]:


heart.iloc[:,:4,]


# In[ ]:





# In[ ]:





# **Methods:**
# 
#     - functions that belong to an object.
#     - perform actions or operations on the object.
#     -  you call a method, you use parentheses () after the method name, 
#        which may or may not include arguments.
#     Example: If dataframe is a pandas DataFrame, dataframe.head() is a method call-> returns first 5 rows
# 
# **Attributes:**
# 
#     - variables that belong to an object. 
#     - hold data or state of the object but don't perform actions.
#     - When you access an attribute, you don't use parentheses.
#     Example: In dataframe.columns, columns is an attribute of the dataframe object. 
#             It holds the information about the column labels of the DataFrame.
# 
#  **The dot notation** 
#  
#  (object.attribute or object.method()) is a way to access these properties and functions of objects. 
#   The key difference is in how they are used: methods called (with parentheses), 
#   attributes are accessed (without parentheses).

# In[ ]:





# In[91]:


heart.columns #here columns is an attribute


# In[2]:


heart.info() #here info is a method/function


# In[94]:


heart.isnull().sum()


# In[95]:


heart['age'].head(5)


# In[97]:


heart.isnull().sum()


# In[98]:


heart.isnull()


# In[101]:


heart['age'].unique()


# In[102]:


heart['age'].value_counts()


# In[103]:


heart.info()


# In[104]:





# # pivot()

# In[106]:


import pandas as pd


# In[142]:


w1 = pd.read_csv('C:/Users/Lenovo/Downloads/weather.csv')


# In[143]:


w1



# index =  what you want in x axis;
# 
# columns = is the thing you want in columns;
# 
# values = the data you want in each of these cells, it might be number, strings etc.
# 
# let's say we want date in rows and city in columns

# In[144]:


w1.pivot(index='city',columns='date')


# Let's say I want only humidity to be present in it -so wewoulduse a thirdargument called values

# In[145]:


w1.pivot(index = 'city',columns = 'date', values = 'humidity')


# In[146]:


w1


# In[147]:


w1.pivot(index='date',columns ='temperature',values = 'city' )


# In[148]:


w1.pivot(index='date',columns = ['temperature','humidity'],values = 'city' )


# In[149]:


w1


# In[150]:


w1.pivot(index= 'city',columns ='date')


# In[151]:


w1.pivot(index ='city', columns = 'date', values = 'humidity')


# # pivot_table() - allows you to summarise and aggregate data

# - index= rows
# - columns = the columns you intend to add
# - values = the value in cell.
# - margins= bool, default False
# 
# If margins is True, special All columns and rows will be added with partial group aggregates across the categories on the rows and columns.

# In[152]:


w2 = pd.read_csv('C:/Users/Lenovo/Downloads/weather2.csv')


# In[153]:


w2


# Observe:For the same date 5/1/2017 I have two temperature ->  1 in morning perhaps in afternoon. Thusperhaps we would need some kind   of aggregate.
# 
# and here there is the same month in date.
# 
# 

# In[ ]:





# In[154]:


w2.pivot_table(index= 'city',columns ='date') # the default argument function in pivot_table is set to be mean


# * see  - by default it agrregated the things.

# *df.pivot(index='city',columns ='date') *#this will not work because there are duplicate entries. let's count-> see the code below.

# In[155]:


w2.pivot_table(index= 'city', columns ='date',aggfunc = 'count')


# * see -> the count was 2 thus, it was not accpeting pivot() function

# In[156]:


w2.pivot_table(index= 'city',columns = 'date',aggfunc = 'sum') #note sum as an aggregate here doesn't makes sense


# In[157]:


w2.pivot_table(index= 'city',columns ='date',aggfunc= 'mean',margins ='True') #so by default it  added all to the mean of means


# # Grouper()

# In[ ]:


-A Grouper allows the user to specify a groupby instruction for an object.

*key -str, defaults to None
Groupby key, which selects the grouping column of the target.

*levelname/number, defaults to None
   The level for the target index.

*freqstr / frequency object, defaults to None
  This will groupby the specified frequency if the target selection (via key or level) is a datetime-like object.


# In[158]:


w3 = pd.read_csv('C:/Users/Lenovo/Downloads/weather3.csv')


# In[159]:


w3


# Observe : there are two months here one is 5 -> may, 2nd i 12 -> which is December

# In[160]:


# The entries in date looks like a date, but they are strings - we need to convert them into date


# In[163]:


type(w3.date)


# In[170]:


#to_datetime()   

w3['date']=pd.to_datetime(w3['date']) 


# In[167]:


w3


# In[173]:


type(w3['date']) #gives the type of -it's a series


# In[177]:


type(w3['date'][0]) # here 0 is the 1st element of the column  since in Python indexing starts with 0


# In[188]:


import numpy

w3.pivot_table(index=pd.Grouper(freq= 'M', key= 'date'),columns = 'city')


# In[192]:


w3.pivot_table(index = pd.Grouper(freq = 'M',key = 'date'), columns = 'city')


# In[ ]:




