from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font


from menu import Menu

def main():
    root = Tk()
    app = MainWindow(root)
    
    # Create name label and position it in the bottom right corner
    name_label = Label(root, text="FaAuAl", font="Helvetica 10",bg="#EEC900", fg="black")
    name_label.pack(side=BOTTOM, anchor=SE)
    
    root.mainloop()

#MAIN WINDOW FOR LOG IN    
class MainWindow:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x500+0+0")
        self.master.config(bg="#FFD700")
        self.frame = Frame(self.master,bg="#FFD700")
        self.frame.pack()

       
        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame,text = "HOSPITAL MANAGEMENT SYSTEM", font="Helvetica 20 bold",bg="#EEC900",fg="black")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=40)
        #======================
        self.LoginFrame1 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#FFC125",bd=20)
        self.LoginFrame1.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#FFC125",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #======LABEL AND ENTRY=========
        self.lblUsername = Label(self.LoginFrame1,text="Username",font="Helvetica 14 bold",bg="#FFC125",bd=22)
        self.lblUsername.grid(row=0,column=0)
        self.lblUsername = Entry(self.LoginFrame1,font="Helvetica 14 bold",textvariable= self.Username,bd=2)
        self.lblUsername.grid(row=0,column=1)
        self.lblPassword = Label(self.LoginFrame1,text="Password ",font="Helvetica 14 bold",bg="#FFC125",bd=22)
        self.lblPassword .grid(row=1,column=0)
        self.lblPassword  = Entry(self.LoginFrame1,font="Helvetica 14 bold",show="*",textvariable= self.Password,bd=2)
        self.lblPassword .grid(row=1,column=1)
        #===========BUTTONS====
        self.btnLogin = Button(self.LoginFrame2,text = "Login" ,font="Helvetica 10 bold", width =10 ,bg="#FFD700",command = self.Login_system)       
        self.btnLogin.grid(row=3,column=0)
        self.btnExit = Button(self.LoginFrame2,text = "Exit" ,font="Helvetica 10 bold", width =10 ,bg="#FFD700",command = self.Exit)       
        self.btnExit.grid(row=3,column=1)

        
               
        self.attempts = 0
        
    def Login_system(self):
       
        S1=(self.Username.get())
        S2=(self.Password.get())
        i=0
        if(S1=='admin' and S2=='1234'):
            self.newWindow = Toplevel(self.master)
            self.app = Menu(self.newWindow)
        elif(S1=='root' and S2=='4321'):
            self.newWindow = Toplevel(self.master)
            self.app = Menu(self.newWindow)
        else:
            #tkinter.messagebox.askretrycancel("HOSPITAL MANAGEMENT SYSTEM" , "PLEASE ENTER VALID USERNAME AND PASSWORD")
            self.attempts += 1
            if self.attempts >= 3:
                tkinter.messagebox.showerror("Login Error", "You have exceeded the maximum number of login attempts.")
                self.master.destroy()
            else:
                tkinter.messagebox.showerror("Login Error", "Invalid username or password. Please try again.")
            
            
    def Exit(self):
        self.master.destroy()
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = self.Menu(self.newWindow)

     
    
if __name__ == "__main__":
    main()


























