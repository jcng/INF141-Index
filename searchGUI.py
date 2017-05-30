from Tkinter import *

class searchGUI:
    def __init__(self, master):
        '''
        Creates the Search button and entry field elements
            -Perform search functions in search()
                -Currently just prints the query
            -self.query.get() is the text input
        '''
        frame = Frame(master)
        frame.pack()
        
        self.search = Button(frame,
                             text="Search",
                             command = self.search)
        self.search.pack(side=LEFT, padx=10, pady=10)

        self.query = Entry(frame)
        self.query.pack(side=LEFT, padx=10, pady=10)

        self.results = Text(frame, height=15, width = 50)
        self.results.pack()

    def search(self):
        resultsString = """
This is a multi line string
You can print
Whatever you want
        """
        self.results.insert(END, resultsString)

root = Tk()
application = searchGUI(root)
root.mainloop()
