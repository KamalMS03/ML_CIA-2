from flask import Flask,request,render_template
import pickle
import pymysql as ps
import pandas as pd
import numpy as np
model = pickle.load(open("model.pkl",'rb'))
app = Flask(__name__)

def database():
    con = ps.connect(host='localhost',port=3306,user="root",password="Kamal26nath@",db="user_data")
    cur = con.cursor()
    cur.execute("select * from users")
    out = cur.fetchone()
    sql = "select * from users"
    df = pd.read_sql(sql, con)
    return df

@app.route("/")
def main():
    return render_template("loginpage.html")

@app.route("/verification", methods = ['POST',"GET"])
def verify():
    a = database()
    cre = request.form.values()
    print(cre)
    arr = np.array(a)
    if cre in arr:
        return render_template('index.html')
@app.route("/RecommendationSystem",methods = ['post'])
def pred():
    features = [float(i) for i in (request.form.values())]
    pred = model.predict([features])
    return render_template("result.html", data = pred)

if __name__ == "__main__":
    app.run(debug = True)