import requests 
from bs4 import BeautifulSoup 
class BSOUP:
    def keyword(self,URL):
        try:
            self.r = requests.get(URL)
        except Exception:
            return []
        self.soup = BeautifulSoup(self.r.content, 'html5lib') 
        self.c=str(self.soup.find(attrs={"name":"keywords"}))
        self.c=self.c[15:-19]
        self.c=self.c.replace(" ","")
        return self.c.split(",")