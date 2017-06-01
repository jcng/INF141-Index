try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from index import Index
from urls import URLS
from collections import namedtuple
from searchResults import searchResults

class searchGUI:
    def __init__(self, master,Index,urls):
        '''
        Creates the Search button and entry field elements
            -Perform search functions in search()
                -Currently just prints the query
            -self.query.get() is the text input
        '''
        self.Index=Index
        self.urls=urls
        master.minsize(width=800, height=400)
        
        
        
        self.search = Button(master,
                             text="Search",
                             command = self.search)
        self.search.grid(row=1, column=2, sticky=W)

        self.query = Entry(master)
        self.query.grid(row=2, column=2, sticky=N)

        self.scrollbar = Scrollbar(master)
        self.scrollbar.grid(row=2, column=0, sticky=(N+S))

        self.listbox = Listbox(master, height=15, width = 4, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        for i in range(1,100):
            self.listbox.insert(END, str(i))
        self.listbox.grid(row=2, column=1)
        
        self.results = Text(master, height=15, width = 150)
        self.results.grid(row=2, column=3)

        self.scrollTitle = Label(master, text="# Results")
        self.scrollTitle.grid(row=1, column=0, columnspan=2)

        self.scrollTitle = Label(master, text="ICS Search Engine", font=("Calibri", 24))
        self.scrollTitle.grid(row=0, column=0, columnspan=4)



    def search(self):
        self.results.delete(1.0,END)
        print(self.query.get())
        print(len(self.listbox.curselection()))
        if len(self.listbox.curselection())==0:
            num=1
        else:
            num=self.listbox.curselection()[0]+1
        results = searchResults(self.Index,num,self.query.get()).results
        resultsString=""
        for item in results:
            resultsString+=self.urls[item[1]]+'\n'
        self.results.insert(END, resultsString)
