import tkinter as tk
from tkinter import *
import pickle #Loads database into a file
import re
import os

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

    def pickling(self):
        with open("database.pkl",'wb') as f:
            pickle.dump(self.storage)

    def unpickle(self):
        with open("database.pkl",'wb') as f:
            self.storage = pickle.load(f)

    def add_EntryFilled(self,name, position, SSN, Address, email, phone, skill):
        newEntry = Entry(name, position, SSN, Address, email, phone, skill)

        #if self.filter_Entry(newEntry) == True:
        self.storage.append(newEntry)
            #print("Entry added.")

       # else:
        #    print("Entry contains unacceptable character, not added.")

    def filter_Entry(self, entry): #function to check that the database entry received from the tkinter UI is valid before pickling
        p = re.compile('[a-zA-Z]+ [a-zA-Z]+')  #regex to check that name only consists of one space and alphabetical characters
        m = p.match(entry.entryInfo['Name'])
        if not m:
                print("invalid name entered")
                return False

        p = re.compile('[a-zA-Z. /-]+') #regex to check position for alphabetical characters and a couple of other possible characters
        m = p.match(entry.entryInfo['Position'])
        if not m:
                print("invalid position entered")
                return False

        p = re.compile('\d\d\d-\d\d-\d\d\d\d')  #regex to check for SSN match
        m = p.match(entry.entryInfo['SSN'])
        if not m:
                print("Invalid SSN entered")
                return False
        p = re.compile('[0-9]{1,6} \w+ \w*') #regex to check address format
        m = p.match(entry.entryInfo['Address'])
        if not m:
                print("Invalid address entered")
                return False

        #email address regex
        #long regex. could look at how to split this off, but did not want to mess with it for now
        #this is taken from https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/
        p = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
        m = p.match(entry.entryInfo['Email'])
        if not m:
                print("invalid email address entered")
                return False

        p = re.compile('\d\d\d-\d\d\d-\d\d\d\d') #regex for phone number validation
        m = p.match(entry.entryInfo['Phone'])
        if not m:
                print("invalid phone number entered")
                return False

        p = re.compile('[a-zA-Z ]+') #regex for skill. makes sure only alphabetical characters and spaces allowed
        m = p.match(entry.entryInfo['Skill'])
        if not m:
                print("invalid skill entered")
                return False
        return True  #if all cases pass

    def search_Entry(self,key,value): #This will be the tag to search by. #Selected using buttons? #Passed in as string.

        print("\nEntries with the",key,value,":")

        for x in self.storage:
            if x.entryInfo[key] == value:
                x.print()

    def import_Txt(self):

        txtFile = str(input("Please enter the name of the file you want to import. \nMake sure it is in the same directory as the exe: "))
        txtFile += ".txt"  #User specifies name of file
        
        if os.path.isfile(txtFile): #Make sure it exists
            data = open(txtFile,'r')
        else:
            print("File does not exist.")
            return

        for line in data:
            dataList = line.split(",")

            for i in range(len(dataList)): #remove any leading/trailing whitespace
                dataList[i] = dataList[i].strip()

            self.add_EntryFilled(dataList[0],dataList[1],dataList[2], dataList[3], dataList[4], dataList[5], dataList[6])
            #Make entry with values from line list


        self.print_Database()


    def print_Database(self):
        for x in self.storage:
            x.print()
        
    def reverse_Data(self):
        self.storage.reverse()


#tkinter main loop
def tkmain():
    #create tkinter window
    root = Tk()

    #open window dimention
    root.geometry('350x500')

    #add data button
    adb = Button(root, text = 'Add Data', bd = '5').place(x=100,y=100)

    #add query data button
    qdb = Button(root, text = 'Query Data', bd = '5').place(x=100,y=200)

    #add import data button
    ipb = Button(root, text = 'Import Data', bd = '5').place(x=100,y=150)

    #add reverse data button
    rdb = Button(root, text = 'Reverse Data', bd = '5').place(x=100,y=250)

    #add Archive/upload data button
    udb = Button(root, text = 'Archive/Upload Data', bd = '5').place(x=100,y=300)


    tk.mainloop()

def main():
    base = Database()
    base.import_Txt()
    tkmain()
    base.search_Entry("Skill","Torture")



if __name__ == "__main__":
    main()
