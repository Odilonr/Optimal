import inspect

class Gymbro:
    def __init__(self,name,age,height,weight,gender,activity,deficit_or_surplus,phase):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.activity = self.determine_activity(activity)
        self.deficit_or_surplus = deficit_or_surplus
        self.phase = phase
        self.steps = 10000

    # BMR = 10W + 6.25H - 5A + 5
    # BMR = 10W + 6.25H - 5A - 161
    @property
    def maintenace_calories(self):
        if self.gender == 'M':
            return ((10*self.weight) + (6.25*self.height) - (5*self.age) + 5) * self.activity
        else:
            return ((10*self.weight) + (6.25*self.height) - (5*self.age) - 161) * self.activity
    
    @property
    def calorie_goal(self):
        return self.maintenace_calories + self.deficit_or_surplus
    
    @property
    def macros(self):
        return Macros(phase=self.phase, total_calories=self.calorie_goal)

    def determine_activity(self, activity):
        activity_levels = {
            'Sedentary': 1.25,
            'Light': 1.4,
            'Moderate': 1.6,
            'Active': 1.8,
            'Very Active': 1.9
        }
        return activity_levels[activity]

    def update_steps(self, num):
        self.steps += num

    def __repr__(self):
        stats = f"""Name: {self.name}
                   Maintenane: {self.maintenace_calories} calories
                   Goal: ---/{self.calorie_goal} calories\tSteps: ---/{self.steps} steps
                   A: {self.age} years\tH: {self.height} meters\tW: {self.weight} kg
                   Carbs: ---/{self.macros.carbs} g\tProtein: ---/{self.macros.protein} g\tFat: ---/{self.macros.fat} g"""
        return inspect.cleandoc(stats)

class Macros:
    def __init__(self, phase, total_calories):
        self.phase = phase
        self.total_calories = total_calories
        self.carbs = 0
        self.protein = 0
        self.fat = 0
        self.calculate_macros()
    
    def calculate_macros(self):
        if self.phase == 'Cut':
            self.carbs = int((0.30 * self.total_calories)/4)
            self.protein = int((0.40 * self.total_calories)/4)
            self.fat = int((0.30 * self.total_calories)/8)
        if self.phase == 'Bulk':
            self.carbs = int((0.60 * self.total_calories)/4)
            self.protein = int((0.25 * self.total_calories)/4)
            self.fat = int((0.15 * self.total_calories)/8)
            

        
member_one = Gymbro(name='Odilon',age=23, height= 188, weight= 98, gender='M', activity='Sedentary', deficit_or_surplus=1000,phase='Bulk')
print(member_one)
    



    