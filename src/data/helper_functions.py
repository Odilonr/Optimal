


def determine_activity(activity):
        activity_levels = {
            'Sedentary': 1.25,
            'Light': 1.4,
            'Moderate': 1.6,
            'Active': 1.8,
            'Very Active': 1.9
        }
        return activity_levels[activity]


def maintenace_calories(gender,weight, height, age, activity):
    height = height * 2.54
    weight = weight / 2.205
    if  gender == 'M':
        return ((10*weight) + (6.25*height) - (5*age) + 5) * activity
    else:
        return ((10*weight) + (6.25*height) - (5*age) - 161) * activity


def macros_goal(calorie_goal, phase):
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