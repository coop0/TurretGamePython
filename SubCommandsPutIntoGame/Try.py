#24/10/16
#Cooper and Angus
#Try and except errors
import sys
import os
import pickle
from tkinter import *
from tkinter import ttk
file = "Halogen.txt"
custOut = []
EmptyDict={'Name':'',"Points":''}


def Continue(root):
    print("Scores will not be saved for this game")
    root.withdraw()
def ResetScores(root, file):
    with open(file,'wb') as file_handler:
        pickle.dump((EmptyDict),(file_handler))
    root.withdraw()
    
def HighscoresGUIError():
    root = Tk()
    root.geometry('1280x720')
    root.title("Warning")
    TextA = "Warning, your score will not be saved for this game"
    TextB = "please chose one of the options below"
    ttk.Label(root, text = TextA, font = (TextA,40)).grid(column=0,row=0)
    ttk.Label(root, text = TextB, font = (TextB,40)).grid(column=0,row=1)
    ttk.Button(root, text = "Reset highscores to allow future highscore to be saved", command=lambda: ResetScores(root, file)).grid(column=0,row=2)
    ttk.Button(root, text = "Continue without saving", command=lambda: Continue(root)).grid(column=0,row=3)
try:
    with open(file,"rb")as file_handler:
        custOut = pickle.load(file_handler)
except EOFError:
    HighscoresGUIError()

HighscoresGUIError()

