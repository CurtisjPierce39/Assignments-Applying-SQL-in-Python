from connect_mysql import connect_database
from mysql.connector import Error

def add_member(name, age): #Question 1 Task 1
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Members (name, age) VALUES (%s, %s)"
            cursor.execute(query, (name, age))
            conn.commit()
            print("New Member Added Successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def add_workout_session(member_id, session_date, duration_minutes, calories_burned): #Question 1 Task 2
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO WorkoutSessions (member_id, session_date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (member_id, session_date, duration_minutes, calories_burned))
            conn.commit()
            print("New Workout Session Added Successfully!")
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

def update_member_age(member_id, new_age): #Question 1 Task 3
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "UPDATE Members SET age = %s WHERE member_id = %s"
            cursor.execute(query, (member_id, new_age))
            conn.commit()
            print("Member age updated Successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def delete_workout_session(session_id): # Question 1 Task 4
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(query, (session_id,))
            conn.commit()
            print("Workout Session Deleted Successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# delete_workout_session(1)
# update_member_age(28, 3)
# add_workout_session(3, "2021-12-23", "30 minutes", "150 Calories Burned")
# add_member("Bob Belcher", 25)
add_member("Linda Belcher", 30)
add_member("Curtis Pierce", 38)
add_member("Tina Belcher", 19)
