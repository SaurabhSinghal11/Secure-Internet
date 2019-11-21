#import Signup
#from SecureInternet import SI
from pymysql import *
from tkinter import *
from PIL import ImageTk
from PWBP import Blocker



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
                bg_lb1 = Label(self.root, image=self.bg_icon)
                bg_lb1.place(x=0, y=0, relwidth=1, relheight=1)

                #login frame......................
                PWB_Frame=Frame(self.root,bg="white")

                PWB_Frame.place(x=500,y=50,)
                title = Label(PWB_Frame, text="Secure Internet", font=("Industry Inc Detail Fill", 40, "bold"),bg="white", fg="gray",\
                              bd=0, relief=GROOVE)
                title.grid(row=0,columnspan=2)
                labeladd=Label(PWB_Frame,text="Add Websites:-",font=("Industry Inc Detail Fill",20,"bold"),bg="white")
                labeladd.grid(row=1,column=0,padx=20,pady=10)
                e2=Entry(PWB_Frame, bd=5,textvariable=self.e1, relief=GROOVE, font=("", 15)).grid(row=2, column=0)
                btn=Button(PWB_Frame,command=self.add, text="+",compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"), bg="skyblue",\
                           fg="white").grid(row=2,column=1,padx=0)
                btn=Button(PWB_Frame,command=self.delete, text="-",compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"),\
                           bg="skyblue", fg="white").grid(row=2,column=2,padx=10)
                lb=Label(PWB_Frame,text="Write in the form www.example.com",font=("Industry Inc Detail Fill",12),bg="white")\
                    .grid(row=3,column=0,pady=2)
                lb=Label(PWB_Frame,text="Click + to add this website",font=("Industry Inc Detail Fill",12),bg="white")\
                    .grid(row=4,column=0,pady=2)
                lb=Label(PWB_Frame,text="Enter Sno. and Click - to delete",font=("Industry Inc Detail Fill",12),bg="white")\
                    .grid(row=5,column=0,pady=2)
                lb=Label(PWB_Frame,text="Websites you want to block are:-",font=("Industry Inc Detail Fill",12),bg="white")\
                    .grid(row=6,column=0,pady=2)
                self.listbox=Listbox(PWB_Frame,borderwidth=2, highlightthickness=0,width=50)
                self.listbox.insert(1,"Sno.      |           Website Name          ")
                self.listbox.grid(row=7,column=0,pady=10,padx=30)
                btn2=Button(PWB_Frame,command=self.start, text="Start",compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"),\
                            bg="skyblue", fg="white").grid(row=8,column=0,padx=10,pady=10)
                btn3=Button(PWB_Frame,command=self.stop,text="Stop",compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"),\
                            bg="skyblue", fg="white").grid(row=9,column=0,padx=10,pady=10)
                

            def add(self):
                self.listbox.delete(1,END)
                if self.e1.get()=='':
                    pass
                else:
                    sql = "INSERT INTO WEBSITES(wname) VALUES('%s')" %(self.e1.get())
                    cursor.execute(sql)
                    db.commit()
                self.sql2="SELECT wname FROM WEBSITES"
                cursor.execute(self.sql2)
                self.website_list =list(cursor.fetchall())
                for i in range(len(self.website_list)):
                    self.website_list[i]=self.website_list[i][0]
                for i in range(0,len(self.website_list)):
                    self.listbox.insert(i+2,str(i+1)+"      |           "+self.website_list[i])
                self.e1.set("")
            def delete(self):
                self.listbox.delete(1,END)
                if self.e1.get()=='':
                    pass
                else:
                    sql = "DELETE FROM WEBSITES where sno=%d" %(int(self.e1.get()))
                    cursor.execute(sql)
                    db.commit()
                self.sql2="SELECT * FROM WEBSITES"
                cursor.execute(self.sql2)
                self.sno=[]
                self.website_list =list(cursor.fetchall())
                for i in range(len(self.website_list)):
                    self.sno.append(self.website_list[i][0])
                    self.website_list[i]=self.website_list[i][1]
                for i in range(0,len(self.website_list)):
                    self.listbox.insert(i+2,self.sno[i]+"      |           "+self.website_list[i])
                self.e1.set("")
                 

            def start(self):
                b=Blocker()
                b.blocker(True)
            def stop(self):
                b=Blocker()
                b.blocker(False)
if __name__=="__main__":
    root = Tk()
    obj = PWB(root)
    root.mainloop()



