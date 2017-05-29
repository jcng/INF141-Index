class URLS:
    def __init__(self,file):
        self.urls={}
        self.buildURLS(file)
        
        
    def buildURLS(self,file):
        file_object = open(file, encoding="utf8")
        for line in file_object:
            temp=line.strip().split('"')
            if len(temp)>1:
                self.urls[temp[1]]=temp[3] 