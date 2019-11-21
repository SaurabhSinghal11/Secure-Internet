# Run this script as root 
from pymysql import *

db=connect("localhost","root","Himanshu","SecureInternet")
cursor=db.cursor() 

# change hosts path according to your OS 
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# localhost's IP 
redirect = "127.0.0.1"

class Blocker:
    def blocker(self,var):
        # websites That you want to block 
        self.sql="SELECT wname FROM WEBSITES"
        cursor.execute(self.sql)
        self.website_list =list(cursor.fetchall())
        for i in range(len(self.website_list)):
            self.website_list[i]=self.website_list[i][0]
        if var:
            with open(hosts_path, 'r+') as file: 
                self.content = file.read() 
                for self.website in self.website_list: 
                    if self.website in self.content: 
                        pass    
                    else: 
					# mapping hostnames to your localhost IP address 
                        file.write(redirect + " " + self.website + "\n")
        else:
            with open(hosts_path, 'r+') as file: 
                self.content=file.readlines() 
                file.seek(0)
                for self.line in self.content: 
                    if not any(self.website in self.line for self.website in self.website_list): 
                        file.write(self.line) 
                # removing hostnmes from host file 
                file.truncate()  
