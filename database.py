
from tkinter import *
import pickle #Loads database into a file

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


    def add_EntryBlank(self):
        
        #Pass in entries from tkinter text boxes
       print("Hello")
    def add_EntryFilled(self):
        #put filter entry function here?
        #use tkinter
        print("Hello")
    
    def search_Entry(self,key,value): #This will be the tag to search by. #Selected using buttons? #Passed in as string.
        
        print("\nEntries with the",key,value,":")

        for x in self.storage:
            if x.entryInfo[key] == value:
                x.print()

    def import_Txt(self):
        
        data = open("employeeInfo.txt",'r') 

        for line in data:
            dataList = line.split(",")
            
            for i in range(len(dataList)): #remove any leading/trailing whitespace
                dataList[i] = dataList[i].strip()

            self.storage.append(Entry(dataList[0],dataList[1],dataList[2], dataList[3], dataList[4], dataList[5], dataList[6]))
            #Make entry with values from line list
        

        for i in self.storage: #To check that everything was read in correctly
            i.print()
    
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