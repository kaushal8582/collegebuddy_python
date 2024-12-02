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
   
   
   print("**************************** \n")
   for row in rows:
       print(row);
   print(" \n**************************** \n")
    
    


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
        print("Press 1 to display data : ")
        print("Press 2 to Insert data : ")
        print("Press 3 to Update  data : ")
        print("Press 4 to Delete data : ")
        print("Press 5 to Exit : ")
        choice = input("Enter your choice : ")
        match choice:
            case '1':
                display_data()
                
            case '2':
                name = input("Enter your name : ")
                college_name = input("Enter your college name : ")
                roll = input("Enter your roll number : ")
                insert_data(name,roll,college_name)
                
            case '3':
                name = input("Enter your name : ")
                college_name = input("Enter your college name : ")
                roll = input("Enter your roll number : ")
                id = input("Enter your id which data you want to update : ")
                update_data(id,name,roll,college_name)
                
            case '4':
                id = input("Enter your id which data you want to Delete : ")
                delete_data(id)
                
            case '5':
                exit()
                
    connection.close()           
        
        



if __name__ == "__main__":
    main()

