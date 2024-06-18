import unittest
from gymGoer import * #Attributes: name,age,height,weight,gender,activity,deficit_or_surplus,phase



class Testing(unittest.TestCase):
    def test_athlete(self):
        member_one = Gymbro(name='Odilon',age=23, height= 188, weight= 98, gender='M', activity='Sedentary', deficit_or_surplus=-400,phase='Cut')
        self.assertEqual(member_one.maintenace_calories, 2556.25)
        member_one.gender = 'F'
        self.assertEqual(member_one.maintenace_calories, 2348.75)
        

if __name__ == '__main__':
    unittest.main()
        