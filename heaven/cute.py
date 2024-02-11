from flask import Flask,render_template,request;
import mysql.connector as mysql
import matplotlib.pyplot as plt
import numpy as np
project=mysql.connect(
    host='localhost',
    user='root',
    password='Sowmya@1115',
    database='project'    
    
)
cur=project.cursor()
app=Flask(__name__)
app.secret_key='sajiseamu'
@app.route('/')
def homepage():
    return render_template('homepage.html')
@app.route('/user')
def user():
    return render_template('user.html')  
@app.route('/admin')
def admin():
    return render_template('admin.html') 
@app.route('/mediator')
def mediator():
    return render_template('mediator.html')
@app.route('/education')
def education():
    return render_template('education.html')
@app.route('/climate')
def climate():
    return render_template('climate.html')
@app.route('/economy')
def economy():
    return render_template('economy.html')
@app.route('/healthcare')
def healthcare():
    return render_template('healthcare.html')
@app.route('/needs')
def needs():
    return render_template('needs.html')
@app.route('/security')
def security():
    return render_template('security.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/adminlog')
def adminlog():
    return render_template('adminlog.html')



@app.route('/home',methods=['POST'] ) #collects data
def homedata():
    return render_template('register.html')

@app.route('/regdata',methods=['POST'] ) #collects data
def regdata():
    adh=request.form['aadhar']
    phn=request.form['phone']
    city=request.form['city']
    pwd=request.form['pwd']
    storereg(adh,phn,city,pwd)
    return render_template('user.html')

def storereg(adh,phn,city,pwd):
    sql="insert into regdata values(%s,%s,%s,%s)";
    val=(adh,phn,city,pwd)
    cur.execute(sql,val)
    project.commit()

@app.route('/logindata',methods=['POST'] ) #collects data
def logindata():
    adh=request.form['aadhar']
    pwd=request.form['pwd']
    res=getlogin(adh,pwd)
    if res:
        return render_template('user.html')
    else:
        p='invalid aadhar or password'
        return render_template('login.html',res=p)

def getlogin(adh,pwd):
    sql="select aadhar,pwd,city from regdata where aadhar=%s and pwd=%s"
    val=(adh,pwd)
    cur.execute(sql,val)
    result=cur.fetchall()
    return result 

@app.route('/admindata',methods=['POST'] ) #collects data
def admindata():
    adid=request.form['Adminid']
    pwd=request.form['Adminname']
    res=adminlogin(adid,pwd)
    if res:
        return render_template('admin.html')
    else:
        p='invalid aadhar or password'
        return render_template('adminlog.html',res=p)

def adminlogin(adid,pwd):
    sql="select AdminID,Adminname from Adminlist where AdminID=%s and Adminname=%s"
    val=(adid,pwd)
    cur.execute(sql,val)
    result=cur.fetchall()
    return result 

@app.route('/edu',methods=['POST'] ) #collects data
def collectedu():
    need=request.form['need1']
    oth=request.form['other']
    if need=='other':
        r1=oth
    else:
        r1=need
    storeeducation([r1])
    return render_template('homepage.html')

def storeeducation(r1):
    sql="insert into education(prblm) values(%s)";
    val=(r1)
    cur.execute(sql,val)
    project.commit()


@app.route('/cli',methods=['POST'] ) #collects data
def collectcli():
    need=request.form['need1']
    oth=request.form['other']
    if need=='other':
        r1=oth
    else:
        r1=need
    storeclimate([r1])
    return render_template('homepage.html')

def storeclimate(r1):
    sql="insert into climate(prblm) values(%s)";
    val=(r1)
    cur.execute(sql,val)
    project.commit()

@app.route('/ned',methods=['POST'] ) #collects data
def collectned():
    need=request.form['need1']
    oth=request.form['other']
    if need=='other':
        r1=oth
    else:
        r1=need
    storeneeds([r1])
    return render_template('homepage.html')

def storeneeds(r1):
    sql="insert into needs(prblm) values(%s)";
    val=(r1)
    cur.execute(sql,val)
    project.commit()

@app.route('/hea',methods=['POST'] ) #collects data
def collecthealth():
    need=request.form['need1']
    oth=request.form['other']
    if need=='other':
        r1=oth
    else:
        r1=need
    storehealth([r1])
    return render_template('homepage.html')

def storehealth(r1):
    sql="insert into health(prblm) values(%s)";
    val=(r1)
    cur.execute(sql,val)
    project.commit()

@app.route('/eco',methods=['POST'] ) #collects data
def collecteco():
    need=request.form['need1']
    oth=request.form['other']
    if need=='other':
        r1=oth
    else:
        r1=need
    storeeco([r1])
    return render_template('homepage.html')

def storeeco(r1):
    sql="insert into economics(prblm) values(%s)";
    val=(r1)
    cur.execute(sql,val)
    project.commit()

@app.route('/sec',methods=['POST'] ) #collects data
def collectsec():
    need=request.form['need1']
    oth=request.form['other']
    if need=='other':
        r1=oth
    else:
        r1=need
    storesec([r1])
    return render_template('homepage.html')

def storesec(r1):
    sql="insert into security(prblm) values(%s)";
    val=(r1)
    cur.execute(sql,val)
    project.commit()

@app.route('/sendedu',methods=['POST'] ) #collects data
def collectsendedu():
    prblm=request.form['prblm']
    cnt=request.form['cnt']
    assign=request.form['assign']
    sendedu(prblm,cnt,assign)
    return render_template('mediator.html')

def sendedu(prblm,cnt,assign):
    sql="insert into edualy(prblm,cnt,statu) values(%s,%s,%s)";
    val=(prblm,cnt,assign)
    cur.execute(sql,val)
    project.commit()

@app.route('/sendcli',methods=['POST'] ) #collects data
def collectsendcli():
    prblm=request.form['prblm']
    cnt=request.form['cnt']
    assign=request.form['assign']
    sendcli(prblm,cnt,assign)
    return render_template('mediator.html')

def sendcli(prblm,cnt,assign):
    sql="insert into clialy(prblm,cnt,statu) values(%s,%s,%s)";
    val=(prblm,cnt,assign)
    cur.execute(sql,val)
    project.commit()

@app.route('/sendned',methods=['POST'] ) #collects data
def collectsendned():
    prblm=request.form['prblm']
    cnt=request.form['cnt']
    assign=request.form['assign']
    sendned(prblm,cnt,assign)
    return render_template('mediator.html')

def sendned(prblm,cnt,assign):
    sql="insert into nedaly(prblm,cnt,statu) values(%s,%s,%s)";
    val=(prblm,cnt,assign)
    cur.execute(sql,val)
    project.commit()

@app.route('/sendhea',methods=['POST'] ) #collects data
def collectsendhea():
    prblm=request.form['prblm']
    cnt=request.form['cnt']
    assign=request.form['assign']
    sendhea(prblm,cnt,assign)
    return render_template('mediator.html')

def sendhea(prblm,cnt,assign):
    sql="insert into heaaly(prblm,cnt,statu) values(%s,%s,%s)";
    val=(prblm,cnt,assign)
    cur.execute(sql,val)
    project.commit()

@app.route('/sendeco',methods=['POST'] ) #collects data
def collectsendeco():
    prblm=request.form['prblm']
    cnt=request.form['cnt']
    assign=request.form['assign']
    sendeco(prblm,cnt,assign)
    return render_template('mediator.html')

def sendeco(prblm,cnt,assign):
    sql="insert into ecoaly(prblm,cnt,statu) values(%s,%s,%s)";
    val=(prblm,cnt,assign)
    cur.execute(sql,val)
    project.commit()

@app.route('/sendsec',methods=['POST'] ) #collects data
def collectsendsec():
    prblm=request.form['prblm']
    cnt=request.form['cnt']
    assign=request.form['assign']
    sendsec(prblm,cnt,assign)
    return render_template('mediator.html')

def sendsec(prblm,cnt,assign):
    sql="insert into secaly(prblm,cnt,statu) values(%s,%s,%s)";
    val=(prblm,cnt,assign)
    cur.execute(sql,val)
    project.commit()

@app.route('/viewedu',methods=['POST'] )
def viewedu():
    cur.execute("select prblm,cnt from edualy")
    r=cur.fetchall()
    k=viewlocal(r)
    return render_template('admin.html',res1=k)

@app.route('/viewcli',methods=['POST'] )
def viewcli():
    cur.execute("select prblm,cnt from clialy")
    r=cur.fetchall()
    k=viewlocal(r)
    return render_template('admin.html',res1=k)
@app.route('/viewned',methods=['POST'] )
def viewned():
    cur.execute("select prblm,cnt from nedaly")
    r=cur.fetchall()
    k=viewlocal(r)
    return render_template('admin.html',res1=k)
@app.route('/viewhea',methods=['POST'] )
def viewhea():
    cur.execute("select prblm,cnt from heaaly")
    r=cur.fetchall()
    k=viewlocal(r)
    return render_template('admin.html',res1=k)
@app.route('/vieweco',methods=['POST'] )
def vieweco():
    cur.execute("select prblm,cnt from ecoaly")
    r=cur.fetchall()
    k=viewlocal(r)
    return render_template('admin.html',res1=k)
@app.route('/viewsec',methods=['POST'] )
def viewsec():
    cur.execute("select prblm,cnt from secaly")
    r=cur.fetchall()
    k=viewlocal(r)
    return render_template('admin.html',res1=k)


def viewlocal(r):
    l1=[]
    l2=[]
    for i in r:
        l1.append(i[0])
        l2.append(i[1])
    x=l1
    y=l2
    plt.pie(y,labels=x)
    z=plt.show()
    return z
def count():
    cur.execute("select count(id) from education")
    s1=cur.fetchall()
    cur.execute("select count(id) from climate")
    s2=cur.fetchall()
    cur.execute("select count(id) from needs")
    s3=cur.fetchall()
    cur.execute("select count(id) from health")
    s4=cur.fetchall()
    cur.execute("select count(id) from economics")
    s5=cur.fetchall()
    cur.execute("select count(id) from security")
    s6=cur.fetchall()
    return s1+s2+s3+s4+s5+s6




@app.route('/result',methods=['POST'] ) #collects data
def results():
    def convert(s):
        l=[]
        for i in range(len(s)):
            l.append(s[i][1])
        s=set(l)
        l1=[]
        for i in s:
            l1.append([i,l.count(i)])
        return l1
    cur.execute("select * from education")
    edu=cur.fetchall()
    edu1=convert(edu)
    cur.execute("select * from climate")
    cli=cur.fetchall()
    cli1=convert(cli)
    cur.execute("select * from needs")
    ned=cur.fetchall()
    ned1=convert(ned)
    cur.execute("select * from health")
    hea=cur.fetchall()
    hea1=convert(hea)
    cur.execute("select * from economics")
    eco=cur.fetchall()
    eco1=convert(eco)
    cur.execute("select * from security")
    sec=cur.fetchall()
    sec1=convert(sec)
    s=count()
    c=0
    for i in s:
        c=c+i[0]
    return render_template('mediator.html',edu=edu1,cli=cli1,ned=ned1,hea=hea1,eco=eco1,sec=sec1,cou=c)
if __name__=='__main__':
    app.run(debug=True)