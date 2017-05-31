from tkinter import *
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
        
        frame = Frame(master)
        frame.pack()
        
        
        self.search = Button(frame,
                             text="Search",
                             command = self.search)
        self.search.pack(side=TOP, padx=10, pady=10)

        self.query = Entry(frame)
        self.query.pack(side=TOP, padx=10, pady=10)


        self.scrollbar = Scrollbar(frame)
        self.scrollbar.pack(side=LEFT, fill=Y)

        self.listbox = Listbox(frame, height=15, width = 4, yscrollcommand=self.scrollbar.set)
        for i in range(1,100):
            self.listbox.insert(END, str(i))
        self.listbox.pack(side=LEFT, fill=Y)
        
        self.results = Text(frame, height=15, width = 150)
        self.results.pack(side=RIGHT)




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

