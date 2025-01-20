#mycursor.execute("""
#    CREATE DATABASE todo_list;
#    USE todo_list;

#    CREATE TABLE tasks (
#    id INT AUTO_INCREMENT PRIMARY KEY,
#    task_name VARCHAR(250) NOT NULL,
#    description TEXT,
#    is_completed BOOLEAN DEFAULT 0 );
#    """)


import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='sahr',
    password='root',
    database='todo_list'
) #Check Connection Settings in MySQL Workbench to get these details

def add_todo(task_name, description):
    cursor = db.cursor()
    sql = "INSERT INTO tasks (task_name, description) VALUES (%s, %s)"
    val = (task_name, description)
    cursor.execute(sql, val)
    db.commit()
    print("Task has been added successfully!")

def view_todo():
    cursor = db.cursor()
    sql = "SELECT * FROM tasks"
    cursor.execute(sql)
    tasks = cursor.fetchall()
    if tasks:
        for task in tasks:
            print(f"""Task ID: {task[0]}, Task Name: {task[1]}, 
                  Description: {task[2]}, Completed: {'Yes' if task[3] else 'No'}""")
    else:
        print("There are no Tasks in the DataBase")  

def todo_completed(task_id):
    cursor = db.cursor()
    sql = "UPDATE tasks SET is_completed = 1 WHERE id = %s"
    val = (task_id,)
    cursor.execute(sql, val)
    db.commit()
    print("Task marked as completed!")

def update_todo(task_id, task_name, description):
    cursor = db.cursor()
    sql = "UPDATE tasks SET task_name = %s, description = %s WHERE id = %s"
    val = (task_name, description, task_id)
    cursor.execute(sql, val)
    db.commit()
    print("Task details updated successfully!")

def delete_todo(task_id):
    cursor = db.cursor()
    sql = "DELETE FROM tasks WHERE id = %s"
    val = (task_id,)
    cursor.execute(sql, val)
    db.commit()
    print("Task deleted successfully!")


while True:
    print("\n--- To-Do List ---")
    print("1. Add Todo")
    print("2. View Todo")
    print("3. Mark Todo as Completed")
    print("4. Update Todo Details")
    print("5. Delete Todo")
    print("6. Exit")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        task_name = input("Enter the todo name: ")
        description = input("Enter the todo description: ")
        add_todo(task_name, description)

    elif choice == 2:
        print("\n--- Todo's ---")
        view_todo()

    elif choice == 3:
        task_id = int(input("Enter the todo ID to mark as completed: "))
        todo_completed(task_id)

    elif choice == 4:
        task_id = int(input("Enter the todo ID to update: "))
        task_name = input("Enter the new todo name: ")
        description = input("Enter the new todo description: ")
        update_todo(task_id, task_name, description)

    elif choice == 5:
        task_id = int(input("Enter the todo ID to delete: "))
        delete_todo(task_id)

    elif choice == 6:
        print("Thanks for using the app. Bye bye!")
        break

    else:
        print("That's not a valid choice. Please try again.")