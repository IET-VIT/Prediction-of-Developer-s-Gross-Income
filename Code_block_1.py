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