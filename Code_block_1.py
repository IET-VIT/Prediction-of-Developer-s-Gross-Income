# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:59:15 2020

@author: apurva sharma
"""

import pandas as pd

''' Importing the data '''

df = pd.read_csv("survey_results_public.csv")

from tqdm import tqdm

''' Converting some categorical features into Integers '''

def Convert_col_Cat_to_int(df):
    first_15_col_excl_yearcode = [ 'MainBranch'	,'Hobbyist',	'OpenSourcer',	'OpenSource',	'Employment',	'Country' ,
                    'Student'	,'EdLevel',	'UndergradMajor',	'EduOther',	'OrgSize',		'CareerSat']
    for i in tqdm(first_15_col_excl_yearcode):
      print('Converting '+i +'\n')
      print(list(df[i].unique()))
      df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
      print(df[i].unique())
    
    second_15_col_excl_yearcode = ['WorkPlan',	'WorkChallenge',	'WorkRemote',	'WorkLoc',	'ImpSyn' ,
                    'CodeRev'	,'UnitTests',	'PurchaseHow',	'PurchaseWhat']
    for i in tqdm(second_15_col_excl_yearcode):
      print('Converting '+i +'\n')
      print(list(df[i].unique()))
      df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
      print(df[i].unique())
    
    
    third_15_col_excl_yearcode = ['OpSys'	,'BlockchainOrg',	'BlockchainIs',	'ITperson']
    for i in tqdm(third_15_col_excl_yearcode):
      print('Converting '+i +'\n')
      print(list(df[i].unique()))
      df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
      print(df[i].unique())
      
    fourth_15_col_excl_yearcode = ['OffOn','SocialMedia',	'SOFindAnswer',	'SOVisitFreq','SOTimeSaved' ,
                    'SOHowMuchTime'	,'SOAccount',	'SOPartFreq',	'SOJobs',	'WelcomeChange',	'SONewContent',	'Gender','Trans','Sexuality','Dependents']
    for i in tqdm(fourth_15_col_excl_yearcode):
      print('Converting '+i)
      print(list(df[i].unique()))
      df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
      print(df[i].unique())
    
    
    last_15_col_excl_yearcode = ['JobSat','MgrIdiot','MgrMoney','MgrWant','JobSeek','LastHireDate','JobFactors','CurrencySymbol']
    for i in tqdm(last_15_col_excl_yearcode):
      print( 'Converting '+ i )
      print(list(df[i].unique()))
      df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
      print(df[i].unique()) 
      
    return df

print("Converting Categorical data to integers , mapping the categories \n\n")

Convert_col_Cat_to_int(df)

'''Dropped non - useful columns '''

def Dropping_Non_useful_data(df):
    
    df = df.drop(axis=1 ,columns=["Respondent", "Age1stCode", "FizzBuzz", "ResumeUpdate", "BetterLife", "ScreenName", "SOVisit1st",
                                 "EntTeams","SOComm","Extraversion","SurveyLength","SurveyEase","LastInt",'CurrencyDesc',
                                 "Ethnicity", "DevEnviron", "LanguageDesireNextYear","DatabaseDesireNextYear","PlatformDesireNextYear",
                                 "WebFrameDesireNextYear","MiscTechDesireNextYear","SOVisitTo", "WelcomeChange",
                                 "CurrencySymbol","CompTotal","CompFreq"])
    return df

Dropping_Non_useful_data(df)

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

''' Multiclass Categorical feature'''
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
d = dict(zip(set(ls), range(len(ls))))
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
d = dict(zip(set(ls), range(len(ls))))
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
d = dict(zip(set(ls), range(len(ls))))
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
d = dict(zip(set(ls), range(len(ls))))
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
d = dict(zip(set(ls), range(len(ls))))
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
d = dict(zip(set(ls), range(len(ls))))
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

''' Imputting data'''

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

'''Normalizing the data''' 

from sklearn import preprocessing

# Create a minimum and maximum processor object
min_max_scaler = preprocessing.MinMaxScaler( feature_range= (0,1))

# Create an object to transform the data to fit minmax processor
x_scaled = min_max_scaler.fit_transform(df.drop(axis = 1, columns= "ConvertedComp"))3
# Run the normalizer on the dataframe
df_normalized = pd.DataFrame(x_scaled)
