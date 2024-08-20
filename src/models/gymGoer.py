
class Gymbro:
    def __init__(self,id, username, age, height, weight,gender, activity, 
              phase, calorie_difference, step_goal, sleep_goal, carb_goal, protein_goal, fat_goal, calorie_goal,
              db_manager):
        self.id = id
        self.username = username
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.activity = activity
        self.phase = phase
        self.calorie_difference = calorie_difference
        self.step_goal =  step_goal
        self.sleep_goal = sleep_goal
        self.carb_goal = carb_goal
        self.protein_goal = protein_goal
        self.fat_goal = fat_goal
        self.calorie_goal = calorie_goal
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
    
    def calculate_calories_remaining(self):
        pass
    
    def update_main(self, **new_attributes):
        if self.id:
            self.db_manager.update_athlete(self.id, **new_attributes)
            for new_attribute in new_attributes:
                self.new_attribute = new_attributes[new_attribute]

    def update_food_record(self,carbs,protein,fat,date):
        current_food_stats = self.db_manager.get_current_food_record(self.id,date)
        new_carb = current_food_stats[0] + carbs
        new_protein = current_food_stats[1] + protein
        new_fat = current_food_stats[2] + fat
        cals_to_add = (new_carb * 4) + (new_protein * 4) + (new_fat * 9)
        new_calories = current_food_stats[3] + cals_to_add
        new_remaing = self.calorie_goal - new_calories
        self.db_manager.update_daily_record(self.id, date,carbs_consumed = new_carb, protein_consumed = new_protein,
                                        fat_consumed = new_fat, calories_consumed = new_calories,
                                        calories_remaining = new_remaing)
        
    def update_step_sleep_record(self, steps,sleep, date):
        current_steps_sleep = self.db_manager.get_current_step_sleep_record(self.id,date)
        new_steps = steps + current_steps_sleep[0]
        new_sleep = sleep + current_steps_sleep[1]
        self.db_manager.update_daily_record(self.id, date, steps = new_steps, sleep = new_sleep)


    

            

        
    



    