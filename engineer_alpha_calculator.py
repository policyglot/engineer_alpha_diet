'''
This program calculates the required macros of foods to be eaten for the 4 phases of the Engineering the Alpha program
'''

# MACRO-NUTRIENT CONSTANTS
cal_per_g = {'carb': 4,
             'protein': 4,
             'fat': 9}


class Alpha_workout():
    """
    Provides an interface for understanding the overall architecture of the project
    This conducts backend calculations which then connect with the UI classes of the calculator
    """

    def __init__(self, stage, week, bodywt, bodyfat):
        self.stage = stage
        self.week = week
        self.bodywt = bodywt
        self.bodyfat = bodyfat

    def calculate_fatfree(self):
        return self.bodywt * (100 - self.bodyfat) / 100

    def calculate_maintain(self):
        """Use body fat to decide constant with which to multiply fatfree mass
        Returns constants based on predecided intervals
        Technically these numbers are percentages, but
        """

        if 6 < self.bodyfat <= 12:
            return 17
        if 12 < self.bodyfat <= 15:
            return 16
        if 15 < self.bodyfat <= 19:
            return 15
        if 19 < self.bodyfat <= 22:
            return 14
        if self.bodyfat > 22:
            return 13

    def maintenance_calories(self):
        """
        Checks the bodyfat against predecided ranges and accordingly
        returns a multiplicative factor
        Then multiplies the
        :return: calories- int- the maintenance calories rounded to
        the nearest integer
        """
        return self.calculate_fatfree() * self.calculate_maintain()

    def deficit(self, day):
        """
        Returns the number of calories by which the total calories in  day
        must be below the maintenance value.

        :param day: str- workout day ('wkt') or non-workout ('nonwkt')
        :return: the amount of deficit required from resting metabolic rate
        """
        deficit_dict = {'prime': {'wkt': 300, 'non_wkt': 500},
                        'adapt': {'wkt': 200, 'non_wkt': 600},
                        'surge': {'wkt': -400, 'non_wkt': 200}
                        }
        return deficit_dict[self.stage][day]

    def final_calories(self, day):
        return self.maintenance_calories() - self.deficit(day)

    def carb_cals(self, day, prime=False):
        """
        :param prime- Boolean- checks for whether the trainee is in the
        :return:
        """
        carbs_fixed = {1: {'wkt': 0, 'nonwkt': 0},
                       2: {'wkt': 0, 'nonwkt': 30},
                       3: {'wkt': 0, 'nonwkt': 50},
                       4: {'wkt': 0, 'nonwkt': 75}}
        if prime:
            return carbs_fixed[self.week][day]
        else:
            carb_lbm = {'adapt': {'wkt': 0.75, 'nonwkt': 0.3},
                        'surge': {'wkt': 1, 'non_wkt': 0.5},
                        'complete': {'wkt': 1, 'nonwkt': 0.25}
                        }
            carb_cal = carb_lbm[self.stage][day] * self.calculate_fatfree()
            return carb_cal / cal_per_g['carb']

    def protein_cals(self, day):
        """
        Calculates the required protein intake in a day, depending on
        whether it is
        :param day: str- workout day ('wkt') or non-workout ('nonwkt')
        :return: int- rounding to the nearest gram the quantity of protein
        required
        """
        protein_lbm = {'adapt': {'wkt': 1, 'non_wkt': 0.8},
                       'prime': {'wkt': 0.8, 'non_wkt': 0.7},
                       'surge': {'wkt': 1.5, 'non_wkt': 1.25},
                       'complete': {'wkt': 1.5, 'non_wkt': 1}
                       }
        protein_cal = protein_lbm[self.stage][day] * self.calculate_fatfree()
        return protein_cal

    def carb_intake(self, day):
        return self.carb_cals(day) - cal_per_g['carb']

    def protein_intake(self, day):
        return self.protein_cals(day) - cal_per_g['protein']

    def fat_cals(self, day):
        return self.final_calories() - self.carb_cals(day) + self.protein_cals(day)

    def fat_intake(self, day):
        return self.fat_cals(day) / cal_per_g['fat']


test_case: Alpha_workout = Alpha_workout('adapt', 1, 166, 13)

print(test_case.calculate_fatfree())
print(test_case.calculate_maintain())
print(test_case.maintenance_calories())
print(test_case.deficit('wkt'))

print(test_case.protein_intake('wkt'))
print(test_case.carb_intake('wkt'))
