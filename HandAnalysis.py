from os import stat

from numpy.lib.shape_base import expand_dims
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

    # Returns true if the passed mask only needs one card to make a straight.
    # Note that the pocket cards must contains at least one card in the 
    # combined straight.
    # pocket - Players pocket mask
    # board - Community board
    # dead - Dead cards
    @staticmethod
    @dispatch(int, int, int)
    def IsStraightDraw(pocket: int, board: int, dead: int):
        return HandAnalysis.StraightDrawCount(pocket, board, dead) > 0
    
    @staticmethod
    @dispatch(int, int)
    def IsStraightDraw(mask: int, dead: int):
        return HandAnalysis.StraightDrawCount(mask, dead) > 0

    @staticmethod
    @dispatch(str, str)
    def IsStraightDraw(mask: str, dead: str):
        return HandAnalysis.IsStraightDraw(HoldemHand.ParseHand(mask)[0], HoldemHand.ParseHand(dead)[0])
    
    @staticmethod
    @dispatch(str, str, str)
    def IsStraightDraw(pocket: str, board: str, dead: str):
        if __debug__:
            if not HoldemHand.ValidateHand(pocket):
                raise Exception("Invalid pocket hand")
            if not HoldemHand.ValidateHand(board):
                raise Exception("Invalid board cards")
        pocketMask = HoldemHand.ParseHand(pocket)[0]
        boardMask = HoldemHand.ParseHand(board)[0]
        deadMask = HoldemHand.ParseHand(dead)[0]
        return HandAnalysis.IsStraightDraw(pocketMask, boardMask, deadMask)
    
    # Returns the count of adjacent cards
    # pocket - Players pocket cards mask
    # Community card mask
    @staticmethod
    @dispatch(int, int)
    def CountContiguous(pocket: int, board: int):
        mask = pocket | board
        bf = HoldemHand.CardMask(mask, HoldemHand.CLUBS) | HoldemHand.CardMask(mask, HoldemHand.DIAMONDS) \
                | HoldemHand.CardMask(mask, HoldemHand.HEARTS) | HoldemHand.CardMask(mask, HoldemHand.SPADES)
        if __debug__: 
            if HoldemHand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if HoldemHand.BitCount(board) != 3 and HoldemHand.BitCount(board) != 4:
                raise Exception("Board must have 3 or 4 cards for this calculation")    

            masks = [0x7f, 0x3f, 0x1f, 0xf, 0x7, 0x3]
            i = 0
            while i < len(masks):
                count = HoldemHand.BitCount(masks[i])
                contmask = 0
                offset = 13 - count
                while offset >= 0:                    
                    contmask = masks[i] << offset
                    if bf & contmask == contmask:
                        return count
                    offset -= 1
                
                contmask = 0x1000 | (masks[i] >> 1)
                if bf & contmask == contmask:
                    return count
                i += 1
            
            return 0
        else:
            return HandAnalysis.__ContiguousCountTable[bf]

    # Returns the count of adjacent cards
    # mask - current hand    
    @staticmethod
    @dispatch(int)
    def CountContiguous(mask: int):
        clubs = HoldemHand.CardMask(mask, HoldemHand.CLUBS)
        diamonds = HoldemHand.CardMask(mask, HoldemHand.DIAMONDS)
        hearts = HoldemHand.CardMask(mask, HoldemHand.Hands)
        spades = HoldemHand.CardMask(mask, HoldemHand.SPADES)
        return HandAnalysis.__ContiguousCountTable[clubs | diamonds | hearts | spades]    

    # Counts the number of hands that are a flush with one more drawn card
    # mask - Hand
    # dead - Cards not allowed to be drawn
    @staticmethod
    @dispatch(int, int)
    def FlushDrawCount(mask: int, dead: int):
        retval = 0

        # Get original mask value
        handType = HoldemHand.EvaluateType(mask)[0]

        # if current mask is better than a straight then return 0 outs
        if handType >= HoldemHand.HandTypes.FLUSH:
            return retval
        
        # look ahead one card
        for card in HoldemHand.Hands(0, mask | dead, 1):
            handType = HoldemHand.EvaluateType(mask | card)[0]

            # include straight flush as this will ensure outs is always the maximum
            if handType == HoldemHand.HandTypes.FLUSH or handType == HoldemHand.HandTypes.STRAIGHT_FLUSH:
                retval += 1
        
        return retval
    
    # Counts the number of hands that are a flush with one more drawn card. However,
    # Flush hands that only improve the board are not considered
    # player - Players two card hand
    # board - Board cards
    # dead - Dead cards
    @staticmethod
    @dispatch(int, int, int)
    def FlushDrawCount(player: int, board: int, dead: int):
        retval = 0
        if __debug__:
            if HoldemHand.BitCount(player) != 2:
                raise Exception("Player must have exactly 2 cards")
            if HoldemHand.BitCount(board) != 3 and HoldemHand.BitCount(board) != 4:
                raise Exception("Board must contain 3 or 4 cards")
        
        # Get original mask value
        playerOrigHandType = HoldemHand.EvaluateType(player | board)[0]

        # if current mask better than a straight then return 0 outs
        if playerOrigHandType == HoldemHand.HandTypes.FLUSH or \
            playerOrigHandType == HoldemHand.HandTypes.STRAIGHT_FLUSH:
            return retval
        
        # look ahead one card
        for card in HoldemHand.Hands(0, board | player | dead, 1):
            # get new mask value
            playerNewHandValue = HoldemHand.Evaluate(player | board | card)
            boardNewHandValue = HoldemHand.Evaluate(board | card)

            # include straight flush as this will ensure outs is always the maximum
            if HoldemHand.HandType(playerNewHandValue) == HoldemHand.HandTypes.FLUSH or \
                HoldemHand.HandType(playerNewHandValue) == HoldemHand.HandTypes.STRAIGHT_FLUSH:
                # if the mask improved, increment out
                if HoldemHand.HandType(playerNewHandValue) > HoldemHand.HandType(boardNewHandValue) or \
                    HoldemHand.HandType(playerNewHandValue) == HoldemHand.HandType(boardNewHandValue) and \
                    HoldemHand.TopCard(playerNewHandValue) > HoldemHand.TopCard(boardNewHandValue):
                    retval += 1
            
        return retval

    # Returns true if there are 4 cards of the same suit
    # pocket - Players pocket cards mask
    # board - Communit card mask
    # dead - dead cards
    @staticmethod
    @dispatch(int, int, int)
    def IsFlushDraw(pocket: int, board: int, dead: int):
        if __debug__:
            if HoldemHand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if HoldemHand.BitCount(board) != 3 and HoldemHand.BitCount != 4:
                raise Exception("board must have 3 or 4 cards for this calculation")

        return HandAnalysis.FlushDrawCount(pocket, board, dead) > 0

    # Returns true if the hand is a flush draw
    # mask - cards
    # dead - dead cards
    @staticmethod
    @dispatch(int, int)
    def IsFlushDraw(mask: int, dead: int):
        return HandAnalysis.FlushDrawCount(mask, dead) > 0    

    # Returns if there are 4 cards of the same suit
    # pocket - Player's pocket cards
    # board community cards
    # dead - Dead cards
    @staticmethod
    @dispatch(str, str, str)
    def IsFlushDraw(pocket: str, board: str, dead: str):
        if __debug__:
            if not HoldemHand.ValidateHand(pocket):
                raise Exception("Invalid pocket cards")
            if not HoldemHand.ValidateHand(board):
                raise Exception("Invalid board")
        
        return HandAnalysis.FlushDrawCount(HoldemHand.ParseHand(pocket)[0], HoldemHand.ParseHand(board)[0], HoldemHand.ParseHand(dead)[0]) > 0

    # Returns true if there are three cards of the same suit. 
    # The pocket cards must have at least one card in that suit.
    # pocket - Players pocket cards mask
    # board - Community card mask
    # dead - Dead cards
    @staticmethod
    @dispatch(int, int, int)
    def IsBackdoorFlushDraw(pocket: int, board: int, dead: int):
        if __debug__:
            if HoldemHand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if HoldemHand.BitCount(board) != 3 and HoldemHand.BitCount(board) != 4:
                raise Exception("Board must have 3 or 4 cards for this calculation")
        
        mask = pocket | board
        currentType = HoldemHand.EvaluateType(mask)[0]
        if currentType >= HoldemHand.HandTypes.FLUSH:
            return False
        
        ss = (mask >> HoldemHand.GetSpadeOffset()) & 0x1FFF
        sc = (mask >> HoldemHand.GetClubOffset()) & 0x1FFF
        sd = (mask >> HoldemHand.GetDiamondOffset()) & 0x1FFF
        sh = (mask >> HoldemHand.GetHeartOffset()) & 0x1FFF

        if HoldemHand.BitCount(ss) == 3:
            ps = (pocket >> HoldemHand.GetSpadeOffset()) & 0x1fff
            return ps != 0
        elif HoldemHand.BitCount(sc) == 3:
            pc = (pocket >> HoldemHand.GetClubOffset()) & 0x1fff
            return pc != 0
        elif HoldemHand.BitCount(sd) == 3:
            pd = (pocket >> HoldemHand.GetDiamondOffset()) & 0x1fff
            return pd != 0
        elif HoldemHand.BitCount(sh) == 3:
            ph = (pocket >> HoldemHand.GetHeartOffset()) & 0x1fff
            return ph != 0
        
        return False

    # Returns true if there are three cards of the same suit. 
    # The pocket cards must have at least one card in that suit.    
    # pocket - players pocket cards
    # board - Community cards
    # dead - Dead cards
    @staticmethod
    @dispatch(str, str, str)
    def IsBackdoorFlushDraw(pocket: str, board: str, dead: str):
        if __debug__:
            if not HoldemHand.ValidateHand(pocket):
                raise Exception("Invalid pocket cards")
            if not HoldemHand.ValidateHand(board):
                raise Exception("Invalid board")
        
        return HandAnalysis.IsBackdoorFlushDraw(HoldemHand.ParseHand(pocket)[0], HoldemHand.ParseHand(board)[0], HoldemHand.ParseHand(dead)[0])

    # The method returns the number of draws that are possible for the
    # specified HandType. This method only returns the counts that improve the 
    # player's mask rather than just the board. Because of this subtle distinction,
    # DrawCount(player, board, dead, type) doesn't necessarily return the same value as
    # DrawCount(player | board, dead, type).
    # player - Two card mask making up the players pocket cards
    # board - The community cards
    # dead - Dead cards
    # handType - the type of mask to count draws for
    @staticmethod
    @dispatch(int, int, int, int)
    def DrawCount(player: int, board: int, dead: int, handType: int):
        retval = 0
        if __debug__:
            if HoldemHand.BitCount(player) != 2:
                raise Exception("Player must have exactly two cards")
            if HoldemHand.BitCount(board) != 3 and HoldemHand.BitCount(board) != 4:
                raise Exception("Board must contain 3 or 4 cards for this calculation")
            if (board | player) & dead != 0: 
                raise Exception("Player and board must not contain dead cards")
        
        # Get original mask value
        playerOrigHandVal = HoldemHand.Evaluate(player | board)

        if HoldemHand.HandType(playerOrigHandVal) > handType:
            return 0
        
        # look ahead one card
        for card in HoldemHand.Hands(0, board | player | dead, 1):
            # get new mask value
            playerNewHandVal = HoldemHand.Evaluate(player | board | card)

            # Get new board value
            boardHandVal = HoldemHand.Evaluate(board | card)

            # Is the new mask better than the old one? We don't
            # want to know about supesizing the kickers so this
            # ensures that mask moved up in mask type
            handImproved = HoldemHand.HandType(playerNewHandVal) > HoldemHand.HandType(playerOrigHandVal)

            # if the mask improved and it matches the specified type, return true
            handStrongerThanBoard = playerNewHandVal > boardHandVal

            if handImproved and handStrongerThanBoard and HoldemHand.HandType(playerNewHandVal) == handType:
                retval += 1

        return retval

    # The method returns the number of draws that are possible for the
    # specified HandType. Note that DrawCount(pocket, board, dead, type) is not
    # necessarily the same as DrawCount(pocket | board, dead, type). 
    # 
    # This method returns all possible draws that are the same as the requested type.
    # mask - hand
    # dead - Dead cards
    # handType - The type of mask to count draws for
    @staticmethod
    @dispatch(int, int, int)
    def DrawCount(mask: int, dead: int, handType: int):
        retval = 0
        if HoldemHand.BitCount(mask) >=7:
            raise Exception("mask must contain less than 7 cards")
        if mask & dead != 0:
            raise Exception("mask must not contain dead cards")

        playerOriginalHandType = HoldemHand.EvaluateType(mask)[0]
        if playerOriginalHandType >= handType:
            return 0

        # Look ahead one card
        for card in HoldemHand.Hands(0, mask | dead, 1):
            # Get new mask value
            playerNewHandType = HoldemHand.EvaluateType(mask | card)[0]

            if playerNewHandType > playerOriginalHandType and playerNewHandType == handType:
                retval += 1

        return retval        
    

    # The method returns the number of draws that are possible for the
    # specified HandType.
    # player - Two card mask making up the players pocket cards
    # board - The community cards
    # dead - Dead cards
    # handType - The type of mask to count draws for
    @staticmethod
    @dispatch(str, str, str, int)
    def DrawCount(player: str, board: str, dead: str, handType: int):
        if __debug__:
            if not HoldemHand.ValidateHand(player):
                raise Exception("Invalid pocket cards")
            if not HoldemHand.ValidateHand(board):
                raise Exception("Invalid board")
        
        return HandAnalysis.DrawCount(HoldemHand.ParseHand(player)[0], HoldemHand.ParseHand(board)[0], HoldemHand.ParseHand(dead)[0], handType)
    
    # This method returns the mask distance from the best possible
    # mask given this board (no draws are considered). The value 0 is the 
    # best possible mask. The value 1 is the next best mask and so on.
    # pocket - The players pocket mask
    # board - The board mask
    @staticmethod
    @dispatch(int, int)
    def HandDistance(pocket: int, board: int):
        if __debug__:
            if HoldemHand.BitCount(pocket) != 2:
                raise Exception("Player must have exactly two cards")
            if HoldemHand.BitCount(board) != 3 and HoldemHand.BitCount(board) !=4:
                raise Exception("Board must containt 3 or 4 cards")
        hv = 0
        handValues = []
        pocketHandVal = HoldemHand.Evaluate(pocket | board)
        for p in HoldemHand.Hands(0, board, 2):
            hv = HoldemHand.Evaluate(p | board)            
            if hv not in handValues:
                handValues.append(hv)
        
        handValues = sorted(handValues)
        count = len(handValues) - 1
        for handval in handValues:
            if handval == pocketHandVal:
                return count
            count -= 1
        
        return -1
    
    # Returns the number of discouted outs possible with the next card.
    # 
    # Players pocket cards
    # The board (must contain either 3 or 4 cards)
    # A list of zero or more opponent cards.
    # The count of the number of single cards that improve the current hand applying the following discouting rules:
    # 1) Drawing to a pair must use an over card (ie a card higher than all those on the board)
    # 2) Drawing to 2 pair / pairing your hand is discounted if the board is paired (ie your 2 pair drawing deat to trips)
    # 3) Drawing to a hand lower than a flush must not make a 3 suited board or the board be 3 suited.
    # 4) Drawing to a hand lower than a stright, the flop must not be 3card connected or on the turn
    # allow a straight to be made with only 1 pocket card or the out make a straight using only 1 card.
    # 
    # Function provided by Matt Baker.    
    # player - players pocket hand
    # board - board cards so far
    # opponents - Opponents pocket hands
    @staticmethod
    def OutsDiscounted(player: int, board: int, opponentsList):
        return HoldemHand.BitCount(HandAnalysis.OutsMaskDiscounted(player, board, opponentsList))
    
    # Creates a Hand mask with the cards that will improve the specified players hand
    # against a list of opponents or if no opponents are list just the cards that improve the 
    # players current hand. 
    # 
    # This implements the concept of 'discounted outs'. That is outs that will improve the
    # players hand, but not potentially improve an opponents hand to an even better one. For
    # example drawing to a straight that could end up loosing to a flush.
    # 
    # Please note that this only looks at single cards that improve the hand and will not specifically
    # look at runner-runner possiblities.
    # 
    # Players pocket cards
    # The board (must contain either 3 or 4 cards)
    # A list of zero or more opponent pocket cards
    # A mask of all of the cards that improve the hand applying the following discouting rules: 
    # 1) Drawing to a pair must use an over card (ie a card higher than all those on the board)
    # 2) Drawing to 2 pair / pairing your hand is discounted if the board is paired (ie your 2 pair drawing deat to trips)
    # 3) Drawing to a hand lower than a flush must not make a 3 suited board or the board be 3 suited.
    # 4) Drawing to a hand lower than a stright, the flop must not be 3card connected or on the turn
    # allow a straight to be made with only 1 pocket card or the out make a straight using only 1 card. 
    # 
    # 
    # Function provided by Matt Baker.
    # player - Players pocket hand
    # board - Board mask
    # opponents - Opponent pocket hands
    # Returns a mask of cards that are probably outs
    @staticmethod
    def OutsMaskDiscounted(player: int, board: int, opponentsList):
        retval = 0
        dead = 0
        ncards = HoldemHand.BitCount(player | board)

        if __debug__:
            if HoldemHand.BitCount(player) != 2:
                raise Exception("Player pocket must have exactly two cards")
            if ncards != 5 and ncards != 6:
                raise Exception("Outs only make sense after the flop and before the river")
        if len(opponentsList) > 0:
            for opp in opponentsList:
                if HoldemHand.BitCount(opp) != 2:
                    raise Exception("Opponent hand ust have exactly two cards")
                dead |= opp
            playerOrigHandVal = HoldemHand.Evaluate(player | board, ncards);
            playerOrigHandType = HoldemHand.HandType(playerOrigHandVal)
            playerOrigTopCard = HoldemHand.TopCard(playerOrigHandVal)

            for card in HoldemHand.Hands(0, dead | board | player, 1):
                bWinFlag = True
                playerNewHandVal = HoldemHand.Evaluate(player | board | card, ncards + 1)
                playerNewHandType = HoldemHand.HandType(playerNewHandVal)
                playerNewTopCard = HoldemHand.TopCard(playerNewHandVal)
                for oppmask in opponentsList:
                    oppHandVal = HoldemHand.Evaluate(oppmask | board | card, ncards + 1)
                    bWinFlag = oppHandVal < playerNewHandVal and \
                        (playerNewHandType > playerOrigHandType or (playerNewHandType == playerOrigHandType and playerNewTopCard > playerOrigTopCard))
                    if not bWinFlag:
                        break
                if bWinFlag:
                    retval |= card
        else:
            # Look at the cards that improve the hand
            playerOrigHandVal = HoldemHand.Evaluate(player | board, ncards)
            playerOrigHandType = HoldemHand.HandType(playerOrigHandVal)
            playerOrigTopCard = HoldemHand.TopCard(playerOrigHandVal)
            boardOrigHandVal = HoldemHand.Evaluate(board)
            boardOrigHandType = HoldemHand.HandType(boardOrigHandVal)
            boardOrigTopCard = HoldemHand.TopCard(boardOrigHandVal)

            # Look at players pocket cards for special cases
            playerPocketHandVal = HoldemHand.Evaluate(player)
            playerPocketHandType = HoldemHand.HandType(playerPocketHandVal)

            # Separate out by suit
            sc = (board >> HoldemHand.GetClubOffset()) & 0x1fff
            sd = (board >> HoldemHand.GetDiamondOffset()) & 0x1fff
            sh = (board >> HoldemHand.GetHeartOffset()) & 0x1fff
            ss = (board >> HoldemHand.GetSpadeOffset()) & 0x1fff

            # Check if board is 3 suited
            discountSuitedBoard = (HoldemHand.nBitsTable[sc] > 2) or (HoldemHand.nBitsTable[sd] > 2) or (HoldemHand.nBitsTable[sh] > 2) or (HoldemHand.nBitsTable[ss] > 2)

            # Check if board is 3 connected on the flop. a dangerous board:
            # 3 possible straights using 2 pocket cards and a higher chance
            # of 2 pair; player often play 2 connected cards which can hit
            countContiguous = 0
            boardCardCount = HoldemHand.BitCount(board)

            if boardCardCount == 3:
                bf = HoldemHand.CardMask(board, HoldemHand.CLUBS) or HoldemHand.CardMask(board, HoldemHand.DIAMONDS) or HoldemHand.CardMask(board, HoldemHand.HEARTS) or HoldemHand.CardMask(board, HoldemHand.SPADES)
                if HoldemHand.BitCount(0x1800 & bf) == 2: countContiguous += 1
                if HoldemHand.BitCount(0xc00 & bf) == 2: countContiguous += 1
                if HoldemHand.BitCount(0x600 & bf) == 2: countContiguous += 1
                if HoldemHand.BitCount(0x300 & bf) == 2: countContiguous += 1
                if HoldemHand.BitCount(0x180 & bf) == 2: countContiguous += 1
                if HoldemHand.BitCount(0xc0 & bf) == 2: countContiguous += 1
                if HoldemHand.BitCount(0x60 & bf) == 2: countContiguous += 1
                if HoldemHand.BitCount(0x30 & bf) == 2: countContiguous += 1
                if HoldemHand.BitCount(0x18 & bf) == 2: countContiguous += 1
                if HoldemHand.BitCount(0xc & bf) == 2: countContiguous += 1;
                if HoldemHand.BitCount(0x6 & bf) == 2: countContiguous += 1;
                if HoldemHand.BitCount(0x3 & bf) == 2: countContiguous += 1;
                if HoldemHand.BitCount(0x1001 & bf) == 2: countContiguous += 1;
            
            discountStraight = countContiguous > 2

            # Look ahead one card
            for card in HoldemHand.Hands(0, dead | board | player, 1):
                boardNewHandVal = HoldemHand.Evaluate(board | card)
                boardNewHandType = HoldemHand.HandType(boardNewHandVal)
                boardNewTopCard = HoldemHand.TopCard(boardNewHandVal)
                playerNewHandVal = HoldemHand.Evaluate(player | board | card, ncards + 1)
                playerNewHandType = HoldemHand.HandType(playerNewHandVal)
                playerNewTopCard = HoldemHand.TopCard(playerNewHandVal)
                playerImproved = HoldemHand.TopCard(playerNewHandVal)
                playerStrongerThanBoard = playerNewHandType > boardNewHandType or (playerNewHandType == boardNewHandType and playerNewTopCard > boardNewTopCard)

                if playerImproved and playerStrongerThanBoard:
                    isOut = False
                    discountSuitedOut = False
                    if not discountSuitedBoard:
                        cc = (card >> HoldemHand.GetClubOffset()) & 0x1fff
                        cd = (card >> HoldemHand.GetDiamondOffset()) & 0x1fff
                        ch = (card >> HoldemHand.GetHeartOffset()) & 0x1fff
                        cs = (card >> HoldemHand.GetSpadeOffset()) & 0x1fff

                        # Check if card will make a 3 suited board
                        discountSuitedOut = (HoldemHand.nBitsTable[sc] > 1 and HoldemHand.nBitsTable[cc] == 1) \
                            or (HoldemHand.nBitsTable[sd] > 1 and HoldemHand.nBitsTable[cd] == 1) \
                            or (HoldemHand.nBitsTable[sh] > 1 and HoldemHand.nBitsTable[ch] == 1) \
                            or (HoldemHand.nBitsTable[ss] > 1 and HoldemHand.nBitsTable[cs] == 1)
                        
                    # Check if board is 4 connected or card + board is 4 connected
                    # Dangerous board: straight using 1 pocket card only
                    if boardCardCount != 4:
                        continue

                    # We need to check for the following:
                    # 9x,8x,7x,6x (4 in a row)
                    # 9x,8x,7x,5x (3 in a row with a 1 gap connected card)
                    # 9x,8x,6x,5x (2 connected with a 1 gap connected in the middle)
                    countContiguous = 0
                    bf = HoldemHand.CardMask(board | card, HoldemHand.CLUBS) | HoldemHand.CardMask(board | card, HoldemHand.DIAMONDS) | HoldemHand.CardMask(board | card, HoldemHand.HEARTS) | HoldemHand.CardMask(board | card, HoldemHand.SPADES)

                    # AxKx
                    if HoldemHand.BitCount(0x1800 & bf) == 2:
                        countContiguous += 1
                    
                    # KxQx
                    if HoldemHand.BitCount(0xc00 & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1 and HoldemHand.BitCount(0x300 & bf) == 2:
                            # 2 connected with a 1 gap connected in the middle
                            discountStraight = True                            
                        countContiguous = 0
                    
                    # QxJx
                    if HoldemHand.BitCount(0x600 & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if HoldemHand.BitCount(0x100 & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for a T
                            if HoldemHand.BitCount(0x100 & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        countContiguous = 0

                    # JxTx
                    if HoldemHand.BitCount(0x300 & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if HoldemHand.BitCount(0xc0 & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 9x
                            if HoldemHand.BitCount(0x00 & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True

                        countContiguous = 0
                    
                    # Tx9x
                    if HoldemHand.BitCount(0x180 & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if HoldemHand.BitCount(0x60 & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 8x or Ax
                            if HoldemHand.BitCount(0x1040 & bf) == 1:
                                discountStraight = True
                        elif countContiguous == 3:
                            discountStraight = True
                        
                        countContiguous = 0
                    
                    # 9x8x
                    if HoldemHand.BitCount(0xc0 & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if HoldemHand.BitCount(0x30 & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 7x or Kx
                            if HoldemHand.BitCount(0x820 & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                        
                        countContiguous = 0
                    
                    # 8x7x
                    if HoldemHand.BitCount(0x60 & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if HoldemHand.BitCount(0x18 & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 6x or Qx
                            if HoldemHand.BitCount(0x410 & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                        
                        countContiguous = 0
                    
                    # 7x6x
                    if HoldemHand.BitCount(0x30 & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if HoldemHand.BitCount(0xc & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 5x or Jx
                            if HoldemHand.BitCount(0x208 & bf) == 1:
                                # 3 in a row with a gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                        
                        countContiguous = 0
                    
                    # 6x5x
                    if HoldemHand.BitCount(0x18 & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if HoldemHand.BitCount(0x6 & bf) == 2:
                                discountStraight = True
                        elif countContiguous == 2:
                            if HoldemHand.BitCount(0x104 & bf) == 1:
                                discountStraight = True
                        elif countContiguous == 3:
                            discountStraight = True
                        
                        countContiguous = 0
                    
                    # 5x4x
                    if HoldemHand.BitCount(0xc & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if HoldemHand.BitCount(0x3 & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 3x or 9x
                            if HoldemHand.BitCount(0x82 & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                        
                        countContiguous = 0

                    # 4x3x
                    if HoldemHand.BitCount(0x6 & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if HoldemHand.BitCount(0x1001 & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 2x or 8x
                            if HoldemHand.BitCount(0x41 & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                        
                        countContiguous = 0
                    
                    # 3x2x
                    if HoldemHand.BitCount(0x3 & bf) == 2:
                        countContiguous += 1
                    else:                            
                        if countContiguous == 2:
                            # test for Ax or 7x
                            if HoldemHand.BitCount(0x1020 & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                        
                        countContiguous = 0

                    # 2xAx
                    if HoldemHand.BitCount(0x1001 & bf) == 2:
                        countContiguous += 1
                        # check one last time
                        if countContiguous == 2:
                            # test for 5x
                            if HoldemHand.BitCount(0x8 & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                    else:                            
                        if countContiguous == 2:
                            # test for 6x
                            if HoldemHand.BitCount(0x10 & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                    
                    # Hand improving to a pair, must use overcards and not make a 3 suited board
                    if playerNewHandType == HoldemHand.HandTypes.PAIR:
                        newCardVal = HoldemHand.Evaluate(card)
                        newTopCard = HoldemHand.TopCard(newCardVal)
                        if boardOrigTopCard < newTopCard and not (discountSuitedBoard or discountSuitedOut) and not discountStraight:
                            isOut = True
                    
                    # Hand imporving to two pair, must use one of the players pocket cards and 
                    # the player already has a pair, either a pocket pair or a pair using the board. 
                    # ie: not drawing to two pair when trips is out - drawing dead.
                    # And not make a 3 suited board and not discounting for a straight. 
                    elif playerNewHandType == HoldemHand.HandTypes.TWO_PAIR:
                        playerPocketHandNewCardVal = HoldemHand.Evaluate(player | card)
                        playerPocketHandNewCardType = HoldemHand.HandType(playerPocketHandNewCardVal)
                        if (playerPocketHandNewCardType == HoldemHand.HandTypes.PAIR and playerPocketHandType != HoldemHand.HandTypes.PAIR) and (boardOrigHandType != HoldemHand.HandTypes.PAIR or playerOrigHandType == HoldemHand.HandTypes.TWO_PAIR):
                            if not (discountSuitedBoard or discountSuitedOut) and not discountStraight:
                                isOut = True;

                    # New hand better than two pair
                    elif playerNewHandType > HoldemHand.HandTypes.TWO_PAIR:
                        # Hand imporving trips, must not make a 3 suited board and not discounting for a straight. 
                        if playerNewHandType == HoldemHand.HandTypes.TRIPS:
                            if not (discountSuitedBoard or discountSuitedOut) and not discountStraight:
                                isOut = True
                        # Hand imporving to a straight, must not make a 3 suited board.
                        elif playerNewHandType == HoldemHand.HandTypes.STRAIGHT:
                            if not (discountSuitedBoard or discountSuitedOut):
                                isOut = True
                        else:
                            # No discounting for a Flush (should we consider a straight Flush?),
                            # Full house, Four of a kind and straight flush
                            isOut = True
                    
                    if isOut:
                        retval |= card

        return retval
    
    __ContiguousCountTable = [
        0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4, 0, 0, 0, 2,
            0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 0, 0, 0, 2, 0, 0, 2, 3,
            0, 0, 0, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3,
            4, 4, 5, 6, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4,
            0, 0, 0, 2, 0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3,
            4, 4, 4, 4, 5, 5, 6, 7, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2,
            2, 2, 3, 4, 0, 0, 0, 2, 0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5,
            0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4, 2, 2, 2, 2,
            2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            3, 3, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 8, 0, 0, 0, 2,
            0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4, 0, 0, 0, 2, 0, 0, 2, 3,
            2, 2, 2, 2, 3, 3, 4, 5, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2,
            2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6,
            0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4, 0, 0, 0, 2,
            0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 2, 2, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4,
            5, 5, 6, 7, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4,
            2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3,
            3, 3, 3, 3, 4, 4, 5, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5,
            5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 9, 0, 0, 0, 2, 0, 0, 2, 3,
            0, 0, 0, 2, 2, 2, 3, 4, 0, 0, 0, 2, 0, 0, 2, 3, 2, 2, 2, 2,
            3, 3, 4, 5, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4,
            2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 0, 0, 0, 2,
            0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4, 0, 0, 0, 2, 0, 0, 2, 3,
            2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            2, 2, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7,
            0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4, 0, 0, 0, 2,
            0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 0, 0, 0, 2, 0, 0, 2, 3,
            0, 0, 0, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3,
            4, 4, 5, 6, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4,
            2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            5, 5, 5, 5, 6, 6, 7, 8, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5,
            2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2,
            2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 6,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7,
            8, 8, 9, 10, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4,
            0, 0, 0, 2, 0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 0, 0, 0, 2,
            0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3,
            3, 3, 3, 3, 4, 4, 5, 6, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2,
            2, 2, 3, 4, 0, 0, 0, 2, 0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5,
            2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 3, 3, 3, 3,
            3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 0, 0, 0, 2, 0, 0, 2, 3,
            0, 0, 0, 2, 2, 2, 3, 4, 0, 0, 0, 2, 0, 0, 2, 3, 2, 2, 2, 2,
            3, 3, 4, 5, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4,
            2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 3, 3, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 8,
            0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4, 0, 0, 0, 2,
            0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 0, 0, 0, 2, 0, 0, 2, 3,
            0, 0, 0, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3,
            4, 4, 5, 6, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4,
            0, 0, 0, 2, 0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3,
            4, 4, 4, 4, 5, 5, 6, 7, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5,
            2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2,
            2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 9, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6,
            2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 2, 2, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4,
            5, 5, 6, 7, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4,
            2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3,
            3, 3, 3, 3, 4, 4, 5, 6, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 8, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 6, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7,
            8, 8, 8, 8, 9, 9, 10, 11, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2,
            2, 2, 3, 4, 0, 0, 0, 2, 0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5,
            0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4, 2, 2, 2, 2,
            2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 0, 0, 0, 2, 0, 0, 2, 3,
            0, 0, 0, 2, 2, 2, 3, 4, 0, 0, 0, 2, 0, 0, 2, 3, 2, 2, 2, 2,
            3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 0, 0, 0, 2,
            0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4, 0, 0, 0, 2, 0, 0, 2, 3,
            2, 2, 2, 2, 3, 3, 4, 5, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2,
            2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6,
            2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5,
            6, 6, 7, 8, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4,
            0, 0, 0, 2, 0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 0, 0, 0, 2,
            0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3,
            3, 3, 3, 3, 4, 4, 5, 6, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2,
            2, 2, 3, 4, 0, 0, 0, 2, 0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5,
            2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 3, 3, 3, 3,
            3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4,
            2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 9,
            0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4, 0, 0, 0, 2,
            0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 0, 0, 0, 2, 0, 0, 2, 3,
            0, 0, 0, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3,
            4, 4, 5, 6, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4,
            0, 0, 0, 2, 0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3,
            4, 4, 4, 4, 5, 5, 6, 7, 0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2,
            2, 2, 3, 4, 0, 0, 0, 2, 0, 0, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5,
            0, 0, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 2, 3, 4, 2, 2, 2, 2,
            2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            3, 3, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 8, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6,
            2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 2, 2, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4,
            5, 5, 6, 7, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 3, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6,
            6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 10, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4,
            2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            2, 2, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7,
            2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3,
            4, 4, 5, 6, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4,
            2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            5, 5, 5, 5, 6, 6, 7, 8, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 5,
            2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2,
            2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 2, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3,
            2, 2, 2, 2, 3, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2,
            2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6,
            7, 7, 8, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 3, 4, 4, 5, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 6, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 8,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 5, 5, 6, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
            8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 11, 12, 0, 2, 0, 3,
            0, 2, 2, 4, 0, 2, 0, 3, 2, 2, 3, 5, 0, 2, 0, 3, 0, 2, 2, 4,
            2, 2, 2, 3, 3, 3, 4, 6, 0, 2, 0, 3, 0, 2, 2, 4, 0, 2, 0, 3,
            2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 3, 3, 3, 3, 4, 4, 5, 7,
            0, 2, 0, 3, 0, 2, 2, 4, 0, 2, 0, 3, 2, 2, 3, 5, 0, 2, 0, 3,
            0, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 2, 2, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
            5, 5, 6, 8, 0, 2, 0, 3, 0, 2, 2, 4, 0, 2, 0, 3, 2, 2, 3, 5,
            0, 2, 0, 3, 0, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 0, 2, 0, 3,
            0, 2, 2, 4, 0, 2, 0, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4,
            3, 3, 3, 3, 4, 4, 5, 7, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3,
            2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5, 4, 4, 4, 4,
            4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 9, 0, 2, 0, 3, 0, 2, 2, 4,
            0, 2, 0, 3, 2, 2, 3, 5, 0, 2, 0, 3, 0, 2, 2, 4, 2, 2, 2, 3,
            3, 3, 4, 6, 0, 2, 0, 3, 0, 2, 2, 4, 0, 2, 0, 3, 2, 2, 3, 5,
            2, 2, 2, 3, 2, 2, 2, 4, 3, 3, 3, 3, 4, 4, 5, 7, 0, 2, 0, 3,
            0, 2, 2, 4, 0, 2, 0, 3, 2, 2, 3, 5, 0, 2, 0, 3, 0, 2, 2, 4,
            2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3,
            2, 2, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 8,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 3, 3, 3, 3,
            4, 4, 5, 7, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 4, 6, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            6, 6, 6, 6, 7, 7, 8, 10, 0, 2, 0, 3, 0, 2, 2, 4, 0, 2, 0, 3,
            2, 2, 3, 5, 0, 2, 0, 3, 0, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6,
            0, 2, 0, 3, 0, 2, 2, 4, 0, 2, 0, 3, 2, 2, 3, 5, 2, 2, 2, 3,
            2, 2, 2, 4, 3, 3, 3, 3, 4, 4, 5, 7, 0, 2, 0, 3, 0, 2, 2, 4,
            0, 2, 0, 3, 2, 2, 3, 5, 0, 2, 0, 3, 0, 2, 2, 4, 2, 2, 2, 3,
            3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5,
            3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 8, 0, 2, 0, 3,
            0, 2, 2, 4, 0, 2, 0, 3, 2, 2, 3, 5, 0, 2, 0, 3, 0, 2, 2, 4,
            2, 2, 2, 3, 3, 3, 4, 6, 0, 2, 0, 3, 0, 2, 2, 4, 0, 2, 0, 3,
            2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 3, 3, 3, 3, 4, 4, 5, 7,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5,
            6, 6, 7, 9, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4,
            3, 3, 3, 3, 4, 4, 5, 7, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3,
            2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 3, 3, 3, 3,
            3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 8, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            3, 3, 4, 6, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 4, 4, 5, 7, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 11,
            0, 2, 0, 3, 0, 2, 2, 4, 0, 2, 0, 3, 2, 2, 3, 5, 0, 2, 0, 3,
            0, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 0, 2, 0, 3, 0, 2, 2, 4,
            0, 2, 0, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 3, 3, 3, 3,
            4, 4, 5, 7, 0, 2, 0, 3, 0, 2, 2, 4, 0, 2, 0, 3, 2, 2, 3, 5,
            0, 2, 0, 3, 0, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4,
            4, 4, 4, 4, 5, 5, 6, 8, 0, 2, 0, 3, 0, 2, 2, 4, 0, 2, 0, 3,
            2, 2, 3, 5, 0, 2, 0, 3, 0, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6,
            0, 2, 0, 3, 0, 2, 2, 4, 0, 2, 0, 3, 2, 2, 3, 5, 2, 2, 2, 3,
            2, 2, 2, 4, 3, 3, 3, 3, 4, 4, 5, 7, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3,
            3, 3, 4, 6, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5,
            4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 9, 0, 2, 0, 3,
            0, 2, 2, 4, 0, 2, 0, 3, 2, 2, 3, 5, 0, 2, 0, 3, 0, 2, 2, 4,
            2, 2, 2, 3, 3, 3, 4, 6, 0, 2, 0, 3, 0, 2, 2, 4, 0, 2, 0, 3,
            2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 3, 3, 3, 3, 4, 4, 5, 7,
            0, 2, 0, 3, 0, 2, 2, 4, 0, 2, 0, 3, 2, 2, 3, 5, 0, 2, 0, 3,
            0, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 2, 2, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
            5, 5, 6, 8, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4,
            3, 3, 3, 3, 4, 4, 5, 7, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 4, 6,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 10, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3,
            3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5,
            2, 2, 2, 3, 2, 2, 2, 4, 3, 3, 3, 3, 4, 4, 5, 7, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3,
            2, 2, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 8,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 3, 3, 3, 3,
            4, 4, 5, 7, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 3, 3, 3, 3,
            3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5, 4, 4, 4, 4, 4, 4, 4, 4,
            5, 5, 5, 5, 6, 6, 7, 9, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 4, 6,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3,
            3, 3, 3, 4, 3, 3, 3, 3, 4, 4, 5, 7, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            3, 3, 4, 6, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5,
            3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 8, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 7,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8,
            9, 9, 10, 12, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4,
            3, 3, 3, 3, 4, 4, 5, 7, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3,
            2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 3, 3, 3, 3,
            3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 8, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3,
            3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5,
            2, 2, 2, 3, 2, 2, 2, 4, 3, 3, 3, 3, 4, 4, 5, 7, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 3, 3, 4, 6, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            3, 3, 3, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 9,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 3, 3, 3, 3,
            4, 4, 5, 7, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4,
            4, 4, 4, 4, 5, 5, 6, 8, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3,
            2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3,
            2, 2, 2, 4, 3, 3, 3, 3, 4, 4, 5, 7, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            3, 3, 4, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 10, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3,
            2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 3, 3, 3, 3, 4, 4, 5, 7,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 2, 2, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
            5, 5, 6, 8, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5,
            2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4,
            3, 3, 3, 3, 4, 4, 5, 7, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3,
            2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 4, 6,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5, 4, 4, 4, 4,
            4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 9, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3,
            3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5,
            2, 2, 2, 3, 2, 2, 2, 4, 3, 3, 3, 3, 4, 4, 5, 7, 2, 2, 2, 3,
            2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 3, 5, 2, 2, 2, 3, 2, 2, 2, 4,
            2, 2, 2, 3, 3, 3, 4, 6, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 3,
            2, 2, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 8,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3,
            3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 4, 6, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            4, 4, 5, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6,
            7, 7, 7, 7, 8, 8, 9, 11, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 4, 6,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3,
            3, 3, 3, 4, 3, 3, 3, 3, 4, 4, 5, 7, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            3, 3, 4, 6, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5,
            3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 8, 3, 3, 3, 3,
            3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 4, 6, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 4, 4, 5, 7,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3,
            3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 4, 6, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5,
            6, 6, 7, 9, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 4, 6, 3, 3, 3, 3,
            3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 4, 4, 5, 7, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 4, 6,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3,
            3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 8, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
            3, 3, 4, 6, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5,
            3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 4, 4, 5, 7, 3, 3, 3, 3,
            3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4,
            3, 3, 3, 3, 3, 3, 4, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 10,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 5, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 5, 5, 6, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 7, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5,
            4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 9, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 6, 8, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
            7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
            8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9,
            9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 12
    ]
                





