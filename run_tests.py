import unittest
<<<<<<< HEAD

from tests.examples.i_dictionaries_sets import tests_dictionaries_and_sets

suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)
=======
''' 
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
from tests.homework.d_repetition import tests_repetition

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
>>>>>>> bb0e719f575c0074fd908af7af32665434653d16
unittest.TextTestRunner(verbosity=2).run(suite)