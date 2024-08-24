import sqlite3
from datetime import date
from ..models.gymGoer import Gymbro
from .helper_functions import determine_activity, macros_goal, maintenace_calories


class Databasemanager:
    def __init__(self, db_name='health_tracker.db'):
        self.open(db_name)
        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS athletes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT UNIQUE,
                                password TEXT,
                                age INTEGER,
                                height INTEGER,
                                gender TEXT
                            )""")
        
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS daily_records (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                athlete_id INTEGER,
                                date DATE,
                                calorie_goal INTEGER,
                                calories_consumed INTEGER,
                                calories_remaining INTEGER,
                                steps INTEGER,
                                step_goal INTEGER,
                                sleep INT,
                                sleep_goal INTEGER,
                                carbs_consumed FLOAT,
                                carb_goal INTEGER,
                                protein_consumed FLOAT,
                                protein_goal INTEGER,
                                fat_consumed FLOAT,
                                fat_goal INTEGER,
                                weight FLOAT,
                                activity TEXT,
                                phase TEXT,
                                FOREIGN KEY (athlete_id) REFERENCES athletes (id)
                                )
                                """
                            )
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS food (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                athlete_id INTEGER,
                                date DATE,
                                meal_type TEXT,
                                food_name TEXT,
                                amount TEXT,
                                carbs FLOAT,
                                protein FLOAT, 
                                fat FLOAT,
                                UNIQUE(athlete_id, date, meal_type,  food_name),
                                FOREIGN KEY (athlete_id) REFERENCES athletes (id)
                                )
                                """
                            )


        self.conn.commit()


    def add_athlete(self,username, password, age, height, gender):
        self.cursor.execute("""
            INSERT INTO athletes (username, password, age, height ,gender) 
            VALUES (?,?,?,?,?)
        """, (username, password, age, height,gender,))
        self.conn.commit()

    def get_athlete_id(self, username, password):
        self.cursor.execute("SELECT id FROM athletes WHERE username = ? AND password = ?", (username,password,))
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
                db_manager=self  
            )
        
        return None
    
    
    def update_athlete(self, athlete_id, **kwargs):
        for feild in kwargs:
            self.cursor.execute(f"""UPDATE athletes SET {feild} = ? WHERE id = ?""",(kwargs[feild], athlete_id,))

        self.conn.commit()

    def get_athlete_data(self, athlete_id):
        self.cursor.execute("SELECT * FROM athletes WHERE id = ?",(athlete_id,))
        result = self.cursor.fetchone()
        return result

    def get_all_athlete_ids(self):
        self.cursor.execute("SELECT id from athletes")
        return [row[0] for row in self.cursor.fetchall()]

    def empty_daily_record(self, athlete_id,date, weight, activity, phase):
        athlete_data = self.get_athlete_data(athlete_id)
        age = athlete_data[3]
        height = athlete_data[4]
        gender = athlete_data[5] 
        activity_multiplier = determine_activity(activity=activity)
        maintenance = maintenace_calories(gender=gender, weight=weight, height=height, 
                                          age=age, activity=activity_multiplier)

        if phase == 'Cut':
            calorie_goal = int(maintenance) - 500
        else:
            calorie_goal = int(maintenance) + 500

        macros_suggestion = macros_goal(calorie_goal=calorie_goal, phase=phase)

        self.cursor.execute("""INSERT INTO daily_records (athlete_id, date, calorie_goal ,calories_consumed,
                                calories_remaining, steps, step_goal, sleep, sleep_goal, carbs_consumed, carb_goal ,
                                protein_consumed ,protein_goal, fat_consumed, fat_goal, weight ,activity, phase)
                                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """,(athlete_id,date,calorie_goal,0,calorie_goal,0,10000,0,8,0,
                                          macros_suggestion['carb_goal'],0,macros_suggestion['protein_goal'],
                                          0,macros_suggestion['fat_goal'],weight, activity, phase,))
        self.conn.commit()

    def update_daily_record(self, athlete_id, date, **kwargs):
        for field in kwargs:
            self.cursor.execute(f"""UPDATE daily_records SET {field} = ? WHERE athlete_id = ? AND 
                                date = ?""",(kwargs[field],athlete_id,date,))
            
        self.conn.commit()

    def get_current_daily_record(self, athlete_id, date):
        self.cursor.execute("""SELECT * FROM daily_records WHERE athlete_id = ? AND date = ? """,
                            (athlete_id, date,))
        
        result = self.cursor.fetchone()
        return result
    
    def daily_record_exists(self, athlete_id, date):
        self.cursor.execute("""
                    SELECT EXISTS(SELECT 1 FROM daily_records WHERE athlete_id = ? AND date = ?)
                            """, (athlete_id, date))
        return self.cursor.fetchone()[0] == 1

    def add_food(self, athlete_id, date, meal_type, food_name, amount, carbs, protein, fat):
        
        self.cursor.execute(""" INSERT OR IGNORE INTO food (athlete_id, date, meal_type, food_name, amount, carbs, protein,fat)
                                VALUES (?,?,?,?,?,?,?,?)
                            """, (athlete_id, date, meal_type, food_name, amount, carbs, protein, fat,))
        
        self.conn.commit()

    def grab_food(self, athlete_id, date, meal_type):
        self.cursor.execute("""SELECT food_name, amount
                            FROM food WHERE athlete_id = ? AND 
                            date = ? AND meal_type = ?
                            """, (athlete_id, date, meal_type,))
        
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

    def open(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

database = Databasemanager()