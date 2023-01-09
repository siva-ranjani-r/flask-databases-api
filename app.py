from flask import Flask,render_template,redirect,request
import requests
import sqlite3 as sql

app = Flask(__name__)


@app.route("/",methods=['POST','GET'])
def link_api():
    conn=sql.connect("trans.db")
    conn.row_factory=sql.Row
    id=request.form.get("scheme_code")
    cur=conn.cursor()
    a=cur.execute("Select * from fund")
    lis=[id]
    l2=[]
    for i in a:
        url="https://api.mfapi.in/mf/"+str(i['scheme_code'])
        resp=requests.get(url)
        temp2=resp.json().get('meta').get('fund_house')
        new_get=resp.json().get('data')[0].get('nav')
        temp={'id':i['scheme_code'],'fund_house':temp2,'nav':new_get}
        l2.append(temp)
        print(i["scheme_code"]) 
    return render_template("fund.html",data=l2)


if __name__=='__main__':
    app.run(debug=True)