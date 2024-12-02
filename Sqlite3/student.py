import sqlite3
connection =  sqlite3.connect("student.db")
cursor =  connection.cursor()

cursor.execute('''
         CREATE TABLE IF NOT EXISTS StudentInfo (
                id INTEGER PRIMARY KEY,
                Roll INTEGER,       
                Name TEXT NOT NULL,  
                College TEXT NOT NULL    
);            
''')

def display_data():
   rows = cursor.execute(''' SELECT * FROM StudentInfo ''')
   for row in rows:
       print(row)
    


def insert_data(name,roll,college_name):
    cursor.execute('''
    Insert into StudentInfo(roll,name,college)
    values(?,?,?);''',(roll,name,college_name))
    connection.commit()

def update_data(id,name,roll,college_name):
    cursor.execute('''
    UPDATE StudentInfo
    SET name = ?, roll = ?, college = ?
    WHERE id=?;''',(name,roll,college_name,id))
    
    connection.commit()


def delete_data(id):
    cursor.execute('''
                   DELETE FROM StudentInfo WHERE id =?
                   ''',(id,))
    connection.commit()

def main():
    while True:
        print("Press 1 to display data : \n")
        print("Press 2 to Insert data : \n")
        print("Press 3 to Update  data : \n")
        print("Press 4 to Delete data : \n")
        print("Press 5 to Exit : \n")
        choice = input("Enter your choice : ")
        match choice:
            case '1':
                display_data()
                break
            case '2':
                name = input("Enter your name : ")
                college_name = input("Enter your college name : ")
                roll = input("Enter your roll number : ")
                insert_data(name,roll,college_name)
                break
            case '3':
                name = input("Enter your name : ")
                college_name = input("Enter your college name : ")
                roll = input("Enter your roll number : ")
                id = input("Enter your id which data you want to update : ")
                update_data(id,name,roll,college_name)
                break
            case '4':
                id = input("Enter your id which data you want to Delete : ")
                delete_data(id)
                break
            case '5':
                break
                
    connection.close()           
        
        



if __name__ == "__main__":
    main()

