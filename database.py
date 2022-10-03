import mysql.connector
import geopy
from geopy.distance import geodesic


connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3307,
         database='flight_game',
         user='root',
         password='rashi432',
         autocommit=True
         )
def getairport(ICAO):
    sql = "SELECT ident, name, municipality FROM airport"
    sql += " WHERE ident='" + ICAO + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The airport name for the ciao code {row[0]} is {row[1]} which is located in {row[2]}")
    return

ICAO = input("please enter a ciao code")
getairport(ICAO)

#2

def code(CODE):
    sql = "SELECT airport.iso_country, airport.type, count(*) FROM airport"
    sql += " WHERE airport.iso_country ='" + CODE + "' GROUP BY airport.type"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"There are {row[2]} {row[1]} in country that has the code {row[0]} ")
    return


CODE = input("Please enter the country code: ")
code(CODE)


#3

def dist(code):
    location = []
    sql =" SELECT ident, longitude_deg, latitude_deg FROM airport"
    sql += " WHERE ident ='" + code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            location.append(row[2])
            location.append(row[1])
        return location



code1= input("please enter the first ICAO code: ")
code2 = input("please enter the second ICAO code: ")

print(f"the distance is {geodesic(dist(code1), dist(code2))}")




