from tkinter import Button, Frame, Label, Menu, Tk 
import webbrowser
from tkinter import messagebox


root = Tk()
root["bg"]="teal"


def openweb(): 
    webbrowser.open("https://www.google.com")
     
def openpen():
    webbrowser.open("https://kidmons.com/game/paint-online/")

def opennote():
    webbrowser.open("https://www.rapidtables.com/tools/notepad.html")

def opengp():
    webbrowser.open("https://www.cartoonnetworkhq.com/games")

def openmeet1():
    webbrowser.open("https://workspace.google.com/signup/businessstarter/welcome?hl=en-IN")

def openmeet2():
    webbrowser.open("https://zoom.us/join")

def openplay():
    webbrowser.open("https://wynk.in/music")

def openwa():
    webbrowser.open("https://web.whatsapp.com/")

def opentube():
    webbrowser.open("https://www.youtube.com/")

def that():
    pass

def info():
    messagebox.showinfo("Coder :", "Eng. Moreshwar Mahale..!")

root.attributes("-fullscreen", True)


class Header(): 

    l1 = Label(root, text="Kid-Destop-0.1", bg="lavender", fg="maroon", font="Times 15 italic bold" ,width='100', height='1').pack()

    f1 = Frame(root, width="1500", height="20", bg="snow").place(x = "0", y = "50")

    f3 = Frame(root,width="40", height="700", bg="snow").place(x="0", y="70") 
    
    f4 = Frame(root,width="40", height="700", bg="snow").place(x="1330", y="70") 


class Middle():

      b1 = Button(root, text="Chrome", bg ="darkorange", width="15", height="10", bd="3px",activebackground="cyan" ,command=openweb).place(x= "200" , y="200")

      b2 = Button(root, text="Notepad", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=opennote).place(x= "400" , y="200")
    
      b3 = Button(root ,text="Pant", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=openpen).place(x= "600" , y="200")    
    
      b4 = Button(root ,text="Games", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=opengp).place(x= "800" , y="200")    
      
      b5 = Button(root ,text="Google Meet", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=openmeet1).place(x= "1000" , y="200")    
     
      b6 = Button(root ,text="Zoom Meet", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=openmeet2).place(x= "300" , y="400")   
    
      b7 = Button(root ,text=" Moru-play", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=openplay).place(x= "500" , y="400")   
      
      b8 = Button(root ,text=" WhatsApp-Web", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=openwa).place(x= "700" , y="400")   
             
      b9 = Button(root ,text=" Youtube", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=opentube).place(x= "900" , y="400")   
      



class Footer():    
    
     f2 = Frame(root, width="1500", height="55", bg="snow").place(x = "0", y = "725")
     
     b10 = Button(root, text="Start", bg="crimson", font="Times 13 italic bold" ,bd="4px", activebackground="cyan", command=that).place(x="5", y="735")
     
     b11 = Button(root, text="Shut down", bg="crimson", font="Times 13 italic bold" ,bd="4px",activebackground="cyan" ,command=root.quit).place(x="1230", y="730")
   
     b12 = Button(root, text="Programer :", bg="crimson", font="Times 13 italic bold" ,bd="4px",activebackground="cyan" ,command=info).place(x="1100", y="730")
   
     

Middle()

Footer()

Header()

root.mainloop()