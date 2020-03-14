######################################
######################################
####                              ####
####                              ####
####       Highscore Sorter       ####
####            & GUI             ####
####                              ####
####                              ####
######################################
######################################
import sys
import pickle
from operator import itemgetter
from tkinter import *
from tkinter import ttk
file = 'HighScores.txt'
Highscores = []
i = 0

def NotFound():
    NA = Tk()
    NA.geometry('460x180')
    NA.title('No Users Found')
    NA.anchor(CENTER)
    ttk.Label(NA, text = 'Search Results', font=('Search User',50)).grid(row=0, column=0, columnspan = 2)
    ttk.Label(NA,text="Name:",font=("Name:", 20)).grid(row=1,column=0)
    ttk.Label(NA,text="Points:",font=("Points:", 20)).grid(row=1,column=1)
    ttk.Label(NA, text = 'No results found', font=('Search User',20)).grid(row=2, column=0,columnspan = 2)
    ttk.Button(NA, text = 'Close', command = lambda: NA.withdraw()).grid(row= 3, column = 1)
    
    
def ResetScores(root, file,YesNo):
    EmptyDict=[{'Name':'Empty',"Points":0}]
    with open(file,'wb') as file_handler:
        pickle.dump((EmptyDict),(file_handler))
    root.withdraw()
    YesNo.withdraw()
    print('Your scores have been reset')
    sys.exit()
def AreYouSure(root,file):
    YesNo = Tk()
    YesNo.anchor(CENTER)
    YesNo.geometry('166x50')
    YesNo.title("Are you sure?")
    ttk.Label(YesNo, text= 'Are you sure?', font=('Are you sure?', 10)).grid(row = 0, column = 0)
    ttk.Button(YesNo,text = 'Yes', command = lambda: ResetScores(root,file,YesNo)).grid(row= 1, column=0)
    ttk.Button(YesNo, text = 'No', command = lambda: YesNo.withdraw()).grid(row=1, column=1)
    
def search(SearchUser, temphs,root,counter):
        found = False
        SearchID = SearchUser.get()
        temp0 = {'Name':'Empty','Points':0}
        temp1 = {'Name':'Empty','Points':0}
        temp2 = {'Name':'Empty','Points':0}
        temp3 = {'Name':'Empty','Points':0}
        temp4 = {'Name':'Empty','Points':0}
        for i in range(len(temphs)):
            hs = temphs[i]

            if hs['Name'].lower() == SearchID:
                counter = counter+1
                found = True
                if counter == 1:
                    temp0 = hs
                if counter == 2:
                    temp1 = hs
                if counter == 3:
                    temp2 = hs
                if counter == 4:
                    temp3 = hs                
                if counter == 5:
                    temp4 = hs
        if found == True:
            Founduser(root, counter,SearchID, temp0, temp1,temp2,temp3,temp4)
        if found == False:
            NotFound()
                



def Founduser(root,counter, SearchID, temp0, temp1,temp2,temp3,temp4):
    SearchResults = Tk()
    SearchResults.geometry('460x344')
    sc = ("Showing results for user:",SearchID)
    SearchResults.title(sc)
    SearchResults.anchor(CENTER)
    ttk.Label(SearchResults,text="Search Results",font=("Highscores", 50)).grid(row=0,column=0,columnspan=2)
    ttk.Label(SearchResults,text="Name:",font=("Name:", 20)).grid(row=1,column=0)
    ttk.Label(SearchResults,text="Points:",font=("Points:", 20)).grid(row=1,column=1)
    ttk.Button(SearchResults, text = 'Close', command = lambda: SearchResults.withdraw()).grid(row= 7, column = 1)
    if counter == 1 or counter > 1:
        ttk.Label(SearchResults,text=(temp0)['Name'],font=(temp1, 20)).grid(row=2,column=0)
        ttk.Label(SearchResults,text=(temp0)['Points'],font=(temp1, 20)).grid(row=2,column=1)
    if counter == 2 or counter > 2:
        ttk.Label(SearchResults,text=(temp1)['Name'],font=(temp1, 20)).grid(row=3,column=0)
        ttk.Label(SearchResults,text=(temp1)['Points'],font=(temp1, 20)).grid(row=3,column=1)
    if counter == 3 or counter > 3:
        ttk.Label(SearchResults,text=(temp2)['Name'],font=(temp2, 20)).grid(row=4,column=0)
        ttk.Label(SearchResults,text=(temp2)['Points'],font=(temp2, 20)).grid(row=4,column=1)
    if counter == 4 or counter > 4:
        ttk.Label(SearchResults,text=(temp3)['Name'],font=(temp3, 20)).grid(row=5,column=0)
        ttk.Label(SearchResults,text=(temp3)['Points'],font=(temp3, 20)).grid(row=5,column=1)
    if counter == 5 or counter > 5:
        ttk.Label(SearchResults,text=(temp4)['Name'],font=(temp4, 20)).grid(row=6,column=0)
        ttk.Label(SearchResults,text=(temp4)['Points'],font=(temp4, 20)).grid(row=6,column=1)
    
        
    
    
            
def Gui(i):     
    with open (file, 'rb') as file_handler:
        Highscores = pickle.load(file_handler)
        counter = 0
    temphs = sorted(Highscores, reverse=True,key=itemgetter('Points'))
    root = Tk()
    root.geometry('460x548')
    root.title('Highscores!')
    root.anchor(CENTER)
    ttk.Label(root,text="Highscores",font=("Highscores", 67)).grid(row=0,column=0,columnspan=2)
    ttk.Label(root,text="Name:",font=("Name:", 20)).grid(row=1,column=0)
    ttk.Label(root,text="Points:",font=("Points:", 20)).grid(row=1,column=1)

    try:
        while i < 10:
            ttk.Label(root,text=(temphs[i])['Name'],font=(temphs[i], 20)).grid(row=i+2,column=0)
            ttk.Label(root,text=(temphs[i])['Points'],font=(temphs[i], 20)).grid(row=i+2,column=1)
            i = i + 1
    except IndexError:
        while i < 10:
            ttk.Label(root,text=('Empty'),font=('Empty', 20)).grid(row=i+2,column=0)
            ttk.Label(root,text=('0'),font=('0', 20)).grid(row=i+2,column=1)
            i = i + 1
    SearchUser = StringVar()

    ttk.Entry(root,textvariable = SearchUser).grid(row=12,column=1)
    SearchUser.get()
    ttk.Button(root,text = ('Search'), command = lambda: search(SearchUser,temphs,root,counter)).grid(row=13, column=1)
    ttk.Button(root,text = ("Reset"), command = lambda: AreYouSure(root, file)).grid(row=13, column = 0)
    mainloop()


Gui(i)

