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

        if self.filter_Entry(newEntry) == True:
            self.storage.append(newEntry)
            print("Entry added.")
            newEntry.print()
        else:
            print("Entry contains unacceptable character, not added.")

    def filter_Entry(self, entry): #function to check that the database entry received from the tkinter UI is valid before pickling
        p = re.compile('[^a-zA-Z ]+')  #regex to check that name only consists of one space and alphabetical characters
        m = p.search(entry.entryInfo['Name'])
        if m:
            print("invalid name entered")
            return False

        p = re.compile('[^a-zA-Z. /-]+') #regex to check position for alphabetical characters and a couple of other possible characters
        m = p.search(entry.entryInfo['Position'])
        if m:
            print("invalid position entered")
            return False

        p = re.compile('\d\d\d-\d\d-\d\d\d\d')  #regex to check for SSN match
        m = p.match(entry.entryInfo['SSN'])
        if not m:
            print("Invalid SSN entered")
            return False
        if len(entry.entryInfo['SSN']) != 11:
            print("Invalid SSN entered.")
            return False

        p = re.compile('[0-9]{1,6} [a-zA-Z0-9\. ]+ \d{5}') #regex to check address format
        m = p.match(entry.entryInfo['Address'])
        if not m:
            print("Invalid address entered")
            return False
        if m.span(0)[1] != len(entry.entryInfo['Address']):
            print("Invalid address entered.")
            return False

        #email address regex
        #long regex. could look at how to split this off, but did not want to mess with it for now
        #this is taken from https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/
        p = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
        m = p.match(entry.entryInfo['Email'])
        if not m:
            print("invalid email address entered")
            return False

        p = re.compile('[\(]?\d\d\d(\\)|-) ?\d\d\d-\d\d\d\d') #regex for phone number validation
        m = p.match(entry.entryInfo['Phone'])
        if not m:
            print("invalid phone number entered")
            return False
        if len(entry.entryInfo['Phone']) > 14:
            print("Invalid phone entered")
            return False

        p = re.compile('[^a-zA-Z ]+') #regex for skill. makes sure only alphabetical characters and spaces allowed
        m = p.search(entry.entryInfo['Skill'])
        if m:
            print("invalid skill entered")
            return False
        return True  #if all cases pass

    def search_Entry(self,key,value): #This will be the tag to search by. #Selected using buttons? #Passed in as string.

        print("\nEntries with the",key,value,":")

        for x in self.storage:
            if x.entryInfo[key] == value:
                x.print()

    def import_Txt(self,txtFile):

        #txtFile = str(input("Please enter the name of the file you want to import. \nMake sure it is in the same directory as the exe: "))
        #txtFile += ".txt"  #User specifies name of file
        
        if os.path.isfile(txtFile): #Make sure it exists
            data = open(txtFile,'r')
        else:
            print("{} File does not exist.".format(txtFile))
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
        self.print_Database()


#tkinter main loop
def tkmain():
    #object for class database
    dataObj = Database()


    #create tkinter window
    root = Tk()

    #open window dimention
    root.geometry('350x500')
    root.maxsize(894, 670)
    root.minsize(350,500)
    root.title("BEAR Software Group")
    #root.iconbitmap("bearicon.ico")

    #image background
    #bg = PhotoImage(file="background.png")
    #canvasRoot = Canvas(root, width = 500, heigh = 500)
    #canvasRoot.pack(fill = "both", expand = True)
    #canvasRoot.create_image(0,0, image = bg, anchor = "nw")
    

        


    #funtion for data entry window
    def dataEntryWindow():
        dataEntry = Toplevel(root)
        dataEntry.title("Add Data")
        dataEntry.geometry("600x500")
        dataEntry.maxsize(894, 670)
        dataEntry.minsize(350,500)
        #dataEntry.iconbitmap("bearicon.ico")

        #photo background
        canvas = tk.Canvas(dataEntry, width = 600, height = 500)
        canvas.pack(fill = "both", expand = True)
        #canvas.create_image(0,0, image = bg, anchor = "nw")

        nameValue = tk.StringVar()
        posValue = tk.StringVar()
        ssnValue = tk.StringVar()
        addressValue = tk.StringVar()
        emailValue = tk.StringVar()
        phoneValue = tk.StringVar()
        skillValue = tk.StringVar()

        #create entry boxes
        name = tk.Entry(dataEntry, textvariable = nameValue)
        position = tk.Entry(dataEntry, textvariable = posValue)
        ssn = tk.Entry(dataEntry, textvariable = ssnValue)
        address = tk.Entry(dataEntry, textvariable = addressValue)
        email = tk.Entry(dataEntry, textvariable = emailValue)
        phone = tk.Entry(dataEntry, textvariable = phoneValue)
        skill = tk.Entry(dataEntry, textvariable = skillValue)
        canvas.create_window(250,100, window=name)
        canvas.create_window(250,150, window=position)
        canvas.create_window(250,200, window=ssn)
        canvas.create_window(250,250, window=address)
        canvas.create_window(250,300, window=email)
        canvas.create_window(250,350, window=phone)
        canvas.create_window(250,400, window=skill)

        #create labels
        example = tk.Label(dataEntry, text="Example Format",bg = "black", fg = "white")
        canvas.create_window(367,65, window=example)
        labelName = tk.Label(dataEntry, text="Name",bg = "black", fg = "white")
        canvas.create_window(150,100, window=labelName)
        nameEx = tk.Label(dataEntry, text="Bruce Wayne",bg = "black", fg = "white")
        canvas.create_window(360,100, window=nameEx)
        labelPosition = tk.Label(dataEntry, text="Position",bg = "black", fg = "white")
        canvas.create_window(150,150, window=labelPosition)
        posEx = tk.Label(dataEntry, text="Batman",bg = "black", fg = "white")
        canvas.create_window(350,150, window=posEx)
        labelSSN = tk.Label(dataEntry, text="SSN",bg = "black", fg = "white")
        canvas.create_window(150,200, window=labelSSN)
        ssnEx = tk.Label(dataEntry, text="123-45-6789",bg = "black", fg = "white")
        canvas.create_window(360,200, window=ssnEx)
        labelAddress = tk.Label(dataEntry, text="Address",bg = "black", fg = "white")
        canvas.create_window(150,250, window=labelAddress)
        addressEx = tk.Label(dataEntry, text="380 S. San Rafael Dr Pasadena CA 91001",bg = "black", fg = "white")
        canvas.create_window(433,250, window=addressEx)
        labelEmail = tk.Label(dataEntry, text="Email",bg = "black", fg = "white")
        canvas.create_window(150,300, window=labelEmail)
        emailEx = tk.Label(dataEntry, text="NANANANANA@batman.com",bg = "black", fg = "white")
        canvas.create_window(410,300, window=emailEx)
        labelPhone = tk.Label(dataEntry, text="Phone Number",bg = "black", fg = "white")
        canvas.create_window(130,350, window=labelPhone)
        phoneEx = tk.Label(dataEntry, text="735-185-7301",bg = "black", fg = "white")
        canvas.create_window(365,350, window=phoneEx)
        labelSkill = tk.Label(dataEntry, text="Skill",bg = "black", fg = "white")
        canvas.create_window(150,400, window=labelSkill)
        skillEx = tk.Label(dataEntry, text="Crime Fighting",bg = "black", fg = "white")
        canvas.create_window(365,400, window=skillEx)

        strName = nameValue.get()
        strPosition = posValue.get()
        strSSN = ssnValue.get()
        strAddress = addressValue.get()
        strEmail = emailValue.get()
        strPhone = phoneValue.get()
        strSkill = skillValue.get()

        def submit():
            strName = nameValue.get()
            strPosition = posValue.get()
            strSSN = ssnValue.get()
            strAddress = addressValue.get()
            strEmail = emailValue.get()
            strPhone = phoneValue.get()
            strSkill = skillValue.get()
            dataObj.add_EntryFilled(strName,strPosition,strSSN,strAddress,strEmail,strPhone,strSkill) 
            nameValue.set("")
            posValue.set("")
            ssnValue.set("")
            addressValue.set("")
            emailValue.set("")
            phoneValue.set("")
            skillValue.set("")

        #submit button
        submit = Button(dataEntry, text = 'Submit', command=submit,bd = '5',bg = "black", fg = "white").place(x=250,y=450)
        
    #function to search data
    def queryDataWindow():
        queryData = Toplevel(root)
        queryData.title("Query Data")
        queryData.geometry("500x300")
        queryData.maxsize(894, 670)
        queryData.minsize(350,500)
        canvas = Canvas(queryData, width = 500, height = 300)
        canvas.pack(fill = "both", expand = True)
        queryData.iconbitmap("bearicon.ico")

        #photo background
        canvas.create_image(0,0, image = bg, anchor = "nw")

        keyValue = tk.StringVar()
        valueValue = tk.StringVar()

        #create entry box with labels
        key = tk.Entry(queryData, textvariable = keyValue )
        canvas.create_window(250,100, window=key)
        labelKey = tk.Label(queryData, text="Key",bg = "black", fg = "white")
        canvas.create_window(150,100, window=labelKey)
        exampleKey = tk.Label(queryData, text="Skill",bg = "black", fg = "white")
        canvas.create_window(350,100, window=exampleKey)

        value = tk.Entry(queryData, textvariable = valueValue)
        canvas.create_window(250,150, window=value)
        labelValue = tk.Label(queryData, text="Value",bg = "black", fg = "white")
        canvas.create_window(150,150, window=labelValue)
        exampleValue = tk.Label(queryData, text="Torture",bg = "black", fg = "white")
        canvas.create_window(350,150, window=exampleValue)

        example = tk.Label(queryData, text="Example Format",bg = "black", fg = "white")
        canvas.create_window(367,65, window=example)


        strKey = keyValue.get()
        strValue = valueValue.get()
        def submit():
            strKey = keyValue.get()
            strValue = valueValue.get()
            dataObj.search_Entry(strKey,strValue)           
            keyValue.set("")
            valueValue.set("")
        
        #submit button
        submit = Button(queryData, text = 'Submit', command=submit,bd = '5',bg = "black", fg = "white").place(x=250,y=200)
          
        
    #import data window
    def importDataWindow():
        fileValue = tk.StringVar()
        importData = Toplevel(root)
        importData.title("Import Data")
        importData.geometry("500x300")
        importData.maxsize(894, 670)
        importData.minsize(350,500)
        canvas = Canvas(importData, width = 500, height = 300)
        canvas.pack(fill = "both", expand = True)
        #importData.iconbitmap("bearicon.ico")

        #photo background
        #canvas.create_image(0,0, image = bg, anchor = "nw")

        file = tk.Entry(importData, textvariable = fileValue)
        canvas.create_window(250,100, window=file)
        labelFile = tk.Label(importData, text="File",bg = "black", fg = "white")
        canvas.create_window(150,100, window=labelFile)
        fileExample = tk.Label(importData, text="employeeInfov2.txt",bg = "black", fg = "white")
        canvas.create_window(375,100, window=fileExample)
        example = tk.Label(importData, text="Example Format",bg = "black", fg = "white")
        canvas.create_window(367,65, window=example)

        strFile = fileValue.get()
        def submit():
            strFile = fileValue.get()
            dataObj.import_Txt(strFile)
            fileValue.set("")

        print(strFile)
        submit = Button(importData, text = 'Submit', command=submit,bd = '5',bg = "black", fg = "white").place(x=200,y=150)



    #add data button
    adb = Button(root, text = 'Add Data',command=dataEntryWindow, bd = '5',bg = "black", fg = "white").place(x=100,y=100)

    #add query data button
    qdb = Button(root, text = 'Query Data',command=queryDataWindow, bd = '5',bg = "black", fg = "white").place(x=100,y=200)

    #add import data button
    ipb = Button(root, text = 'Import Data',command=importDataWindow, bd = '5',bg = "black", fg = "white").place(x=100,y=150)

    #add reverse data button
    rdb = Button(root, text = 'Reverse Data', command=dataObj.reverse_Data, bd = '5',bg = "black", fg = "white").place(x=100,y=250)



    tk.mainloop()

def main():
    #base = Database()
    #base.import_Txt()
    #base.search_Entry("Skill","Torture")
    tkmain()



if __name__ == "__main__":
    main()
