from HandAnalysis import HandAnalysis
import unittest
from HandEvaluator import Hand
import numpy as np
from timeit import Timer, default_timer as timer
import time

class HandEvaluatorTest(unittest.TestCase):

    def test_ValidateHand(self):
        self.assertTrue(Hand.ValidateHand("As Ks"))
        self.assertTrue(Hand.ValidateHand("JdJh"))
        self.assertTrue(Hand.ValidateHand("2d 3c", "Ad 5d 4c"))
        self.assertTrue(Hand.ValidateHand("TdTh", "Jc3d3h 7h 9s"))
        self.assertTrue(Hand.ValidateHand("8c 9c Tc Jc Qc"))        
        self.assertFalse(Hand.ValidateHand("Xc Yx"))
        self.assertFalse(Hand.ValidateHand("AA"))
        self.assertFalse(Hand.ValidateHand("5s5c", "1h 3"))
        self.assertFalse(Hand.ValidateHand("KcKc"))
        self.assertFalse(Hand.ValidateHand("AcAd", "AcAdAcAd"))    
    
    def test_Comparable(self):
        board = "2s 3s 5s"
        player1 = Hand("AsKc", board)
        player2 = Hand("AdKs", board)
        self.assertTrue(player1 == player2)

        player2 = Hand("AdQd", board)
        self.assertTrue(player1 > player2)
        self.assertTrue(player2 < player1)

        board = "Qs Jh 7c"
        player1 = Hand("QdQh", board)
        player2 = Hand("JdJs", board)        
        self.assertTrue(player1 > player2)
    
    def test_StraightDraw(self):
        # open ended straight draw
        board = Hand.ParseHand("7s 8c Qh")
        pocket = Hand.ParseHand("9d Td")
        outs = HandAnalysis.StraightDrawCount(pocket[0], board[0], np.uint64(0))
        self.assertTrue(outs == 8)
        self.assertTrue(HandAnalysis.IsOpenEndedStraightDraw(pocket[0], board[0], np.uint64(0)))

        dead = Hand.ParseHand("Ac Js")
        outs = HandAnalysis.StraightDrawCount(pocket[0], board[0], dead[0])
        self.assertTrue(outs == 7)

        # gut shot
        pocket = Hand.ParseHand("Jd 9d")
        outs = HandAnalysis.StraightDrawCount(pocket[0], board[0], np.uint64(0))
        self.assertTrue(outs == 4)
        self.assertFalse(HandAnalysis.IsOpenEndedStraightDraw(pocket[0], board[0], np.uint64(0)))
        self.assertTrue(HandAnalysis.IsGutShotStraightDraw(pocket[0], board[0], np.uint64(0)))
    
    def test_IsStraightDraw(self):
        pocket = "2c3d"
        board = "9d 5d 4c"
        dead = "AdJh"
        self.assertTrue(HandAnalysis.IsStraightDraw(pocket, board, dead))

        pocketMask = Hand.ParseHand(pocket)[0]
        boardMask = Hand.ParseHand(board)[0]
        self.assertTrue(HandAnalysis.IsStraightDraw(pocketMask | boardMask, np.uint64(0)))

    def test_FlushDraw(self):
        pocket = "Th 2h"
        board = "9h Qh 7s"
        dead = "Ah Kc"
        # expected flush draw outs: 8
        outs = HandAnalysis.FlushDrawCount(Hand.ParseHand(pocket)[0], Hand.ParseHand(board)[0], Hand.ParseHand(dead)[0])
        self.assertTrue(outs == 8)

        # expected 9 outs
        outs = HandAnalysis.FlushDrawCount(Hand.ParseHand(pocket)[0] | Hand.ParseHand(board)[0], np.uint64(0))
        self.assertTrue(outs == 9)

        # expected 0 outs
        board = "9h Qh 7h"
        outs = HandAnalysis.FlushDrawCount(Hand.ParseHand(pocket)[0] | Hand.ParseHand(board)[0], np.uint64(0))
        self.assertTrue(outs == 0)

        pocket = Hand.ParseHand("6d 7d")[0]
        board = Hand.ParseHand("8d Tc 9d")[0]
        self.assertTrue(HandAnalysis.IsFlushDraw(pocket, board, np.uint64(0)))

        pocket = "7c 2d"
        board = "Ac 2h Tc"
        dead = "Jc Jd"
        self.assertFalse(HandAnalysis.IsFlushDraw(pocket, board, dead))

        # backdoor flush draw test
        pocket = "Jc Tc"
        board = "Ac 2h Td"
        dead = "Ad Kd"
        self.assertTrue(HandAnalysis.IsBackdoorFlushDraw(pocket, board, dead))
    
    def test_DrawCount(self):
        pocket = Hand.ParseHand("Kc Qd")[0]
        board = Hand.ParseHand("Kd Qc 5c 7s")[0]
        # draw to a full house
        # expected outs = 4
        outs = HandAnalysis.DrawCount(pocket, board, np.uint64(0), Hand.HandTypes.FULLHOUSE)
        self.assertTrue(outs == 4)

        # quad draw, outs = 1
        pocket = "3s 3c"
        board = "As 3d Th"
        dead = "Ac Ad"
        outs = HandAnalysis.DrawCount(pocket, board, dead, Hand.HandTypes.FOUR_OF_A_KIND)
        self.assertTrue(outs == 1)
    
    def test_HandDistance(self):
        pocket = Hand.ParseHand("As Ks")[0]
        board = Hand.ParseHand("Qs Ts 2c")[0]
        # expected distance is 46
        self.assertTrue(HandAnalysis.HandDistance(pocket, board) == 46)

        # the nuts, expected distance is 0
        board = Hand.ParseHand("Qs Ts 2c Js")[0]
        self.assertTrue(HandAnalysis.HandDistance(pocket, board) == 0)

        # second nuts, expected distance is 1
        pocket = Hand.ParseHand("Kc Ks")[0]
        board = Hand.ParseHand("Kd Ac 2h 7s")[0]
        self.assertTrue(HandAnalysis.HandDistance(pocket, board) == 1)
    
    def test_OutsMaskDiscounted(self):
        pocket = Hand.ParseHand("Qs Js")[0]
        board = Hand.ParseHand("9c Ts 7d 3c")[0]
        opponents = []
        outs = HandAnalysis.OutsMaskDiscounted(pocket, board, opponents)
        expected = "Ks 8s Kh 8h Kd 8d"
        self.assertTrue(expected == Hand.MaskToString(outs))

        opponents = [Hand.ParseHand("8s 9s")[0], Hand.ParseHand("Ac Ks")[0]]
        outs = HandAnalysis.OutsMaskDiscounted(pocket, board, opponents)
        expected = "Kh Qh 8h Kd Qd 8d Kc Qc 8c"
        self.assertTrue(expected == Hand.MaskToString(outs))

        # Kc does not help our hero and clubs puts our hero in danger
        opponents = [Hand.ParseHand("8s 9s")[0], Hand.ParseHand("Ac Kc")[0]]
        outs = HandAnalysis.OutsMaskDiscounted(pocket, board, opponents)
        expected = "Ks Kh Qh 8h Kd Qd 8d"
        self.assertTrue(expected == Hand.MaskToString(outs))

    def test_Outs(self):
        pocket = "As Ks"
        board = "2s 3s 5c 6d"
        opponents = [Hand.ParseHand("5s 6c")[0]]
        expectedOuts = 7 # because 6s does not improve our heroe's hand
        self.assertTrue(expectedOuts == HandAnalysis.Outs(Hand.ParseHand(pocket)[0], Hand.ParseHand(board)[0], opponents))
        expectedOuts = "Qs Js Ts 9s 8s 7s 4s"
        self.assertTrue(expectedOuts == HandAnalysis.OutCards(pocket, board, ["5s 6c"]))

        opponents = [Hand.ParseHand("6s 7s")[0]]
        expectedOuts = 13
        self.assertTrue(expectedOuts == HandAnalysis.Outs(Hand.ParseHand(pocket)[0], Hand.ParseHand(board)[0], opponents))
    
    def test_Suitedness(self):
        pocket = Hand.ParseHand("2d 3d")[0]
        self.assertTrue(HandAnalysis.IsSuited(pocket))

    def test_Connectivity(self):
        pocket = Hand.ParseHand("6h 7h")[0]
        self.assertTrue(HandAnalysis.GapCount(pocket) == 0)

        pocket = Hand.ParseHand("6h 8h")[0]
        self.assertTrue(HandAnalysis.GapCount(pocket) == 1)

        pocket = Hand.ParseHand("6h 9h")[0]     
        self.assertTrue(HandAnalysis.GapCount(pocket) == 2)

        pocket = Hand.ParseHand("6h Th")[0]      
        self.assertTrue(HandAnalysis.GapCount(pocket) == 3)
    
    # This function evaluates all possible 5 card poker hands and tallies the
    # results. The results should come up with know values. If not there is either
    # and error in the iterator function Hands() or the EvaluateType() function.
    def test_5CardHands(self):
        handTypes = [0] * 9
        count = 0

        # iterate through all possible 5 card hands
        for mask in Hand.Hands(5):
            handTypes[Hand.EvaluateType(mask, 5)[0]] += 1
            count += 1
        
        self.assertTrue(1302540 == handTypes[Hand.HandTypes.HIGH_CARD]);
        self.assertTrue(1098240 == handTypes[Hand.HandTypes.PAIR]);
        self.assertTrue(123552 == handTypes[Hand.HandTypes.TWO_PAIR]);
        self.assertTrue(54912 == handTypes[Hand.HandTypes.TRIPS]);
        self.assertTrue(10200 == handTypes[Hand.HandTypes.STRAIGHT]);
        self.assertTrue(5108 == handTypes[Hand.HandTypes.FLUSH]);
        self.assertTrue(3744 == handTypes[Hand.HandTypes.FULLHOUSE]);
        self.assertTrue(624, handTypes[Hand.HandTypes.FOUR_OF_A_KIND]);
        self.assertTrue(40 == handTypes[Hand.HandTypes.STRAIGHT_FLUSH]);
        self.assertTrue(2598960 == count);
    
    # This function evaluates all possible 7 card poker hands and tallies the
    # results. The results should come up with know values. If not there is either
    # and error in the iterator function Hands() or the EvaluateType() function.
    # THIS PASSED THE FIRST RUN. TOOK 17 MINUTES TO FINISH.
    # def test_7CardsHands(self):
    #     handTypes = [0] * 9
    #     count = 0

    #     # iterate through all possible 7 card hands
    #     for mask in Hand.Hands(7):
    #         handTypes[Hand.EvaluateType(mask, 7)[0]] += 1
    #         count += 1
        
    #     #self.assertTrue(58627800 == handTypes[Hand.HandTypes.HIGH_CARD]);
    #     self.assertTrue(58627800 == handTypes[Hand.HandTypes.PAIR]);
    #     self.assertTrue(31433400 == handTypes[Hand.HandTypes.TWO_PAIR]);
    #     self.assertTrue(6461620 == handTypes[Hand.HandTypes.TRIPS]);
    #     self.assertTrue(6180020 == handTypes[Hand.HandTypes.STRAIGHT]);
    #     self.assertTrue(4047644 == handTypes[Hand.HandTypes.FLUSH]);
    #     self.assertTrue(3473184 == handTypes[Hand.HandTypes.FULLHOUSE]);
    #     self.assertTrue(224848, handTypes[Hand.HandTypes.FOUR_OF_A_KIND]);
    #     self.assertTrue(41584 == handTypes[Hand.HandTypes.STRAIGHT_FLUSH]);
    #     self.assertTrue(133784560 == count);
    
    # Tests the Parser and the ToString for masks.
    def test_ParseWith5Cards(self):
        count = 0
        i = 0
        while i < 52:
            card = Hand.CardTable[i]
            self.assertTrue(Hand.ParseCard(card) == i)
            i += 1
        
        for mask in Hand.Hands(5):
            hand = Hand.MaskToString(mask)
            testMask = Hand.ParseHand(hand)[0]
            self.assertTrue(Hand.BitCount(testMask) == 5)
            self.assertTrue(mask == testMask)
            count += 1
    
    # Tests the parser and the ToString for masks.
    def test_ParserWith7Cards(self):
        for mask in Hand.RandomHands(7, 20.0):
            hand = Hand.MaskToString(mask)
            testMask = Hand.ParseHand(hand)[0]
            self.assertTrue(Hand.BitCount(testMask) == 7)
            self.assertTrue(mask == testMask)
    
    def test_RandomIterators(self):
        count = 0
        for mask in Hand.RandomHands(7, 20000):
            count += 1
        self.assertTrue(count == 20000)
        
        # startTime = time.perf_counter()
        # count = 0
        # for mask in Hand.RandomHandss(7, 2.5):
        #     count += 1
        # endTime = time.perf_counter()
        # self.assertGreater(endTime - startTime, 2.5)
    
    def test_SuitConsistency(self):
        x = np.uint64(0x1fff)
        mask = Hand.ParseHand("Ac Tc 2c 3c 4c")[0]
        sc = (mask >> Hand.GetClubOffset()) & x
        self.assertTrue(Hand.BitCount(sc) == 5)

        mask = Hand.ParseHand("Ad Td 2d 3d 4d")[0]
        sd = (mask >> Hand.GetDiamondOffset()) & x
        self.assertTrue(Hand.BitCount(sd) == 5)

        mask = Hand.ParseHand("Ah Th 2h 3h 4h")[0]
        sh = (mask >> Hand.GetHeartOffset()) & x
        self.assertTrue(Hand.BitCount(sh) == 5)

        mask = Hand.ParseHand("As Ts 2s 3s 4s")[0]
        ss = (mask >> Hand.GetSpadeOffset()) & x
        self.assertTrue(Hand.BitCount(ss) == 5)
    
    def test_BasicIterators(self):
        count = 0
        for mask in Hand.Hands(1):
            count += 1
        self.assertTrue(count == 52)

        count = 0
        for mask in Hand.Hands(2):
            count += 1
        self.assertTrue(count == 1326)

        count = 0
        for mask in Hand.Hands(3):
            count += 1
        self.assertTrue(count == 22100)

        count = 0
        for mask in Hand.Hands(4):
            count += 1
        self.assertTrue(count == 270725)

        count = 0
        for mask in Hand.Hands(5):
            count += 1
        self.assertTrue(count == 2598960)

        count = 0
        for mask in Hand.Hands(6):
            count += 1
        self.assertTrue(count == 20358520)

    def test_Analysis(self):
        # The outs are: Aces (1), Queens (4), Kinds (3), Jacks (3), Tens (3), Spades (9)
        outs = HandAnalysis.Outs(Hand.ParseHand("As Ks")[0], Hand.ParseHand("Js Ts Ad")[0], [])
        self.assertTrue(outs == 23)

        # The only outs are the remaining spades, but not the 5 of spades (7)
        outs = HandAnalysis.Outs(Hand.ParseHand("As Kd")[0], Hand.ParseHand("2s 3s 4s")[0], [Hand.ParseHand("6s 5d")[0]])
        self.assertTrue(outs == 7)

        # The outs are the remaining spades, aces, and kings (15)
        outs = HandAnalysis.Outs(Hand.ParseHand("As Ks")[0], Hand.ParseHand("2s 3s 4d")[0], [Hand.ParseHand("2d 6c")[0]])
        self.assertTrue(outs == 15)

        for mask in Hand.Hands(2):
            sum = 0
            player = [0.0] * 9
            opponent = [0.0] * 9
            result = HandAnalysis.HandPlayerMultiOpponentOdds(mask, 0)
        pass


if __name__ == '__main__':
    unittest.main()