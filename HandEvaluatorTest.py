from typing import Union
import unittest
from HandEvaluator import HoldemHand

class HandEvaluatorTest(unittest.TestCase):

    def test_ValidateHand(self):
        self.assertTrue(HoldemHand.ValidateHand("As Ks"))
        self.assertTrue(HoldemHand.ValidateHand("JdJh"))
        self.assertTrue(HoldemHand.ValidateHand("2d 3c", "Ad 5d 4c"))
        self.assertTrue(HoldemHand.ValidateHand("TdTh", "Jc3d3h 7h 9s"))
        self.assertTrue(HoldemHand.ValidateHand("8c 9c Tc Jc Qc"))        
        self.assertFalse(HoldemHand.ValidateHand("Xc Yx"))
        self.assertFalse(HoldemHand.ValidateHand("AA"))
        self.assertFalse(HoldemHand.ValidateHand("5s5c", "1h 3"))
        self.assertFalse(HoldemHand.ValidateHand("KcKc"))
        self.assertFalse(HoldemHand.ValidateHand("AcAd", "AcAdAcAd"))    

if __name__ == '__main__':
    unittest.main()