# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 00:14:40 2020

@author:  Ravi shankar sharma-19bcs091
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

if __name__=='__main__':
    print("For admin rights enter 1 and user enter 0")
    a=int(input("enter the code  "))
    
    if (a==0):
        print("If you want to register enter 2 otherwise enter any other number.")
        y=int(input())
        
        if (y==2):
            x=str(input("Enter your Name to register in our system and please write \\n on end to change the line if you are already registerd please ignore this message.   "))
            f=open("fts.txt", "a")
            f.write(x)
            f.close()
            print("Congratulations you have been registered with our system.\n")
        else:
            pass
        
        z=int(input("Press 3 if you want check or view your funds transfer details related to their transactions otherwise ignore this message.   "))
        
        if (z==3):
            naam=str(input("Enter your name.   "))
            f=open("fts.txt","r")
            out=[i for i in f if naam in i]
            print(str(out))
    
    
    
    if (a==1):
        print("If you want to see and read all the data press 4 or if you want to add something in file press 5.")
        ra=int(input())
        
        if(ra==4):
            q=open("fts.txt", "r")
            print(q.read())
        
        if(ra==5):
            print("if you want to replace a string enter 6 or if you want to add a new string enter 7.")
            replace=int(input())
            
            if (replace==6):
                d=str(input("Enter the string which you want to replace.  "))
                e=str(input("Enter the new string which is placed in place on older one.  "))
                fin = open("fts.txt", "rt")
                data = fin.read()
                data = data.replace(d,e)
                fin.close()
                fin = open("fts.txt", "wt")
                fin.write(data)
                fin.close()
                print("Modified text file is.\n")
                print("                          ")
                k=open("fts.txt", "r")
                print(k.read())
            
            if(replace==7):
                text_file = open("fts.txt", "a")
                z=str(input("Enter the string which you want to add in text file, in the given format    'NameTabTabFundTabTabTabTabTabTabFrom BankTabTabTabTo BankTabTabDate and TimeTabTabEmail id'      "))
                m=text_file.write("\n"+z)
                text_file.close()
                print("Modified text file is.\n")
                print("                          ")
                k=open("fts.txt", "r")
                print(k.read())





        