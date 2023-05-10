#importing the required libraby containing functions to help out with the making of a calendar
from tkinter import *
import calendar
#function to display the calendar
def dispcal():
 newRoot = Tk()
#Tk initialises the toolkit us of the Tkinter library
#Newroot controls the event loop of displays and to make it run lag free
#this is the setting up of the calendar screen by adjusting various configurations and features of the screen
 newRoot.title('Calendar Screen')
 newRoot.config(bg='light blue')
 newRoot.geometry('700x700')
 actualyear=int(yearEntry.get())
 Calendarcontent=calendar.calendar(actualyear)
 lbNew = Label(newRoot,text=Calendarcontent,font='Consolas 10 bold')
 lbNew.grid(row=0,column=0,padx=30,pady=30)
 newRoot.mainloop()
#definiton of the function performing the task the leap year check and provide the demanded output to the user and also set up of the screen cnfiguration on which the desired output is to be shown
def checkcal():
  oldroot=Tk()
  oldroot.title('Check Result')
  oldroot.config(bg='light blue')
  oldroot.geometry('400x400')
  #input command for taking the required year as provided by the user on which the check is to be performed on
  leapcheck=float(entyear.get())
  #condition to check whether the input year is a leap year or not 
  if (((leapcheck%4==0) and (leapcheck%100!=0)) or (leapcheck%400==0)):
    header = Label(oldroot, text='The year is a leap year', bg='light green',fg='brown', 
    font='times,32,bold')
    header.grid(row=7, column=10, padx=25)
  else:
   header = Label(oldroot, text='The year is not a leap year', bg='red',fg='white', 
   font='times,32,bold')
   header.grid(row=7, column=10, padx=25)
  exitButton = Button(oldroot,text='Exit',fg='red',command=oldroot.destroy)
  exitButton.grid(row=14, column=10,padx=25,pady=15)
  oldroot.mainloop()
#defining the features of the home control screen which is to be operated by the user according to his/her wish
#the features of the home control screen consists of colour, geometry,fonts,button setup and their respective functions
root=Tk()
root.config(bg='deep sky blue')
root.title('Calendar App')
root.geometry('400x400')

header = Label(root, text='CALENDAR', bg='light pink',fg='brown', font='times,32,bold')
header.grid(row=1, column=0, padx=25)

yearEntry = Entry(root,width=5)
yearEntry.grid(row=2, column=0, padx=25, pady=10)

showcalendar = Button(root, text='Show Calendar' , fg='dark green',command=dispcal)
showcalendar.grid(row=3,column=0,padx=25)

exitButton = Button(root,text='Exit',fg='purple',command=root.destroy)
exitButton.grid(row=4 , column=0,padx=25)

header = Label(root, text='LEAP YEAR CHECK', bg='purple',fg='yellow', font='times,32,bold')
header.grid(row=9, column=0, padx=15,pady=20)

entyear = Entry(root,width=5)
entyear.grid(row=10,column=0,padx=25,pady=10)
check = Button(root, text='Check',fg='dark blue',command=checkcal)
check.grid(row=12,column=0,padx=25)
root.mainloop()
