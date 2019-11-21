from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from PWB import PWB
from CWB import CWB

class SI:
    def __init__(self,root):
        self.root=root

        self.root.title("Secure Internet")
        self.root.geometry("1350x700+0+0")
        self.bg_icon=ImageTk.PhotoImage(file=r"C:\Users\himan\.spyder-py3\Secure Internet\security-background.jpg")
        bg_lb1 = Label(self.root, image=self.bg_icon)
        bg_lb1.place(x=0, y=0, relwidth=1, relheight=1)
        SI_Frame=Frame(self.root,bg="steel blue")
        SI_Frame.place(x=330,y=150,)
        title = Label(SI_Frame, text="Welcome to Secure Internet", font=("Industry Inc Detail Fill", 40, "bold"),\
                      bg="steel blue", fg="light cyan", bd=0, relief=GROOVE)
        title.grid(row=0,columnspan=2)
        l2=Label(SI_Frame,text="Basis of Website Filtering", font=("Industry Inc Detail Fill", 18, "bold") \
        ,bg="steel blue", fg="light cyan", bd=0, relief=GROOVE,width=50)
        l2.grid(row=1,column=0)
        self.v = IntVar()
        r1=Radiobutton(SI_Frame, text='Particular Websites', variable=self.v, value=1,bg="steel blue",font=("bold",16))
        r1.grid(row=2,column=0,padx=20,pady=30)
        r2=Radiobutton(SI_Frame, text='Categories', variable=self.v, value=2,bg="steel blue",font=("bold",16))
        r2.grid(row=3,column=0)
        b1=Button(SI_Frame,text="Proceed",fg="white",bg="blue",font="bold",command=self.button)
        b1.grid(row=4,column=0,padx=20,pady=10)
    def button(self):
        if self.v.get()==1:
            self.root.withdraw()
            self.pwb=Toplevel()
            ob=PWB(self.pwb)
        elif self.v.get()==2:
            self.root.withdraw()
            self.cwb=Toplevel()
            ob=CWB(self.cwb)
        else:
            messagebox.showerror("ERROR",'Please select any of these')
if __name__=="__main__":
    root = Tk()
    obj = SI(root)
    root.mainloop()