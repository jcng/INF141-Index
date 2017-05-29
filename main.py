from index import Index
from urls import URLS
from collections import namedtuple

def search(Index,k,query_str):
    result={}
    query_list=query_str.split()
    for word in query_list:
        try:
            for item in Index.index[word.strip().lower()]:
                if item not in result:
                    result[item]=Index.index[word.strip().lower()][item].tfidf
                else:
                    result[item]=result[item]+Index.index[word.strip().lower()][item].tfidf
        except:
            pass
    
    return sorted([(result[item],item) for item in result],reverse=True)[:k]

    
if __name__ == "__main__":
    a=Index('WEBPAGES_CLEAN')
    b=URLS('WEBPAGES_CLEAN/bookkeeping.json')
    
    while(True):
        query=input("Search: ")
        if query=='q':
            break
        s=search(a,10,query)
        for item in s:
            print(b.urls[item[1]])

