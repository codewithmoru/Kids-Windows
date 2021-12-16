from os import read, terminal_size
from tkinter import Button, Frame, Label, Tk
from tkinter.constants import BOTTOM, CENTER, FALSE, LEFT, RIGHT, TOP 
from tkinter import messagebox
from typing import MappingView
import webbrowser
from tkinter.filedialog import askopenfile

root = Tk()
root["bg"]="teal"
root.attributes("-fullscreen", True)

def openpc():
    file = [("All File", "* *")]
    file = askopenfile(filetypes = file, defaultextension = file) 


def openweb(): 
    webbrowser.open("https://www.google.com", "_self")
     
def openpen():
    webbrowser.open("https://kidmons.com/game/paint-online/","_self")

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

def opencal():
    webbrowser.open("https://www.desmos.com/scientific")

def openppt():
    webbrowser.open("https://office.live.com/start/powerpoint.aspx")

def opengita():
    webbrowser.open("https://bhaktivedantavediclibrary.org/books/bhagavad-gita/")

def openfun():
    webbrowser.open("https://www.boomerangtv.co.uk/games")

def openzone():
    webbrowser.open("https://nces.ed.gov/nceskids/index.asp")

def openshop():
    webbrowser.open("https://www.amazon.in/kids-clothing/b?ie=UTF8&node=4091091031")

def opencorner():
    webbrowser.open("https://kidscorner.net/")

def openbook():
    webbrowser.open("http://www.kidscornerbookshop.com")

def openedu():
    webbrowser.open("https://www.education.com/worksheets")        

def openchart():
    webbrowser.open("https://www.pinterest.com.au/guruparents/educational-charts/")
    
def opencart():
    webbrowser.open("https://www.cartoonnetworkhq.com/videos")    

def openlern():
    webbrowser.open("https://www.e-learningforkids.org/")

def info():
    messagebox.showinfo("Coder :", "Eng. Moreshwar Mahale..!")

def openhelp():
    messagebox.showwarning("Help", "\t\t * hallo Myself Moreshwar Mahale \n\n\t *This destop very easy to handle & run \n\n\t * Hear all of the tabs are open in your webbrowser \n\n\t * You does not install any other apps in thar destop \n\n\t * If you have any qury then fill feedback form  \n\n\n\t *Enjoy the destop")

def openfb():
    webbrowser.open("https://feedbackdekstop.wordpress.com/")

def createNewWindow():

    newWindow = (root)
    
    top= Tk()
    top.geometry("250x500+0+180")
    top.resizable(width=FALSE, height=FALSE) 
   
    l = Label(top ,text=" Powerdby : Eng.Moreshwar Mahale", bg ="pink").pack(side = BOTTOM, fill="x")
    

    l1 = Label(top, text="Kid-Destop-0.1", bg="black", fg="tan").pack(fill="x")
   
    b1 = Button(top, text="Chrome", bg ="darkorange", bd="3px",activebackground="cyan" , relief= "groove" ,command=openweb).pack(side = TOP, fill="x")

    b2 = Button(top, text="Notepad", bg ="darkorange", bd="3px",activebackground="cyan" , relief= "groove",command=opennote).pack(side = TOP, fill="x")
    
    b3 = Button(top ,text="Pant", bg ="darkorange", bd="3px",activebackground="cyan" , relief= "groove",command=openpen).pack(side = TOP, fill="x") 
    
    b4 = Button(top ,text="Games", bg ="darkorange", bd="3px",activebackground="cyan", relief= "groove" ,command=opengp).pack(side = TOP, fill="x")   
      
    b5 = Button(top ,text="Google Meet", bg ="darkorange", bd="3px",activebackground="cyan", relief= "groove" ,command=openmeet1).pack(side = TOP, fill="x")   
     
    b6 = Button(top ,text="Zoom Meet", bg ="darkorange", bd="3px",activebackground="cyan" , relief= "groove",command=openmeet2).pack(side = TOP, fill="x")
    
    b7 = Button(top ,text=" Moru-play", bg ="darkorange", bd="3px",activebackground="cyan" , relief= "groove",command=openplay).pack(side = TOP, fill="x")  
      
    b8 = Button(top ,text=" WhatsApp-Web", bg ="darkorange", bd="3px",activebackground="cyan" , relief= "groove",command=openwa).pack(side = TOP, fill="x")   
             
    b9 = Button(top ,text=" Youtube", bg ="darkorange", bd="3px",activebackground="cyan" , relief= "groove",command=opentube).pack(side = TOP, fill="x")
    
    b10 = Button(top ,text=" Calculator", bg ="darkorange", bd="3px",activebackground="cyan" , relief= "groove",command=opencal).pack(side = TOP, fill="x")
     
    b11 = Button(top ,text=" PowerPoint", bg ="darkorange", bd="3px",activebackground="cyan" , relief= "groove",command=openppt).pack(side = TOP, fill="x")
    
    b12 = Button(top ,text=" Bhagvat Gita", bg ="darkorange", bd="3px",activebackground="cyan" , relief= "groove",command=opengita).pack(side = TOP, fill="x")

    b13 = Button(top ,text=" Help", bg ="darkorange", bd="3px",activebackground="cyan" , relief= "groove",command=openhelp).place(x="40", y="420")

    b14 = Button(top ,text=" Feedback", bg ="darkorange", bd="3px",activebackground="cyan" , relief= "groove",command=openfb).place(x="150", y="420")


    


def createNewWindow2():

    newWindow = (root)
    
    pop= Tk()
    pop.geometry("350x500+100+180")
    pop.resizable(width=FALSE, height=FALSE) 

    l = Label(pop ,text=" Powerdby : Eng.Moreshwar Mahale", bg ="pink").pack(side = BOTTOM, fill="x")

    b1 = Button(pop, text="Kids Pc", bg="pink", width="13", height="12", activebackground="blue" ,command=openpc).place(x="25", y="28")
   
    b2 = Button(pop, text="Kids Fun", bg="pink", width="20", height="3", activebackground="blue" ,command=openfun).place(x="150", y="25")
   
    b3 = Button(pop, text="Kids Zone", bg="pink", width="20", height="3", activebackground="blue" ,command=openzone).place(x="150", y="90")

    b4 = Button(pop, text="Kids Shop", bg="pink", width="20", height="3", activebackground="blue" ,command=openshop).place(x="150", y="160")

    b5 = Button(pop, text="Kids Cormer", bg="pink", width="20", height="3", activebackground="blue" ,command=opencorner).place(x="25", y="250")

    b6 = Button(pop, text="Kids Book Shop", bg="pink", width="20", height="3", activebackground="blue" ,command=openbook).place(x="25", y="325")

    b7 = Button(pop, text="Kids Edu", bg="pink", width="20", height="3", activebackground="blue" ,command=openedu).place(x="25", y="400")

    b8 = Button(pop, text="Kids Charts", bg="pink", width="20", height="3", activebackground="blue" ,command=openchart).place(x="180", y="250")

    b9 = Button(pop, text="Kids Cartoon", bg="pink", width="20", height="3", activebackground="blue" ,command=opencart).place(x="180", y="325")

    b10 = Button(pop, text="Kids Learn", bg="pink", width="20", height="3", activebackground="blue" ,command=openlern).place(x="180", y="400")

    f1 = Frame(pop, bg="red", width="600", height="10").pack(side=LEFT , fill="x")
   
   
    

class Header(): 

      l1 = Label(root, text="Kid-Destop-0.1", bg="lavender", fg="maroon", font="Times 15 italic bold" ,width='100', height='1').pack()

      f1 = Frame(root, width="1500", height="20", bg="snow").place(x = "0", y = "50")

      f3 = Frame(root,width="40", height="700", bg="snow").place(x="0", y="70") 
    
      f4 = Frame(root,width="40", height="700", bg="snow").place(x="1330", y="70") 


class Middle():

      b1 = Button(root, text="Chrome", bg ="darkorange", width="15", height="10", bd="3px",activebackground="cyan", command=openweb).place(x= "200" , y="150")

      b2 = Button(root, text="Notepad", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=opennote).place(x= "400" , y="150")
    
      b3 = Button(root ,text="Pant", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=openpen).place(x= "600" , y="150")    
    
      b4 = Button(root ,text="Games", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=opengp).place(x= "800" , y="150")    
      
      b5 = Button(root ,text="Google Meet", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=openmeet1).place(x= "1000" , y="150")    
     
      b6 = Button(root ,text="Zoom Meet", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=openmeet2).place(x= "300" , y="350")   
    
      b7 = Button(root ,text=" Moru-play", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=openplay).place(x= "500" , y="350")   
      
      b8 = Button(root ,text=" WhatsApp-Web", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=openwa).place(x= "700" , y="350")   
             
      b9 = Button(root ,text=" Youtube", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=opentube).place(x= "900" , y="350")   
            
      b10 = Button(root ,text=" Calculator", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=opencal).place(x= "400" , y="550")   

      b11 = Button(root ,text="Powerpoint ", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=openppt).place(x= "600" , y="550")   

      b12 = Button(root ,text="Bhagvat Gita", bg ="darkorange", width="15", height="10", bd="3px", activebackground="cyan" ,command=opengita).place(x= "800" , y="550")   



class Footer():    
    
      f4 = Frame(root, width="1500", height="55", bg="snow").place(x = "0", y = "725")
      
      b13 = Button(root, text="Start", bg="crimson", font="Times 13 italic bold" ,bd="4px", activebackground="cyan", command=createNewWindow).place(x="5", y="730")
           
      b14 = Button(root, text="Taks Bar", bg="crimson", font="Times 13 italic bold" ,bd="4px",activebackground="cyan",width="30" ,command=createNewWindow2).place(x="80", y="730")

      b15 = Button(root, text="Shut down", bg="crimson", font="Times 13 italic bold" ,bd="4px",activebackground="cyan" ,command=root.quit).place(x="1230", y="730")
      
      b16 = Button(root, text="!", bg="crimson", font="Times 13 italic bold" ,bd="4px",activebackground="cyan" , relief= "groove" ,command=info).place(x="1335", y="60")
   
      b17 = Button(root, text="1", bg="crimson", font="Times 13 italic bold" ,bd="4px",activebackground="cyan" ,command=openweb).place(x="500", y="730")
         
      b18 = Button(root, text="3", bg="crimson", font="Times 13 italic bold" ,bd="4px",activebackground="cyan" ,command=openpen).place(x="550", y="730")

      b19 = Button(root, text="4", bg="crimson", font="Times 13 italic bold" ,bd="4px",activebackground="cyan" ,command=opengp).place(x="600", y="730")
  
      b20 = Button(root, text="9", bg="crimson", font="Times 13 italic bold" ,bd="4px",activebackground="cyan", command=opentube).place(x="650", y="730")


Middle()
Footer()
Header()


root.mainloop()  
 
