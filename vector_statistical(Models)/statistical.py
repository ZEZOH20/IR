import random
from flask import Flask,redirect,url_for,request,render_template 

app=Flask(__name__)


@app.route('/',methods=["POST","GET"])
def operations():
    #read Query
    if request.method=='POST':
        global query
        query={'A':-1,'B':-1,'C':-1,'D':-1,'E':-1,'F':-1}
        query_temp=str(request.form['query']).replace(':',' ').split(' ')
        value=' '
        i=0
        while(i<len(query_temp)):
            if(i%2==0):
                value=query_temp[i] 
            else:
                query[value]=query_temp[i]
            i+=1    
        #verify
        for i in list(query.keys()):
            if(query[i]==-1):
                return 'query syntaix are wrong'

        #printQ(query)
        return render_template("result.html",result=cDoc(query))
       

'''def printQ(query):
    for key,value in query.items():
        print(f'{key}:{value}')'''
doc={}        

def cDoc(query):
    for i in range(1,6):
        doc[f'doc{i}']=calcSumDocWeight(f'D{i}.txt',query)
    
    #print(doc,query)
    #print(doc)  

    return sortDoc(doc) 
        
def calcSumDocWeight(namef,query):

    #inRandom(namef) // Random ..............
    repeatD=repeat(namef)
    sum=0
    for char in ['A','B','C','D','E','F']:
        sum+=(repeatD[char]/fsize(repeatD))*float(query[char])
    
    print(repeatD)
    return sum
   
def inRandom(namef):
    key=['A','B','C','D','E','F']
    f=open(f'{namef}','w')
    content=random.choices(key,k=random.randint(1,151))
    for i in range(len(content)):
        f.write(str(content[i])+' ')
    f.close()

def repeat(namef):
    D={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
    f=open(namef,'r')
    content=str(f.readline()).split(' ')
    f.close()
    for i in content:
        if i!='':
            D[i]+=1
    return D        
        
def fsize(repeatD):
    size=0
    for char in ['A','B','C','D','E','F']:
        size+=repeatD[char]
    return size

def sortDoc(doc):
    import operator

    doc= sorted(doc.items(), key=operator.itemgetter(1),reverse=True) 
    sortdict=dict(doc)
    #print(doc)
    return sortdict


if __name__=='__main__':
    app.run()
