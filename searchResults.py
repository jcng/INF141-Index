class searchResults:
    def __init__(self,Index,k,query_str):
        self.query_str=query_str
        self.index=Index.index
        self.k=k
        self.results={}
        self.search()
        
    def search(self):
        query_list=self.query_str.split()
        for word in query_list:
            try:
                for item in self.index[word.strip().lower()]:
                    if item not in self.results:
                        self.results[item]=self.index[word.strip().lower()][item].tfidf
                    else:
                        self.results[item]=self.results[item]+self.index[word.strip().lower()][item].tfidf
            except:
                pass
        
        self.results=sorted([(self.results[item],item) for item in self.results],reverse=True)[:self.k]