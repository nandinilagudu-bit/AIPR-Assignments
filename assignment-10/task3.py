class emp:
    def __init__(self,n,s):
        self.n=n
        self.s=s
    def inc(self,p):
        self.s=self.s+(self.s*p/100)
    def pr(self):
        print("emp:",self.n,"salary:",self.s) 


e = emp("nandini", 900000)   # creating object
e.pr()                    # display info
e.inc(10)                 # increase salary by 10%
e.pr()  