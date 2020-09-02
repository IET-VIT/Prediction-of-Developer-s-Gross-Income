# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:59:15 2020

@author: apurva sharma
"""

import pandas as pd

''' Importing the data '''

df = pd.read_csv("survey_results_public.csv")

contries = list(df["Country"].unique())

#df = df[df["Country"]=='South Africa']

from tqdm import tqdm

''' Converting some categorical features into Integers '''

def Convert_col_Cat_to_int(df):
    first_15_col_excl_yearcode = [ 'MainBranch'	,'Hobbyist',	'OpenSourcer',	'OpenSource',	'Employment',	'Country' ,
                    'Student'	,'EdLevel',	'UndergradMajor',	'EduOther',	'OrgSize','CareerSat']
    for i in tqdm(first_15_col_excl_yearcode):
      print('Converting '+ i +'\n')
      
      df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
      print(df[i].unique())
    
    second_15_col_excl_yearcode = ['WorkPlan',	'WorkChallenge',	'WorkRemote',	'WorkLoc',	'ImpSyn' ,
                    'CodeRev'	,'UnitTests',	'PurchaseHow',	'PurchaseWhat']
    for i in tqdm(second_15_col_excl_yearcode):
      print('Converting '+i +'\n')
      df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
      print(df[i].unique())
    
    
    third_15_col_excl_yearcode = ['OpSys'	,'BlockchainOrg',	'BlockchainIs',	'ITperson']
    for i in tqdm(third_15_col_excl_yearcode):
      print('Converting '+i +'\n')
 
      df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
      print(df[i].unique())
      
    fourth_15_col_excl_yearcode = ['OffOn','SocialMedia',	'SOFindAnswer',	'SOVisitFreq','SOTimeSaved' ,
                    'SOHowMuchTime'	,'SOAccount',	'SOPartFreq',	'SOJobs',	'WelcomeChange',	'SONewContent',	'Gender','Trans','Sexuality','Dependents']
    for i in tqdm(fourth_15_col_excl_yearcode):
      print('Converting '+i)
      df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
      print(df[i].unique())
    
    
    last_15_col_excl_yearcode = ['JobSat','MgrIdiot','MgrMoney','MgrWant','JobSeek','LastHireDate','JobFactors','CurrencySymbol']
    for i in tqdm(last_15_col_excl_yearcode):
      print( 'Converting '+ i )
      df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
      print(df[i].unique()) 
      
    return df

print("Converting Categorical data to integers , mapping the categories \n\n")

Convert_col_Cat_to_int(df)

'''Dropped non - useful columns

def Dropping_Non_useful_data(df): '''
    
df = df.drop(axis=1, columns=["Respondent", "Age1stCode", "FizzBuzz", "ResumeUpdate", "BetterLife", "ScreenName", "SOVisit1st",
                                 "EntTeams","SOComm","Extraversion","SurveyLength","SurveyEase","LastInt",'CurrencyDesc',
                                 "Ethnicity", "DevEnviron", "LanguageDesireNextYear","DatabaseDesireNextYear","PlatformDesireNextYear",
                                 "WebFrameDesireNextYear","MiscTechDesireNextYear","SOVisitTo", "WelcomeChange",
                                 "CurrencySymbol","CompTotal","CompFreq"])
'''   return df

Dropping_Non_useful_data(df) '''

def Convert_YearsCodePro_and_YearsCode ( df ):
    
    df["YearsCode"].replace(to_replace = ['Less than 1 year', 'More than 50 years'],
                            value = [1,50] , inplace = True) 
    df["YearsCode"].fillna(value= '-1', inplace = True )
    df["YearsCode"] = df["YearsCode"].apply(pd.to_numeric) 
    df["YearsCodePro"].replace(to_replace = ['Less than 1 year', 'More than 50 years'],
                            value = [1,50] , inplace = True) 
    df["YearsCodePro"].fillna(value= '-1', inplace = True )
    df["YearsCodePro"] = df["YearsCodePro"].apply(pd.to_numeric)
    
    return df

Convert_YearsCodePro_and_YearsCode(df)

                     
def conv_multi_cat(df):
    DevType = df["DevType"]
    DevType.fillna(value= '-1', inplace = True )
    ls = []
    for i in DevType:    
        if i != '-1':
            cat = i.split(';')
            for j in cat:
                if j not in ls:
                    ls.append(j)
    d = dict(zip(set(ls),[1]*len(ls)))
    rep_devtype = []
    for i in DevType:
        if i == '-1':
            rep_devtype.append(-1)
        if i != '-1':
            sum = 0
            cat = i.split(';')
            for j in cat:
                sum = d[ j ] + sum
            rep_devtype.append(sum) 
            
    DevType = pd.DataFrame(rep_devtype)
    
    df["DevType"] = DevType
    
    LanguageWorkedWith = df["LanguageWorkedWith"]
    LanguageWorkedWith.fillna(value= '-1', inplace = True )
    ls = []
    for i in LanguageWorkedWith  :    
        if i != '-1':
            cat = i.split(';')
            for j in cat:
                if j not in ls:
                    ls.append(j)
    d = dict(zip(set(ls), [1]*len(ls)))
    rep_LanguageWorkedWith   = []
    for i in LanguageWorkedWith  :
        if i == '-1':
            rep_LanguageWorkedWith.append(-1)
        if i != '-1':
            sum = 0
            cat = i.split(';')
            for j in cat:
                sum = d[ j ] + sum
            rep_LanguageWorkedWith.append(sum) 
    LanguageWorkedWith = pd.DataFrame(rep_LanguageWorkedWith)
    
    df["LanguageWorkedWith"] = LanguageWorkedWith
    
    DatabaseWorkedWith = df["DatabaseWorkedWith"]
    DatabaseWorkedWith.fillna(value= '-1', inplace = True )
    ls = []
    for i in DatabaseWorkedWith  :    
        if i != '-1':
            cat = i.split(';')
            for j in cat:
                if j not in ls:
                    ls.append(j)
    d = dict(zip(set(ls), [1]*len(ls)))
    rep_DatabaseWorkedWith   = []
    for i in DatabaseWorkedWith  :
        if i == '-1':
            rep_DatabaseWorkedWith.append(-1)
        if i != '-1':
            sum = 0
            cat = i.split(';')
            for j in cat:
                sum = d[ j ] + sum
            rep_DatabaseWorkedWith.append(sum) 
    DatabaseWorkedWith = pd.DataFrame(rep_DatabaseWorkedWith)
    
    df["DatabaseWorkedWith"] = DatabaseWorkedWith
    
    PlatformWorkedWith = df["PlatformWorkedWith"]
    PlatformWorkedWith.fillna(value= '-1', inplace = True )
    ls = []
    for i in PlatformWorkedWith  :    
        if i != '-1':
            cat = i.split(';')
            for j in cat:
                if j not in ls:
                    ls.append(j)
    d = dict(zip(set(ls), [1]*len(ls)))
    rep_PlatformWorkedWith   = []
    for i in PlatformWorkedWith  :
        if i == '-1':
            rep_PlatformWorkedWith.append(-1)
        if i != '-1':
            sum = 0
            cat = i.split(';')
            for j in cat:
                sum = d[ j ] + sum
            rep_PlatformWorkedWith.append(sum) 
    PlatformWorkedWith = pd.DataFrame(rep_PlatformWorkedWith)
    
    df["PlatformWorkedWith"] = PlatformWorkedWith
    
    WebFrameWorkedWith = df["WebFrameWorkedWith"]
    WebFrameWorkedWith.fillna(value= '-1', inplace = True )
    ls = []
    for i in WebFrameWorkedWith  :    
        if i != '-1':
            cat = i.split(';')
            for j in cat:
                if j not in ls:
                    ls.append(j)
    d = dict(zip(set(ls), [1]*len(ls)))
    rep_WebFrameWorkedWith   = []
    for i in WebFrameWorkedWith  :
        if i == '-1':
            rep_WebFrameWorkedWith.append(-1)
        if i != '-1':
            sum = 0
            cat = i.split(';')
            for j in cat:
                sum = d[ j ] + sum
            rep_WebFrameWorkedWith.append(sum) 
    WebFrameWorkedWith = pd.DataFrame(rep_WebFrameWorkedWith)
    
    df["WebFrameWorkedWith"] = DatabaseWorkedWith
    
    MiscTechWorkedWith = df["MiscTechWorkedWith"]
    MiscTechWorkedWith.fillna(value= '-1', inplace = True )
    ls = []
    for i in MiscTechWorkedWith  :    
        if i != '-1':
            cat = i.split(';')
            for j in cat:
                if j not in ls:
                    ls.append(j)
    d = dict(zip(set(ls), [1]*len(ls)))
    rep_MiscTechWorkedWith   = []
    for i in MiscTechWorkedWith  :
        if i == '-1':
            rep_MiscTechWorkedWith.append(-1)
        if i != '-1':
            sum = 0
            cat = i.split(';')
            for j in cat:
                sum = d[ j ] + sum
            rep_MiscTechWorkedWith.append(sum) 
    MiscTechWorkedWith = pd.DataFrame(rep_MiscTechWorkedWith)
    
    df["MiscTechWorkedWith"] = MiscTechWorkedWith
    
    Containers = df["Containers"]
    Containers.fillna(value= '-1', inplace = True )
    ls = []
    for i in Containers  :    
        if i != '-1':
            cat = i.split(';')
            for j in cat:
                if j not in ls:
                    ls.append(j)
    d = dict(zip(set(ls), [1]*len(ls)))
    rep_Containers   = []
    for i in Containers  :
        if i == '-1':
            rep_Containers.append(-1)
        if i != '-1':
            sum = 0
            cat = i.split(';')
            for j in cat:
                sum = d[ j ] + sum
            rep_Containers.append(sum) 
    Containers = pd.DataFrame(rep_Containers)
        
    
    df["Containers"] = Containers   
    corr = df.corr()["ConvertedComp"]
    
    return df

conv_multi_cat(df)

'''Impute data'''
def impute_data(df):
    df['WorkWeekHrs'] = df['WorkWeekHrs'].fillna((df['WorkWeekHrs'].mean()))
    df['CodeRevHrs'] = df['CodeRevHrs'].fillna((df['CodeRevHrs'].mean()))
    df['Age'] = df['Age'].fillna((df['Age'].median()))
    ls = []
    for i in range(len(df["MainBranch"])):
      if df["MainBranch"][i] == 1:
        ls.append(i)
    len(ls)
    for i in range(len(df["ConvertedComp"])):
      if i in ls:
        df["ConvertedComp"][i] = 0
    df["ConvertedComp"] = df["ConvertedComp"].fillna(value = df["ConvertedComp"].mean())
    newConvComp=[]
    for i in df["ConvertedComp"]:
      newConvComp.append(i//200000)
    df["ConvertedComp"]=newConvComp
    
    return df

impute_data(df)
'''Normalizing the data''' 

from sklearn import preprocessing

def normalize_data(df):
    # Create a minimum and maximum processor object
    min_max_scaler = preprocessing.MinMaxScaler( feature_range= (0,1))
    
    # Create an object to transform the data to fit minmax processor
    x_scaled = min_max_scaler.fit_transform(df)
    # Run the normalizer on the dataframe
    df_normalized = pd.DataFrame(x_scaled)   
    
    return df_normalized 



df_normalized = normalize_data(df)
corr = df.corr()["ConvertedComp"]


'''Exploratory Data analysis'''

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(20, 6))
sns.barplot(x = 'MainBranch', y = 'ConvertedComp', data = df, ax = ax1, palette='coolwarm')
sns.barplot(x = 'Hobbyist', y = 'ConvertedComp', data = df, ax = ax2, palette = 'magma')
sns.barplot(x = 'OpenSource', y = 'ConvertedComp', data = df, ax = ax3)

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(20, 6))
sns.barplot(x = 'OpenSourcer', y = 'ConvertedComp', data = df, ax = ax1, palette='coolwarm')
sns.barplot(x = 'Employment', y = 'ConvertedComp', data = df, ax = ax2, palette = 'magma')

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(20, 6))
sns.barplot(x = 'Student', y = 'ConvertedComp', data = df, ax = ax1, palette='coolwarm')
sns.barplot(x = 'EdLevel', y = 'ConvertedComp', data = df, ax = ax2, palette = 'magma')
sns.barplot(x = 'UndergradMajor', y = 'ConvertedComp', data = df, ax = ax3)

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(20, 6))
sns.barplot(x = 'OrgSize', y = 'ConvertedComp', data = df, ax = ax1, palette='coolwarm')
sns.barplot(x = 'CareerSat', y = 'ConvertedComp', data = df, ax = ax2, palette = 'magma')
sns.barplot(x = 'JobSat', y = 'ConvertedComp', data = df, ax = ax3)


fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(20, 6))
sns.barplot(x = 'MgrIdiot', y = 'ConvertedComp', data = df, ax = ax1, palette='coolwarm')
sns.barplot(x = 'MgrMoney', y = 'ConvertedComp', data = df, ax = ax2, palette = 'magma')
sns.barplot(x = 'MgrWant', y = 'ConvertedComp', data = df, ax = ax3)


fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20, 6))
sns.barplot(x = 'JobSeek', y = 'ConvertedComp', data = df, ax = ax1, palette='coolwarm')
sns.barplot(x = 'LastHireDate', y = 'ConvertedComp', data = df, ax = ax2, palette = 'magma')
# JobFactors

fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 5))
#WorkWeekHrs
sns.barplot(x = 'WorkPlan', y = 'ConvertedComp', data = df, ax = ax1, palette = 'magma')
#WorkChallenge

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(20, 6))
sns.barplot(x = 'WorkRemote', y = 'ConvertedComp', data = df, ax = ax1, palette='coolwarm')
sns.barplot(x = 'WorkLoc', y = 'ConvertedComp', data = df, ax = ax2, palette = 'magma')
sns.barplot(x = 'ImpSyn', y = 'ConvertedComp', data = df, ax = ax3)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20, 6))
sns.barplot(x = 'CodeRev', y = 'ConvertedComp', data = df, ax = ax1, palette='coolwarm')
sns.barplot(x = 'UnitTests', y = 'ConvertedComp', data = df, ax = ax2)

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(20, 6))
sns.barplot(x = 'OpSys', y = 'ConvertedComp', data = df, ax = ax1, palette='coolwarm')
sns.barplot(x = 'BlockchainOrg', y = 'ConvertedComp', data = df, ax = ax2, palette = 'magma')
sns.barplot(x = 'ITperson', y = 'ConvertedComp', data = df, ax = ax3)

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(20, 6))
sns.barplot(x = 'OffOn', y = 'ConvertedComp', data = df, ax = ax1, palette='coolwarm')
sns.barplot(x = 'SocialMedia', y = 'ConvertedComp', data = df, ax = ax2, palette = 'magma')
sns.barplot(x = 'SOVisitFreq', y = 'ConvertedComp', data = df, ax = ax3)

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(20, 6))
sns.barplot(x = 'SOFindAnswer', y = 'ConvertedComp', data = df, ax = ax1, palette='coolwarm')
sns.barplot(x = 'SOTimeSaved', y = 'ConvertedComp', data = df, ax = ax2, palette = 'magma')
sns.barplot(x = 'SOHowMuchTime', y = 'ConvertedComp', data = df, ax = ax3)

fig, ((ax1, ax2), (ax3,ax4)) = plt.subplots(ncols=2,nrows=2, figsize=(20, 6))
sns.barplot(x = 'SOAccount', y = 'ConvertedComp', data = df, ax = ax1, palette='coolwarm')
sns.barplot(x = 'SOPartFreq', y = 'ConvertedComp', data = df, ax = ax2, palette = 'magma')
sns.barplot(x = 'SOJobs', y = 'ConvertedComp', data = df, ax = ax3)
sns.barplot(x = 'SONewContent', y = 'ConvertedComp', data = df, ax = ax4)

#Age

fig, ((ax1, ax2), (ax3,ax4)) = plt.subplots(ncols=2,nrows=2, figsize=(20, 6))
sns.barplot(x = 'Gender', y = 'ConvertedComp', data = df, ax = ax1, palette='coolwarm')
sns.barplot(x = 'Trans', y = 'ConvertedComp', data = df, ax = ax2, palette = 'magma')
sns.barplot(x = 'Sexuality', y = 'ConvertedComp', data = df, ax = ax3)
sns.barplot(x = 'Dependents', y = 'ConvertedComp', data = df, ax = ax4)









    
    
    
    
    
    