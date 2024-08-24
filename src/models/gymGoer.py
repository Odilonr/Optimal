
class Gymbro:
    def __init__(self,id, username,db_manager):
        self.id = id
        self.username = username
        self.db_manager = db_manager

    def inches_to_ftinch(self, amount):
        feet = amount//12
        feet_remaining = (amount/12) - feet
        inches = int(feet_remaining * 12)

        return {
                 'feet':feet,
                 'inches':inches
                }
    
    def ftinch_to_inches(self, feet, inches):
        total_inches = (feet * 12 ) + inches
        return total_inches
    
    
    def update_main(self, **new_attributes):
        if self.id:
            self.db_manager.update_athlete(self.id, **new_attributes)
            
    def get_current_athlete_data(self):
        return self.db_manager.get_athlete_data(self.id)
    
    def get_remaining_cals(self, date):
        return self.current_daily_record(date=date)[3] - self.current_daily_record(date=date)[4]
    
    def update_consumed_record(self,carbs,protein,fat,date):
        current_record = self.current_daily_record(date=date)
        new_carb = current_record[10] + carbs
        new_protein = current_record[12] + protein
        new_fat = current_record[14] + fat
        calories = (new_carb * 4) + (new_protein * 4) + (new_fat * 9)
        new_calories = current_record[4] + calories
        new_remaing = current_record[3] - new_calories
        self.db_manager.update_daily_record(self.id, date,carbs_consumed = new_carb, protein_consumed = new_protein,
                                        fat_consumed = new_fat, calories_consumed = new_calories,
                                        calories_remaining = new_remaing)
        
    def update_StepSleep_record(self, steps,sleep, date):
        current_steps_sleep = self.current_daily_record(date=date)
        new_steps = steps + current_steps_sleep[6]
        new_sleep = sleep + current_steps_sleep[8]
        self.db_manager.update_daily_record(self.id, date, steps = new_steps, sleep = new_sleep)


    def current_daily_record(self,date):
        return self.db_manager.get_current_daily_record(self.id, date)
    
    def current_athlete_record(self):
        return self.db_manager.get_athlete_data(self.id)
    



    

            

        
    



    