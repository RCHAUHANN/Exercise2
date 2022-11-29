from flask import Flask
import mysql.connector


app = Flask(__name__)
@app.route('/prime_number/<number>')

def prime_number(number):
    isPrime = True
    number = int(number)
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                isPrime = False
                break


    response = {
        "isPrime" : isPrime,
        "Number" : number
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)



#ex2
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3307,
         database='flight_game',
         user='root',
         password='rashi432',
         autocommit=True
         )

app = flask(__name__)
@app.route('/airport/<ICAO>')
def airport(ICAO):
    sql = "SELECT ident, name, municipality FROM airport"
    sql += " WHERE ident='" + ICAO + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:

         name= row[0]
         location =row[1]

    response={
        "ICAO": ICAO,
        "Name": name,
        "Location": location

    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
