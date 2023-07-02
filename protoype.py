import mysql.connector as mysql
from datetime import date


cnx = mysql.connect(
    host ='localhost',
    user = 'guilherme',
    password = '@becker',
    database = 'empresa'
)

print("Actually, to use this code, you need to select some of the following options:\n[a]dd a new employer\n[d]elete a employer\n[s]earch")
answer = input("What will you do? ")





if answer =="a":
        func_id = int(input("What is the employee ID? "))
        nome = str(input("What is the name of the employee? "))
        carg = str(input('What is the job of the employee? '))
        data_contratacao = input("When was this employee hired? (YYYY-MM-DD) ")
        id_depto = int(input("What is the ID of the department? "))
        salario = int(input("What is the salary of this employee? "))
elif answer =="d":
        func_id = int(input("What is the function ID?"))
        nome = str(input("What is the name of the employee? "))


def search():
    query = "Select * FROM funcionarios"
    cursor.execute(query)
    results=cursor.fetchall()
    for row in results:
        print(row)

 
def newemp(func_id, nome, salario, carg, data_contratacao, id_depto):
    add = "INSERT INTO funcionarios (id_func, nome, salario, cargo, data_contratacao, id_depto) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (func_id, nome, salario, carg, data_contratacao, id_depto)   
    cursor.execute(add, values)
    cnx.commit()

def del_employer(func_id, nome):
    delete = "DELETE FROM funcionarios WHERE id_func = %s AND nome = %s"
    cursor.execute(delete, (func_id, nome))
    cnx.commit()
 
cursor = cnx.cursor()

if answer == "a":
    newemp(func_id, nome, salario, carg, data_contratacao, id_depto)
    print("The new employer was been added")
elif answer =="s":
    search()
elif answer =="d":
     del_employer(func_id, nome)
     print("The employer was been deleted")

cursor.close()
cnx.close()

