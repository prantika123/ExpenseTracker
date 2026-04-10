import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Enter MySQL password: "),
    database="expense_tracker"
)
cursor=conn.cursor()
def add_expense():
    Date=input("Enter date(YYYY-MM-DD):")
    Category=input("Enter category:")
    Amount=float(input("Enter amount:"))
    desc=input("Enter description:")
    query="INSERT INTO expenses(date,category,amount,description)VALUES(%s,%s,%s,%s)"
    values=(Date,Category,Amount,desc)
    cursor.execute(query,values)
    conn.commit()
    print("Expense added successfully!")
def view_expenses():
    cursor.execute("SELECT*FROM expenses")
    records=cursor.fetchall()
    for row in records:
        print(row)
def total_expenses():
    cursor.execute("SELECT SUM(Amount) FROM expenses")
    total=cursor.fetchone()[0]
    print("Total Expense:",total)
def filter_category():
    cat=input("Enter category:")
    query="SELECT*FROM expenses WHERE category=%s"
    cursor.execute(query,(cat,))
    for row in cursor.fetchall():
        print(row)
def delete_expense():
    ID=input("Enter ID to delete:")
    cursor.execute("DELETE FROM expenses WHERE ID= %s",(ID,))
    conn.commit()
    print("Deleted successfully!")
while True:
    print("=====Expense Tracker====")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Filter Category")
    print("5. Delete Expense")
    print("6. Exit")

    choice=input("Enter your choice: ")
    if choice=="1":
        add_expense()
    elif choice=="2":
        view_expenses()
    elif choice=="3":
        total_expenses()
    elif choice=="4":
        filter_category()
    elif choice=="5":
        delete_expense()
    elif choice=="6":
        print("Exiting....")
        break
    else:
        print("Invalid choice!\n")
