from HandEvaluator import HoldemHand
from multipledispatch import dispatch
from timeit import default_timer as timer
import random

class HandAnalysis:
    DEFAULT_TIME_DURATION = 0.25

    # The classic HandStrength Calculation from page 21 of Aaron Davidson's
    # Masters Thesis
    # pocket - Pocket cards
    # board - Current board
    # returns hand strength as a percentage of hands won
    @staticmethod
    @dispatch(int, int)
    def HandStrength(pocket: int, board: int):
        win = 0.0
        count = 0.0

        if __debug__:
            if HoldemHand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if HoldemHand.BitCount(board) < 3 or HoldemHand.BitCount(board) > 5:
                raise Exception("Board must have 3, 4, or 5 cards for this calculation")
        
        ourRank = HoldemHand.Evaluate(pocket | board)
        for opponentHand in HoldemHand.Hands(0, pocket | board, 2):
            opponentRank = HoldemHand.Evaluate(opponentHand | board)
            if ourRank > opponentRank:
                win += 1.0
            elif ourRank == opponentRank:
                win += 0.5
            count += 1.0
        return win / count
    
    #TODO - require pocket query parser
    @staticmethod
    @dispatch(str, str, int, float)
    def HandStrength(pocketQuery: str, board: str, numOpponents: int, duration: float):
        pass

    #TODO
    @staticmethod
    @dispatch(int, int, int, float)
    def HandStrength(pocket: int, board: int, numOpponents: int, duration: float):
        win = 0.0
        count = 0.0        

        if __debug__:
            if HoldemHand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if HoldemHand.BitCount(board) > 5:
                raise Exception("Board must have 5 or less cards")
            if numOpponents < 1 or numOpponents > 9:
                raise Exception("May only select 1-9 opponents")

        startTime = timer()
        ourRank = HoldemHand.Evaluate(pocket | board)
        if numOpponents == 1:
            while timer() - startTime < duration:
                oppcards = HoldemHand.RandomHand(0, pocket | board, 2)
                opprank = HoldemHand.Evaluate(oppcards | board)
                if ourRank > opprank:
                    win += 1.0
                elif ourRank == opprank:
                    win += 0.5
                count += 1.0

        elif numOpponents == 2:
            while timer() - startTime < duration:
                opp1cards = HoldemHand.RandomHand(0, pocket | board, 2)
                opp2cards = HoldemHand.RandomHand(0, pocket | board | opp1cards, 2)
                opp1rank = HoldemHand.Evaluate(opp1cards | board)
                opp2rank = HoldemHand.Evaluate(opp2cards | board)

                if (ourRank > opp1rank) and (ourRank > opp2rank):
                    win += 1.0
                elif ourRank >= opp1rank and ourRank >= opp2rank:
                    win += 0.5
                count += 1.0
        
        elif numOpponents == 3:
            while timer() - startTime < duration:
                opp1cards = HoldemHand.RandomHand(0, pocket | board, 2)
                opp2cards = HoldemHand.RandomHand(0, pocket | board | opp1cards, 2)
                opp3cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards, 2)
                opp1rank = HoldemHand.Evaluate(opp1cards | board)
                opp2rank = HoldemHand.Evaluate(opp2cards | board)
                opp3rank = HoldemHand.Evaluate(opp3cards | board) 

                if (ourRank > opp1rank) and (ourRank > opp2rank) and (ourRank > opp3rank):
                    win += 1.0
                elif (ourRank >= opp1rank) and (ourRank >= opp2rank) and (ourRank >= opp3rank):
                    win += 0.5
                count += 1.0
        
        elif numOpponents == 4:
            while timer() - startTime < duration:
                opp1cards = HoldemHand.RandomHand(0, pocket | board, 2)
                opp2cards = HoldemHand.RandomHand(0, pocket | board | opp1cards, 2)
                opp3cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards, 2)
                opp4cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards, 2)
                opp1rank = HoldemHand.Evaluate(opp1cards | board)
                opp2rank = HoldemHand.Evaluate(opp2cards | board)
                opp3rank = HoldemHand.Evaluate(opp3cards | board)
                opp4rank = HoldemHand.Evaluate(opp4cards | board)

                if (ourRank > opp1rank) and (ourRank > opp2rank) \
                    and (ourRank > opp3rank) and (ourRank > opp4rank):
                    win += 1.0
                elif (ourRank >= opp1rank) and (ourRank >= opp2rank) \
                    and (ourRank >= opp3rank) and (ourRank >= opp4rank):
                    win += 0.5
                count += 1.0
        
        elif numOpponents == 5:
            while timer() - startTime < duration:
                opp1cards = HoldemHand.RandomHand(0, pocket | board, 2)
                opp2cards = HoldemHand.RandomHand(0, pocket | board | opp1cards, 2)
                opp3cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards, 2)
                opp4cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp1rank = HoldemHand.Evaluate(opp1cards | board)
                opp2rank = HoldemHand.Evaluate(opp2cards | board)
                opp3rank = HoldemHand.Evaluate(opp3cards | board)
                opp4rank = HoldemHand.Evaluate(opp4cards | board)
                opp5rank = HoldemHand.Evaluate(opp5cards | board)
            
                if (ourRank > opp1rank) and (ourRank > opp2rank) \
                    and (ourRank > opp3rank) and (ourRank > opp4rank) \
                    and (ourRank > opp5rank):
                    win += 1.0
                elif (ourRank >= opp1rank) and (ourRank >= opp2rank) \
                    and (ourRank >= opp3rank) and (ourRank >= opp4rank) \
                    and (ourRank >= opp5rank):
                    win += 0.5
                count += 1.0
        
        elif numOpponents == 6:
            while timer() - startTime < duration:
                opp1cards = HoldemHand.RandomHand(0, pocket | board, 2)
                opp2cards = HoldemHand.RandomHand(0, pocket | board | opp1cards, 2)
                opp3cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards, 2)
                opp4cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp6cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards, 2)
                opp1rank = HoldemHand.Evaluate(opp1cards | board)
                opp2rank = HoldemHand.Evaluate(opp2cards | board)
                opp3rank = HoldemHand.Evaluate(opp3cards | board)
                opp4rank = HoldemHand.Evaluate(opp4cards | board)
                opp5rank = HoldemHand.Evaluate(opp5cards | board)
                opp6rank = HoldemHand.Evaluate(opp6cards | board)
            
                if (ourRank > opp1rank) and (ourRank > opp2rank) \
                    and (ourRank > opp3rank) and (ourRank > opp4rank) \
                    and (ourRank > opp5rank) and (ourRank > opp6rank):
                    win += 1.0
                elif (ourRank >= opp1rank) and (ourRank >= opp2rank) \
                    and (ourRank >= opp3rank) and (ourRank >= opp4rank) \
                    and (ourRank >= opp5rank) and (ourRank >= opp6rank):
                    win += 0.5
                count += 1.0
        
        elif numOpponents == 7:
            while timer() - startTime < duration:
                opp1cards = HoldemHand.RandomHand(0, pocket | board, 2)
                opp2cards = HoldemHand.RandomHand(0, pocket | board | opp1cards, 2)
                opp3cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards, 2)
                opp4cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp6cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards, 2)
                opp7cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards, 2)
                opp1rank = HoldemHand.Evaluate(opp1cards | board)
                opp2rank = HoldemHand.Evaluate(opp2cards | board)
                opp3rank = HoldemHand.Evaluate(opp3cards | board)
                opp4rank = HoldemHand.Evaluate(opp4cards | board)
                opp5rank = HoldemHand.Evaluate(opp5cards | board)
                opp6rank = HoldemHand.Evaluate(opp6cards | board)
                opp7rank = HoldemHand.Evaluate(opp7cards | board)
            
                if (ourRank > opp1rank) and (ourRank > opp2rank) \
                    and (ourRank > opp3rank) and (ourRank > opp4rank) \
                    and (ourRank > opp5rank) and (ourRank > opp6rank) \
                    and (ourRank > opp7rank):
                    win += 1.0
                elif (ourRank >= opp1rank) and (ourRank >= opp2rank) \
                    and (ourRank >= opp3rank) and (ourRank >= opp4rank) \
                    and (ourRank >= opp5rank) and (ourRank >= opp6rank) \
                    and (ourRank >= opp7rank):
                    win += 0.5
                count += 1.0

        elif numOpponents == 8:
            while timer() - startTime < duration:
                opp1cards = HoldemHand.RandomHand(0, pocket | board, 2)
                opp2cards = HoldemHand.RandomHand(0, pocket | board | opp1cards, 2)
                opp3cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards, 2)
                opp4cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp6cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards, 2)
                opp7cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards, 2)
                opp8cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards | opp7cards, 2)
                opp1rank = HoldemHand.Evaluate(opp1cards | board)
                opp2rank = HoldemHand.Evaluate(opp2cards | board)
                opp3rank = HoldemHand.Evaluate(opp3cards | board)
                opp4rank = HoldemHand.Evaluate(opp4cards | board)
                opp5rank = HoldemHand.Evaluate(opp5cards | board)
                opp6rank = HoldemHand.Evaluate(opp6cards | board)
                opp7rank = HoldemHand.Evaluate(opp7cards | board)
                opp8rank = HoldemHand.Evaluate(opp8cards | board)
            
                if (ourRank > opp1rank) and (ourRank > opp2rank) \
                    and (ourRank > opp3rank) and (ourRank > opp4rank) \
                    and (ourRank > opp5rank) and (ourRank > opp6rank) \
                    and (ourRank > opp7rank) and (ourRank > opp8rank):
                    win += 1.0
                elif (ourRank >= opp1rank) and (ourRank >= opp2rank) \
                    and (ourRank >= opp3rank) and (ourRank >= opp4rank) \
                    and (ourRank >= opp5rank) and (ourRank >= opp6rank) \
                    and (ourRank >= opp7rank) and (ourRank >= opp8rank):
                    win += 0.5
                count += 1.0
        
        elif numOpponents == 9:
            while timer() - startTime < duration:
                opp1cards = HoldemHand.RandomHand(0, pocket | board, 2)
                opp2cards = HoldemHand.RandomHand(0, pocket | board | opp1cards, 2)
                opp3cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards, 2)
                opp4cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp6cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards, 2)
                opp7cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards, 2)
                opp8cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards | opp7cards, 2)
                opp9cards = HoldemHand.RandomHand(0, pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards | opp7cards | opp8cards, 2)
                opp1rank = HoldemHand.Evaluate(opp1cards | board)
                opp2rank = HoldemHand.Evaluate(opp2cards | board)
                opp3rank = HoldemHand.Evaluate(opp3cards | board)
                opp4rank = HoldemHand.Evaluate(opp4cards | board)
                opp5rank = HoldemHand.Evaluate(opp5cards | board)
                opp6rank = HoldemHand.Evaluate(opp6cards | board)
                opp7rank = HoldemHand.Evaluate(opp7cards | board)
                opp8rank = HoldemHand.Evaluate(opp8cards | board)
                opp9rank = HoldemHand.Evaluate(opp9cards | board)
            
                if (ourRank > opp1rank) and (ourRank > opp2rank) \
                    and (ourRank > opp3rank) and (ourRank > opp4rank) \
                    and (ourRank > opp5rank) and (ourRank > opp6rank) \
                    and (ourRank > opp7rank) and (ourRank > opp8rank) \
                    and (ourRank > opp9rank):
                    win += 1.0
                elif (ourRank >= opp1rank) and (ourRank >= opp2rank) \
                    and (ourRank >= opp3rank) and (ourRank >= opp4rank) \
                    and (ourRank >= opp5rank) and (ourRank >= opp6rank) \
                    and (ourRank >= opp7rank) and (ourRank >= opp8rank) \
                    and (ourRank >= opp9rank):
                    win += 0.5
                count += 1.0

        return win / count

    # This method returns the number of straight draws that are possible for the current mask
    # mask - current hand
    # dead - dead cards
    @staticmethod
    @dispatch(int, int)
    def StraightDrawCount(mask: int, dead: int):
        retval = 0

        # Get original mask value
        origType = HoldemHand.EvaluateType(mask)[0]

        # If current mask is better than a straight then return 0 outs
        if origType >= HoldemHand.HandTypes.STRAIGHT:
            return retval
        
        # look ahead one card
        for card in HoldemHand.Hands(0, mask | dead, 1):

            # Get new mask value
            newHandType = HoldemHand.EvaluateType(mask | card)[0]

            # Include straight flush as this will ensure outs is always the maximum
            if newHandType == HoldemHand.HandTypes.STRAIGHT or newHandType == HoldemHand.HandTypes.STRAIGHT_FLUSH:
                retval += 1
            
        return retval
    
    # The method returns the number of straight draws that are possible for the player and board configuration.   
    # This method filters the results so only player hand improvements are counted.
    # player - Two card mask making up the players pocket cards
    # board - The community cards
    # dead - Dead cards
    @staticmethod
    @dispatch(int, int, int)
    def StraightDrawCount(player: int, board: int, dead: int):
        retval = 0
        ncards = HoldemHand.BitCount(player | board)

        if __debug__:
            if HoldemHand.BitCount(player) != 2:
                raise Exception("Player must have exactly 2 cards")
            if HoldemHand.BitCount(board) != 3 and HoldemHand.BitCount(board) != 4:
                raise Exception("Board must contain 3 or 4 cards")
        
        playerOrigHandVal = HoldemHand.Evaluate(player | board, ncards);

        if HoldemHand.HandType(playerOrigHandVal) >= HoldemHand.HandTypes.STRAIGHT:
            return retval
        
        for card in HoldemHand.Hands(0, board | player | dead, 1):
            playerNewHandVal = HoldemHand.Evaluate(player | board | card, ncards + 1)
            playerHandType = HoldemHand.HandType(playerNewHandVal);

            # Include straight flush as this will ensure outs is always the maximum
            if playerHandType == HoldemHand.HandTypes.STRAIGHT or playerHandType == HoldemHand.HandTypes.STRAIGHT_FLUSH:
                boardHandVal = HoldemHand.Evaluate(board | card)

                if (HoldemHand.HandType(playerNewHandVal) > HoldemHand.HandType(boardHandVal)) \
                    or (HoldemHand.HandType(playerNewHandVal) == HoldemHand.HandType(boardHandVal) \
                    and HoldemHand.HandType(playerNewHandVal) > HoldemHand.TopCard(boardHandVal)):
                    retval += 1
        
        return retval

    # Returns true if the mask is an open ended straight draw
    # mask - Players pocket cards mask
    # dead - Community card mask
    # returns true if the combined mask is an open ended straight draw
    @staticmethod
    @dispatch(str, str)
    def IsOpenEndedStraightDraw(mask: str, dead: str):
        return HandAnalysis.IsOpenEndedStraightDraw(HoldemHand.ParseHand(mask)[0], HoldemHand.ParseHand(dead)[0])

    # Returns true if the combined mask is an open ended straight draw. Only straight possibilities that
    # improve the player's mask are considered in this method
    # pocket - Players pocket cards mask
    # board - Community card mask
    # dead - Dead cards
    # Returns true if the combined mask is an open ended straight draw
    @staticmethod
    @dispatch(int, int, int)
    def IsOpenEndedStraightDraw(pocket: int, board: int, dead: int):
        if __debug__:
            if HoldemHand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if HoldemHand.BitCount(board) != 3 and HoldemHand.BitCount(board) != 4:
                raise Exception("Board must have 3 or 4 cards for this calculation")
        return HandAnalysis.IsOpenEndedStraightDraw(pocket | board, 0) and HandAnalysis.StraightDrawCount(pocket, board, dead) > 0
    
    # Returns true if the combined mask is an open ended straight draw
    # mask - Players pocket cards mask
    # dead - Communit cards mask
    # Returns true if the combined mask is an open ended straight draw
    @staticmethod
    @dispatch(int, int)
    def IsOpenEndedStraightDraw(mask: int, dead: int):
        if __debug__:
            if mask and dead != 0:
                raise Exception("Mask and dead cards must not have any cards in common")
            if HoldemHand.BitCount(mask) < 4 or HoldemHand.BitCount(mask) > 6:
                raise Exception("Mask must have 4-6 cards")
        return HandAnalysis.StraightDrawCount(mask, 0) > 4 and HandAnalysis.StraightDrawCount(mask, dead)

    # Returns true if the mask is an open ended straight draw
    # mask - Players pocket cards mask
    # dead - Community card mask
    # Returns true if the combined mask is an open ended straight draw    
    @staticmethod
    @dispatch(str, str)
    def IsOpenEndedStraightDraw(mask: str, dead: str):
        return HandAnalysis.IsOpenEndedStraightDraw(HoldemHand.ParseHand(mask)[0], HoldemHand.ParseHand(dead)[0])

    # Return true if the combined cards contains a gut shot straight draw
    # pocket - Players pocket cards mask
    # board - Communit board mask
    # dead - Dead cards    
    @staticmethod
    @dispatch(int, int, int)
    def IsGutShotStraightDraw(pocket: int, board: int, dead: int):
        if __debug__:
            if HoldemHand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if HoldemHand.BitCount(board) != 3 and HoldemHand.BitCount(board) != 4:
                raise Exception("Board must have 3 or 4 cards for this calculation")
        
        
        return HandAnalysis.IsGutShotStraightDraw(pocket | board, dead) and HandAnalysis.StraightDrawCount(pocket, board, dead) > 0

    # mask - Current mask
    # dead - Dead cards
    @staticmethod
    @dispatch(int, int)
    def IsGutShotStraightDraw(mask: int, dead: int):
        if __debug__:
            if mask & dead != 0:
                raise Exception("Mask and dead cards must not have any cards in common")
            if HoldemHand.BitCount(mask) < 4 or HoldemHand.BitCount(mask) > 6:
                raise Exception("mask must have 4-6 cards")
        
        return HandAnalysis.StraightDrawCount(mask, 0) <= 4 and HandAnalysis.StraightDrawCount(mask, dead) > 0
    
    # mask - Current mask
    # dead - Dead cards
    @staticmethod
    @dispatch(str, str)
    def IsGutShotStraightDraw(mask: str, dead: str):
        return HandAnalysis.IsGutShotStraightDraw(HoldemHand.ParseHand(mask)[0], HoldemHand.ParseCard(dead)[0])




