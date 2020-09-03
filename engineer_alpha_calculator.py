'''
This program calculates the required macros of foods to be eaten for the 4 phases of the Engineering the Alpha program
'''

# MACRO-NUTRIENT CONSTANTS
cal_per_g = {'carb': 4,
             'protein': 4,
             'fat': 9}

class alpha_workout():
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
        return self.bodywt * (1 - self.bodyfat)

    def maintenance_calories(self):
        """
        Checks the bodyfat against predecided ranges and accordingly
        returns a multiplicative factor
        Then multiplies the
        :return: calories- int- the maintenance calories rounded to
        the nearest integer
        """
        pass

    def deficit(self, day):
        """
        Returns the number of calories by which the total calories in  day
        must be below the maintenance value.

        :param day: str- workout day ('wkt') or non-workout ('nonwkt')
        :return: the amount of deficit required from resting metabolic rate
        """
        deficit = {'prime':{'wkt': 300, 'non_wkt': 500},
                   'adapt': {'wkt': 200, 'non_wkt': 600},
                   'surge': {'wkt': -400, 'non_wkt': 200}
                   }
        pass

    def carbohydrate_intake(self, prime=False, day):
        """
        :param prime- Boolean- checks for whether the trainee is in the
        :return:
        """
        carbs_fixed = {1: 0,
                 2: 30,
                 3: 75,
                 4: 100}
        if prime:
            if day == 'nonwkt':
                return 0
            return carbs_fixed[self.week]
        else:
            carb_lbm = {'adapt': {'wkt': 0.75, 'nonwkt': 0.3},
                        'surge': {'wkt': 1, 'non_wkt': 0.5},
                        'complete': {'wkt': 1, 'nonwkt': 0.25}
                        }
            return carb_lbm[self.stage][day]

    def protein_intake(self, day):
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
                       'complete': {'wkt':1.5, 'nonwkt': 1}
                   }
        return protein_lbm[self.stage][day]

    def fat_intake(self, day):
        pass
