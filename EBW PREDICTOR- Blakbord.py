import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
window = Tk()

#--------window--------#

window.title("EBW Predictor")
window.wm_iconbitmap("radiat.ico")
window.geometry("1920x1080")
#window.resizable(0,0)
window.configure(bg="#222")

#--------Frames---------#

frame1 = Frame(window,background="#222")
frame1.pack()

frame2 = Frame(window,bg="#222")
frame2.pack()

frame3 = Frame(window,bg="#222")
frame3.pack()

frame4 = Frame(window,bg="#222")
frame4.pack()


#---------Image(f1)----------#
   
c1 = Canvas(frame1,width=260,height=150,bg="#222",borderwidth=-2)
c1.grid(row=1,column=0)
image1 = PhotoImage(file='logo1.png')    #-----ISRO logo
c1.create_image(40,0, image=image1, anchor=NW)
#----------------------------------------------------#
c2=Canvas(frame1,width=280,height=150,bg="#222",borderwidth=-2)
c2.grid(row=1,column=2)
image2 = PhotoImage(file='logo2.png')  #-------LPSC logo
c2.create_image(40,0, image=image2, anchor=NW)
#----------------------------------------------------#
c3=Canvas(frame1,width=500,height=150,bg="#222",borderwidth=-2)
c3.grid(row=1,column=1)
image3 = PhotoImage(file='image.gif') #---------LPSC Image
c3.create_image(60,0, image=image3, anchor=NW)

      
#--------- Titles (f1)------#

headline = Label(frame1,text="NANE OF YOUR ORGANISATION", font=("Calibri",32,"bold"), fg="#67f",bg="#222")
headline.grid(row=0,column=0,columnspan=3,padx=10, pady=10)

headline = Label(frame1,text="NAME OF YOUR CENTRE \n BENGALURU", font=("Calibri",25,"bold"),fg="#2bf",bg="#222")
headline.grid(row=2,column=0,columnspan=3,padx=10, pady=3)

title = Label(frame2,text="ELECTRON BEAM PREDICTOR", font=("Verdana",18,"bold"),fg="#f11",bg="#222")
title.grid(row=0,column=1,padx=10, pady=10)

#-----------user label (f3)---------#

line1 = Label(frame3, text="    Machine Name :",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line1.grid(row=0,column=0) 
line2 = Label(frame3, text=" Component Name :",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line2.grid(row=1,column=0)
line3 = Label(frame3, text="   Material Name :",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line3.grid(row=2,column=0)
line4 = Label(frame3, text="   Joint Diameter :",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line4.grid(row=3,column=0)              
line4_u = Label(frame3, text=" mm",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line4_u.grid(row=3,column=3)
line5 = Label(frame3, text="      Joint Depth :",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line5.grid(row=4,column=0)
line5_u = Label(frame3, text=" mm",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line5_u.grid(row=4,column=3)
line6 = Label(frame3, text="            Backup :",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line6.grid(row=5,column=0)
line6_u = Label(frame3, text=" mm",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line6_u.grid(row=5,column=3)
line7 = Label(frame3, text="            GTWD :",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line7.grid(row=6,column=0)
line7_u = Label(frame3, text=" mm",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line7_u.grid(row=6,column=3)
line8 = Label(frame3, text="          Max DOP : ",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line8.grid(row=7,column=0)
line8_u = Label(frame3, text=" mm",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line8_u.grid(row=7,column=3)
line9 = Label(frame3, text="          Min DOP :",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line9.grid(row=8,column=0)
line9_u = Label(frame3, text=" mm",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222")
line9_u.grid(row=8,column=3)

#---------input (f3)----------#

list1 = ["Select"," TM 1M3","CVE 1ft3","SST 35M3"]
list2 = ["Select","IPR-BODY TO BODY CAP","FILTER-FLANG TO COVER","BPLV-INLET TUBE TO FILTER"]
list3 = ["Select","SS304L","SS ALLOY","INCONEL","TITANIUM"]

comb1 = ttk.Combobox(frame3,font=("Adobe Garamond Pro",15), value=list1,width=29,cursor="hand2")
comb1.grid(row=0,column=1)
comb2 = ttk.Combobox(frame3,font=("Adobe Garamond Pro",15),value=list2, width=29)
comb2.grid(row=1,column=1)
comb3 = ttk.Combobox(frame3,font=("Adobe Garamond Pro",15), value=list3, width=29)
comb3.grid(row=2,column=1)
comb1.current(0)
comb2.current(0)
comb3.current(0)

#------------------------------------------------------------------#

entry1 = Entry(frame3,font=("Adobe Garamond Pro",15), bd=3, width=30,fg="#111",bg="#ddd")
entry1.grid(row=3,column=1)
entry2 = Entry(frame3,font=("Adobe Garamond Pro",15), bd=3, width=30,fg="#111",bg="#ddd")
entry2.grid(row=4,column=1)
entry3 = Entry(frame3,font=("Adobe Garamond Pro",15), bd=3, width=30,fg="#111",bg="#ddd")
entry3.grid(row=5,column=1)
entry4 = Entry(frame3,font=("Adobe Garamond Pro",15), bd=3, width=30,fg="#111",bg="#ddd")
entry4.grid(row=6,column=1)
entry5 = Entry(frame3,font=("Adobe Garamond Pro",15), bd=3, width=30,fg="#111",bg="#ddd")
entry5.grid(row=7,column=1)
entry6 = Entry(frame3,font=("Adobe Garamond Pro",15), bd=3, width=30,fg="#111",bg="#ddd")
entry6.grid(row=8,column=1)

#------------Function-------------------#

def calculation():
     
    
    mach_name = comb1.get()
    comp_name = comb2.get()
    mate_name = comb3.get()
	
    jdia = entry1.get()
    jdpt = entry2.get()
    jbck = entry3.get()
    jgtwd = entry4.get()	
    xdop = entry5.get()
    ndop = entry6.get()
    
    
    print(mach_name)
    print(comp_name)
    print(mate_name)
    print(jdia)
    print(jdpt)
    print(jbck,jgtwd,xdop,ndop )
    
 #--------------------------------message-----------------#
    
    if mach_name == "Select":
        messagebox.showinfo("Alart !!!","Please Select Machine Name.")
    elif comp_name == "Select":
        messagebox.showinfo("Alart !!!","Please Select Component Name.")
    elif mate_name == "Select":
        messagebox.showinfo("Alart !!!","Please Select Material Name.")
    elif jdia == "":
        messagebox.showinfo("Alart !!!","Please put Joint Diameter.")
    elif jdpt == "":
        messagebox.showinfo("Alart !!!","Please put Joint Depth value.")
    elif jbck == "":
        messagebox.showinfo("Alart !!!","Please put Joint Backup value.")
    elif jgtwd == "":
        messagebox.showinfo("Alart !!!","Please put GTWD value.")
    elif xdop == "":
        messagebox.showinfo("Alart !!!","Please put Max DOP value.")
    elif ndop == "":
        messagebox.showinfo("Alart !!!","Please put Min DOP value.")
   # else:
      #  messagebox.showinfo("Successful !!!","Your Answer is Reddy...")
    
  #------------------------------------------------------------#  
  
    dia = float(jdia)
    dpt = float(jdpt)
    bkp = float(jbck)
    gtwd = float(jgtwd)
    dmax = float(xdop)
    dmin = float(ndop)
    print(dia,dpt,bkp,gtwd,dmax,dmin )
	
  #--------------------------Calculation section----------------#
     
    focus_current = eval("(dia+dpt)/bkp")            # Put the Formula
    print(f"Predicted Focus Current{focus_current} mA")  
    beam_current = eval("(dia+dpt)/bkp")             # put the formula
    print(f"Predicted Focus Current{beam_current} mA")  
    
    Label(frame4, text= "%2f" %(focus_current), font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222",width=15).grid(row=1, column=1)
    Label(frame4, text= "%2f" %(beam_current), font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222",width=15).grid(row=2, column=1)
   
       
#------------Button-------------#
    
button = Button(frame4,text="Predict",font=("Emmett",16,"bold"),fg="firebrick",bg="gold",
                cursor="hand2",width=10,height=1,bd=5,command=calculation)
button.grid(row=0,column=1)

#-----------------------------------#
Label(frame4, text="Predicted Focus Current (mA) : ",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222").grid(row=1, column=0)
Label(frame4, text="Predicted Beam Current (mA) : ",font=("Comic Sans MS",16,"bold"),fg="#eee",bg="#222").grid(row=2, column=0)
#-----------------------------------#

window.mainloop()
