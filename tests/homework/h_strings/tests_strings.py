import unittest
from src.homework.h_strings import get_hammering_distance
from src.homework.h_strings import get_dna_complement

class Test_Config(unittest.TestCase):
    def test_get_hammering_distance(self):
        self.assertEqual(7, get_hammering_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))

    def test_get_dna_complement(self):
        self.assertEqual("ACCGGGTTTT", get_dna_complement("AAAACCCCGGT"))