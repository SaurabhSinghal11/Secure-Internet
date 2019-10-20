#import Signup
#from SecureInternet import SI
from pymysql import *
from tkinter import *
from PIL import ImageTk



db=connect("localhost","root","Himanshu","SecureInternet")
cursor=db.cursor()

class PWB:
            def __init__(self,root):
                self.root=root
                self.root.title("PWB")
                self.root.geometry("1350x700+0+0")
                #for images.....................
                self.bg_icon=ImageTk.PhotoImage(file=r"C:\Users\himan\.spyder-py3\Secure Internet\security-background.jpg")
                #variables for entry.............
                self.e1=StringVar()
                self.no=StringVar()
                self.i=2
                bg_lb1 = Label(self.root, image=self.bg_icon)
                bg_lb1.place(x=0, y=0, relwidth=1, relheight=1)

                #login frame......................
                PWB_Frame=Frame(self.root,bg="white")

                PWB_Frame.place(x=500,y=100,)
                title = Label(PWB_Frame, text="Secure Internet", font=("Industry Inc Detail Fill", 40, "bold"),bg="white", fg="gray", bd=0, relief=GROOVE)
                title.grid(row=0,columnspan=2)
                labeladd=Label(PWB_Frame,text="Add Websites:-",font=("Industry Inc Detail Fill",20,"bold"),bg="white")
                labeladd.grid(row=1,column=0,padx=20,pady=10)
                e2=Entry(PWB_Frame, bd=5,textvariable=self.e1, relief=GROOVE, font=("", 15)).grid(row=2, column=0)
                btn=Button(PWB_Frame,command=self.add, text="+",compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"), bg="skyblue", fg="white").grid(row=2,column=1,padx=0)
                lb=Label(PWB_Frame,text="Click + to add this website",font=("Industry Inc Detail Fill",12),bg="white").grid(row=3,column=0,pady=5)
                lb=Label(PWB_Frame,text="Websites you want to block are:-",font=("Industry Inc Detail Fill",12),bg="white").grid(row=4,column=0,pady=5)
                self.listbox=Listbox(PWB_Frame,borderwidth=2, highlightthickness=0,width=50)
                self.listbox.insert(1,"Sno.      |           Website Name          ")
                self.listbox.grid(row=5,column=0,pady=10)
                btn2=Button(PWB_Frame,command=self.start, text="Start",compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"), bg="skyblue", fg="white").grid(row=6,column=0,padx=10,pady=10)
                

            def add(self):
                sql = "INSERT INTO WEBSITES(wname) VALUES('%s')" %(self.e1.get())
                cursor.execute(sql)
                db.commit()
                self.listbox.insert(self.i,str((self.i)-1)+"      |           "+self.e1.get())
                (self.i)+=1
                self.e1.set("")
                 

            def start(self):
                pass
if __name__=="__main__":
    root = Tk()
    obj = PWB(root)
    root.mainloop()



