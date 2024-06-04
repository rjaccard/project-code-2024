``` python
''' Package import test '''
import os
import gzip
import random
import pickle
import re
import itertools
import collections
import operator
import requests
from urllib.parse import *
from datetime import *
from dateutil.parser import parse

import math
import sklearn
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import *

import ast
import gensim
import string
import nltk
import codecs
import json
import vaderSentiment
import spacy
from empath import Empath
from bs4 import BeautifulSoup

import networkx as nx

from IPython.display import Image
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.simplefilter('ignore')

print("Package import test successful!")
```
:::

::: {.cell .code id="hrszqMuJm1O1"}
``` python
import warnings
warnings.filterwarnings('ignore')
```
:::

::: {.cell .code id="53bTbK3qLqjk"}
``` python
%matplotlib inline

# General
import pandas as pd
import numpy as np

# For plotting
import matplotlib.pyplot as plt
import seaborn as sns

# For graph-related stuff
import networkx as nx

# For regression analyses and statistical tests
import scipy.stats as stats
import statsmodels.stats
import statsmodels.formula.api as smf

# For classification
from sklearn import linear_model as lm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```
:::

::: {.cell .markdown id="Oig-75U9wJQb"}
# **BASIC PYTHON**
:::

::: {.cell .markdown id="dcg1i1jrMolU"}
### **Lists**
:::

::: {.cell .code id="dgEpw5DjMvSJ"}
``` python
#Sort list
sorted_list = sorted(my_list, reverse=True)

#Cumulative sum
np.array(my_list).cumsum()

#Extend
l = [0,1]
l.extend([1,1])
# --> [0,1,1,1]
```
:::

::: {.cell .markdown id="aC5Qx2aZMsyS"}
### **Dicts**
:::

::: {.cell .code id="uRUW48LiMn9A"}
``` python
from operator import itemgetter

#Sort dict by values
sorted_dict = sorted(dict.items(), key=itemgetter(1), reverse=True)

#Sort dict by keys
sorted_dict = sorted(dict.items(), key=itemgetter(0), reverse=True)

#Create dict from two lists
my_dict = dict(zip(keys_list, values_list))
```
:::

::: {.cell .markdown id="HAJYoJIOetfs"}
### **Combinations**
:::

::: {.cell .code id="xDq-GtUOevtt"}
``` python
import itertools
from itertools import combinations

#All combinations of 2 elements from one list
for i,j in itertools.combination(my_list, 2) :
```
:::

::: {.cell .markdown id="oAK9kJB9TSW4"}
# **BASIC PANDAS**
:::

::: {.cell .markdown id="m5QBcbtAbPu_"}
### **ADD - Column / Row** {#add---column--row}
:::

::: {.cell .code id="tR7uBExNbQRi"}
``` python
# ---- Add column as dict ------
# df['key'] = column containing keys of dict
# df['col'] = column containing values of dict
df['col'] = df['key'].map(my_dict)

# ---- Add row as list ----
df.loc[len(df.index)] = [1, 2, 3]
```
:::

::: {.cell .markdown id="rKU4W0iKbVI9"}
### **CREATE - DataFrame / Serie** {#create---dataframe--serie}
:::

::: {.cell .code id="zVmvTNfcbX2E"}
``` python
# ----- From lists ----
l1 = [1,2]
l2 = [3,4]
df = pd.DataFrame(list(zip(l1, l2)),
                  columns =['name1', 'name2'])

# ----- From 1 dict ----
my_dict = {'Japan' : 2, 'USA' : 6}
df = pd.DataFrame.from_dict(my_dict, orient='index').reset_index()
df.columns = ['key_name', 'value_name']

# ------ From 2 dicts -----
d1 = {'Japan' : 2, 'USA' : 6}
d2 = {'Japan' : 'Tokyo', 'USA' : 'Miami'}
s1 = pd.Series(d1)
s2 = pd.Series(d2)
df = pd.DataFrame([s1, s2]).T.reset_index()
df.columns = ['key_name', 'val_d1', 'val_d2']


# ----- From Series ----
s = df['col'].value_counts()
df2 = pd.DataFrame(s)

# ----- From Series - quick -----
df2 = pd.DataFrame(df['col'].value_counts())


# ----- Empty ----
df = pd.DataFrame(columns = ['col1', 'col2'])


# ----------------------------------------
# ----- Serie from dict ----
s = pd.Series(my_dict)
```
:::

::: {.cell .markdown id="rqxA8izLZfuB"}
### **Dates**
:::

::: {.cell .code id="9_ZJhqk2Zh40"}
``` python
from datetime import datetime

# ---- Today ----
now = datetime.now()
day = now.strftime("%d")
print("day:", day)

# ---- Convert to Datetime ----
df.date = pd.to_datetime(df.date)

# ----- Retrieve year -----
df['year'] = df.date.apply(lambda x : x.year)
df['year']= df['date'].dt.day

# ------ Retrieve day of year -----
df['dayofyear'] = df['date'].dt.dayofyear


# ----- Retrieve Month and Year -----
df['month_year'] = df['date'].apply(lambda x : pd.to_datetime(x.strftime('%Y-%m')))

# ----- Filter DF -----
df_t2 = df.loc[ (df['date'] >= pd.to_datetime("2014-04-31")) &
                (df['date'] < pd.to_datetime("2014-12-31"))
              ]
```
:::

::: {.cell .markdown id="1Ts1c6I1cMF4"}
### **Duplicates**
:::

::: {.cell .code id="MtL3R4G0cN77"}
``` python
df.drop_duplicates(subset=['col'], keep='first', inplace=True)
```
:::

::: {.cell .markdown id="9pR0Byy8ipmv"}
### **Groupby**
:::

::: {.cell .code id="EJFwl9PDirYZ"}
``` python
#----- By 2 columns ----
df.groupby(["col1", "col2"]).count().reset_index()

#---- Iterate through grouped DataFrames ----
grouped_df = df.groupby('col')

#g_name --> value of grouped_col
#g_df --> DF with index = row_index (original df)
for g_name, g_df in grouped_df :
    row_idx = list(g_df.index.values)
```
:::

::: {.cell .markdown id="jiWYgYe1TYM-"}
### **Index/ID**
:::

::: {.cell .code id="YHaz5KNYTW9i"}
``` python
# ----- Add column ID -----
df['id'] = [i for i in range(len(df))]

# ----- Set column as index -----
df.set_index('col', inplace=True)

# ----- Reset index ------
df.reset_index(inplace=True)
```
:::

::: {.cell .markdown id="Gy-4-SInc5_L"}
### **Merge**
:::

::: {.cell .code id="vC4KmC0Bc7kK"}
``` python
df1 = df1.merge(df2, right_index=True, left_on='col')
df1 = df1.merge(df2, right_on='col2', left_on='col')
```
:::

::: {.cell .markdown id="p8SMjTk2cScg"}
### **NaN values**
:::

::: {.cell .code id="WSNK3YCwcUJT"}
``` python
# ---- Check if NaN in df -----
s = pd.DataFrame(df.isna().sum())
s = s.loc[s['eee'] > 0]

#---- All columns -----
df.dropna(inplace=True)

#---- Replace all NaN ----
df.fillna(0)

#---- Count NaN 1 column ----
print('Number of NaN values : ', df['col'].isna().sum())

#---- Replace NaN 1 column ----
df['col'].fillna(0, inplace=True)
```
:::

::: {.cell .markdown id="UEsnCqb5ikEr"}
### **Pivot-table**
:::

::: {.cell .code id="oYPF0JxXijcr"}
``` python
# ----- Predefined function numpy -----
pivot_table = pd.pivot_table(df,  index=['birthyear'],
                                  columns=['birthdate'],
                                  values='alive', aggfunc=np.mean)

# ----- Create function ----
def my_func(list_val) :
    return list_val.mean()

pivot_table = pd.pivot_table(df,  index=['birthyear'],
                                  columns=['birthdate'],
                                  values='alive', aggfunc=my_func)

# ----- Cross-table -----
table = pd.pivot_table(df, index=['A', 'B'], columns=['C'], values='D', aggfunc=np.sum)
```
:::

::: {.cell .markdown id="FPWHQqt4b49w"}
### **Rename/Drop columns**
:::

::: {.cell .code id="vrAHmNWtb5sT"}
``` python
#----- Drop columns -----
df.drop(columns=['col', 'col2'], inplace=True)
df.drop('col', axis=1, inplace=True)

# ---- Rename columns -----
df.rename({'old_name' : 'new_name'}, axis=1, inplace=True)
df.columns = ['new1', 'new2']
```
:::

::: {.cell .markdown id="P53-ehD3LzQk"}
# **PANDAS**
:::

::: {.cell .markdown id="4msyLFZ3L3qX"}
### **Open files**
:::

::: {.cell .code id="_kgBq7xEL1V3"}
``` python
# ---- .csv -----
path = "/data/part-1/edgelist.csv"
df = pd.read_csv(path, sep=",")

# ----- .tsv -----
path = "/data/part-1/edgelist.tsv"
df = pd.read_csv(path, sep="\t")

# ----- .tsv.gz -----
path = "/data/part-2/questions.tsv.gz"
df = pd.read_csv(path, sep="\t", compression="infer")
```
:::

::: {.cell .markdown id="PZvUgo-XL_tF"}
### **Distribution**
:::

::: {.cell .markdown id="iV0vz3EuI4xg"}
We can see here that the \'VARIABLE\' follows a power-law distribution :
very large values are rare but not very rare.
:::

::: {.cell .code id="65upH4EskhWM"}
``` python
# ---- With value_counts -----
dist = df[col_name].value_counts()
dist.plot(kind='bar')

plt.title('Distribution - ')
plt.xscale('log')
plt.yscale('log')

# ---- Histogram with seaborn ----
fig, ax = plt.subplots(1,1, figsize=(10,6))
sns.histplot(data = df, x = col_name, element ='step', ax=ax)

ax.set_title('Distribution - ')
ax.set_xscale('log')
ax.set_yscale('log')

# ---- Histogram with KDE -----
fig, ax = plt.subplots(1,1, figsize=(10,6))
sns.distplot(data = df, x = col_name)
plt.title('Distribution - ')
ax.xscale('log')
ax.yscale('log')

# ---- KDE -----
fig, ax = plt.subplots(1,1, figsize=(10,6))
sns.histplot(data = df, x = col_name, stat='density', kde=True)
ax.set_title('Distribution - ')
ax.set_xscale('log')
ax.set_yscale('log')

# ----- ECDF (Empirical Cumulative Distribution Function) -----
def plot_ecdf_ccdf(df, col_name, log_x=False, log_y=False, figsize=(10,6)) :
    fig, ax = plt.subplots(1,1, figsize=figsize)
    sns.ecdfplot(data=df, x=col_name, ax=ax, label='ECDF')
    sns.ecdfplot(data=df, x=col_name, complementary=True, ax=ax, label='CCDF')

    if log_x :
        ax.set_xscale('log')
    if log_y :
        ax.set_yscale('log')

    ax.set_title('ECDF / CCDF - '+ col_name)
    ax.legend()
    plt.show()

plot_ecdf_ccdf(df, 'birthyear', log_
               x=False, log_y=False, figsize=(10,6))
```
:::

::: {.cell .markdown id="dZ9FONCOl0pw"}
### **Count values of 1 column**
:::

::: {.cell .code id="UBY_FSi_l3Kr"}
``` python
# ---- After GroupBy ----
diff_values = df.groupby('col')['col2'].nunique()

# ---- Unique values ----
nb_unique_val = df['col'].nunique()
```
:::

::: {.cell .markdown id="tElK3cA5XeFD"}
### **Retrieve values of 1 column**
:::

::: {.cell .code id="tkb0XXknmk_K"}
``` python
#------ UNIQUE ------
col_unique = list(df['col'].unique())

# ----- ALL -----
#Numpy
col = df['var'].to_numpy()
#List
col = list(df['var'].to_numpy())
#Dict : index --> df['col']
dict_col = df['col'].to_dict()
```
:::

::: {.cell .markdown id="Kzs_zu2bg0eD"}
### **Categorical**
:::

::: {.cell .code id="Cx626vLdg2k6"}
``` python
# ----- Own categories -----
df['category_col'] = pd.cut(  df['col'],
                              [0, 20, 40, 60, 80],
                              labels=['young','middle-aged','old','really old'])
# ---- Empirical quantiles ----
df['category_col'] = pd.qcut( df['col'], 4,
                              labels=['young','middle-aged','old','really old'])
```
:::

::: {.cell .markdown id="zxgf975AhJHJ"}
### **Top values**
:::

::: {.cell .code id="KRVP0OfPhLph"}
``` python
# ----- Retrieve top 10 -----
df_top10 = df.nlargest(n=10, columns=['to_sort'])

df_top10 = df.sort_values('to_sort', ascending=False).head(10)

#---- Groupby/count/top10 -----
top_10 = pd.DataFrame(df.groupby('col')['val'].count())
print(top_10.nlargest(n=10, columns=['val']))

# ----- SERIE ----
s = df['col'].value_counts()
print('Max value : ', s.max())
print('Index of max value : ', s.idxmax())

# ---- COLUMN ----
print('Max value of column col : ', df['col'].max())
print('Index max value of column col : ', df['col'].idxmax())

row_max = df.iloc[df['col'].idxmax(), :]
```
:::

::: {.cell .markdown id="IXmHzuKCduDL"}
### **Filter Serie**
:::

::: {.cell .code id="9KDRf-cRd2Jz"}
``` python
counts = df.groupby(['col'])['col2'].nunique()
to_keep = counts.loc[counts > 1].index

#Filter original df
df2 = df.loc[df['col'].isin(to_keep)]
```
:::

::: {.cell .markdown id="DBVMdPQAbfZj"}
### **All possible combinations**
:::

::: {.cell .code id="W0yUNflcbhjs"}
``` python
def compare(elem1, elem2) :
  return  elem1['col1'] == elem2['col1'] and \
          elem1['col2'] == elem2['col2']

#Create empty dataframe
merged_df = pd.DataFrame(columns = ['col1', 'col2', 'col3'])

#Group by one value and iterate through the different dataframes
grouped_df = df.groupby('col')

for group_name, group_df in grouped_df :
      x = list(group_df.index.values)

      #For each combination of two elements
      for i,j in itertools.combinations(x,2) :

          #Retrieve elements
          elem1 = df.iloc[i, :]
          elem2 = df.iloc[j, :]

          #Satisfy conditions for matching
          if compare(elem1, elem2) :

              #Add to empty DataFrame
              merged_df.loc[len(merged_df.index)] = [elem1['col1'], elem2['col2'], elem1['col2']]
```
:::

::: {.cell .markdown id="9rftL1rBhcK2"}
### **All possible combinations - Merge**
:::

::: {.cell .code id="BH6slbcYhemB"}
``` python
df2 = df.merge(df, how='outer', on='var_in_common')

filter_conditions = ((df2['col1_x'] == df2['col1_y']) &
                     (df2['col2_x'] == df2['col2_y']))

df_merged = df2.loc[filter_conditions]
```
:::

::: {.cell .markdown id="mrF8Xn0GJ_nx"}
# **DATA VISUALIZATION**
:::

::: {.cell .markdown id="bCx_jw2enkT2"}
### **Initialisation**
:::

::: {.cell .markdown id="q24ycB1oMfcn"}
#### **Seaborn - Fig Size**
:::

::: {.cell .code id="fdSpz1o5MiFx"}
``` python
fig, axs = plt.subplots(1,2, figsize=(15, 5))
sns.pointplot(data=df, x="finished", y="col1", ax=axs[0])
sns.pointplot(data=df, x="finished", y="col2", ax=axs[1])
```
:::

::: {.cell .markdown id="ZBp-7vg4k9NG"}
#### **Multiple subplots**
:::

::: {.cell .code id="pA3V9Sqjk_av"}
``` python
fig, ax = plt.subplots(4,4, figsize= (8,6), sharey = True, sharex = True)

for i in range(16):
    sbplt = ax[i%4, math.floor(i/4)]
    sbplt.hist(serie.iloc[i].values)
    sbplt.set_title(serie.index[i])

fig.tight_layout()
```
:::

::: {.cell .markdown id="SBvtdapLVFgU"}
### **Array / Heatmap** {#array--heatmap}
:::

::: {.cell .code id="ybiNzCp4VDrm"}
``` python
arr = np.zeros((5,5))

arr = pd.crosstab(df['col1'], df['col2']).fillna(0)

arr = pd.crosstab(df['col1'], df['col2'], values = df['col3'],
                  margins=False, aggfunc='sum')

sns.heatmap(arr, annot=True)
```
:::

::: {.cell .markdown id="bfMI7HHFnyC7"}
### **Boxplot (distribution)**
:::

::: {.cell .code id="scQGwpx-n8Yl"}
``` python
plt.boxplot(df['col'])

#Compare distributions of categorical variable
sns.boxplot(x="occupation", y="pageviews", data=df)
```
:::

::: {.cell .markdown id="wq7wbUQpr_X5"}
### **Point estimates**
:::

::: {.cell .markdown id="sQk-ClFasCTa"}
#### **Pointplot**
:::

::: {.cell .code id="HOApwQ_rsGX_"}
``` python
# x --> categorical/binary variable
# y --> point estimates + CI
sns.pointplot(data=df, x="sexe", y="pageviews", join=False)
sns.pointplot(data=df, x="sexe", y="pageviews", join=True)
```
:::

::: {.cell .markdown id="_XMywEiasHIi"}
#### **Barplot**
:::

::: {.cell .code id="VSLjJIj-sIr0"}
``` python
# x --> categorical variable
# y --> point estimates of pageviews for each category + CI
sns.barplot(x="occupation", y="pageviews", data=df)
```
:::

::: {.cell .markdown id="9QKHko9Pn04H"}
### **Scatter**
:::

::: {.cell .code id="wrjUjvoupTOg"}
``` python
plt.scatter(df['col1'], df['col2'], s=2, alpha=0.2)

#With regression line
fig, ax = plt.subplots(1,1, figsize=(10,6))
sns.lmplot(data=df, x='col1', y='col2', hue='col3', ax=ax)

#Scatter + histogram for each variable
sns.jointplot(x=df['col1'], y=df['col2'], kind="hex")
sns.jointplot(x=df['col1'], y=df['col2'], kind="reg")

#Grille de scatterplots
sns.pairplot(df)
```
:::

::: {.cell .markdown id="danm51vCvWdd"}
#### **Stacked plots**
:::

::: {.cell .code id="pVNQgnpDvYt4"}
``` python
fig, ax = plt.subplots()
ax.stackplot(year, my_dict.values(),
             labels=my_dict.keys(), alpha=0.8)
ax.legend(loc='upper left')

#index on x
#Vals of col1, col2 on y
df.plot.bar(stacked=True)
```
:::

::: {.cell .markdown id="6xT-0aNXrU_4"}
### **Uncertainty**
:::

::: {.cell .markdown id="YKHrOU_mtf3b"}
#### **Courbes evolution**
:::

::: {.cell .code id="I1h5n-Vmip3o"}
``` python
# ----- Directly ----
# Like groupby month + avg on numwords1 + CIs
sns.lineplot(x="month_created", y="numwords1", data=df)


# ---- With std ----
grouped_df = df.groupby(df['year']).apply(lambda x: pd.Series({
                                          'avg': x['col'].mean(),
                                          'std': x['col'].std()
                                          }))

plt.fill_between(grouped_df.index, grouped_df.avg - grouped_df.std,
                 grouped_df.avg + grouped_df.std, alpha = 0.5, color = 'gray')
plt.plot(grouped_df.avg, color = 'black', marker='o')


# ---- With bootstrap ----
def bootstrap(df, nb_iters=1000):
    vals = []
    for i in range(nb_iters) :
        sample = df.sample(len(df), replace=True)

        #TO CHANGE !!! Compute the value you want to estimate
        val_ = np.mean(sample.groupby('year')['pageviews'].mean().values)
        vals.append(val_)

    return np.mean(np.array(vals)), (np.percentile(vals, 2.5), np.percentile(vals, 97.5))

avg_list = []
inf_list = []
sup_list = []

for year in range(2000, 2010) :
    avg, (inf,sup) = bootstrap(df)
    avg_list.append(avg)
    inf_list.append(inf)
    sup_list.append(sup)

plt.fill_between([year for year in range(2000, 2010)], inf_list,
                 sup_list, alpha = 0.5, color = 'gray')
plt.plot(avg_list, color = 'black')
```
:::

::: {.cell .markdown id="ldQBDpIgtku3"}
#### **Errorbar**
:::

::: {.cell .code id="2T_slRqRtmVz"}
``` python
# ---- With std ----
grouped_df = df.groupby(df['year']).apply(lambda x: pd.Series({
                                          'avg': x['col'].mean(),
                                          'std': x['col'].std()
                                          }))

plt.errorbar(grouped_df.index, grouped_df.avg,
             yerr = grouped_df.std,
             capsize= 3)


# ---- With Bootstrap ----
def bootstrap(df, nb_iters=1000):
    vals = []
    for i in range(nb_iters) :
        sample = df.sample(len(df), replace=True)

        #TO CHANGE !!! Compute the value you want to estimate
        val_ = np.mean(sample.groupby('year')['pageviews'].mean().values)
        vals.append(val_)

    return np.mean(np.array(vals)), (np.percentile(vals, 2.5), np.percentile(vals, 97.5))

avg_list = []
inf_list = []
sup_list = []

for year in range(2000, 2010) :
    avg, (inf,sup) = bootstrap(df)
    avg_list.append(avg)
    inf_list.append(inf)
    sup_list.append(sup)

plt.errorbar([year for year in range(2000, 2010)], avg_list,
             yerr = [inf_list, sup_list],
             capsize= 3)
```
:::

::: {.cell .markdown id="vd9iddTKTMro"}
### **Horizontal Barplot (display results)**
:::

::: {.cell .code id="juYMW5osTQh9"}
``` python
from operator import itemgetter

#Sort dictionary by values
res_sorted = sorted(res.items(), key=itemgetter(1), reverse=True)
keys = [i for (i,j) in res_sorted]
values = [j for (i,j) in res_sorted]

fig, ax = plt.subplots(1, 1, figsize=(10, 20))
sns.barplot(x=values, y=keys, ax = ax)
```
:::

::: {.cell .markdown id="XQnp9UKkDIJZ"}
### **PCA**
:::

::: {.cell .markdown id="rE5_CFYvGpUw"}
Tip : use PCA on data before clustering (curse of dimensionality!)
:::

::: {.cell .code id="UcJ28bLwDKHg"}
``` python
#TSNE --> features of sample in new dimension
from sklearn.manifold import TSNE

X_reduced_tsne = TSNE(n_components=2, init='random', learning_rate='auto', random_state=0).fit_transform(X)

#PCA
from sklearn.decomposition import PCA

pca_transformer = PCA(n_components=2)

X_train_pca = pca_transformer.fit_transform(X_train)
X_test_pca = pca_transformer.transform(X_test)

plt.scatter(X_train_pca[:,0], X_train_pca[:,1], alpha=0.6)
```
:::

::: {.cell .markdown id="RWVtURVIeWvB"}
#### **Most important features - PCA**
:::

::: {.cell .markdown id="hpsJmwTTecZB"}
-   Now, the importance of each feature is reflected by the magnitude of
    the corresponding values in the eigenvectors (higher magnitude -
    higher importance)
:::

::: {.cell .code id="F5QI4z4nebUq"}
``` python
#Let's see first what amount of variance does each PC explain.
pca.explained_variance_ratio_
[0.72770452, 0.23030523, 0.03683832, 0.00515193]

#PC1 explains 72% and PC2 23%. Together, if we keep PC1 and PC2 only, they explain 95%.


#Most important features
print(abs( pca.components_ ))

[[0.52237162 0.26335492 0.58125401 0.56561105]
 [0.37231836 0.92555649 0.02109478 0.06541577]
 [0.72101681 0.24203288 0.14089226 0.6338014 ]
 [0.26199559 0.12413481 0.80115427 0.52354627]]

#Here, pca.components_ has shape [n_components, n_features].
#Thus, by looking at the PC1 (First Principal Component) which is the first row:
#[0.52237162 0.26335492 0.58125401 0.56561105]]
# we can conclude that feature 1, 3 and 4 are the most important.
```
:::

::: {.cell .markdown id="v2S4lNROfeD6"}
The important features are the ones that influence more the components
and thus, have a large absolute value/score on the component.

To get the most important features on the PCs with names and save them
into a pandas dataframe use this:
:::

::: {.cell .code id="4FGBIEvIfZ-Q"}
``` python
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
np.random.seed(0)

# 10 samples with 5 features
train_features = np.random.rand(10,5)

model = PCA(n_components=2).fit(train_features)
X_pc = model.transform(train_features)

# number of components
n_pcs= model.components_.shape[0]

# get the index of the most important feature on EACH component
most_important = [np.abs(model.components_[i]).argmax() for i in range(n_pcs)]

initial_feature_names = ['a','b','c','d','e']
# get the names
most_important_names = [initial_feature_names[most_important[i]] for i in range(n_pcs)]

# LIST COMPREHENSION HERE AGAIN
dic = {'PC{}'.format(i): most_important_names[i] for i in range(n_pcs)}

# build the dataframe
df = pd.DataFrame(dic.items())

     0  1
 0  PC0  e
 1  PC1  d
```
:::

::: {.cell .markdown id="QWcfxNaYff30"}
So on the PC1 the feature named e is the most important and on PC2 the
d.
:::

::: {.cell .markdown id="_cW_HgwTJ_sV"}
# **STATISTICS**
:::

::: {.cell .markdown id="esuCzd9gjQLF"}
### **Increase rates**
:::

::: {.cell .code id="5GzFIyLDjSC6"}
``` python
# ---- Percentage increase ----
100 * (new_number-old_number)/old_number

# ---- Diff of percentage ----
p1 - p2 = 20% ==> 1 is 20% more likely than 2
```
:::

::: {.cell .markdown id="-i7yDoNRl5q3"}
### **Create random variable with numpy**
:::

::: {.cell .code id="gYPyYbf4l9Af"}
``` python
#Uniform sample on [0,1] of size 30
X = np.random.random(30)

#Array where each row follows a uniform distribution
X_arr = np.random.rand(3,2)

#Normal sample of mean 0 and std 1
X = np.random.normal(loc=0.0, scale=1.0, size=30)
```
:::

::: {.cell .markdown id="96LPi0g678Ak"}
### **Geometric mean / median** {#geometric-mean--median}
:::

::: {.cell .code id="lQmrgZCf7-I2"}
``` python
from scipy.stats import gmean

#Geometric mean
gmean = gmean(df.pageviews.values)
plt.vlines(x=gmean(df.pageviews.values), ymin=0, ymax=1, color='orange')

#Median
median = np.nanmedian(list(counts.values), axis=0)
```
:::

::: {.cell .markdown id="11p8dA62n9w3"}
### **Power**
:::

::: {.cell .code id="BUczR1Iwn_RO"}
``` python
#Compute power : proba the test reject H0, knowing that H1 is true
for i in range(10000):
    pval_ind_x_z.append(stats.ttest_ind(X, Z).pvalue)

print("Power of the independent sample t-test comparing X and Z:",
     (np.array(pval_ind_x_z) < 0.05).mean())
```
:::

::: {.cell .markdown id="Ly630PRdohll"}
#### **Entropy**
:::

::: {.cell .code id="2YZMCbfAojKC"}
``` python
import numpy as np
from scipy.stats import entropy
base = 2
pk = np.array([1/2, 1/2])
H = entropy(pk, base=base)
H == -np.sum(pk * np.log(pk)) / np.log(base)
```
:::

::: {.cell .markdown id="w6esyOSlbll4"}
### **Correlation : Pearson, Spearman** {#correlation--pearson-spearman}
:::

::: {.cell .markdown id="iQbCjwmmxz3I"}
-   We test here the null hypothesis H0 that there is no correlation
    between the two variables.
-   As we have a **p-value \< 0.05**, we reject H0, meaning that there
    is a **significant correlation**.
-   There is **no significant correlation** between the two variables
    since we have a **p-value \>= 0.05**.
:::

::: {.cell .code id="J4v-Z8kaYLfk"}
``` python
import scipy
import scipy.stats as stats

#Spearman coefficient
print('Results for Spearman coefficient')
print(stats.spearmanr(df['col1'],df['col2']))

#Pearson coefficient
print('Results for Pearson coefficient')
print(stats.pearsonr(df['col1'],df['col2']))
```
:::

::: {.cell .markdown id="diGhOjz5boEB"}
### **T-test**
:::

::: {.cell .markdown id="p3HY37ks0uba"}
-   H0 : The two variables have the same average.
-   As we get a p-value \< 0.05 for the test, we reject the null
    hypothesis that the two variables have the same average and the
    difference is statistically significant.
-   As we get a p-value \>= 0.05 for the test, we cannot reject the null
    hypothesis that the two variables have the same average and there is
    no statistically significant difference.
-   The higher the t-statistic, the more confidently we can reject the
    null hypothesis
:::

::: {.cell .code id="fLaBbWyGbrT1"}
``` python
from statsmodels.stats import diagnostic

#Normal distribution
diagnostic.kstest_normal(df['col'].values, dist = 'norm')

#Exp distribution
diagnostic.kstest_normal(df['col'].values, dist = 'exp')

#p_value < 0.05 -> we can reject the null hypothesis that the data comes from a normal distribution!
#p_value >= 0.05 -> we cannot reject the null hypothesis that the data comes from a normal distribution!

# -----------------------
# Independant t-test
print(stats.ttest_ind(a, b))

# Paired t-test : when the two variables are correlated
print(stats.ttest_rel(a, b))

#Get p-values from t-test
pval = stats.ttest_ind(a, b).pvalue
```
:::

::: {.cell .markdown id="tywqcJuT1E3J"}
### **Effect of an experiment on 2 groups**
:::

::: {.cell .markdown id="mUUIB9an0z7a"}
Does the effects observed remained the same throughout the study period?

-   Divide dataset into 2 groups
-   T-test for the studied value between the 2 datasets
:::

::: {.cell .markdown id="ON-1rFjoZvlq"}
-   H0 : The two variables have the same average.
-   As we get a p-value \< 0.05 for the test, we reject the null
    hypothesis that the two variables have the same average and the
    difference is statistically significant.
-   As we get a p-value \>= 0.05 for the test, we cannot reject the null
    hypothesis that the two variables have the same average and there is
    no statistically significant difference. The higher the t-statistic,
    the more confidently we can reject the null hypothesis
:::

::: {.cell .code id="YWpFP7681Mox"}
``` python
print(stats.ttest_ind(  df_t1['studied_val'].values,
                        df_t2['studied_val'].values))
```
:::

::: {.cell .markdown id="PxeQtNQlbpun"}
### **Bootstrap**
:::

::: {.cell .markdown id="hZD6WdRU3pWZ"}
-   2 CIs are overlapping \--\> the difference is not significant
:::

::: {.cell .code id="0_CTRYkH-alM"}
``` python
# ---- Scipy ----
import scipy.stats as stats
from scipy.stats import bootstrap

amean = stats.bootstrap((df.pageviews.values,), statistic=np.mean)
gmean = stats.bootstrap((df.pageviews.values,), statistic=gmean)

print("Arith. mean 95%CI:", amean.confidence_interval.low, amean.confidence_interval.high )
print("Geom. mean  95%CI:",  gmean.confidence_interval.low, gmean.confidence_interval.high )

# ---- Own function ----
def bootstrap(df, nb_iters=1000):
    vals = []
    for i in range(nb_iters) :
        sample = df.sample(len(df), replace=True)

        #TO CHANGE !!! Compute the value you want to estimate
        val_ = np.mean(sample.groupby('val')['col'].mean().values)

        vals.append(val_)

    return np.mean(vals), (np.percentile(vals, 2.5), np.percentile(vals, 97.5))

inf_val, sup_val = bootstrap(df)
print("95%CI (val) : [", inf_val, ', ', sup_val, ']')
```
:::

::: {.cell .markdown id="hYWdGlgTnJFu"}
### **Upsampling/Downsampling**
:::

::: {.cell .code id="A-gha9hznM3N"}
``` python
#Upsampling contries with large population
df.sample(n=10, replace=True, weights=df['pop'])
```
:::

::: {.cell .markdown id="A1oUvHEAy4I2"}
### **Regression models**
:::

::: {.cell .markdown id="9Csc4FCY3IQ4"}
-   Regression can deal with correlation between predictors.

`<br>`{=html}

-   a:b (add a\*b) \--\> categorical (a et b)
-   a\*b (add a + b + a:b)
-   Categorical C(a)

`<br>`{=html}

-   The p-value associated to the coefficient of the variable \'VAR\' is
    **\< 0.05**. Hence, we can reject the null hypothesis and the
    coefficient is statistically significant for predicting the outcome
    variable.
-   The p-value associated to the coefficient of the variable \'VAR\' is
    **\>= 0.05**. Hence, we cannot reject the null hypothesis and the
    coefficient is **not** statistically significant for predicting the
    outcome variable.
:::

::: {.cell .code id="aU3eSRdB3FGv"}
``` python
# ----- Linear Regression -----

import statsmodels.formula.api as smf

mod = smf.ols(formula='y ~ x1 + x2', data=df)
res=mod.fit()
print(res.summary())
```
:::

::: {.cell .code id="UNomNVwiy6do"}
``` python
# ----- Logistic regression -----
import statsmodels.formula.api as smf

mod = smf.logit(formula='y ~ x1 + x2', data=df)
res=mod.fit()
print(res.summary())
```
:::

::: {.cell .code id="bSfxnnh53hH3"}
``` python
#Get parameters of the model
variables = res.params.index
coefficients = res.params.values
p_values = res.pvalues
standard_errors = res.bse.values
ci = res.conf_int()

#Plot coeffs
l1, l2, l3, l4 = zip(*sorted(zip(coefficients[1:], variables[1:], standard_errors[1:], p_values[1:])))

plt.errorbar(l1, np.array(range(len(l1))), xerr= 2*np.array(l3), linewidth = 1,
             linestyle = 'none',marker = 'o',markersize= 3,
             markerfacecolor = 'black',markeredgecolor = 'black', capsize= 5)

plt.vlines(0,0, len(l1), linestyle = '--')

plt.yticks(range(len(l2)),l2);
```
:::

::: {.cell .markdown id="0R7w8jcDzEtq"}
-   days at hospital = 139 + 4.9 \* diabetes - 31.8 \* high blood
    pressure

    > People who don\'t have diabetes nor high blood pressure stay at
    > the hospital on average for 139 days

-   Logistic regression : Since all predictors are standardized, we can
    interpret in the following way

    > When all other predictors take mean values, an increase of age by
    > 1 standard deviation, leads on average to an increase by 0.66 of
    > log odds of death.

-   Take log of output variable : makes the model multiplicative, coef
    high_blood_pressure = -0.22

    > Increase of 1 in the variable ==\> multiply the outcome by
    > exp(-0.22)

-   R : more variance of the data is explained
:::

::: {.cell .markdown id="BENuvmHoD7T1"}
-   y \~ x + C(ind) : The coefficient associated with the dummy variable
    `ind` captures the discontinuity between March and April. More
    precisely, it captures the difference between students born in March
    and in April that is not captured by the linear trend (`x`).
:::

::: {.cell .markdown id="AqDNbcOcEee8"}
-   Yes, we can say that there is a causal effect. Whether individuals
    are born on the 31st of March or on the 1st of April happens
    entirely by chance. Thus, it is as if we assign treatment at random
    to these individuals close to the cutoff date; half of them join
    older peers in school, and half go on to join younger peers. Since
    the half that joined younger peers systematically become athletes
    prominent enough to have a page on Wikipedia, we can say there is a
    causal effect.
:::

::: {.cell .markdown id="c6hyDLkVxIuL"}
### **Q-Q plots**
:::

::: {.cell .code id="DDgNzjYhxK3_"}
``` python
import statsmodels.api as sm

#Compare data (array of val) with normal distribution
fig = sm.qqplot(data, line='45')
plt.show()
```
:::

::: {.cell .markdown id="91-4mtK4YMK0"}
# **MACHINE LEARNING**
:::

::: {.cell .markdown id="nZ8rLnXWMJ74"}
### **Prepare Data**
:::

::: {.cell .markdown id="9RhzvpVu6SRe"}
#### **Get dummies**
:::

::: {.cell .code id="DJjC2TXU3s5r"}
``` python
#One hot encoding
df = pd.get_dummies(df, columns=['var'])

#All columns
df = pd.get_dummies(df)
```
:::

::: {.cell .markdown id="Wsb3G5XP4Cnt"}
#### **String to binary**
:::

::: {.cell .code id="VULF21a1MM0H"}
``` python
#String to [0,1]
df['gender_binary'] = (df['gender']=='M').astype('int')
```
:::

::: {.cell .markdown id="JA2_kcrDI79a"}
#### **Feature matrix**
:::

::: {.cell .code id="ZugjgAMyI99A"}
``` python
to_keep = ['col1', 'col2']
X = df[to_keep].to_numpy()
```
:::

::: {.cell .markdown id="DKLtZUBI4Tlj"}
#### **Labels**
:::

::: {.cell .code id="xauEgqlt4VEJ"}
``` python
#Retrieve label
y = df['label'].to_numpy()
```
:::

::: {.cell .code id="cRhmF-Pp394_"}
``` python
#Create multiclass labels
labels, uniques = pd.factorize(df['var'])
df['label'] = labels

#Create dict label to name
label_to_name = dict()

for name in list(uniques) :
    df_tmp = dfA.loc[dfA['channel_cat']==name]
    label = df_tmp.iloc[0,:]['label']
    label_to_name[label] = name

print(label_to_name)
```
:::

::: {.cell .markdown id="0Psok7H-mlIq"}
#### **Split**
:::

::: {.cell .code id="sK5qF0-4moMn"}
``` python
# ---- When already X and y -----
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
```
:::

::: {.cell .code id="LC045f4c6h0A"}
``` python
# ---- On df directly -----
from sklearn.model_selection import train_test_split

train, test = train_test_split(df, test_size=0.4, random_state=42)
```
:::

::: {.cell .markdown id="6ghg_HVE8-Es"}
#### **Normalize**
:::

::: {.cell .code id="gm4mXOYn9A05"}
``` python
for c in df.columns:
    df[c] = (df[c]-df[c].mean())/df[c].std()
```
:::

::: {.cell .markdown id="vdCc7to3__is"}
#### **Create Artificial Data**
:::

::: {.cell .code id="z0X_cfw5ACkp"}
``` python
from sklearn.datasets import make_moons, make_gaussian_quantiles
from sklearn.datasets import make_blobs

#Plot moon
X_moons, y_moons = make_moons(500, noise=0.2, random_state=0)
plt.scatter(X_moons[:,0], X_moons[:,1], c=y_moons)
plt.set_title('Moon Data')

#Data with clusters
nb_clusters = 3   #Number of clusters to generate
X, _, centers = make_blobs(n_samples=100,
                           centers=nb_clusters,
                           cluster_std=2,
                           n_features=2,
                           return_centers=True,
                           random_state=42)

#X in 2-dim (data points)
plt.scatter(X[:,0], X[:,1], alpha=0.6)

#Plot centers
for c in centers:
    plt.scatter(c[0], c[1], marker="+", color="red")
```
:::

::: {.cell .markdown id="YSgstaDPggnb"}
#### **SVD - Dimensionnality reduction**
:::

::: {.cell .code id="ue__xXhgglvb"}
``` python
from sklearn.decomposition import TruncatedSVD

#Perform SVD on the training TF-IDF matrix
#Calculate a 25-dim approximation for both the training and test TF-IDF matrix

svd = TruncatedSVD(n_components=25, random_state=42)
X_train_svd = svd.fit_transform(X_train)
X_test_svd = svd.transform(X_test)
print(X_train_svd.shape, X_test_svd.shape)
```
:::

::: {.cell .markdown id="Uy1KxtitMRvR"}
#### **Generate features - Example**
:::

::: {.cell .code id="CTH1VbszMVEz"}
``` python
def generate_features(combat_row) :
    pok1 = combat_row['First_pokemon']
    pok2 = combat_row['Second_pokemon']
    winner = combat_row['Winner']
    pok1_row = pokemon_ml.loc[pokemon_ml['pid']==pok1]
    pok2_row = pokemon_ml.loc[pokemon_ml['pid']==pok2]
    x = pd.concat([pok1_row, pok2_row], axis=0)
    y = [1,0] if pok1 == winner else [0,1]
    return x.to_numpy(), y

def create_features(combat, pokemon_ml) :
    X = np.zeros((2*len(combat), pokemon_ml.shape[1]))
    Y = []
    cpt = 0
    for index, combat_row in combat.iterrows() :
        x,y = generate_features(combat_row)
        X[cpt] = x[0]
        cpt += 1
        X[cpt] = x[1]
        cpt+=1
        Y.extend(y)
    return X,Y

X,Y = create_features(combats, pokemon_ml)
```
:::

::: {.cell .markdown id="zZMOkZR42JJR"}
### **Models**
:::

::: {.cell .markdown id="xYpJUHAxCyHC"}
#### **Model definition**
:::

::: {.cell .markdown id="EwXqb4VK-4v5"}
-   The lower `C`, the stronger the regularization penalty.
-   Increasing C \--\> Decreasing regularization \--\> Increase
    Overfitting
:::

::: {.cell .code id="XfoMeAmC7Cst"}
``` python
from sklearn import linear_model as lm
model = lm.LinearRegression()

from sklearn import linear_model as lm
model = lm.Ridge(alpha=1.0)

from sklearn import linear_model as lm
model = lm.LogisticRegression(C = c, random_state=42)

#max_iter = 2000, solver='lbfgs', penalty='l2', class_weight='balanced'

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(k = k)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42, n_estimators=nt, max_depth=d)

from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,
    max_depth=1, random_state=0)
```
:::

::: {.cell .markdown id="tI_MSx5z7GYd"}
#### **Cross val score**
:::

::: {.cell .code id="ZmtNRhNs8b5Z"}
``` python
from sklearn.model_selection import cross_val_score

# ---- Cross validation with cross_val_score -----
def cross_validation(X_train, y_train, params, cv, score) :
    scores_list = []
    for param in params:

        #Define model
        model = lm.LogisticRegression(C = param, max_iter = 2000, solver='lbfgs', random_state=42)

        #Compute score via cross-validation
        scores = cross_val_score(model, X_train, y_train, cv=cv, scoring=score)
        scores_list.append(np.mean(scores))

    print(scores_list)

    #Find best parameter
    ind_opt = np.argmax(scores_list)
    opt_param = params[ind_opt]
    opt_score = scores_list[ind_opt]

    print('Best score (train_set) : ', opt_score)
    print('Optimal parameter : ', opt_param)

    best_model = lm.LogisticRegression(C = opt_param, max_iter = 2000, solver='lbfgs', random_state=42)
    best_model.fit(X_train, y_train)

    return best_model
```
:::

::: {.cell .code id="q2NFbzYx-Rm4"}
``` python
#Define parameters
params = []
cv=5
score='accuracy'
score = 'neg_mean_squared_error'

#Find best model
model = cross_validation(X_train, y_train, params, cv, score)

#Predict on test set
y_pred = model.predict(X_test)

#Compute score
```
:::

::: {.cell .markdown id="AxTaaiaB-7Nl"}
#### **Grid Search CV**
:::

::: {.cell .code id="lipz1vWLJlCt"}
``` python
from sklearn.model_selection import GridSearchCV

# ----- With Grid Search -----
def grid_search_cv(X_train, y_train, params, cv, score):

    #Create model without parameter
    model = lm.LogisticRegression(max_iter=2000, solver='lbfgs', random_state=42)

    #Find optimal model with Grid Search
    best_model = GridSearchCV(model, params, cv=cv, scoring=score)
    best_model.fit(X_train, y_train)

    #Print results
    opt_param = best_model.best_params_
    opt_score = best_model.best_score_
    print('Best score (train set) : ', opt_score)
    for param_name in params.keys():
        print("%s: %r" % (param_name, opt_param[param_name]))

    return best_model
```
:::

::: {.cell .code id="Yw9neSFXCHuW"}
``` python
#Define parameters
params = {'C' : [1, 10, 100]}
cv=5
score='accuracy'
score = 'neg_mean_squared_error'

#Find best model
model = grid_search_cv(X_train, y_train, params, cv, score)

#Predict on test set
y_pred = model.predict(X_test)

#Compute score
```
:::

::: {.cell .markdown id="QkHEfQa5C20y"}
#### **Logistic CV**
:::

::: {.cell .code id="gardxk2zC4hi"}
``` python
# ------ LogisticRegressionCV -----
from sklearn.linear_model import LogisticRegressionCV

params = [1, 10, 100]
clf = LogisticRegressionCV(Cs = params, cv=10, random_state=42)
clf.fit(X_train, y_train)

score_train = clf.score(X_train, y_train)
print('Best score - train set : ', score_train)
print('Best parameter : ', clf.C_[0])

y_pred = clf.predict(X_test)
score_test = clf.score(X_test, y_test)
print('Best score - test set : ', score_test)
```
:::

::: {.cell .code id="zmpSN_h0S6TD"}
``` python
#Retrieve scores obtained with the best parameter
#Take the mean on the scores on each test set during cv
clf.scores_[1].mean(axis=0)
```
:::

::: {.cell .markdown id="v0nxusDeGaUS"}
#### **k-NN - Show res**
:::

::: {.cell .code id="hlLdaz40Gc_D"}
``` python
plt.scatter(X_test, c = y_pred)
```
:::

::: {.cell .markdown id="wXTDfNjIC1b9"}
### **Unbalanced**
:::

::: {.cell .markdown id="TSSllbhDfhCo"}
-   **Class_weight=\'balanced\'**

    > Using \'balanced\' class weights while training the model forces
    > the loss function to give higher relative importance to training
    > samples corresponding to the classes with lower frequency.
    > Actually, the training samples are weighted as inverse of the
    > class proportions.

-   **Problems with unbalanced** : It is very easy for accuracy to be
    biased. It is hard to correctly predict the labels in the minority
    class because :

    -   The model didn\'t get enough training data from the minority
        class to learn to classify it.
    -   The loss function treats each training samples as equally
        important. Thus, trying to minimize the overall loss would guide
        the model to focus more on the majority class.

-   **Scores to use** : confusion matrix, balanced accuracy score,
    weighted averaged F1 scores

    -   weighted scores : calculate metrics for each label, and find
        their average weighted by support (nb of true instances for each
        label)
:::

::: {.cell .markdown id="YF3Zzky3Tyw_"}
### **More complex models**
:::

::: {.cell .markdown id="zBo1YvCPV4PT"}
#### **Random Forest**
:::

::: {.cell .code id="KM0s9xIOM9u9"}
``` python
# ----------- Feature importance ----------
model.feature_importances_

# ----------- Score boosted trees ---------
model.score(X_test, y_test)
```
:::

::: {.cell .code id="S3dtKsjMV4xP"}
``` python
#Define parameters
params = {'n_estimators' : [3, 4, 5],
         'max_depth' : [6,7]}
cv=3
score='accuracy'

#Find best model
model = grid_search_cv(X_train, y_train, params, cv, score)

#Predict on test set
y_pred = model.predict(X_test)

#Compute score
```
:::

::: {.cell .code id="c_nMlJdHMiJt"}
``` python
# -------- 2 parameter --------

from sklearn.ensemble import RandomForestClassifier

# ---- Cross validation (own score) -----
def cv_random_forest(X_train, y_train, X_test, y_test, nb_trees, depths) :
  scores_list = np.zeros((4,3))
  for i, nb_tree in enumerate(nb_trees):
    for j, depth in enumerate(depths) :
      model = RandomForestClassifier(max_depth = depth, random_state=42, n_estimators=nb_tree)
      model.fit(X_train, y_train)
      y_pred = model.predict(X_test)
      score = np.mean((y_pred == y_test).astype(int))
      scores_list[i,j] = score
  return scores_list

nb_trees = [10,25,50,100]
depths = [2,4,10]
scores_list = cv_random_forest(X_train, y_train, X_test, y_test, nb_trees, depths)

# ---------------------------
#Train again classifier with optimal parameters and compute accuracy
def random_forest(X_train, y_train, X_test, y_test, best_nt, best_d) :
  model = RandomForestClassifier(max_depth = best_d, random_state=42, n_estimators=best_nt).fit(X_train, y_train)
  y_pred = model.predict(X_test)
  acc = np.mean((y_pred == y_test).astype(int))
  print("Accuracy : {:.2f}%".format(acc*100))
  return model

model= random_forest(X_train, y_train, X_test, y_test, best_nt = 25, best_d = 10

# ---- Cross validation (scikit) -----
from sklearn.model_selection import cross_val_score

# ---- Cross validation -----
def cv_random_forest(X_train, y_train, nb_trees, depths, cv, score) :

  scores_list = np.zeros((len(nb_trees), len(depths)))

  for i, nb_tree in enumerate(nb_trees):
    for j, depth in enumerate(depths) :
      model = RandomForestClassifier(max_depth=depthn n_estimators=nb_tree, random_state=42)
      model.fit(X_train, y_train)
      score = cross_val_score(model, X_train, y_train, cv=cv, scoring=score)
      scores_list[i,j] = score.mean()

  print(scores_list)
  return scores_list

nb_trees = [10,25,50,100]
depths = [2,4,10]
scores_list = cv_random_forest(X_train, y_train, nb_trees, depths, cv, score)
```
:::

::: {.cell .markdown id="7GZOp8j7an75"}
#### **k-means**
:::

::: {.cell .code id="futEmQiNauZO"}
``` python
from sklearn.cluster import KMeans

def k_means(n_clusters, X) :
    kmean = KMeans(n_clusters=n_clusters, random_state=42).fit(X)

    #Plot results
    plt.scatter(X[:,0], X[:,1], c=kmean.labels_, alpha=0.6)

    for c in kmean.cluster_centers_:
        ax.scatter(c[0], c[1], marker="+", color="red")

def predict_k_means(n_clusters, X) :
    labels = KMeans(n_clusters=3, random_state=0).fit_predict(X)
    #Plot results
    plt.scatter(X[:,0], X[:,1], c=labels, alpha=0.6)

# -------------------------------
#Find best K (number of clusters)

#1. SSE - Sum of squared errors
def plot_sse(features_X, start=2, end=11):
    sse = []
    for k in range(start, end):
        # Assign the labels to the clusters
        kmeans = KMeans(n_clusters=k, random_state=10).fit(features_X)
        sse.append({"k": k, "sse": kmeans.inertia_})

    sse = pd.DataFrame(sse)
    # Plot the data
    plt.plot(sse.k, sse.sse)
    plt.xlabel("K")
    plt.ylabel("Sum of Squared Errors")

plot_sse(X)

#2. Silhouette score (measure of cohesion/separation)
# Close to one, good (far from the other clusters),
from sklearn.metrics import silhouette_score

silhouettes = []

# Try multiple k
for k in range(2, 11):
    # Cluster the data and assigne the labels
    labels = KMeans(n_clusters=k, random_state=10).fit_predict(X)
    # Get the Silhouette score
    score = silhouette_score(X, labels)
    silhouettes.append({"k": k, "score": score})

# Convert to dataframe
silhouettes = pd.DataFrame(silhouettes)

# Plot the data
plt.plot(silhouettes.k, silhouettes.score)
plt.xlabel("K")
plt.ylabel("Silhouette score")
```
:::

::: {.cell .markdown id="rSMydGr5bijg"}
#### **DBSCAN**
:::

::: {.cell .code id="2yWgz8iDbkKX"}
``` python
from sklearn.cluster import DBSCAN

# Create a list of eps
eps_list = np.linspace(0.05, 0.15, 14)

# Compute number of row and columns
COLUMNS = 7
ROWS = math.ceil(len(eps_list)/COLUMNS)

fig, axs = plt.subplots(ROWS, COLUMNS, figsize=(12, 4), sharey=True, sharex=True)

for i in range(0, len(eps_list)):
    eps = eps_list[i]

    current_column = i%COLUMNS
    current_row = i//COLUMNS

    ax = axs[current_row, current_column]
    labels = DBSCAN(eps=eps).fit_predict(X_moons)
    ax.scatter(X_moons[:,0], X_moons[:,1], c=labels, alpha=0.6)
    ax.set_title("eps = {:.3f}".format(eps))

plt.tight_layout()
```
:::

::: {.cell .markdown id="VYAOuSkK-9xT"}
### **Importance of each feature**
:::

::: {.cell .code id="B86Lki3j_ABg"}
``` python
def most_important_features(model, features, k=3) :
    #Get coefficients
    weights = model.coef_

    #Sort by most important coefs
    tmp = []
    for name, value in zip(features, weights):
        tmp.append({"name": name, "value": value})

    #Retrieve top k features
    features_coef = pd.DataFrame(tmp).sort_values("value", ascending=False)
    features_coef = features_coef.head(k)

    #plt.barh(features_coef.name, features_coef.value, alpha=0.6)
    fig, ax = plt.subplots(1, 1, figsize=(10, 20))
    sns.barplot(x=features_coef.value, y=features_coef.name, ax = ax)

#Features --> name of features
most_important_features(model, features, k=3)
```
:::

::: {.cell .markdown id="XYZrfYFT7y-i"}
### **Scores**
:::

::: {.cell .markdown id="oqdlPOBp_Qtm"}
#### **Basics**
:::

::: {.cell .code id="mL8NEEW58Ab8"}
``` python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import balanced_accuracy_score

# ----- Self accuracy ----
acc = np.mean((y_pred == y_test).astype(int))
print("Accuracy : {:.2f}%".format(acc*100))

# ------ Accuracy -----
acc = accuracy_score(y_test, y_pred)
print("Accuracy : {:.2f}%".format(acc*100))

# ------ Balanced accuracy -----
balanced_acc = balanced_accuracy_score(y_test, y_pred)
print("Balanced accuracy : {:.2f}%".format(balanced_acc*100))

# ------ F1 score -----
#Harmonic mean of precision and recall

f1 = f1_score(y_test, y_pred, average='weighted')
print('Balanced F1 score : ', f1)

f1 = f1_score(y_test, y_pred)
print('F1 score : ', f1)

# ----- Precision : tp / (tp+fp) -----
#Fraction of true positive samples classified as positive
#ability not to label positive when negative

precision = precision_score(y_test, y_pred, average='weighted')
print('Balanced precision : ', precision)

precision = precision_score(y_test, y_pred)
print('Precision : ', precision)

# ----- Recall : tp / (tp+fn) -----
#Fraction of true positive well classified
#(ability to find all positive samples)

recall = recall_score(y_test, y_pred, average='weighted')
print('Balanced recall : ', recall)

recall = recall_score(y_test, y_pred)
print('Recall : ', recall)

# ----- ALL SCORES ----
print(classification_report(y_test, y_pred, digits=3))
```
:::

::: {.cell .code id="2-qbcZwl_mEZ"}
``` python
#Compute confusion matrix
def compute_confusion_matrix(y_true, y_pred):

    TP = np.sum(np.logical_and(y_true==1, y_pred==1))
    TN = np.sum(np.logical_and(y_true==0, y_pred==0))
    FP = np.sum(np.logical_and(y_true==1, y_pred==0))
    FN = np.sum(np.logical_and(y_true==0, y_pred==1))

    confusion_matrix = np.asarray([[TP, FP],
                                    [FN, TN]])

    label = np.asarray([['TP {}'.format(TP), 'FP {}'.format(FP)],
                        ['FN {}'.format(FN), 'TN {}'.format(TN)]])

    df_cm = pd.DataFrame(confusion_matrix, index=['Yes', 'No'], columns=['Positive', 'Negative'])

    fig, ax = plt.subplots(1,1,figsize=(3,3))
    sns.heatmap(df_cm, cmap='YlOrRd', annot=label, annot_kws={"size": 16}, cbar=False, fmt='', ax=ax)
    plt.show()
    return confusion_matrix

def compute_all_scores(confusion_matrix) :
    [[TP, FP],[FN, TN]] = confusion_matrix.astype(float)

    accuracy =  (TP+TN)/np.sum(confusion_matrix)

    precision_positive = TP/(TP+FP) if (TP+FP) !=0 else np.nan
    precision_negative = TN/(TN+FN) if (TN+FN) !=0 else np.nan

    recall_positive = TP/(TP+FN) if (TP+FN) !=0 else np.nan
    recall_negative = TN/(TN+FP) if (TN+FP) !=0 else np.nan

    F1_score_positive = 2 *(precision_positive*recall_positive)/(precision_positive+recall_positive) if (precision_positive+recall_positive) !=0 else np.nan
    F1_score_negative = 2 *(precision_negative*recall_negative)/(precision_negative+recall_negative) if (precision_negative+recall_negative) !=0 else np.nan

    return [accuracy, precision_positive, recall_positive, F1_score_positive, precision_negative, recall_negative, F1_score_negative]

print('----- TEST SET -----')
confusion_matrix = compute_confusion_matrix(y_test, y_pred_test)
[accuracy, precision_positive, recall_positive, F1_score_positive, \
    precision_negative, recall_negative, F1_score_negative] = compute_all_scores(confusion_matrix)

print("The accuracy of this model is {0:1.3f}".format(accuracy))
print("For the positive case (Sheldon), the precision is {0:1.3f}, the recall is {1:1.3f} and the F1 score is {2:1.3f}"\
      .format(precision_positive, recall_positive, F1_score_positive))
print("For the negative case (not Sheldon), the precision is {0:1.3f}, the recall is {1:1.3f} and the F1 score is {2:1.3f}"\
      .format(precision_negative, recall_negative, F1_score_negative))

print('\n----- TRAIN SET -----')
confusion_matrix = compute_confusion_matrix(y_train, y_pred_train)
[accuracy, precision_positive, recall_positive, F1_score_positive, \
    precision_negative, recall_negative, F1_score_negative] = compute_all_scores(confusion_matrix)

print("The accuracy of this model is {0:1.3f}".format(accuracy))
print("For the positive case (Sheldon), the precision is {0:1.3f}, the recall is {1:1.3f} and the F1 score is {2:1.3f}"\
      .format(precision_positive, recall_positive, F1_score_positive))
print("For the negative case (not Sheldon), the precision is {0:1.3f}, the recall is {1:1.3f} and the F1 score is {2:1.3f}"\
      .format(precision_negative, recall_negative, F1_score_negative))
```
:::

::: {.cell .markdown id="h5YZuLEYhuSy"}
#### **False Positive/False Negative**
:::

::: {.cell .code id="K8GN6Nhzhx0A"}
``` python
#Retrieve y_test, y_pred, probas in one DataFrame
y_probas_test = model.predict_proba(X_test)
y_probas_test = np.max(y_probas_test, axis=1)

probas_df = pd.DataFrame({  'y_pred' : y_pred_test,
                            'y_probas' : y_probas_test,
                            'y_true' : y_test,
                            'id' : [i for i in range(len(y_pred_test))]
                        })


#Create False Positive df and False Negative df
FP_df = probas_df.loc[(probas_df['y_pred'] == 1) & (probas_df['y_true'] == 0)]
FN_df = probas_df.loc[(probas_df['y_pred'] == 0) & (probas_df['y_true'] == 1)]

#Top 10 worst FP and FN
top10_FP = FP_df.sort_values('y_probas', ascending=False).head(10)
top10_FN = FN_df.sort_values('y_probas', ascending=False).head(10)

top10_FP = top10_FP.merge(df, how='inner', left_on='id', right_index=True)
```
:::

::: {.cell .markdown id="nrmi7ySg_UoW"}
#### **MAE/MSE**
:::

::: {.cell .code id="J6_5CSxg_Wf7"}
``` python
from sklearn.metrics import mean_squared_error, mean_absolute_error

print(mean_absolute_error(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))
```
:::

::: {.cell .markdown id="4kKv7muz_aa9"}
#### **Confusion matrix**
:::

::: {.cell .code id="70E-E6DD_c2f"}
``` python
from sklearn.metrics import confusion_matrix

#Confusion matrix
#C_ij = nb of observation with true label i and predicted as j
#C_00 = true negative     C_01 = false positive
#C_10 = false negative    C_11 = true positive
cm = confusion_matrix(y_test, y_pred)

#Display confusion matrix
sns.heatmap(cm, annot=True)
plt.xlabel('Predicted class')
plt.ylabel('True class')
plt.title('Confusion matrix')
plt.show()
```
:::

::: {.cell .markdown id="42VwnrALAklN"}
#### **ROC/AUC**
:::

::: {.cell .code id="ch9oKdj0AmPL"}
``` python
from sklearn.metrics import auc, roc_curve

# ---- ROC curve ----
#True positive rate (TP/P) - Power against
#False positive Rate (FP/N) - Type I error
#at various threshold settings
fpr, tpr, _ = roc_curve(y_true, y_pred)

# ----- AUC score ----
# 1 ---> Perfect
# 0.5 --> random
auc_score = auc(fpr, tpr)
```
:::

::: {.cell .markdown id="9-2vWaMucq6A"}
# **Observational studies**
:::

::: {.cell .markdown id="UUh1cRf15E-C"}
### **Naive analysis**
:::

::: {.cell .markdown id="GTiN8fyN5HAH"}
-   It also hints towards the possibility of finding a causal effect,
    however, further exploration is needed to substantitate that
    assumption!
-   **Naive analysis** : any cofounder may have an effect on the direct
    causal effect
:::

::: {.cell .markdown id="xXgi298Z5BIT"}
### **Cofounders**
:::

::: {.cell .markdown id="fqxk0ysIcuC7"}
-   **Confounding** occurs when an apparently causal relationship
    between an exposure (e.g. a treatment) and an outcome is, in
    reality, distorted by the effect of a third variable (the
    confounder).

-   **Confounder** : ranking is NOT a cofounder of similarity because it
    is totally **uncorrelated** with similarity

-   Si une variable a un impact sur le résultat, alors c\'est un
    confounder.

-   Remédier au confounder : faire Linear Regression avec y =
    conséquence, x1 = cause, x2 = confounder.

    > Dans ce cas, on contrôle le confounder et si x1 a une p-value \>=
    > 0.05, alors on peut dire que x1 ne cause PAS y.
:::

::: {.cell .markdown id="ZBGStSgjwkdk"}
### **Propensity score**
:::

::: {.cell .markdown id="VIc43aRfwonM"}
-   P(Y=1\|x)
-   Estimated from the data using **Logistic Regression**
-   **Fitted values** = estimates of propensity scores for each line in
    the dataframe !
-   Logit model (with normalized data) + predict probas for each row
:::

::: {.cell .code id="9X-jq_RVwnes"}
``` python
import statsmodels.formula.api as smf

# y = treated/control --> binary variables
# [x1, ...., xn] --> covariates
mod = smf.logit(formula='treat ~  age + educ + C(black) + C(hispan)  + C(married) + C(nodegree)', data=df)
res = mod.fit()
print(res.summary())

# Extract the estimated propensity scores
df['Propensity_score'] = res.predict()
```
:::

::: {.cell .markdown id="rBpDsd1F4-5F"}
### **Matching - Propensity scores**
:::

::: {.cell .markdown id="Zw4UnsLIxn2b"}
-   Matching : same propensity score, minimize diff between propensity
    score

    > Graph with nodes for treated, control, edges with weight = 1 -
    > diff_prop_score `<br>`{=html} **Goal** : maximize matching

-   Problematic features : force them to be equal !
:::

::: {.cell .code id="TqGDMJO_xto6"}
``` python
def get_similarity(propensity_score1, propensity_score2):
    '''Calculate similarity for instances with given propensity scores'''
    return 1-np.abs(propensity_score1-propensity_score2)

# Separate the treatment and control groups
treatment_df = df[df['treat'] == 1]
control_df = df[df['treat'] == 0]

# Create an empty undirected graph
G = nx.Graph()

# Loop through all the pairs of instances
for control_id, control_row in control_df.iterrows():
    for treatment_id, treatment_row in treatment_df.iterrows():

        #Add a condition on covariates
        #if (control_row['black'] == treatment_row['black'])\
           # and (control_row['hispan'] == treatment_row['hispan']):

        # Calculate the similarity
        similarity = get_similarity(control_row['Propensity_score'],
                                    treatment_row['Propensity_score'])

        # Add an edge between the two instances weighted by the similarity between them
        G.add_weighted_edges_from([(control_id, treatment_id, similarity)])

# Generate and return the maximum weight matching on the generated graph
matching = nx.max_weight_matching(G)

matched = [i[0] for i in list(matching)] + [i[1] for i in list(matching)]
balanced_df = df.iloc[matched]
```
:::

::: {.cell .markdown id="oQ0IJizkObvD"}
### **Perfect matching**
:::

::: {.cell .code id="6E3q5GnHOhkh"}
``` python
def create_matched_pairs(cov1, cov2, var, df) :

    #Add ID for each element in the DataFrame
    df['id'] = [i for i in range(len(df))]

    #Retrieve unique values for each covariate
    cov1_val = list(set(df[cov1]))
    cov2_val = list(set(df[cov2]))

    #Create unique index
    index = [[i,j]  for i in cov1_val
                    for j in cov2_val
            ]

    matched_pairs = []
    ids_matched1 = []
    ids_matched2 = []

    #For each of the possible combination of covariates
    for _, ind in enumerate(index) :
        i, j = ind

        #Select the rows which satisfy our conditions
        df_tmp = df.loc[(df[cov1] == i) & (df[cov2] == j)]

        #Only look for subsets with a number of rows > 1 to be able to match individuals
        if df_tmp.shape[0] > 1 :

            #Separate in two groups depending variable dividing the 2 groups
            #!!!!!! To choose the condition !!!!!!
            df_tmp1 = df_tmp.loc[df_tmp[var] < 20]
            df_tmp2 = df_tmp.loc[df_tmp[var] >= 20]

            #Retrieve the ids of each group
            ids1 = df_tmp1['id'].to_numpy()
            ids2 = df_tmp2['id'].to_numpy()

            #Retrieve the length of the smallest group
            N = min(len(ids1), len(ids2))
            if N > 0 :
                ids1_perm = np.random.permutation(N)
                ids2_perm = np.random.permutation(N)
                ids1 = ids1[ids1_perm]
                ids2 = ids2[ids2_perm]
                for i,j in zip(ids1, ids2) :
                    matched_pairs.append((i,j))
                    ids_matched1.append(i)
                    ids_matched2.append(j)

    df_matched1 = df.loc[df['id'].isin(ids_matched1)]
    df_matched2 = df.loc[df['id'].isin(ids_matched2)]
    df_matched = pd.concat([df_matched1, df_matched2], axis=0)
    return matched_pairs, df_matched, df_matched1, df_matched2

#Cov1 / Cov2 : names of covariates which should be exact for the matching (str)
#Var : different variable between treated/control
matched_pairs, df_matched, df_matched1, df_matched2 = create_matched_pairs(cov1, cov2, var, df)
```
:::

::: {.cell .markdown id="x23yF484Ypgw"}
# **TEXT**
:::

::: {.cell .markdown id="jQRuHHtiY1II"}
$$\text{TF}(i,j) = \text{number of times the $j$-th word occurs in the $i$-th document}$$

$$\text{IDF}(j) =  \log \frac{\text{number of documents}}{\text{number of documents the $j$-th word occurs in}}$$
:::

::: {.cell .markdown id="FfyTtBSLyAvs"}
#### **TF-IDF matrix**
:::

::: {.cell .code id="VjIPHtmqJLSy"}
``` python
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

features = vectorizer.get_feature_names()
```
:::

::: {.cell .code id="7rLXj3UZYq98"}
``` python
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

def simple_tokeniser(text):
    return text.split()

def create_vocabulary(X_train) :
    all_lines = ' '.join(list(X_train))
    tokens = all_lines.split()
    word_freq = dict(Counter(tokens))
    df_freq = pd.DataFrame.from_dict(word_freq, orient='index').reset_index().rename({'index' : 'words', 0:'occ'}, axis=1)

    #Take off words which appear just 1 time
    vocab = df_freq.loc[df_freq['occ'] > 1]['words'].values

    return vocab

def create_tf_idf(X_train, X_test, stopwords_list) :
    #Create vocabulary
    vocab = create_vocabulary(X_train)

    #Use TF-IDF Vectorizer from scikit
    vectorizer = TfidfVectorizer(tokenizer=simple_tokeniser,\
                                 stop_words=stopwords_list, \
                                  vocabulary=vocab))

    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)
    print(X_train.shape, X_test.shape)

    #Retrieve vocabulary (mapping words --> index)
    vocab = vectorizer.vocabulary_

    #Retrieve feature names
    features = vectorizer.get_feature_names()

    return vocab, features, X_train, X_test

vocab, features, X_train, X_test = create_tf_idf(X_train, X_test, stopwords_list)
```
:::

::: {.cell .markdown id="A0-cGZpOM9VZ"}
#### **Bag-of-words**
:::

::: {.cell .code id="25xV1tQANAGu"}
``` python
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(seq_list)
```
:::

::: {.cell .markdown id="glculh6EJzhL"}
#### **NLP Pipeline with SpaCy**
:::

::: {.cell .code id="l9wAP6sRZB3b"}
``` python
import spacy
from collections import Counter

#NLP Pipeline

#Transform to SpaCy object
nlp = spacy.load('en_core_web_sm')
doc = nlp(txt)    #txt = raw text

#Tokenization
tokens = [token.text for token in doc]
#Pos tagging
pos_tagged = [(token.text, token.pos_) for token in doc]
#Named Entities Recognition
ents = [(ent.text, ent.label_) for ent in doc.ents]
#Stop words removal
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
no_stop_words = [token.text for token in doc if not token.is_stop and not token.is_punct]
#Lemmatization
lemmatized = [token.lemma_ for token in doc]

#Word occurences
words = [token.text for token in doc]
word_freq = Counter(words)
common_words = word_freq.most_common()

#Store to dataframe
word_freq = dict(Counter(words))
df_freq = pd.DataFrame.from_dict(word_freq, orient='index').reset_index().rename({'index' : 'words', 0:'occ'}, axis=1)
```
:::

::: {.cell .markdown id="nLcfSbczQrBY"}
#### **Embedding representation (300)**
:::

::: {.cell .code id="ScjrB23mQyaC"}
``` python
nlp(sentence).vector
```
:::

::: {.cell .markdown id="vfrwBWApRDes"}
#### **Bigram**
:::

::: {.cell .code id="Z9zdzfzXRFSs"}
``` python
from gensim.models.phrases import Phrases

# Add bigrams to docs (only ones that appear 15 times or more).
bigram = Phrases(docs, min_count=15)

for idx in range(len(docs)):
    for token in bigram[docs[idx]]:
        if '_' in token:
            # Token is a bigram, add to document.
            docs[idx].append(token)
```
:::

::: {.cell .markdown id="l6MVDnWARa1J"}
#### **Filter rare/extreme**
:::

::: {.cell .code id="kkkXbNJPROGx"}
``` python
from gensim.corpora import Dictionary
dictionary = Dictionary(docs)

# Remove rare and common tokens.
# Filter out words that occur too frequently or too rarely.
max_freq = 0.5
min_wordcount = 5
dictionary.filter_extremes(no_below=min_wordcount, no_above=max_freq)

# Bag-of-words representation of the documents.
corpus = [dictionary.doc2bow(doc) for doc in docs]
```
:::

::: {.cell .markdown id="sx--513ARj2P"}
#### **LDA**
:::

::: {.cell .code id="ZbYxxm5RRmtF"}
``` python
# models
from gensim.models import LdaMulticore
params = {'passes': 10, 'random_state': seed}
base_models = dict()
model = LdaMulticore(corpus=corpus, num_topics=4, id2word=dictionary, workers=6,
                passes=params['passes'], random_state=params['random_state'])

model.show_topics(num_words=5)

# assignment
sent_to_cluster = list()
for n,doc in enumerate(corpus):
    if doc:
        cluster = max(model[doc],key=lambda x:x[1])
        sent_to_cluster.append(cluster[0])
```
:::

::: {.cell .markdown id="-96AyzR2M47r"}
#### **Sentiment Analysis**
:::

::: {.cell .code id="2L65uN4PM7ok"}
``` python
analyzer = SentimentIntensityAnalyzer()
vs = analyzer.polarity_scores(example)  #One sentence
print('Negative sentiment:',vs['neg'])
print('Neutral sentiment:',vs['neu'])
print('Positive sentiment:',vs['pos'])
# >= 0.05 --> positive / <= -0.05 --> negative
print('Compound sentiment:',vs['compound'])

#Example - Distribution of sentiment scores (positive)
positive_sent = []
for sent in sentences :
    positive_sent.append(analyzer.polarity_scores(sent.text)['pos'])

plt.hist(positive_sent,bins=15)
```
:::

::: {.cell .markdown id="EzeMXao7SPl_"}
#### **Main topics**
:::

::: {.cell .code id="Hat0prgKSSnJ"}
``` python
from empath import Empath
lexicon = Empath()
doc = nlp(example)
empath_features = lexicon.analyze(doc.text,categories = ["disappointment", "pain", "joy", "beauty", "affection"], normalize = True)

#Example : evolution of sentiment over text
love = []
pain = []
beauty = []
affection = []

for sentence in doc:
    empath_features = lexicon.analyze(sentence,
                                      categories = ["love", "pain", "joy", "beauty", "affection"], normalize = True)
    love.append(empath_features["love"])
    pain.append(empath_features["pain"])
    beauty.append(empath_features["beauty"])
    affection.append(empath_features["affection"])

#Create custom category
lexicon.create_category("healthy_food", ["healthy_food","low_carb","kale","avocado"], model="nytimes")
```
:::

::: {.cell .markdown id="8fVc8G9TGHgw"}
# **BASIC TEXT**
:::

::: {.cell .markdown id="C1hyUb4xRSqZ"}
#### **Read text**
:::

::: {.cell .code id="wVzuINGtRUgB"}
``` python
f = open("demofile.txt", "r")
txt = f.read()
f.close()

f = open("demofile.txt", "r", encoding='utf8')
lines = f.readlines()
for line in lines :
  #Do something
f.close()
```
:::

::: {.cell .markdown id="C5qhyYU0RYlO"}
#### **Create DF while reading file**
:::

::: {.cell .code id="vPF6fZXhRdFt"}
``` python
season = ""
episode = ""
scene = ""
data = []
with open("data/all_scripts.txt") as f:
    for line in f.readlines():
        line = line[:-1]
        if line.startswith(">> "):
            season = int(line[10:12])
            episode = line[3:]
            continue
        if line.startswith("> "):
            scene = line[2:]
            continue
        character, line = line.split(": ", 1)
        data.append([season, episode, scene, character, line])
lines = pd.DataFrame(data, columns=["Season", "Episode", "Scene", "Character", "Line"])
```
:::

::: {.cell .markdown id="KWQ4TAIOUE-1"}
#### **Transform text into list of chunks**
:::

::: {.cell .code id="LbskznO2UIuy"}
``` python
#Remove new lines
txt = " ".join(txt.split())

#Spacy object for NLP
doc = nlp(txt)

#Sentences
doc = nlp(book)
sentences = [sent for sent in doc.sents]
print('Number of sentences:',len(sentences))

#Divide into chunks of same size
def get_chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

size = 50 # how many sentences per chunk/page
chunks_of_sents = [x for x in get_chunks(sentences,size)]

chunks = list()
# regroup so to have a list of chunks which are strings
for c in chunks_of_sents:
    grouped_chunk = list()
    for s in c:
        grouped_chunk.extend(s)
    chunks.append(" ".join(grouped_chunk))
print("Number of chunks:",len(chunks),'\n')

#Use one chunk as one sample
#Example : bag of words matrix
X = vectorizer.fit_transform(chunks)
```
:::

::: {.cell .markdown id="nV5tp-2FGVbp"}
### **Text cleaning**
:::

::: {.cell .code id="8WFS5PIIGNq3"}
``` python
#Remove punctuation and lower the text
def clean_line(line, to_exclude):
    for char in to_exclude:
        line = line.replace(char, ' ')
    return line.lower()

df["line"] = df["line"].apply(clean_line)
```
:::

::: {.cell .markdown id="6yMO4LMhHKlA"}
### **Get text from DataFrame**
:::

::: {.cell .code id="MewYob3dTfDd"}
``` python
#Get list of sentences
lines_list = list(df.line.values)

#Get all lines as one text
lines_list = list(df.line.values)
all_lines = ' '.join(txt)

#Get all tokens as list
lines_list = list(df.line.values)
all_lines = ' '.join(txt)
tokens = all_lines.split()
```
:::

::: {.cell .markdown id="IsrWZ9h_HPAG"}
### **Words frequency**
:::

::: {.cell .code id="z2mJfsF9W3fL"}
``` python
from collections import Counter

def get_word_frequency(corpus) :
    #Corpus frequency, number of occurences
    #Counter takes a list of tokens as input
    word_freq = dict(Counter(corpus))
    df_freq = pd.DataFrame.from_dict(word_freq, orient='index').reset_index().rename({'index' : 'words', 0:'occ'}, axis=1)
    return df_freq

lines_list = list(df['col'].values)
all_lines = ' '.join(lines_list)
tokens = all_lines.split()
df_freq = get_word_frequency(tokens)
```
:::

::: {.cell .code id="fX3BTk7KJiGH"}
``` python
#Plot distribution of word frequence in all corpus
sns.displot(data=df_freq, x='occ', element='step')
plt.yscale('log')
plt.xscale('log')
```
:::

::: {.cell .markdown id="JO1qbM7VJ_vs"}
# **GRAPHS**
:::

::: {.cell .markdown id="S_0beSClGLjw"}
#### **Creation graph**
:::

::: {.cell .code id="gESkJvlCLnsm"}
``` python
#----- Graph -----
G = nx.Graph()
G = nx.DiGraph()      #Oriented Graph
G = nx.MultiDiGraph() #Multi edges between nodes
G = nx.gnm_random_graph(nb_nodes, nb_edges) #Random graph

# ----- From DataFrame of edges list -----
G = nx.from_pandas_edgelist(edges_df, 'Source', 'Target', edge_attr='gender', create_using= nx.Graph())
print(nx.info(G))
nx.draw_spring(G, with_labels=True,  alpha = 0.8)

# ----- Create graph from adjacency matrix -----
G = nx.from_numpy_matrix(adjacency_matrix, create_using=nx.Graph())
labels = nx.get_edge_attributes(G, "weight")
print(labels)

# ----- Add node -----
G.add_node(1)
G.add_nodes_from(node_list)

# ----- Add edge -----
G.add_edge(1,2)
G.add_edges_from(edges_list)

# ---- Create from DataFrame ----
for _, node in node_list.iterrows():
    node = dict(node)
    G.add_node(node['u'], score=node['score'], name=node['name'])

for _, edge in edge_list.iterrows():
    edge = dict(edge)
    G.add_edge(edge['u'], edge['v'], gender=edge['gender'])

#------ Create from list of nodes and edges -----
def create_graph(node_list, edge_list) :
    G = nx.Graph()
    G.add_nodes_from(node_list)
    G.add_edges_from(edges)

    print(nx.info(G))
    nx.draw_spring(G, with_labels=True,  alpha = 0.8)

    return G
```
:::

::: {.cell .markdown id="6hD7Sk5VP3zK"}
##### **Adjacency matrix**
:::

::: {.cell .markdown id="JHhGCq7HT2bl"}
-   k-th power of adjacency matrix A contains number of length-k paths
    for each node pair
:::

::: {.cell .code id="5N2mU-uLP5r4"}
``` python
adjacency_matrix = nx.adjacency_matrix(G)

#Returns the graph as an adjacency matrix
df = nx.to_pandas_adjacency(G, weight='edge_attribute')

   0  1  2
0  0  2  0
1  1  0  0
2  0  0  4
```
:::

::: {.cell .markdown id="ERvaMFonQAXF"}
#### **Creation subgraph**
:::

::: {.cell .code id="hkdltpo6QCYt"}
``` python
#Local subgraph
subgraph_u = G.subgraph(['u']+list(G.neighbors('u')))

#Subgraph from list of nodes
subgraph = G.subgraph(nodes_list)
```
:::

::: {.cell .markdown id="Lm8gxD5vOETH"}
#### **Directed \--\> Undirected**
:::

::: {.cell .code id="H_yzA9DLOHsT"}
``` python
G_u = G.to_undirected()
```
:::

::: {.cell .markdown id="myiZ9tYjjh8R"}
#### **Visualize/Basic infos**
:::

::: {.cell .code id="2_McHWtZjfbk"}
``` python
# Number of nodes and edges
print(nx.info(G))

# Show graph
nx.draw_spring(G, with_labels=True,  alpha = 0.8)

# With k = optimal distance between nodes
def visualize_graph(G, with_labels=True, k=None, alpha=1.0, node_shape='o'):
    pos = nx.spring_layout(G, k=k)
    if with_labels:
        lab = nx.draw_networkx_labels(G, pos, labels=dict([(n, n) for n in G.nodes()]))
    ec = nx.draw_networkx_edges(G, pos, alpha=alpha)
    nc = nx.draw_networkx_nodes(G, pos, nodelist=G.nodes(), node_color='g', node_shape=node_shape)
    plt.axis('off')

visualize_graph(G, k=0.05, alpha=0.4)
visualize_graph(G, k=0.2, alpha=0.4, node_shape='.')
```
:::

::: {.cell .markdown id="jROlhA9tNe3G"}
#### **Attributes**
:::

::: {.cell .markdown id="EhsJPNc8n6QQ"}
##### **Node Attributes**
:::

::: {.cell .code id="oKdwJxgpn80o"}
``` python
# ----- Set node attributes (from dict id_node --> attribute) -----
keys = df['node']
values = df['attribute']
attribute_dict = dict(zip(keys, values))

nx.set_node_attributes(G, attribute_dict, 'name_attribute' )

# ----- Get attribute for all nodes ------
nodes_attributes = nx.get_node_attributes(G, "score")
print(nodes_attributes)
```
:::

::: {.cell .code id="XkWZNuALKyrt"}
``` python
# ----- Exemple -----
#Create a dict : node_id --> node_name
attribute_dict = dict()
for i in range(len(characters_list)) :
    attribute_dict[i] = characters_list[i]
nx.set_node_attributes(G, attribute_dict, 'name_attribute' )
```
:::

::: {.cell .markdown id="JdpNkpHeoJXF"}
##### **Edges Attributes**
:::

::: {.cell .code id="CKpTZkDFoM54"}
``` python
#Retrieve edge attributes
edges_attributes = nx.get_edge_attributes(G, "weight")
print(edges_attributes)

print(G.edges(data=True))
```
:::

::: {.cell .markdown id="wcH8msh-wCS_"}
#### **Degrees**
:::

::: {.cell .markdown id="Vssnqh5dLxVQ"}
-   The average degree is not a good summary statistic because the
    degree distribution is heavy-tailed (roughly a power law
    distribution). A better choice of summary statistic would be the
    median, as it is a robust statistic.
-   Directed - total degree of one node : indegree+outdegree
:::

::: {.cell .markdown id="6TsYsgzWOfgB"}
##### **Basics** {#basics}
:::

::: {.cell .code id="qOxyC410wExn"}
``` python
G.neighbors('u')
G.predecessors('u')
G.successors('u')

#One node
G.degree('u')
G.in_degree('u')
G.out_degree('u')

#All nodes --> Returns a dict
G.degree(G.nodes())
G.in_degree(G.nodes())
G.out_degree(G.nodes())

#Average degree (directed graph)
avg_degree = len(G.edges())/len(G.nodes())

#Average degree (undirected graph)
avg_degree = 2 * len(G.edges())/len(G.nodes())
```
:::

::: {.cell .markdown id="aJ0Kn6pcGRzS"}
##### **Degree distribution**
:::

::: {.cell .markdown id="n0msqlJEQ8dd"}
-   Normalized degree distribution : #degree/Nb_nodes

    > Proba that a randomly chosen node has degree k
:::

::: {.cell .code id="Up87wsP4euUD"}
``` python
#Degree distribution for undirected graph
def create_degree_df(G):
    degrees = []
    for node in G.nodes():
        d = G.degree(node)
        degrees.append(d)

    df_degree = pd.DataFrame('node' : list(G.nodes()), 'degree' : degrees)

    return df_degree

df_degree = create_degree_df(G)

sns.displot(df_degree, x ='degree', element='step', height=6)
plt.title("Degree Distribution")
plt.ylabel("Frequency")
plt.xlabel("Degree")
plt.xscale('log')
plt.yscale('log')
```
:::

::: {.cell .markdown id="wpWiuiBJOjYH"}
##### **In degree distribution**
:::

::: {.cell .code id="7NKccxopGUNE"}
``` python
#Get in-degrees / out-degrees
def create_in_out_degree_df(G) :
    indegree = []
    outdegree = []

    for node in G.nodes:
        indegree.append(len(list(G.predecessors(node))))
        outdegree.append(len(list(G.successors(node))))

    indegree = np.array(indegree)
    outdegree = np.array(outdegree)

    #Store results in a dataframe
    in_out_degree_df = pd.DataFrame({'node' : list(G.nodes), 'indegree' : indegree, 'outdegree' : outdegree})

in_out_degree_df = create_in_out_degree_df(G)

#Plot distribution of in-degree/out-degree
fig, axs = plt.subplots(1,2,figsize=(18,6))

#Plot the distribution of indegree
sns.displot(in_out_degree_df, x ='indegree', element='step', ax=axs[0])
plt.title('Indegree distribution')
plt.xscale('log')
plt.yscale('log')
plt.ylabel("Frequency")
plt.xlabel("Indegree")

#Plot the distribution of outdegree
sns.displot(in_out_degree_df, x ='outdegree', element='step', ax=axs[1])
plt.title('Outdegree distribution')
plt.xscale('log')
plt.yscale('log')
plt.ylabel("Frequency")
plt.xlabel("Outdegree")
plt.show()
```
:::

::: {.cell .markdown id="Gzran8PuhPxg"}
#### **Connection**
:::

::: {.cell .markdown id="QnT4yWVePTK0"}
##### **Connected/Density**
:::

::: {.cell .code id="EE-_JpQFhTN1"}
``` python
#Connected / Hubs : nodes with many connections
print('Connected : ', nx.isconnected(G))
print('The graph contains', len(number_connected_components(G)), 'connected components')

#Weakly connected
#Directed --> undirected
#It is possible to reach any node starting from any other node by traversing an edge
#in the associated undirected graph
print("Weakly connected: ", nx.is_weakly_connected(G))
print(f"There are {len(list(nx.weakly_connected_components(G)))} weakly connected components")

#Strongly connected
#If every node is reachable from every other node
print("Strongly connected: ", nx.is_strongly_connected(G))
print(f"There are {len(list(nx.strongly_connected_components(G)))} strongly connected components")

# Density / Sparsity : edges/max_edges_possible
# Undirected : e/(n(n-1)/2) = 2e/n(n-1)
# Directed : e/n(n-1)
# 0 --> no connexion/no edges = SPARSE
# 1 --> fully connected = DENSE
print('Density : ', nx.density(G))
```
:::

::: {.cell .markdown id="5WDnJtAfPZp2"}
##### **Connected components**
:::

::: {.cell .code id="iFISJHS0PcMY"}
``` python
#Number connected components
print('The graph contains', len(number_connected_components(G)), 'connected components')

#Length of each connected component
print([len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)])

#Largest connected component
largest_cc = max(nx.connected_components(G), key=len)
print('The largest component has', len(largest_comp), 'nodes')

#Create subgraph of largest connected component
subG = G.subgraph(largest_cc)

#Create all subgraphs
S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
```
:::

::: {.cell .markdown id="QA5clknQPzwX"}
##### **Weakly connected components**
:::

::: {.cell .code id="d5CyC6fAP4ME"}
``` python
#Get the largest weakly connected component
largest_cc = max(nx.weakly_connected_components(G), key=len)

#Create a subgraph of largest weakly connected component
H = G.subgraph(list(largest_cc))
```
:::

::: {.cell .markdown id="YngpepN-hqOu"}
#### **Paths**
:::

::: {.cell .markdown id="BYINL_BOxxpg"}
Navigability in the network depends on the existence of short paths

-   Decrease navigability in the network :

    > Find the edge with the highest edge betweenness centrality value.
    > Removing such an edge would impact a lot of shortest paths, as the
    > highest fraction of shortest paths pass through this edge.

-   Average shortest-path length

    > 6 degrees of separation
:::

::: {.cell .code id="4KyWwdlMhsu8"}
``` python
#Existence of a path
nx.has_path(G,u,v)

#Avg shortest path length
#Milgram's experiment --> 6
#Due to skewed distribution/presence of hubs
avg_path = nx.average_shortest_path_length(G)
print("Avg. Shortest Path Length: {:.4f}".format(avg_path))

#Longest shorth path / Diameter
diameter = nx.diameter(G)
print("Longest path : ", diameter)

#Find shortest path
u_v_path = nx.shortest_path(G, source="u", target="v")
```
:::

::: {.cell .markdown id="XDTYA3HPiztX"}
#### **Scores** {#scores}
:::

::: {.cell .markdown id="j1jbGiQgxFrD"}
What are the most important nodes ?
:::

::: {.cell .markdown id="lIQO4fzrQdJL"}
##### **Clustering coefficients**
:::

::: {.cell .markdown id="vxsdDqsYRXK7"}
-   Large clustering coefficients
-   Triadic closure makes real networks cluster into locally dense
    "communities"
-   Communities connected via "weak ties" (edges with low betweenness
    centrality)
:::

::: {.cell .code id="8OBeC7ETi2B_"}
``` python
# ---- TRANSITIVITY = global clustering coefficient -----
# 1 --> 2 --> 3 ==> how much likely 3 --> 1 ?

# nb_triangles/nb_all_possible_triangles
# possible = open and closed triangles

# 1 --> very likely
print('Transitivity : ', nx.transitivity(G))

# ----- CLUSTERING = local measure ------
# For a node, how much the graph is connected around?
# Probability of being a clique (complete graph)

# e/max_possible_edges_between_neighbours
clustering_coefs = nx.clustering(G, list(G.nodes())
print('Clustering coef : ', nx.clustering(G, ['u', 'v']))
```
:::

::: {.cell .markdown id="swLh5yTRQ01B"}
##### **Degree coefficients**
:::

::: {.cell .code id="rseeE4cWQ3wE"}
``` python
from operator import itemgetter
# ----- DEGREE CENTRALITY -----
# The most important nb of neighbors (edges)
# The more people you know, the most important you are
degrees = dict(G.degree(G.nodes()))
sorted_degree = sorted(degrees.items(), key=itemgetter(1), reverse=True)

print('Degree centrality')
for node, degree in sorted_degree[:5]:
    print(node, ' --> ', degree)


from operator import itemgetter
# ---- INDEGREE CENTRALITY -----
degrees = dict(G.in_degree(G.nodes()))
sorted_indegree = sorted(indegrees.items(), key=itemgetter(1), reverse=True)

print('Indegree centrality')
for node, degree in sorted_indegree[:5]:
    print(node, ' --> ', degree)

from operator import itemgetter
# ---- OUTDEGREE CENTRALITY -----
degrees = dict(G.out_degree(G.nodes()))
sorted_outdegree = sorted(outdegrees.items(), key=itemgetter(1), reverse=True)

print('Outegree centrality')
for node, degree in sorted_outdegree[:5]:
    print(node, ' --> ', degree)

from operator import itemgetter
# ----- KATZ CENTRALITY -----
#Generalization of degree centrality
#Counts also neighbours at distance 2,3,..
#Nb of paths from other nodes to i, less weights
#to further nodes
katz = nx.katz_centrality(G)
sorted_katz = sorted(katz.items(), key=itemgetter(1), reverse=True)

print('Katz centrality')
for node, katzc in sorted_katz[:5]:
    print(node, ' --> ', katzc)
```
:::

::: {.cell .markdown id="zIMjWh1NSkQz"}
##### **Closeness centrality**
:::

::: {.cell .markdown id="mLB98-fYVMPa"}
how long the paths connecting an entity with the others are
:::

::: {.cell .code id="czPqebWLSphV"}
``` python
# Only for connected graphs
# C(x) = 1/total_distance_of_x_to_others_nodes
# High --> important

from operator import itemgetter

# Unweighted : length of shortest paths
# Weighted : min. sum of weights along connecting path
closeness_centrality = nx.closeness_centrality(G)
sorted_closeness = sorted(closeness.items(), key=itemgetter(1), reverse=True)

print('Closeness centrality')
for node, c in sorted_closeness[:5]:
    print(node, ' --> ', c)
```
:::

::: {.cell .markdown id="H-MHdaJeQ7oy"}
##### **Betweeness centrality**
:::

::: {.cell .code id="1ZQtYHFaQ-Ge"}
``` python
from operator import itemgetter

# ----- NODE BETWEENNESS CENTRALITY -----
#The more shortest paths pass through a node, the more important it is!
betweenness = nx.betweenness_centrality(quakerG)
sorted_betweenness = sorted(betweenness.items(), key=itemgetter(1), reverse=True)

print('Betweenness centrality')
for node, betweennessc in sorted_betweenness[:5]:
    print(node, ' --> ', betweennessc)

# ----- EDGE BETWEENNESS CENTRALITY -----
edge_betweenness = edge_betweenness_centrality(G)
sorted_edge_betweenness = sorted(edge_betweenness.items(), key=itemgetter(1), reverse=True)

print('Edge betweenness centrality')
for node, edge_betweennessc in sorted_edge_betweenness[:5]:
    print(node, ' --> ', edge_betweenness)
```
:::

::: {.cell .markdown id="uiXV6bE1T_5C"}
##### **PageRank centrality**
:::

::: {.cell .markdown id="uyzVLBJDUE9b"}
C(i) =: xi is high if I receive inlinks from many other central nodes
:::

::: {.cell .code id="ayx_TnFRUCYl"}
``` python
from operator import itemgetter

#For directed
#Add two directed edges for undirected
pr = nx.pagerank(G, alpha=0.9)
sorted_pr = sorted(pr.items(), key=itemgetter(1), reverse=True)

print('Page rank centrality')
for node, c in sorted_pr[:5]:
    print(node, ' --> ', c)
```
:::

::: {.cell .markdown id="MKQYgYo3Vnn1"}
##### **Eigenvector centrality**
:::

::: {.cell .markdown id="osYkOvVmVqX_"}
-   Based on the concept that connections to high-scoring nodes
    contribute more to the score of the node in question than equal
    connections to low-scoring nodes.

-   Google's PageRank and the Katz centrality are variants of the
    eigenvector centrality.

-   Ax= lambda.x

\--\> A adjacency matrix

\--\> score = eigenvector associated to the largest eigenvalue
:::

::: {.cell .code id="UcT0qEZEVpo8"}
``` python
from operator import itemgetter

eigen_centrality = nx.eigenvector_centrality(G)
sorted_eigen = sorted(eigen_centrality.items(), key=itemgetter(1), reverse=True)

print('Eigenvector centrality')
for node, c in sorted_eigen[:5]:
    print(node, ' --> ', c)
```
:::

::: {.cell .markdown id="mBeMHF2ERFV6"}
##### **Homophily**
:::

::: {.cell .code id="Q97veXxMRIp3"}
``` python
# ----- HOMOPHILY ----
# Simimar nodes (same attributes) more likely to have connection
# No --> due to unbalanced attribute

# for categorical attributes
# Might do df['Gender'] = df['Gender'].astype('category')
nx.attribute_assortativity_coefficient(G, 'Gender')

# for numerical attributes
nx.numeric_assortativity_coefficient(G, 'Deathdate')
```
:::

::: {.cell .markdown id="TTce2OFNRp4f"}
#### **Communities**
:::

::: {.cell .markdown id="hbK3iyNrRrxH"}
-   Large clustering coefficients
-   Often not disjoint, overlapping (many edges between communities)
:::

::: {.cell .markdown id="5jNkDQx5os7O"}
#### **Store score to DataFrame**
:::

::: {.cell .code id="exA0ktE6XUuf"}
``` python
#Store scores to DataFrame

betweenness = nx.betweenness_centrality(G)

betweenness_df = pd.DataFrame.from_dict(betweenness, orient='index').reset_index()
betweenness_df.columns = ['node', 'score']
```
:::

::: {.cell .markdown id="H-8QK6V2oyu0"}
#### **Visualize scores**
:::

::: {.cell .code id="OkhvmA3S3fTn"}
``` python
# ------ Visualize scores ------

#Add scores as attributes of nodes
nx.set_node_attributes(G, dict_scores, 'betweeness')

#Retrieve list of nodes
list_nodes = list(G.nodes())
list_nodes.reverse()

pos = nx.spring_layout(G)
ec = nx.draw_networkx_edges(G, pos, alpha=0.1)
nc = nx.draw_networkx_nodes(G, pos, nodelist=list_nodes, node_color=[G.nodes[n][name_score] for n in list_nodes],
                                alpha=0.8, node_shape = '.')
plt.colorbar(nc)
plt.axis('off')
plt.show()
```
:::

::: {.cell .markdown id="OIQD2Va859u0"}
#### **ALGOS - Communities / Clustering** {#algos---communities--clustering}
:::

::: {.cell .code id="l9Wh1-dQ6ATG"}
``` python
# ----- Girvan Newman ----
# Removes edges with highest betweeness centrality
from networkx.algorithms.community.centrality import girvan_newman

comp = girvan_newman(G)
it = 0
for communities in itertools.islice(comp, 4):
    it +=1
    print('Iteration', it)
    print(tuple(sorted(c) for c in communities))

# ---- Louvain ----
# Init : 1 node = 1 community
# Join to neighbors communities and see if it is better
!pip install networkx python-louvain
from community import community_louvain

#Dict : nodes --> community
partition = community_louvain.best_partition(G)

# add it as an attribute to the nodes
for n in G.nodes:
    G.nodes[n]["louvain"] = partition[n]

# plot it out
pos = nx.spring_layout(quakerG,k=0.2)
ec = nx.draw_networkx_edges(quakerG, pos, alpha=0.2)
nc = nx.draw_networkx_nodes(quakerG, pos, nodelist=quakerG.nodes(), node_color=[quakerG.nodes[n]["louvain"] for n in quakerG.nodes],
                            node_size=100, cmap=plt.cm.jet)
plt.axis('off')
plt.show()
```
:::

::: {.cell .markdown id="WgUNk0fHN6Mv"}
#### **FAMOUS GRAPHS**
:::

::: {.cell .markdown id="U507Q070N90T"}
##### **Dominance-directed graph**
:::

::: {.cell .markdown id="1TZlQ19JOCjk"}
Theorem: In any dominance-directed graph there is at least one vertex
from which there is a 1-step or 2-step connection to any other vertex.
The entries of G correspond to 1-step connections between two vertices;
and non-zero entries of G² correspond to 2-step connections. Thus
non-zero entries of (G+G²)\_i,j correspond to existence of 1 or two-step
connections from G_i to G_j. Hence, the vertex i with the property that
row i of G+G² has the largest sum is the vertex referred to in above
theorem, i.e., the vertex with a 1 or 2 step connection to every other
vertex.
:::

::: {.cell .markdown id="xSgn8h_XMrxE"}
##### **Bipartite**
:::

::: {.cell .code id="dgXPglv0Muy0"}
``` python
from networkx.algorithms import bipartite

# ----- Create bipartite graph -----------
B = nx.Graph()
# Add nodes with the node attribute "bipartite"
B.add_nodes_from([1, 2, 3, 4], bipartite=0)
B.add_nodes_from(["a", "b", "c"], bipartite=1)
# Add edges only between nodes of opposite node sets
B.add_edges_from([(1, "a"), (1, "b"), (2, "b"), (2, "c"), (3, "c"), (4, "a")])


# ----- Find 2 sets of nodes (if G is connected) ---------
nx.is_connected(B)
#True
bottom_nodes, top_nodes = bipartite.sets(B)

# ----- Find 2 sets of nodes (if G is connected) ---------
top_nodes = {n for n, d in B.nodes(data=True) if d["bipartite"] == 0}
bottom_nodes = set(B) - top_nodes


# ---- Check if graph is bipartite -----
nx.is_bipartite(G)
```
:::

::: {.cell .markdown id="5oTZ4yH8Ox1o"}
##### **Projection of bipartite graph**
:::

::: {.cell .markdown id="ULmLxiCfPUBY"}
-   Two nodes in G are connected if they have a common neighbor
-   One edge in G = path of length 2 in B !
:::

::: {.cell .code id="PHrt8IDUO0sO"}
``` python
from networkx.algorithms import bipartite

# Projection of bipartite graph onto the set of nodes
G = bipartite.projected_graph(B, [1, 3], multigraph=False)
```
:::

::: {.cell .markdown id="qc2xBWlcM9eJ"}
#### **Examples creation**
:::

::: {.cell .markdown id="WRV8t78CV5rp"}
##### **Exemple - Creation with adjacency matrix**
:::

::: {.cell .code id="0Kfp637yR4vo"}
``` python
# ----( EXEMPLE - Undirected graph from adjacency ) -----
#Create an adjacency matrix of size (c, c)
adjacency_matrix = np.zeros((len(characters_list), len(characters_list)))

for i1, c1 in enumerate(characters_list) :
    #Retrieve all lines where c1 appears
    df_c1 = df.loc[df['character'] == c1]

    #Retrieve all scenes where he appears and stores as a list
    #of tuples (season, episod, scene)
    scenes = list(df_c1.groupby(['season', 'episode', 'scene']).line.count().index)

    #For each other character
    for i2, c2 in enumerate(characters_list) :
        #Retrieve the list of scenes he appears
        df_c2 = df.loc[df['character'] == c2]
        scenes2 = list(df_c2.groupby(['season', 'episode', 'scene']).line.count().index)

        #Count the number of common elements
        res = len(set(scenes) & set(scenes2))

        adjacency_matrix[i1, i2] = res

#Remove edges from i to i
for i in range(len(characters_list)) :
    adjacency_matrix[i,i] = 0

#Create graph from adjacency matrix
G = nx.from_numpy_matrix(adjacency_matrix, create_using=nx.Graph())
print(nx.info(G))

#Retrieve edges attributes
labels = nx.get_edge_attributes(G, "weight")
print(labels)
print(G.edges(data=True))

#Set node attributes
#Create a dict : node_id --> node_name
attribute_dict = dict()
for i in range(len(characters_list)) :
    attribute_dict[i] = characters_list[i]
nx.set_node_attributes(G, attribute_dict, 'name_attribute' )

nodes_attributes = nx.get_node_attributes(G, "name_attribute")
print(nodes_attributes)
```
:::

::: {.cell .markdown id="89u6TiYbWEjr"}
##### **Exemple - Creation of DataFrame with edges**
:::

::: {.cell .code id="XKY8zyXiWLSx"}
``` python
import itertools
import networkx as nx

dfC_grouped = dfC.groupby(['season', 'scene', 'episode'])

edges_dict = dict()
for df_name, df_g in dfC_grouped :
    #Retrieve list of characters
    characters_episod = list(set(df_g['character'].values))
    if len(characters_episod) > 1 :
        for i,j in itertools.combinations(characters_episod,2) :
            u = min(i,j)
            v = max(i,j)
            if (u,v) not in edges_dict :
                edges_dict[(u,v)] = 1
            else :
                edges_dict[(u,v)] += 1


edges_df = pd.DataFrame(columns = ['u', 'v', 'w'])
for key, value in edges_dict.items() :
    edges_df.loc[len(edges_df.index)] = [key[0], key[1], value]

G = nx.from_pandas_edgelist(edges_df, 'u', 'v', edge_attr='w', create_using= nx.Graph())
print(nx.info(G))
```
:::

::: {.cell .markdown id="tMFc7yHiNXC5"}
##### **Exemple - Create adjacency matrix**
:::

::: {.cell .markdown id="V-Rex8CYNijb"}
-   Careful : don\'t iterate over all data points !
:::

::: {.cell .code id="5PDhF6bkNaiP"}
``` python
#Compute adjacency matrix
pok_ids = pokemon.pid.unique()
adjacency_matrix = np.zeros((len(pok_ids), len(pok_ids)))
for index_i, i in enumerate(pok_ids) :
    for index_j, j in enumerate(pok_ids) :
        if index_i < index_j :
            #Find combats of i against j

            i_wins = len(combats.loc[(combats['Winner']==i) & (combats['Loser']==j)])
            i_loses = len(combats.loc[(combats['Winner']==j) & (combats['Loser']==i)])

            if i_wins > i_loses :
                adjacency_matrix[index_i,index_j] = 1

            else :
                adjacency_matrix[index_j,index_i] = 1

adjacency_matrix
```
:::

::: {.cell .markdown id="2TqNc0JVQwyU"}
# **SPARK**
:::

::: {.cell .code id="clLC6AuTLbvz"}
``` python
#Read data
reddit = spark.read.json("messages.json.gz")

#Display columns
reddit.printSchema()

#Get sample
reddit.take(3)

#Show table
reddit.show()

#Put into memory
reddit.cache()

#Count the number of rows
reddit.count()

#GroupBy and count all lines
counts = reddit\
        .groupBy(["col1", "col2"])\
        .agg(count("*").alias("counts"))\
        .sort(asc("count"))

counts = reddit\
        .groupBy(["col1", "col2"])\
        .agg(count("*").alias("counts"))\
        .sort(desc("count"))

#Map : apply one function to each row
# (col_val1, 1)
# (col_val1, 1)
# (col_val2, 1)
map_res = reddit.rdd.map(lambda row : (row.col1, 1))

#Group by col_val and count the number of items
#Sort plus grand au plus petit
map_res_count = map_res\
    .reduceByKey(lambda a,b:a+b)\
    .sortBy(lambda r: -r[1])

#Join 2 dataframes (based on 1 condition)
joined = rdd1.join(rdd2,
                   rdd1.col_to_merge == rdd2.col_to_merge)

#GroupBy subreddit and create different columns
subreddit_info = reddit.groupBy('subreddit').agg(
    count('*').alias('total_posts'),
    countDistinct('author').alias('users_count'),
    avg(length('body')).alias('posts_length')
).cache()

#Select columns
subreddit_info.select('subreddit', 'total_posts', 'users_count', 'posts_length')

#Sort by one column and send to Pandas
by_posts = subreddit_info.select("subreddit", "total_posts")\
                         .sort(col("total_posts").desc()).toPandas()

#Join
reddit.join(score, "id")\
    .groupBy("subreddit")\
    .agg(avg("score").alias("score"))\
    .sort(col("score").desc()).show()

# --------------------

#Tokenize and stopwords removal
from pyspark.ml.feature import RegexTokenizer, StopWordsRemover
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, col

# tokenize the text
regexTokenizer = RegexTokenizer(inputCol="body", outputCol="all_words", pattern="\\W")
reddit_with_words = regexTokenizer.transform(reddit)

# remove stop words
remover = StopWordsRemover(inputCol="all_words", outputCol="words")
reddit_with_tokens = remover.transform(reddit_with_words).drop("all_words")

#Get one dataframe with 1 row per elem in the list
all_words = reddit_with_tokens.select(explode("words").alias("word"))

# group by, sort and limit to 50k
top50k = all_words.groupBy("word")\
    .agg(count("*").alias("total"))\
    .sort(col("total").desc())\
    .limit(50000)

top50k.show()

#Word count
# Word count at subreddit level
#(subreddit, [w1, w2, w1])
#(r, w1) --> 1
#(r, w2) --> 1
#(r, w1) --> 1
# -------
#(r, w1) --> 2
#(r, w2) --> 1

words_count_by_subreddit_rdd = reddit_with_tokens.rdd\
    .flatMap(lambda r: [((r.subreddit, w), 1) for w in r.words])\
    .reduceByKey(lambda a,b: a+b).cache()

# conversion in a dataframe
words_count_by_subreddit = spark.createDataFrame(
            words_count_by_subreddit_rdd.map(lambda r: Row(subreddit=r[0][0], word=r[0][1], count=r[1]))
)

# Window on the words grouped by subreddit
window = Window.partitionBy(words_count_by_subreddit['subreddit']).orderBy(col('count').desc())

# Add position with rank() function (rowNumber is accepted, and it would be more correct)
top1000_rdd = words_count_by_subreddit.select('*', rank().over(window).alias('rank'))\
  .filter(col('rank') <= 1000).rdd.map(lambda r: (r.subreddit, [r.word])).reduceByKey(lambda a,b: a+b)

top1000 = top1000_rdd.collect()
```
:::

::: {.cell .markdown id="JwdpK9CvLHs0"}
### **Bag of words representation of the document**
:::

::: {.cell .code id="Q_nMXeGoLGdC"}
``` python
import org.apache.spark.ml.feature.CountVectorizer

sparkDF = spark.createDataFrame(df[['character', 'line']])
sparkDF = sparkDF.filter(lambda x: x in characters_list)

#Get one dataframe with 1 row per elem in the list
all_words = sparkDF.select(explode("line").alias("word"))
all_words = all_words.groupBy("word")\
    .agg(count("*").alias("total"))\
    .sort(col("total").desc())

#Retrieve all the vocabulary
val list_words = all_words.select("word").rdd.map(row => row(0))
                .collect().toList

val cvModel: CountVectorizerModel = new CountVectorizer()
  .setInputCol("words")
  .setOutputCol("features")
  .setVocabSize(len(list_words))
  .fit(sparkDF)
```
:::
