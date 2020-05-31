from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)

@app.route('/add/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    
    content = request.json

    print (content)
    if (uuid=='2'):
        asset = content['asset']
        assetClass = content['assetClass']
        instutionalValue60 = content['instutionalValue60']
        fibonacciValue60 = content['fibonacciValue60']
        price = content['price']
        time = content['time']
        with sqlite3.connect("Fibonacci.db") as database:
            cursor =  database.cursor()
    #cursor.execute("CREATE TABLE Fibonacci(asset TEXT,assetClass TEXT,instutionalValue60 REAL,fibonacciValue60 REAL, price REAL, time NUMERIC)")
            cursor.execute("INSERT INTO Fibonacci(asset,assetClass,instutionalValue60,fibonacciValue60,price,time) VALUES(?,?,?,?,?,?)",(asset,assetClass,instutionalValue60,fibonacciValue60,price,time))
            database.commit()
            print("f.added")
    if (uuid=='3'):
        asset = content['asset']
        assetClass = content['assetClass']
        buySetUps = content['buySetUps']
        sellSetUps = content['sellSetUps']
        scalper = content['scalper']
        price = content['price']
        time = content['time']
        with sqlite3.connect("Scalper.db") as database:
            cursor =  database.cursor()
    #cursor.execute("CREATE TABLE Scalper(asset TEXT,assetClass TEXT,buySetUps REAL,sellSetUps REAL, scalper REAL,price REAL, time NUMERIC)")
            cursor.execute("INSERT INTO Scalper(asset,assetClass,buySetUps,sellSetUps,scalper,price,time) VALUES(?,?,?,?,?,?,?)",(asset,assetClass,buySetUps,sellSetUps,scalper,price,time))
            database.commit()
            print("s.added")
    return jsonify({"uuid":uuid})

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port='80',debug=True)

