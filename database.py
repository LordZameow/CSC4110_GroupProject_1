
from tkinter import *
import pickle #Loads database into a file
import re

class Entry:
        def __init__(self):  #Default constructor
            self.entryInfo = {
                "Name":"Unknown",
                "Position":"Unknown",
                "SSN": "Unknown",
                "Address":"Unknown",
                "Email":"Unknown",
                "Phone":"Unknown",
                "Skill":"Unknown"
                
                }
            

        def __init__(self, name, position, SSN, Address, email, phone, skill): #Parameterized Constructor
            
            #call filter entry function here?
            
            self.entryInfo = {
                "Name":"Unknown",
                "Position":"Unknown",
                "SSN": "Unknown",
                "Address":"Unknown",
                "Email":"Unknown",
                "Phone":"Unknown",
                "Skill":"Unknown"
                
                }
            
            self.entryInfo["Name"] = name
            self.entryInfo["Position"] = position
            self.entryInfo["SSN"] = SSN
            self.entryInfo["Address"] = Address
            self.entryInfo["Email"] = email
            self.entryInfo["Phone"] = phone
            self.entryInfo["Skill"] = skill

        def print(self):
            
            print("\nName:",self.entryInfo["Name"])
            print("Position:",self.entryInfo["Position"])
            print("SSN:",self.entryInfo["SSN"])
            print("Address:", self.entryInfo["Address"])
            print("Email:", self.entryInfo["Email"])
            print("Phone #:",self.entryInfo["Phone"])
            print("Skill:",self.entryInfo["Skill"])

class Database: #This is the applications main class. Everything is contained here.

    def __init__(self):
        self.storage = []


   
    def add_EntryFilled(self,name, position, SSN, Address, email, phone, skill):
        newEntry = Entry(name, position, SSN, Address, email, phone, skill)

        if self.filter_Entry(newEntry) == True:
            self.storage.append(newEntry)
            #print("Entry added.")
            
        else:
            print("Entry contains unacceptable character, not added.")
        
    def filter_Entry(self): #function to check that the database entry received from the tkinter UI is valid before pickling
        p = re.compile('[a-zA-Z]+ [a-zA-Z]+')  #regex to check that name only consists of one space and alphabetical characters
        m = p.match(self.entryInfo['Name'])
        if !m:
                print("invalid name entered")
                return False
        
        p = re.compile('[a-zA-Z. /-]+') #regex to check position for alphabetical characters and a couple of other possible characters
        m = p.match(self.entryInfo['Position'])
        if !m:
                print("invalid position entered")
                return False
        
        p = re.compile('\d\d\d-\d\d-\d\d\d\d')  #regex to check for SSN match
        m = p.match(self.entryinfo['SSN'])
        if !m:
                print("Invalid SSN entered")
                return False
        p = re.compile('[0-9]{1,6} \w+ \w*') #regex to check address format
        m = p.match(self.entryInfo['Address'])
        if !m:
                print("Invalid address entered")
                return False
        
        #email address regex
        #long regex. could look at how to split this off, but did not want to mess with it for now
        #this is taken from https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/
        p = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
        m = p.match(self.entryInfo['Email'])
        if !m:
                print("invalid email address entered")
                return False
        
        p = re.compile('\d\d\d-\d\d\d-\d\d\d\d') #regex for phone number validation
        m = p.match(self.entryInfo['Phone'])
        if !m:
                print("invalid phone number entered")
                return False
        
        p = re.compile('[a-zA-Z ]+') #regex for skill. makes sure only alphabetical characters and spaces allowed
        m = p.match(self.entryInfo['Skill'])
        if !m:
                print("invalid skill entered")
                return False
        return True  #if all cases pass
                                                            
    def search_Entry(self,key,value): #This will be the tag to search by. #Selected using buttons? #Passed in as string.
        
        print("\nEntries with the",key,value,":")

        for x in self.storage:
            if x.entryInfo[key] == value:
                x.print()

    def import_Txt(self):
        
        data = open("employeeInfov2.txt",'r') 

        for line in data:
            dataList = line.split(",")
            
            for i in range(len(dataList)): #remove any leading/trailing whitespace
                dataList[i] = dataList[i].strip()

            self.add_EntryFilled(dataList[0],dataList[1],dataList[2], dataList[3], dataList[4], dataList[5], dataList[6])
            #Make entry with values from line list
        

        self.print_Database()
    
   ##TODO: FILTER ENTRY FUNCTION


    def print_Database(self):
        for x in self.storage:
            x.print()

  


def main():
    base = Database()
    base.import_Txt()

    base.search_Entry("Skill","Torture")



if __name__ == "__main__":
    main()
