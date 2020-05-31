import sqlite3



with sqlite3.connect("Fibonacci.db") as database:
    cursor =  database.cursor()
    cursor.execute("CREATE TABLE Fibonacci(asset TEXT,assetClass TEXT,instutionalValue60 REAL,fibonacciValue60 REAL, price REAL, time NUMERIC)")
    #cursor.execute("INSERT INTO Fibonacci(asset,assetClass,instutionalValue60,fibonacciValue60,price,time) VALUES(?,?,?,?,?,?)",(asset,assetClass,instutionalValue60,fibonacciValue60,price,time))
    #database.commit()

    
with sqlite3.connect("Scalper.db") as database:
    cursor =  database.cursor()
    cursor.execute("CREATE TABLE Scalper(asset TEXT,assetClass TEXT,buySetUps REAL,sellSetUps REAL, scalper REAL,price REAL, time NUMERIC)")




