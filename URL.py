from pywinauto import Application
from time import sleep
class URL:
    def giveurl(self):
        try:
            self.app = Application(backend='uia')
            self.app.connect(title_re=".*Chrome.*")
            self.dlg = self.app.top_window()
            self.obj = self.dlg.child_window(title="Address and search bar", control_type="Edit")
            self.url=self.obj.get_value()
        except Exception:
            return ''
        return str(self.url)