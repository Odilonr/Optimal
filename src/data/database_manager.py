import sqlite3
from datetime import date
from ..models.gymGoer import Gymbro


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
                                weight FLOAT,
                                gender TEXT,
                                activity TEXT,
                                phase TEXT,
                                calorie_difference INTEGER,
                                step_goal INTEGER,
                                sleep_goal INTEGER,
                                carb_goal INTEGER,
                                protein_goal INTEGER,
                                fat_goal INTEGER, 
                                calorie_goal INTEGER
                            )""")
        
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS daily_records (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                athlete_id INTEGER,
                                date DATE,
                                calories_consumed INTEGER,
                                calories_remaining INTEGER,
                                steps INTEGER,
                                carbs_consumed FLOAT,
                                protein_consumed FLOAT,
                                fat_consumed FLOAT,
                                weight FLOAT,
                                sleep INT,
                                FOREIGN KEY (athlete_id) REFERENCES athletes (id)
                                )
                                """
                            )
        self.conn.commit()

    def determine_activity(self, activity):
        activity_levels = {
            'Sedentary': 1.25,
            'Light': 1.4,
            'Moderate': 1.6,
            'Active': 1.8,
            'Very Active': 1.9
        }

        return activity_levels[activity]

    def maintenace_calories(self,gender,weight, height, age, activity):
        if  gender == 'M':
            return ((10*weight) + (6.25*height) - (5*age) + 5) * activity
        else:
            return ((10*weight) + (6.25*height) - (5*age) - 161) * activity
        
    def macros_goal(self, calorie_goal, phase):
        if phase == 'Cut':
            carbs = int((0.30 * calorie_goal)/4)
            protein = int((0.40 * calorie_goal)/4)
            fat = int((0.30 * calorie_goal)/8)
        if phase == 'Bulk':
            carbs = int((0.60 * calorie_goal)/4)
            protein = int((0.25 * calorie_goal)/4)
            fat = int((0.15 * calorie_goal)/8)

        return { 'carb_goal':carbs,
                'protein_goal':protein,
                'fat_goal':fat
                }

    def add_athlete(self,username, password, age, height, weight, gender, activity, phase, calorie_difference=500,
                    step_goal= 10000, sleep_goal = 8):
        activity_multiplier = self.determine_activity(activity=activity)
        maintenance = self.maintenace_calories(gender=gender, age=age, height=height, weight=weight, activity=activity_multiplier)

        if phase == 'Cut':
            calorie_goal = maintenance - calorie_difference
        else:
            calorie_goal = maintenance + calorie_difference
            
        athlete_macros = self.macros_goal(calorie_goal=calorie_goal, phase=phase)
        carb_goal = athlete_macros['carb_goal']
        protein_goal = athlete_macros['protein_goal']
        fat_goal = athlete_macros['fat_goal']

        self.cursor.execute("""
            INSERT INTO athletes (username, password, age, height, weight,gender, activity, phase, calorie_difference,
                            step_goal,sleep_goal,carb_goal,protein_goal,fat_goal, calorie_goal) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (username, password, age, height, weight,gender, activity, 
              phase, calorie_difference, step_goal, sleep_goal, carb_goal, protein_goal, fat_goal, calorie_goal))
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
                step_goal=user_data[10],
                sleep_goal=user_data[11],
                carb_goal = user_data[12],
                protein_goal = user_data[13],
                fat_goal = user_data[14],
                calorie_goal = user_data[15]
            )
        
        return None
    
    def get_athlete_edited(self, username, age):
        self.cursor.execute("SELECT * FROM athletes WHERE username = ? AND age = ?", (username,age,))
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
                step_goal=user_data[10],
                sleep_goal=user_data[11],
                carb_goal = user_data[12],
                protein_goal = user_data[13],
                fat_goal = user_data[14],
                calorie_goal = user_data[15]
            )
        
        return None
    
    def update_athlete(self, athlete_id, **kwargs):
        for feild in kwargs:
            self.cursor.execute(f"""UPDATE athletes SET {feild} = ? WHERE id = ?""",(kwargs[feild], athlete_id,))

        self.conn.commit()

    def get_athlete_data(self, athlete_id):
        self.cursor.execute("SELECT weight, calorie_goal FROM athletes WHERE id = ?",(athlete_id,))
        result = self.cursor.fetchone()
        return result

    def empty_daily_record(self, athlete_id):
        current_date = date.today()
        weight_and_remaining = self.get_athlete_data(athlete_id=athlete_id)
        weight = weight_and_remaining[0]
        calories_remaining = weight_and_remaining[1]
        self.cursor.execute("""INSERT INTO daily_records (athlete_id, date, calories_consumed, calories_remaining,
                            steps, carbs_consumed, protein_consumed, fat_consumed, weight, sleep)
                                VALUES (?,?,?,?,?,?,?,?,?,?) """,(athlete_id,current_date.isoformat(),0,calories_remaining,0,0,0,0,
                                               weight,0,))
        self.conn.commit()

    def update_daily_record(self, athlete_id, date, **kwargs):
        for field in kwargs:
            self.cursor.execute(f"""UPDATE daily_records SET {field} = ? WHERE athlete_id = ? AND 
                                date = ?""",(kwargs[field],athlete_id,date,))
            
        self.conn.commit()

    def get_current_food_record(self, athlete_id, date):
        self.cursor.execute("""SELECT carbs_consumed,protein_consumed, fat_consumed,
                             calories_consumed, calories_remaining 
                            FROM daily_records WHERE athlete_id = ? AND date = ? """,
                            (athlete_id, date,))
        result = self.cursor.fetchone()
        return result
    
    def get_current_step_sleep_record(self, athlete_id, date):
        self.cursor.execute("""SELECT steps, sleep 
                            FROM daily_records WHERE athlete_id = ? AND date = ? """,
                            (athlete_id, date,))
        result = self.cursor.fetchone()
        return result
    
    def close(self):
        self.conn.close()

    def open(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

database = Databasemanager()