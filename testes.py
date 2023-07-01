import mysql.connector as mysql




#function to generate a vanilla search
def search():
    query = "Select * FROM funcionarios"
    cursor.execute(query)
    results=cursor.fetchall()
    for row in results:
        print(row)



#credentials to logon on BD
cnx = mysql.connect(
    host ='localhost',
    user = 'guilherme',
    password = '@becker',
    database = 'empresa'
)

#create a cursor to acess the BD
cursor = cnx.cursor()

#call function
search()


#close the conection
cursor.close()
cnx.close()

