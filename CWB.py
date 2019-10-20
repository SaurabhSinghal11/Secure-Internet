from pymysql import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

class CWB:
            def __init__(self,root):
                self.root=root
                self.root.title("CWB")
                self.root.geometry("1350x700+0+0")
                #for images.....................
                self.bg_icon=ImageTk.PhotoImage(file=r"C:\Users\himan\.spyder-py3\Secure Internet\security-background.jpg")

                bg_lb1 = Label(self.root, image=self.bg_icon)
                bg_lb1.place(x=0, y=0, relwidth=1, relheight=1)

                #login frame......................
                CWB_Frame=Frame(self.root,bg="white")

                CWB_Frame.place(x=500,y=100,)
                title = Label(CWB_Frame, text="Secure Internet", font=("Industry Inc Detail Fill", 40, "bold"),bg="white", fg="gray", bd=0, relief=GROOVE)
                title.grid(row=0,columnspan=2,padx=20)
                labeladd=Label(CWB_Frame,text="Select Categories:-",font=("Industry Inc Detail Fill",20,"bold"),bg="white")
                labeladd.grid(row=1,column=0,padx=20,pady=10,sticky=W)
                self.var1=IntVar()
                c1=Checkbutton(CWB_Frame,text="Games",variable=self.var1, font=("Industry Inc Detail Fill", 20, "bold"),bg="white").grid(row=2,column=0,padx=10,pady=(20,10),sticky=W)
                self.var2=IntVar()
                c2=Checkbutton(CWB_Frame,text="Movies",variable=self.var2, font=("Industry Inc Detail Fill", 20, "bold"),bg="white").grid(row=3,column=0,padx=10,pady=(10,10),sticky=W)
                self.var3=IntVar()
                c3=Checkbutton(CWB_Frame,text="Social Media",variable=self.var3, font=("Industry Inc Detail Fill", 20, "bold"),bg="white").grid(row=4,column=0,padx=10,pady=(10,10),sticky=W)
                btn2=Button(CWB_Frame,command=self.start, text="Start",compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"), bg="skyblue", fg="white").grid(row=5,column=0,padx=10,pady=10)
                 

            def start(self):
                pass
if __name__=="__main__":
    root = Tk()
    obj = CWB(root)
    root.mainloop()



