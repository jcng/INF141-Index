from tkinter import *
from index import Index
from urls import URLS
from collections import namedtuple
from searchGUI import searchGUI

    
if __name__ == "__main__":
    a=Index('WEBPAGES_CLEAN')
    b=URLS('WEBPAGES_CLEAN/bookkeeping.json')
    root = Tk()
    application = searchGUI(root,a,b.urls)
    root.mainloop()
