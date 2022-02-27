
import unittest
from webbrowser import get
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):
    get_options_ratio(5, 20, .25)




   # def test_options_ratio(self):
    #    self.assertEqual('Excellent', get_faculty_rating(get_options_ratio(9.1,10)))
     #  self.assertEqual('Good', get_faculty_rating(get_options_ratio(7.1,10)))
      #  self.assertEqual('Needs Improvement', get_faculty_rating(get_options_ratio(.6,10)))