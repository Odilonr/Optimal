
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


    def calculate_calories_remaining(self):
        pass
    
    def update_main(self, **new_attributes):
        if self.id:
            self.db_manager.update_athlete(self.id, **new_attributes)
            for new_attribute in new_attributes:
                self.new_attribute = new_attributes[new_attribute]


    

            

        
    



    