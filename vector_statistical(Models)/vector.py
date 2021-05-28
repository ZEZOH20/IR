import random
import math
from flask import Flask,redirect,url_for,request,render_template 

app=Flask(__name__)


@app.route('/',methods=["POST","GET"])
def operations():
    #read Query
    if request.method=='POST':
        global query
        query=[]
        query=str(request.form['query']).split(' ')
   
        return '%s'%calcSumDocWeight(query)

doc={}
tf=[] 
idf=[]       
def calcSumDocWeight(query):
    for i in range(1,6):
        tf.append(TF(f'D{i}.txt'))
    
    idf=IDF(i+1)   #Idf on Document level 
    j=1
    for List in tf:
        tf_idf=[]
        i=0
        for value in List:
           tf_idf.append(value*idf[i])
           i+=1 
        #print(tf_idf)
        doc[f'doc{j}']=CosSimilarity(tf_idf,TF_IDFQ(query,idf) ) #tf_idf for query &&tf_idf for files 
        j+=1           
    print(doc)
    
    return sortDoc(doc)  

        
def TF(namef):
    tf_forFile=[]
    #inRandom(namef) // Random ..............
    repeatf=repeat(namef)
    for char in ['A','B','C','D','E','F']:
        tf_forFile.append(repeatf[char]/Maxsize(repeatf))
    
    #print(tf_forFile)
    return  tf_forFile


'''def printQ(query):
    for key,value in query.items():
        print(f'{key}:{value}')'''

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
        
def Maxsize(repeatf):
    M=0
    for char in repeatf:
        if repeatf[char]>M:
            M=repeatf[char]
    return M

def IDF(sizeD):
    idf=[]
    repeatL=repeatD(sizeD)
    for i in ['A','B','C','D','E','F']:
        if repeatL[i]!=0:
            idf.append(math.log2((sizeD-1)/repeatL[i]))
        else:
            idf.append(0)
     
    print(idf)
    return idf


def repeatD(sizeD):
    D={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
    
    for i in range(1,sizeD):
        f=open(f'D{i}.txt')
        content=str(f.readline()).split(' ')
        f.close()
        frontier=[]
        for j in content:
            if j in ['A','B','C','D','E','F'] and j not in frontier:
                D[j]+=1
                frontier.append(j)
                
        i+=1                            
    print(D)            
    return D

def TF_IDFQ(query,idf):
    tf_idf_query=[]
    repeat={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
    for char in query:
        if char in ['A','B','C','D','E','F']:
            repeat[char]+=1
    i=0
    for char in repeat:
        tf_idf_query.append((repeat[char]/Maxsize(repeat))*idf[i])
        i+=1
    
    #print(tf_idf_query)
    return tf_idf_query       

def CosSimilarity(tf_idf,TF_IDFQ):
    #print(tf_idf)
    numerator=0
    denominator=0
    for i in range(len(tf_idf)):
        numerator+=tf_idf[i]*TF_IDFQ[i]

    denominator=math.sqrt(math.pow(sumL(tf_idf),2)*math.pow(sumL(TF_IDFQ),2))
    #print(numerator)
    print(denominator)
    return numerator/denominator

def sumL(Lname):
    sum=0
    for i in Lname:
        sum+=i
    return sum    

def sortDoc(doc):
    import operator

    doc= sorted(doc.items(), key=operator.itemgetter(1),reverse=True) 
    sortdict=dict(doc)
    #print(doc)
    return sortdict    

if __name__=='__main__':
    app.run()