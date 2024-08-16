
class Gymbro:
    def __init__(self,id,username,age,height,weight,gender,activity,phase, db_manager, calorie_difference, step_goals):
        self.username = username
        self.id = id
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.activity = self.determine_activity(activity)
        self.phase = phase
        self.db_manager = db_manager
        self.calorie_difference = calorie_difference
        self.steps_goal =  step_goals

    
    @property
    def maintenace_calories(self):
        if self.gender == 'M':
            return ((10*self.weight) + (6.25*self.height) - (5*self.age) + 5) * self.activity
        else:
            return ((10*self.weight) + (6.25*self.height) - (5*self.age) - 161) * self.activity
    
    @property
    def calorie_goal(self):
        return self.maintenace_calories + self.calorie_difference
    
    @property
    def macros_goal(self):
        if self.phase == 'Cut':
            self.carbs = int((0.30 * self.calorie_goal)/4)
            self.protein = int((0.40 * self.calorie_goal)/4)
            self.fat = int((0.30 * self.calorie_goal)/8)
        if self.phase == 'Bulk':
            self.carbs = int((0.60 * self.calorie_goal)/4)
            self.protein = int((0.25 * self.calorie_goal)/4)
            self.fat = int((0.15 * self.calorie_goal)/8)

        return { 'Carbs':self.carbs,
                'Protein':self.protein,
                'Fat':self.fat
                }


    def determine_activity(self, activity):

        activity_levels = {
            'Sedentary': 1.25,
            'Light': 1.4,
            'Moderate': 1.6,
            'Active': 1.8,
            'Very Active': 1.9
        }

        return activity_levels[activity]
    
    def update_main_fields(self, new_attributes):
        if self.id:
            self.db_manager.update_athlete(self.id, new_attributes)

    

            

        
    



    