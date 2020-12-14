from HandAnalysis import HandAnalysis
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
    
    def test_Comparable(self):
        board = "2s 3s 5s"
        player1 = HoldemHand("AsKc", board)
        player2 = HoldemHand("AdKs", board)
        self.assertTrue(player1 == player2)

        player2 = HoldemHand("AdQd", board)
        self.assertTrue(player1 > player2)
        self.assertTrue(player2 < player1)

        board = "Qs Jh 7c"
        player1 = HoldemHand("QdQh", board)
        player2 = HoldemHand("JdJs", board)        
        self.assertTrue(player1 > player2)
    
    def test_StraightDraw(self):
        # open ended straight draw
        board = HoldemHand.ParseHand("7s 8c Qh")
        pocket = HoldemHand.ParseHand("9d Td")
        outs = HandAnalysis.StraightDrawCount(pocket[0], board[0], 0)
        self.assertTrue(outs == 8)
        self.assertTrue(HandAnalysis.IsOpenEndedStraightDraw(pocket[0], board[0], 0))

        dead = HoldemHand.ParseHand("Ac Js")
        outs = HandAnalysis.StraightDrawCount(pocket[0], board[0], dead[0])
        self.assertTrue(outs == 7)

        # gut shot
        pocket = HoldemHand.ParseHand("Jd 9d")
        outs = HandAnalysis.StraightDrawCount(pocket[0], board[0], 0)
        self.assertTrue(outs == 4)
        self.assertFalse(HandAnalysis.IsOpenEndedStraightDraw(pocket[0], board[0], 0))
        self.assertTrue(HandAnalysis.IsGutShotStraightDraw(pocket[0], board[0], 0))
    
    def test_IsStraightDraw(self):
        pocket = "2c3d"
        board = "9d 5d 4c"
        dead = "AdJh"
        self.assertTrue(HandAnalysis.IsStraightDraw(pocket, board, dead))

        pocketMask = HoldemHand.ParseHand(pocket)[0]
        boardMask = HoldemHand.ParseHand(board)[0]
        self.assertTrue(HandAnalysis.IsStraightDraw(pocketMask | boardMask, 0))

if __name__ == '__main__':
    unittest.main()