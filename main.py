from flask import Flask,render_template
import pyodbc


app=Flask(__name__)

app.debug=True

conn_str= ('DRIVER={ODBC Driver 17 for SQL Server};'
           'SERVER=bootcampaug5server.database.windows.net;'
           'DATABASE=bootcampaug5db;'
           'UID=bootcamp;'
           'PWD=Pass@123;')

@app.route('/')
def home():
    return render_template("Task1.html")

@app.route('/Task1')
def task1():
    return render_template("Task1.html")


@app.route('/Task2')
def task2():
    conn=pyodbc.connect(conn_str)
    cursor=conn.cursor()
    cursor.execute("SELECT TOP 20 * FROM SalesLT.Customer")
    ans = cursor.fetchall()
    return render_template('Task2.html', rows=ans)

@app.route('/Task3')
def task3():
    conn=pyodbc.connect(conn_str)
    cursor=conn.cursor()
    ans=cursor.execute(" select SP.Name,SP.Color,SP.Weight,SP.Size  from SalesLT.Product as SP inner join SalesLT.ProductCategory as SPC on SP.ProductCategoryID = SPC.ProductCategoryID ")
    return render_template("Task3.html",rows=ans)

if __name__ == "__main__":
    app.run(port=5000)