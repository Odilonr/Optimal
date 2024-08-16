import sqlite3
from datetime import date
from ..models.gymGoer import Gymbro


class Databasemanager:
    def __init__(self, db_name='health_tracker.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    
    def create_tables(self):
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS athletes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT,
                                password TEXT,
                                age INTEGER,
                                height FLOAT,
                                weight FLOAT,
                                gender TEXT,
                                activity TEXT,
                                phase TEXT,
                                calorie_difference INTEGER,
                                step_goal
                            )""")
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS daily_records (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                athlete_id INTEGER
                                date DATE,
                                calories_consumed INTEGER,
                                steps INTEGER,
                                carbs_consumed FLOAT,
                                protein_consumed FLOAT,
                                fat_consumed FLOAT,
                                weight FLOAT,
                                FOREIGN KEY (athlete_id) REFERENCES athletes (id)
                                )
                                """
                            )
        self.conn.commit()

    def add_athlete(self,username, password, age, height, weight, gender, activity, phase, calorie_difference=500,
                    step_goal= 10000):
        self.cursor.execute("""
            INSERT INTO athletes (username, password, age, height, weight,gender, activity, phase, calorie_difference,
                            step_goal) 
            VALUES (?,?,?,?,?,?,?,?,?,?)
        """, (username, password, age, height, weight,gender, activity, 
              phase, calorie_difference, step_goal))
        self.conn.commit()


    def get_athlete_id(self, username):
        self.cursor.execute("SELECT id FROM athletes WHERE username = ?", (username,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None
    
    
    def get_athlete(self, username, password):
        self.cursor.execute("SELECT * FROM athletes WHERE username = ? AND password = ?", (username,password,))
        user_data = self.cursor.fetchone()

        if user_data:
             
             return Gymbro(
                id=user_data[0],
                username=user_data[1],  
                age=user_data[3],
                height=user_data[4],
                weight=user_data[5],
                gender=user_data[6],
                activity=user_data[7],
                phase=user_data[8],
                db_manager=self, 
                calorie_difference=user_data[9],
                step_goals=user_data[10]
            )
        
        return None
    
    def update_athlete(self, athlete_id, **kwargs):
        for feild in kwargs:
            self.cursor.execute(f"""UPDATE athletes SET {feild} = ? WHERE id = ?""",(kwargs[feild], athlete_id))

        self.conn.commit()





    
    
    
    

        

    def close(self):
        self.conn.close()


