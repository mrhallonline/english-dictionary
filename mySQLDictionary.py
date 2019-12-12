import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()
user_word = input("Enter the word to define: ")
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %user_word)
results = cursor.fetchall()


if results:
    for result in results:
        print(result[1])
else:
    print("This word was not found")