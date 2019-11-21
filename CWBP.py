from URL import URL
from BSOUP import BSOUP
from time import sleep
import re

# change hosts path according to your OS 
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# localhost's IP 
redirect = "127.0.0.1"
u=URL()
b=BSOUP()
urlis=[]
class CWBP:
    def cwblocker(self,lis):
        global urlis
        self.ur=u.giveurl()
        self.a=re.search('/',self.ur)
        self.kw=b.keyword("https://www."+self.ur)
        for i in lis:
            if i in self.kw:
                urlis.append("www."+self.ur[:self.a.start()])
                with open(hosts_path, 'r+') as file: 
                    self.content = file.read() 
                    if self.ur in self.content: 
                        pass    
                    else: 
			           # mapping hostnames to your localhost IP address 
                        file.write(redirect + " " +"www."+self.ur[:self.a.start()]+ "\n")
    def unblocker(self):
        global urlis
        with open(hosts_path, 'r+') as file: 
            self.content=file.readlines() 
            file.seek(0)
            for self.line in self.content: 
                if not any(self.cu in self.line for self.cu in urlis): 
                    file.write(self.line) 
        # removing hostnmes from host file 
            file.truncate()