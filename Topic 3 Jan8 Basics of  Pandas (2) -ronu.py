#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pandas==2.0.2')


# In[2]:


get_ipython().system('pip install pandas == 2.0.2')


# In[4]:


import pandas as pd


# In[5]:


import numpy as np


# In[7]:


help(pd.DataFrame) #Recall: functions could be used on to get list of Functions, variables, class 
                   # in a module or Library or a datatype of a module/library


# In[12]:


pwd #present working directory -> just to check where your kernel is


# In[317]:


heart = pd.read_csv('C:/Python Excel Files  BEPC/clevelanda.csv')


# In[318]:


heart


# In[14]:


heart.head()   #default = 5 thus shows 5 records


# In[15]:


heart.head(6)  #thus,specification would do


# In[16]:


heart.describe()


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





# In[17]:


heart.columns #here columns is an attribute


# In[18]:


heart.info()


# In[19]:


heart['ca']


# In[23]:


#object = mixed set of multiple datatypes


# In[20]:


heart['ca'].unique()


# In[22]:


heart['ca'].value_counts()


# In[26]:


heart.shape 
#recall - not doing any operation -> thus it is an attribute attribute = variable that holds
#data of the module/library


# In[27]:


heart.iloc[1,5]


# In[28]:


#if we wish to change the zero to nan , we will have to use Numpy.

import  numpy as np


# In[29]:


heart.iloc[1,5] = np.nan #nan = attribute = variable in numpy library and so no brackets


# In[35]:


heart.iloc[1,5] #nan = Not a number


# -- changed

# In[34]:


heart.info() #check not just that value but also the entire column whiuch was int changed to float type


# # NAN(NOT A NUMBER):  attribute in Numpy library
# 

# In[37]:


# Example 1: Creating an Array with np.nan

import numpy as np
array_with_nan = np.array([1, 2, np.nan, 4, 5])
print(array_with_nan)


# In[38]:


#Example 2: Basic Operations with np.nan

result1 = np.nan + 10
print(result1)  # Output will be nan

result2 = np.nan * 2
print(result2)  # Output will be nan


# - Any arithmetic operation with np.nan results in np.nan.

# # isnan() : check nan values

# In[39]:


#Example 3: Checking for np.nan with np.isnan()
# Checking which elements are np.nan

nan_check = np.isnan(array_with_nan)
print(nan_check)


# - checking the elements with nan - true if present,and false if not

# In[319]:


heart


# In[321]:


x = np.isnan(heart['age']) #you could use np.isnan with a pandas DataFrame also
x


# In[324]:


x = np.isnan(heart['age']).sum()  #also you could count the number of nan in a column
x


# In[41]:


#Example 4: Handling np.nan in Statistics
# Calculating mean, ignoring np.nan

                         
mean_value = np.nanmean(array_with_nan)
print(mean_value)


# In[ ]:


# Example 5: Replacing np.nan with a Specific Value
# Replacing np.nan with a specific value

filled_array = np.nan_to_num(array_with_nan, nan=0)
print(filled_array) /*don't run - this is for Indication only*/


# In[42]:


heart




# In[43]:


heart['fps'].isnull().sum() #sum()-gives you the total number of Null values for a column  or ever columns


# In[45]:


heart.isnull().sum()#for every columsns


# In[46]:


heart['ca'].unique()


# In[47]:


heart['ca'].value_counts()


# In[48]:


# NOTE : always advisable to check with unique firt, coz it gives nam value as well.

a = [1,2,3,4,5,6,np.nan] #list varibale can also hol nan
a = pd.DataFrame(a) #converted to DataFrame using pandas. 
u = a[0].unique()
v = a[0].value_counts()

print(u)
print(v)


# [ 1.  2.  3.  4.  5.  6. nan] # see counted the nan as well
#                               # but value_counts dint consider nan.

# In[49]:


heart


# In[50]:


heart['class']


# In[51]:


heart['class'].value_counts()


# # .index

# In[64]:


#now let's say from the above I intend to see only details of class 1 or any particular class.

classcounts = heart['class'].value_counts()
classcounts_1 = classcounts[classcounts.index == 1]
print(classcounts_1)


# this way we could filter a particular row

# In[325]:


heart


# In[326]:


#let's say I need to find out 300th row only for columns fps and restecg

x = heart[['fps','restecg']]
y = x[x.index==300] #WAY TO READ MULTIPLE COLUMNS DOUBLE SQUARE BRACKETS.
y


# # i.sin()

# In[65]:


#now let's say  I intend to see  details of class 1 and class 2 or multiple classes


classcounts_1_2 = classcounts[classcounts.index.isin([1,2])]
print(classcounts_1_2)


# # groupby()

# In[ ]:


heart.groupby('class').mean()  

#This will throw error because -> the datatypes in the DataFrame has objects as well.
#so we need to first filter those columns and then find the mean


# In[59]:


heart.dtypes #Gives the list of datatypes used: 'ca' and 'thal' are objects      


# In[60]:


heart_numeric = heart.select_dtypes(include=[np.number])



# In[62]:


heart_numeric


# In[63]:


heart_numeric.groupby('class').mean()


# #Now,mean is calculated and grouped by class

# In[66]:


heart_numeric


# # pivot_table()

# In[67]:


heart_numeric.pivot_table(index='class',columns='age',values ='fps',aggfunc ='mean')


# In[68]:


heart_numeric.pivot_table(index='class',columns='fps',values ='age',aggfunc ='mean')


# In[69]:


heart_numeric.pivot_table(index='class',columns='fps',values =('age','chol'),aggfunc ='mean')


# # sort_values() - ASCENDING

# In[72]:


heart_numeric


# In[73]:


heart_numeric.groupby('class').mean()


# In[79]:


#Ascending

sorted_by_age_asc= heart_numeric.sort_values(by=['age'],ascending = True)


# In[80]:


sorted_by_age_asc


# # sort_values() - ASCENDING

# In[84]:


#descending

sorted_by_age_desc = heart_numeric.sort_values(by= ['age'],ascending = False)


# In[85]:


sorted_by_age_desc


# In[86]:


#for multiple columns

sorted_by_age_trestbps = heart_numeric.sort_values(by=['age','trestbps'],ascending = True)


# In[87]:


sorted_by_age_trestbps


# In[89]:


heart_numeric


# # set_index()
# 

# sorts the table and arranges indexing with respect to the column
# 
# After this operation, each row in the DataFrame is identified by the value in the 'age' column instead of the default integer index.
# 
# 

# In[90]:


set_index_age = heart_numeric.set_index('age')
set_index_age


# In[92]:


set_index_age.head(2)


# In[93]:


set_index_age.iloc[0,0]  


# see this : it gives the result 1 i.e now the age column is taken as index
# 

# # reset_index()

# In[95]:


set_index_age.reset_index()


# In[96]:


#lambda : operation of something to a column


# In[97]:


heart_numeric


# In[98]:


heart_reformed = heart #gave this sothagt original table doesnt changes


# In[99]:


heart_reformed['age']= heart['age'].apply(lambda x: x+100)


# In[100]:


heart_reformed


# In[101]:


heart_reformed['age']=heart_reformed['age'].apply(lambda x: x-100)


# In[102]:


heart_reformed


# In[104]:


heart_reformed['gender']= heart_reformed['gender'].apply(lambda x:x*1)


# In[105]:


heart_reformed


# # DATA CLEANING

# In[106]:


import pandas as pd


# In[108]:


data = pd.read_csv('C:/Python Excel Files  BEPC/Company_Data (1).csv')


# In[109]:


data


# The above was in csv format hence the method.
# let's do it for xlsx format

# In[110]:


import pandas as pd


# In[111]:


import openpyxl


# In[113]:


data = pd.ExcelFile('C:/Python Excel Files  BEPC/Company_Data(1) xlxs.xlsx')


# In[114]:


data


# In[119]:


lend = pd.read_excel(data)


# In[118]:


lend


# In[120]:


lend = pd.read_excel('C:/Python Excel Files  BEPC/Company_Data(1) xlxs.xlsx')


# In[121]:


lend


# In[122]:


lend.shape


# In[123]:


lend.head()


# In[124]:


lend.tail()


# In[125]:


lend.info()


# Check  there are two object type. Lets exploremore
# 

# In[129]:


lend['Urban']


# In[131]:


lend['Urban'].unique()


# In[133]:


lend['Urban'].value_counts()


# In[135]:


lend['US'].unique()


# In[136]:


lend_numeric = lend.select_dtypes(include=[np.number])


# In[137]:


lend_numeric


# In[138]:


lend_numeric.dtypes


# In[139]:


lend_numeric.isnull()


# In[141]:


lend_numeric.isnull().sum()


# # dropna(): removes the 

# In[144]:


#1. axis Parameter:

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9]
})



# AXIS specifies whether to drop rows or columns that contain missing values.
# axis=0 ->Drop rows with missing values (default).. i.e dropna(without parameters)= removing rows with missing values.
# axis =1 ->drop columns with missing values.

# In[ ]:


df_drop_rows = df.dropna(axis=0) #will drop the rows where rows would  have missing values.

df_drop_columns = df.dropna(axis=1) ##will drop the rows where Columns would  have missing values.


# In[150]:


# 2. how Parameter

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9],
    'D': [np.nan,np.nan,np.nan]
})


# The how parameter determines how to decide if a row/column should be dropped.
# 
# how='any': Drop if any value is missing (default).
# how='all': Drop if all values are missing.

# In[151]:


df


# In[164]:


df_drop_any = df.dropna(how='any', axis=0) # Drop rows where any value is missing_


# In[156]:


df_drop_any = df.dropna(how='all',axis =0)  # Drop rows where all values are missing


# In[159]:


df_drop_any =df.dropna(how='all',axis=1) # Drop Columns where all values are missing


# In[161]:


#3. thresh Parameter

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9],
    'D': [np.nan,np.nan,np.nan]
})


# The thresh parameter sets a threshold for the minimum number of non-NA values.

# In[162]:


# Drop rows with less than 2 non-NA values
df_thresh = df.dropna(thresh=2,axis =0)


# In[166]:


#examples


# In[167]:


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9],
    'D': [np.nan,np.nan,np.nan]
})


# In[168]:


df.dropna()


# In[169]:


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9],
    'D': [np.nan,np.nan,np.nan]
})


# In[171]:


df.dropna(axis =0)


# In[172]:


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9],
    'D': [np.nan,np.nan,np.nan]
})


# In[173]:


df.dropna(axis =1)


# In[174]:


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9],
    'D': [np.nan,np.nan,np.nan]
})


# In[175]:


df


# In[176]:


df.dropna(how='any',axis =0)


# In[177]:


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9],
    'D': [np.nan,np.nan,np.nan]
})


# In[178]:


df


# In[179]:


df.dropna(how ='any',axis =1)


# In[180]:


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9],
    'D': [np.nan,np.nan,np.nan]
})
df


# In[181]:


df.dropna(how='all',axis =1)


# In[182]:


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9],
    'D': [np.nan,np.nan,np.nan]
})
df


# In[184]:


df.dropna(how ='all',axis =0)


# In[185]:


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9],
    'D': [np.nan,np.nan,np.nan]
})
df


# In[186]:


df.dropna(thresh = 4,axis =0)


# In[187]:


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9],
    'D': [np.nan,np.nan,np.nan]
})
df


# In[188]:


df.dropna(thresh =3)


# In[189]:


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9],
    'D': [np.nan,np.nan,np.nan]
})
df


# In[190]:


df.dropna(thresh=2)


# In[191]:


df.dropna(thresh=1)


# # del : for removal of a column

# In[192]:


lend


# In[193]:


lend.info()


# In[194]:


#deleting US column

del lend['US']


# In[195]:


lend


# In[196]:


lend.head()


# In[197]:


lend.info()


# In[199]:


lend.isnull().sum()


# # drop_duplicates():removes the duplicate values

# In[200]:


lend.drop_duplicates()


# In[201]:


lend.info()


# # rename(): to rename a particular column
# 

# In[203]:


lend = lend.rename(columns = {'Sales':'sales'})


# In[204]:


lend


# In[205]:


lend = lend.rename(columns = {'sales':'sales1'})


# In[206]:


lend


# # .astype() Changing the datatype in a dataframe 

# In[207]:


lend.dtypes


# In[208]:


#CompPrice - change it to float

lend['CompPrice']=lend['CompPrice'].astype(float)


# In[209]:


lend.dtypes


# In[211]:


#to change to numeric lets say sales1

lend['sales1']=pd.to_numeric(lend['sales1'])


# In[212]:


lend.dtypes


# # .str.strip() : removes white spaces if any
# 
# 

# .str can be used only with string values #Remember!!

# In[213]:


lend['Urban']=lend['Urban'].str.strip()


# In[214]:


lend


# # .str.lower() :converts into lower script

# In[215]:


lend


# In[216]:


lend['Urban']= lend['Urban'].str.lower()


# In[217]:


lend


# # .replace() replaces a particular value with value of your choice

# In[219]:


lend['Age'].unique()


# In[220]:


lend['Age'] =lend['Age'].replace(42,44)


# In[221]:


lend['Age'].unique()


# *Replaced

# In[222]:


lend


# In[223]:


#lets make it for a column with Characters

lend['Urban'].unique()


# In[225]:


lend['Urban'] = lend['Urban'].replace('yes', 'Yeah')


# In[227]:


lend['Urban'].unique()


# In[230]:


lend['Urban'] = lend['Urban'].replace('no','Nah')


# In[231]:


lend['Urban'].unique()


# - You might see lot of spaces or some values like (0.28,' _  ', 0.28,0.29,....)
#   here you might dot thew same thing copy then gofo rreplace
#   

# In[ ]:


lend['Urban'] = lend['Urban'].replace('' _ '',0.11) #DONT RUN


# In[232]:


lend


# In[234]:


lend = lend.rename(columns = {'sales1':'sales2'})


# In[235]:


lend = lend.rename(columns = {'sales1':'sales2'})


# In[236]:


del lend['Urban']


# In[237]:


lend


# # drop()  : drops one or multiple columns

# In[238]:


lend


# In[ ]:


#dropping Advertising and Population column

lend = lend.drop(columns= ['Advertising','Population'])


# In[247]:


lend


# # CREATION OF DATA FRAME

# - array based : should have same number of elements

# In[259]:


salesops = pd.DataFrame ({'bda': ('Santosh','Sahil','Rohit','Pawan','Joshi'), 'city': ('Delhi','Gaziabad','Mumbai','Bhubaneswar',np.nan),'salary':(20000,45000,45000,30000,50000),'revenue':(800000,300000,600000,800000,400000)})


# In[260]:


salesops


# In[262]:


salesops.dropna(how ='all',axis = 0)


# In[263]:


salesops = pd.DataFrame ({'bda': ('Santosh','Sahil','Rohit','Pawan','Joshi'), 'city': ('Delhi','Gaziabad','Mumbai','Bhubaneswar',np.nan),'salary':(20000,45000,45000,30000,50000),'revenue':(800000,300000,600000,800000,400000)})


# # fillna : replacing nan with a value of choice

# In[264]:


salesops


# In[266]:


salesops['city']=salesops['city'].fillna('Dehradun')


# In[267]:


salesops


# In[268]:


salesops['bda'] = salesops['bda'].str.upper()


# In[269]:


salesops


# In[270]:


lend


# In[277]:


salesops = pd.DataFrame ({'bda': ('Santosh','Sahil','np.nan','Pawan','Joshi'), 'city': ('Delhi',np.nan,'Mumbai','Bhubaneswar',np.nan),'salary':(20000,'45%000','45000$',30000  ,50000),'revenue':(800000,300000,600000,800000,np.nan)})


# In[278]:


salesops


# In[279]:


salesops.info()


# Look at the issue - 1st 2columsn  city got 2 null values and revenue got 2. we need to fix themup first

# In[280]:


salesops['city'].unique()


# In[281]:


#need to remove nan

salesops['city']=salesops['city'].fillna('Dehradun')


# In[282]:


salesops


# In[283]:


salesops.info()


# city column is fixed now-no of rowsmatching non-null  values

# In[285]:


#need to fix revenue

salesops['revenue'].unique()


# In[290]:


salesops['revenue'] =salesops['revenue'].fillna(100000)


# In[291]:


salesops


# In[292]:


salesops.info()


# *nan is removed but look athe values in salary

# In[293]:


salesops


# In[294]:


salesops['salary'].unique()


# # REGEX

# In[295]:


#This has to be replaced with something that is numeric we would use both replace and regex = regular expression

# Recall lend['Urban'] = lend['Urban'].replace('' _ '',0.11) (this was the syntax)


# In[303]:


salesops['salary']=salesops['salary'].replace(regex=True,to_replace = '[^0-9]',value ='')


# - In Python, there's a tool called "regular expression" (often shortened to "regex") that's really good at finding patterns in     text. 
# - The pattern ^0-9 way of saying "any number from 0 to 9" in the language of regular expressions.

# In[305]:


salesops


# *gone

# In[306]:


salesops.info()


# In[307]:


salesops['salary'] = salesops['salary'].astype(float)


# In[308]:


salesops.info()


# In[309]:


salesops['city'] =salesops['city'].str.lower()


# In[ ]:


#multiple replacements

salesops['city']


# In[310]:


salesops.info()


# In[311]:


salesops


# In[312]:


#multiple replacements

salesops['city'] =salesops['city'].replace(['delhi','dehradun','mumbai','bhubaneswar','dehradun'],['NCR','UK','Maharashtra','Odisha','JK'])


# In[313]:


salesops


# *did multiple replacements

# In[314]:


#renamed the column city to state

salesops = salesops.rename(columns = {'city':'state'})


# In[315]:


salesops


# In[316]:


salesops.info()


# In[ ]:




