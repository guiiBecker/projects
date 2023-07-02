import mysql.connector as mysql
from datetime import date
import PySimpleGUI as sg


# Establish the database connection
cnx = mysql.connect(
    host ='localhost',
    user = 'guilherme',
    password = '@becker',
    database = 'empresa'
)
cursor = cnx.cursor()

# Define functions with SQL queries
def search():
    query = "Select * FROM funcionarios"
    cursor.execute(query)
    results=cursor.fetchall()
    return results
def del_employer(employeeid, employee_name):
    delete = "DELETE FROM funcionarios WHERE id_func = %s AND nome = %s"
    cursor.execute(delete, (employeeid, employee_name))
    cnx.commit()
def newemp(func_id, nome, salario, carg, data_contratacao, id_depto):
    add = "INSERT INTO funcionarios (id_func, nome, salario, cargo, data_contratacao, id_depto) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (func_id, nome, salario, carg, data_contratacao, id_depto)   
    cursor.execute(add, values)
    cnx.commit()

# Define layout for adding a new employee
def layout_add():
    layout_add = [
          [sg.Text("What is the employee ID?"), sg.Input(key='func_id')],
          [sg.Text("What is the name of the employee?"), sg.Input(key='nome')],
          [sg.Text("What is the job of the employee?"), sg.Input(key='carg')],
          [sg.Text("When was this employee hired? (YYYY-MM-DD)"), sg.Input(key='data_contratacao')],
          [sg.Text("What is the ID of the department?"), sg.Input(key='id_depto')],
          [sg.Text("What is the salary of this employee?"), sg.Input(key='salario')],
          [sg.Button("Send"), sg.Button("Cancel")]
      ]  
    return layout_add


# Define layout for removing an employee
def layout_remove():
    layout_remove = [
        [sg.Text("What is the employee ID?"), sg.Input(key='func_id')],
        [sg.Text("What is the name of the employee?"), sg.Input(key='nome')],
        [sg.Button("Send"), sg.Button("Cancel")]
    ]
    return layout_remove

# Define layout for basic search
def layout_search():
    layout_search = [
      [sg.Table(values=search(), headings=['ID', 'Nome', 'Salário', 'Cargo', 'Data de Contratação', 'Departamento'],
              justification='left', num_rows=10, auto_size_columns=False,
              col_widths=[10, 20, 10, 20, 20, 15])],
    [sg.Button('Done')]
    ]
    return layout_search

# Define initial layout
layout =[
    [sg.Button("search")],
    [sg.Button("Add a employee")],
    [sg.Button("Delete a employee")],
    [sg.Button("Cancel")]
]
window = sg.Window("Manager Database", layout)
# Main event loop
while True:
    event, values = window.read()
 # Handle window closed or cancel event
    if event == sg.WINDOW_CLOSED or event =="Cancel":
        break
    elif event == "Add a employee":
        window = sg.Window("Add a employee", layout_add())
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event =="Cancel":
                break
             # Add an employee
            elif event == "Send":
                employeeid= int(values['func_id'])
                employee_name = values['nome']
                employee_job = values['carg']
                employee_hired = values['data_contratacao']
                department_id = int(values['id_depto'])
                employee_salary = int(values['salario'])
                newemp(employeeid, employee_name, employee_salary, employee_job, employee_hired, department_id)
                print("The new employer was been added")
                window.close()
    
    elif event == "Delete a employee":
        window = sg.Window("Add a employee", layout_remove())
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event =="Cancel":
                break
            # Delete an employee
            elif event == "Send":
                employeeid= int(values['func_id'])
                employee_name = values['nome']
                del_employer(employeeid, employeeid)
                print("The employee has been removed")
                window.close()
      # Perform a search
    elif event == "search":
        window_search = sg.Window('Search Results', layout_search())
        while True:
            event_search, values_search = window_search.read()
            if event_search == sg.WINDOW_CLOSED:
                break
            elif event_search == "Done":
                window.close()

# Close the cursor, connection, and window
cursor.close()
cnx.close()           
window.close()