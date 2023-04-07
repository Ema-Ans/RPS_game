
#STUDENT NAME: MALAIKA ANSAR


#INSTALL THE LIBRARIES FOR THE GAME TO WORK
#pip install Pillow
#pip install playsound

# THE GAME HAS SOUND EFFECTS 

from ctypes import resize
from tkinter import *
from PIL import Image,ImageTk
#lib that generates a random integer for us
from random import randint
#to create the main window
from playsound import playsound


root = Tk()
root.title("Malaika's Game - Rock, Paper, Scissors!")
root.configure(background = "black")

#to get the images 


background_image=ImageTk.PhotoImage(Image.open('bts.jpg'))
background_label = Label(root, image=background_image, bg = "black")
background_label.place(x=0, y=0, relwidth=1, relheight=1)


rock_img_user = ImageTk.PhotoImage(Image.open("rock_computer.gif"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock_user.gif"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper_user.gif"))
paper_img_user = ImageTk.PhotoImage(Image.open("paper_computer.gif"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor_user.gif"))
scissor_img_user = ImageTk.PhotoImage(Image.open("scissor_computer.gif"))

#Inserting Pictures
comp_label = Label(root, image = rock_img_comp, bg = "black")
user_label = Label(root,image = rock_img_user, bg = "black")
#fixing where they are placed on the screen
user_label.grid(row = 1, column = 0)
comp_label.grid(row = 1, column = 4)
#Set scores for both the play and the computer
playerScore = Label(root, text = 0, font = 100, bg = "white", fg = "black")
computerScore = Label(root, text = 0, font = 100, bg = "white", fg = "black")
#align where the scores are shown on the screen
playerScore.grid(row=1, column=1)
computerScore.grid(row=1, column=3)

#indicatorss
user_indicator = Label(root, font = 50, text="USER").grid(row = 3, column = 0)
comp_indicator = Label(root, font = 50, text = "COMPUTER").grid(row = 3, column = 4)

#Messages that'll be displayed on the screen
message = Label(root, font=50 , bg= "black", fg= "white")
message.grid(row=3, column = 2)



def updateMessage(m):
    message['text'] = m

#Updating the User Score
#adds 1 to the current score shown on the screen
def updateScoreUser():
    #we convert the score to integer because it'll be in string form 
    score = int(playerScore["text"])
    #we add 1 to that integer
    score += 1
    #we set the score back to the new score after adding 1
    #we convert it back to string
    playerScore["text"] = str(score)
def updateCompScore():
    #we convert the score to integer because it'll be in string form 
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)
#Checking who wins

def checkWinner(user, comp):
    if user == comp: 
        
        updateMessage("Welp, thats a tie!")
        playsound("Tie.mp3")
        #updateSong(message["text"])
        
    elif user == "rock":
        if comp == "paper":
            playsound("Lost.mp3")
            updateMessage("AAh, you lost :C")
            updateCompScore()
        else:
            playsound("winning.mp3")
            updateMessage("Yay, you win!")
            updateScoreUser()

    elif user == "paper":
        if comp == "scissor":
            playsound("Lost.mp3")
            updateMessage("AAh, you lost :C")
            updateCompScore()
        else:
            playsound("winning.mp3")
            updateMessage("Yay, you win!")
            updateScoreUser()
    elif user == "scissor":
        if comp == "rock":
            playsound("Lost.mp3")
            updateMessage("AAh, you lost :C")
            updateCompScore()
        else:
            playsound("winning.mp3")
            updateMessage("Yay, you win!")
            updateScoreUser()
    else:
        pass





#update choices

#choices for the computer must be random
choices = ["rock", "paper", "scissor"]
#mke a function that'll update the choices for the computer and the user
def choice(c):
    #FOR THE COMPUTER
    #WE UPDATE THE CHOICES RANDOMLY
    #get a random index from 0, 1 , 2
    randIndex = randint(0,2)
    #randomly get a choice from the list of choices
    compChoice = choices[randIndex]
    if compChoice == "rock":
        #update the computers image to the rock_img
        comp_label.configure(image = rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image = paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    
    
    #FOR THE USER
    #WE UPDATE THE CHOICES DEPENING ON THE BUTTON PRESSED BY THE USER
    if c == "rock":
        #update the image to the rock_img
        user_label.configure(image = rock_img_user)
    elif c == "paper":
        #and if its paper then update the image to 
        #the paper image
        user_label.configure(image = paper_img_user)
    else:
        #the last option is that its a scissor
        #so update it to the scissor image
        user_label.configure(image=scissor_img_user)
    #call the function you wrote above and update the scores
    #and the message
    checkWinner(c, compChoice)

    
#buttons
rock = Button(root, width = 20 , height = 2, text = "ROCK", bg = "#aa0c90", fg = "white", command = lambda:choice("rock")).grid(row=2, column=1)
scissor = Button(root, width = 20 , height = 2, text = "SCISSOR", bg = "#e5051b", fg = "white",command = lambda:choice("scissor")).grid(row=2, column=2)
paper = Button(root, width = 20 , height = 2, text = "PAPER", bg = "green", fg = "white", command = lambda:choice("paper")).grid(row=2, column=3)
root.mainloop()
