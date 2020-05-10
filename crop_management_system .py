# Ravi shankar sharma-19bcs091
import pandas as pd
import re
import matplotlib.pyplot as plt
import sys
from getpass import getpass

# ADMIN USERNAME: admin
# ADMIN PASSWORD: password


class User:
    def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname

    def getUsername(self):
      #print(self.firstname, self.lastname)
      print("Enter Username:")
      self.username=input()
    def getPassword(self):
      self.password = getpass("Enter Password:")
      User.password=self.password
      User.username=self.username
      print("****************User Registered******************")

response = int(input("ADMIN(1) | NEW USER(2) | REGISTERED USER(3)  ?"))

if(response is 2):
  fname=input("Enter First Name:")
  lname=input("Enter Last Name:")
  x = User(fname, lname)
  x.getUsername()
  x.getPassword()
  response = 3

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
     
        Login.username=self.username
        Login.password=self.password
        Login.token=0
        #Login.AdminAccess=False
        if((User.username == Login.username) and (User.password == Login.password)):
            print("Login Successful!")
            Login.token=1
        else:
            print("Login Failed!")
            Login.token=0
        Login.token=self.token

if(response is 3):
  uname=input("Enter Username:")
  pword = getpass("Enter Password:")
  x = Login(uname, pword)
if(response is 1):
  uname=input("Enter Username:")
  pword= getpass("Enter Password:")
if((uname == "ADMIN" ) and (pword is "password")):
     Login.token=2
     #Login.AdminAccess=True
else:
     Login.token= 0

#class Productivity_Details:
def TokenCheck(token):
  print(Login.token)
  if(Login.token == 1): # and (Login.AdminAccess == False)):
    ans=input("DO you want to see the graph (Y/N):")
    if(ans=='Y'):
      print ("The graph of productivity vs crop year")
      print("Select the crop")
      print("For Arecanut click 1")
      print("For Other kharif click 2") 
      print("For Rice  click 3")
      print("For Banana click 4")
      print("For Cashewnut click 5")
      print("For Cocunut click 6")
      n=int(input())
      if(n==1):
        #set directory
        f=pd.read_excel(r'file1.xlsx','Sheet2')
        #set plot
        plt.plot(f['Production'],f['Crop_Year'])
        #set label
        plt.xlabel('Production')
        plt.ylabel('Crop_Year')
        plt.title('Crop Production Details')
        plt.legend()
        plt.show()
      elif(n==2):
        #set directory
        f=pd.read_excel(r'file1.xlsx','Sheet3')
        #set plot
        plt.plot(f['Production'],f['Crop_Year'])
        #set label
        plt.xlabel('Production')
        plt.ylabel('Crop_Year')
        plt.title('Crop Production Details')
        plt.legend()
        plt.show()    
      elif(n==3):
        #set directory
        f=pd.read_excel(r'file1.xlsx','Sheet4')
        #set plot
        plt.plot(f['Production'],f['Crop_Year'])
        #set label
        plt.xlabel('Production')
        plt.ylabel('Crop_Year')
        plt.title('Crop Production Details')
        plt.legend()
        plt.show()    
      elif(n==4):
        #set directory
        f=pd.read_excel(r'file1.xlsx','Sheet5')
        #set plot
        plt.plot(f['Production'],f['Crop_Year'])
        #set label
        plt.xlabel('Production')
        plt.ylabel('Crop_Year')
        plt.title('Crop Production Details')
        plt.legend()
        plt.show()    
      elif(n==5):
        #set directory
        f=pd.read_excel(r'file1.xlsx','Sheet6')
        #set plot
        plt.plot(f['Production'],f['Crop_Year'])
        #set label
        plt.xlabel('Production')
        plt.ylabel('Crop_Year')
        plt.title('Crop Production Details')
        plt.legend()
        plt.show()    
      elif(n==6):
        #set directory
        f=pd.read_excel(r'file1.xlsx','Sheet7')
        #set plot
        plt.plot(f['Production'],f['Crop_Year'])
        #set label
        plt.xlabel('Production')
        plt.ylabel('Crop_Year')
        plt.title('Crop Production Details')
        plt.legend()
        plt.show()    
    path1 = "CropsDataFile.xlsx"
    cropdata = pd.read_excel(path1)
    print(cropdata.columns)
    cropdatanew = cropdata.groupby(['Crop_Year', 'Crop', 'State_Name', 'District_Name'])
    print(cropdatanew.first())
  elif (Login.token == 2): #and (Login.AdminAccess == True)):
    answer = input("Do you want to insert more details?")
    if (answer == "yes"):
      statename = input("Enter the statename: ")
      districtname = input("Enter the district name: ")
      cropyear = input("Enter the crop year: ")
      season = input("Enter the season: ")
      crop = input("Enter the crop: ")
      area = input("Enter the area: ")
      production = input("Enter the production amount: ")
      new_row = {'State_Name': statename, 'District_Name': districtname, 'Crop_Year': cropyear, 'Season': season, 'Crop': crop, 'Area': area, 'Production': production}
      cropdata = cropdata.append(new_row, ignore_index=True)
      print("This is the new data frame after appending the details that you entered:")
      print(cropdata)
    else:
      print("This is the current data:")
      print(cropdata)
  else:
    print("Wrong credentials:")

y = TokenCheck(Login.token)