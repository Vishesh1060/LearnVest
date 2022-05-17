from flask import Flask as F, render_template as rt
app=F(__name__)

cvalp=[]
file=open("static/archive/AXISBANK.csv",'r')
file.readline()
di={}
di={"prevclose":[]}
i=23
j=0    
"""
while(1):
    line=file.readline()
    if not line:
        break
    for z in line:
        x=line[22:i-1]
        if(x.find(',')==","or z=='z'):
            break

"""
@app.route('/dynm', methods = ['GET', 'POST'])
def dynm():
    return rt("/dynm/dynm.html")

@app.route('/',methods = ['GET', 'POST'])
def index():
    return rt("index.html")

#di.prevclose[0]+z[j];    
#print(di)

if __name__ == ("__main__"):
    app.run()


