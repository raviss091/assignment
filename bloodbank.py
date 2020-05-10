# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:29:15 2020

@author: Ravi shankar sharma-19bcs091

"""
import xlrd

def Retrieval_Donor_data(id_):
    x=int(0)
    loc=("C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\pytavi\\blood_bank.xls")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    for i in range(sheet.nrows):
        if(id_==sheet.cell_value(i,0)):
            x=1
            for j in range(sheet.ncols):
                print(sheet.cell_value(i,j))
    if(x==0): 
        print("no such record")


def rare_bloodgroup():
    n=int(0)
    
    loc=("C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\pytavi\\blood_bank.xls")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    for i in range(sheet.nrows):
        if(sheet.cell_value(i,13)=="o-" or sheet.cell_value(i,13)=="ab-"):
            n=n+1
    print("no of rare blood group is %d :",n)
    print("particular of patients")
    for i in range(sheet.nrows):
        if(sheet.cell_value(i,13)=="o-" or sheet.cell_value(i,13)=="ab-"):
            for j in range(sheet.ncols):
                
                print(sheet.cell_value(i,j))

def branch_data():
    loc=("C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\pytavi\\blood_bank.xls")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    b=input("enter branch name :")
    for i in range(sheet.nrows):
        if(b==sheet.cell_value(i,4)):
            print(sheet.cell_value(i,1))
            print(sheet.cell_value(i,2))
            print(sheet.cell_value(i,3))
            print(sheet.cell_value(i,5))
            print(sheet.cell_value(i,6))
            print(sheet.cell_value(i,7))
          
        
if __name__=='__main__':
    
    m=int(input("enter your choice \n1. donor data\n2.rare blood data\n3.branch data"))
    if(m==1):
        id_=int(input("enter the id number :"))
        Retrieval_Donor_data(id_)
    if(m==2):
        rare_bloodgroup()
    if(m==3):
        branch_data()
"""
output
enter your choice 
1. donor data
2.rare blood data
3.branch data1

enter the id number :6
6.0
Andhra Pradesh
Eluru
West Godavari
Alluri Sita Rama Raju Acadamy of Medical Sciences Blood Bank
Ground Floor, Hospital Block, NH5
NA
08812 244484
NA
NA
NA
http://asram.isram_hospitals/aboutus.php
NA
b+
NA
NA
NA
NA

"""
    
   
    
    