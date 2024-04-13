from tkinter import *
import math
#Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MILLISECONDS = 20 #Change if you want to just see the program without waiting so long
reps = 1
checkCounter = ""
checkMarkText = "✓"
timer = None
#Resetting Timer

def resetTimer():
    window.after_cancel(timer)
    timerText.config(text="Timer", fg=GREEN)
    canvas.itemconfig(screenTimer,text="00:00")
    global reps
    reps = 1
    resetChecks()

#Timer Functionality
def startTimer():
    
    global reps
    if reps > 8:
        #reset (because user finished a full loop)
        reps = 1
        resetChecks()
    if reps == 8:
        #long break
        counting(LONG_BREAK_MIN * 60)
        timerText.config(text="Long Break", fg=GREEN)
        addCheck()
    elif (reps % 2) == 1:
        #working timer
        timerText.config(text="Work", fg=RED)
        counting(WORK_MIN * 60)
    elif (reps % 2) == 0:
        #break timer
        timerText.config(text="Short Break", fg=GREEN)
        counting(SHORT_BREAK_MIN * 60)
        addCheck()
        
def addCheck():
    global checkCounter
    checkCounter += checkMarkText
    checkMark.config(text=checkCounter)

def resetChecks():
    global checkCounter
    checkCounter = ""
    checkMark.config(text=checkCounter)


#clock/countdown
def counting(count):
    minutes = math.floor(count / 60)
    minutesTextForm = str(minutes)
    if minutes < 10:
        minutesTextForm = "0" + minutesTextForm
    
    seconds = count % 60
    secondsTextForm = str(seconds)
    if seconds < 10:
        secondsTextForm = "0" + secondsTextForm

    textFormTimer = minutesTextForm + ":" + secondsTextForm
    canvas.itemconfig(screenTimer, text=textFormTimer)


    if count >= 0:
        global timer
        timer = window.after(MILLISECONDS,counting,count - 1)
    else:
        global reps
        reps+=1
        startTimer()
        
#UI 
window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=50, bg=YELLOW)
canvas = Canvas(width=250,height=220, background=YELLOW, highlightthickness=0)
tomatoPhoto = PhotoImage(file="tomato.png")
canvas.create_image(125,110, image=tomatoPhoto)

screenTimer = canvas.create_text(125,125,text="00:00", font=(FONT_NAME, 28, "bold"), fill="white")
canvas.grid(column=1,row=1)

timerText = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
timerText.grid(column=1,row=0)

startButton = Button(text="Start",fg="Black",background=RED,font=(FONT_NAME, 14, "bold"), highlightthickness=0, command=startTimer, activebackground=RED)
startButton.grid(column=0,row=2)

resetButton = Button(text="Reset", fg="Black", background=RED,font=(FONT_NAME, 14, "bold"), highlightthickness=0, command=resetTimer, activebackground=RED)
resetButton.grid(column=2,row=2)

checkMark = Label(text="",fg=GREEN, background=YELLOW,font=(FONT_NAME,16,"bold"))
checkMark.grid(column=1,row=3)



window.mainloop()
