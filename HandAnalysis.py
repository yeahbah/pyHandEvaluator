from os import stat
import numpy as np
from numpy.core.fromnumeric import shape
from HandEvaluator import Hand
from multipledispatch import dispatch
from timeit import Timer, default_timer as timer

class HandAnalysis:
    DEFAULT_TIME_DURATION = 0.25

    # The classic HandStrength Calculation from page 21 of Aaron Davidson's
    # Masters Thesis
    # pocket - Pocket cards
    # board - Current board
    # returns hand strength as a percentage of hands won
    @staticmethod
    @dispatch(np.uint64, np.uint64)
    def HandStrength(pocket: np.uint64, board: np.uint64):
        win = 0.0
        count = 0.0

        if __debug__:
            if Hand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if Hand.BitCount(board) < 3 or Hand.BitCount(board) > 5:
                raise Exception("Board must have 3, 4, or 5 cards for this calculation")
        
        ourRank = Hand.Evaluate(pocket | board)
        for opponentHand in Hand.Hands(np.uint64(0), pocket | board, 2):
            opponentRank = Hand.Evaluate(opponentHand | board)
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
    @dispatch(np.uint64, np.uint64, int, float)
    def HandStrength(pocket: np.uint64, board: np.uint64, numOpponents: int, duration: float):
        win = 0.0
        count = 0.0        

        if __debug__:
            if Hand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if Hand.BitCount(board) > 5:
                raise Exception("Board must have 5 or less cards")
            if numOpponents < 1 or numOpponents > 9:
                raise Exception("May only select 1-9 opponents")

        startTime = timer()
        ourRank = Hand.Evaluate(pocket | board)
        if numOpponents == 1:
            while timer() - startTime < duration:
                oppcards = Hand.RandomHand(np.uint64(0), pocket | board, 2)
                opprank = Hand.Evaluate(oppcards | board)
                if ourRank > opprank:
                    win += 1.0
                elif ourRank == opprank:
                    win += 0.5
                count += 1.0

        elif numOpponents == 2:
            while timer() - startTime < duration:
                opp1cards = Hand.RandomHand(np.uint64(0), pocket | board, 2)
                opp2cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards, 2)
                opp1rank = Hand.Evaluate(opp1cards | board)
                opp2rank = Hand.Evaluate(opp2cards | board)

                if (ourRank > opp1rank) and (ourRank > opp2rank):
                    win += 1.0
                elif ourRank >= opp1rank and ourRank >= opp2rank:
                    win += 0.5
                count += 1.0
        
        elif numOpponents == 3:
            while timer() - startTime < duration:
                opp1cards = Hand.RandomHand(np.uint64(0), pocket | board, 2)
                opp2cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards, 2)
                opp3cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards, 2)
                opp1rank = Hand.Evaluate(opp1cards | board)
                opp2rank = Hand.Evaluate(opp2cards | board)
                opp3rank = Hand.Evaluate(opp3cards | board) 

                if (ourRank > opp1rank) and (ourRank > opp2rank) and (ourRank > opp3rank):
                    win += 1.0
                elif (ourRank >= opp1rank) and (ourRank >= opp2rank) and (ourRank >= opp3rank):
                    win += 0.5
                count += 1.0
        
        elif numOpponents == 4:
            while timer() - startTime < duration:
                opp1cards = Hand.RandomHand(np.uint64(0), pocket | board, 2)
                opp2cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards, 2)
                opp3cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards, 2)
                opp4cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards, 2)
                opp1rank = Hand.Evaluate(opp1cards | board)
                opp2rank = Hand.Evaluate(opp2cards | board)
                opp3rank = Hand.Evaluate(opp3cards | board)
                opp4rank = Hand.Evaluate(opp4cards | board)

                if (ourRank > opp1rank) and (ourRank > opp2rank) \
                    and (ourRank > opp3rank) and (ourRank > opp4rank):
                    win += 1.0
                elif (ourRank >= opp1rank) and (ourRank >= opp2rank) \
                    and (ourRank >= opp3rank) and (ourRank >= opp4rank):
                    win += 0.5
                count += 1.0
        
        elif numOpponents == 5:
            while timer() - startTime < duration:
                opp1cards = Hand.RandomHand(np.uint64(0), pocket | board, 2)
                opp2cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards, 2)
                opp3cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards, 2)
                opp4cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp1rank = Hand.Evaluate(opp1cards | board)
                opp2rank = Hand.Evaluate(opp2cards | board)
                opp3rank = Hand.Evaluate(opp3cards | board)
                opp4rank = Hand.Evaluate(opp4cards | board)
                opp5rank = Hand.Evaluate(opp5cards | board)
            
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
                opp1cards = Hand.RandomHand(np.uint64(0), pocket | board, 2)
                opp2cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards, 2)
                opp3cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards, 2)
                opp4cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp6cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards, 2)
                opp1rank = Hand.Evaluate(opp1cards | board)
                opp2rank = Hand.Evaluate(opp2cards | board)
                opp3rank = Hand.Evaluate(opp3cards | board)
                opp4rank = Hand.Evaluate(opp4cards | board)
                opp5rank = Hand.Evaluate(opp5cards | board)
                opp6rank = Hand.Evaluate(opp6cards | board)
            
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
                opp1cards = Hand.RandomHand(np.uint64(0), pocket | board, 2)
                opp2cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards, 2)
                opp3cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards, 2)
                opp4cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp6cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards, 2)
                opp7cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards, 2)
                opp1rank = Hand.Evaluate(opp1cards | board)
                opp2rank = Hand.Evaluate(opp2cards | board)
                opp3rank = Hand.Evaluate(opp3cards | board)
                opp4rank = Hand.Evaluate(opp4cards | board)
                opp5rank = Hand.Evaluate(opp5cards | board)
                opp6rank = Hand.Evaluate(opp6cards | board)
                opp7rank = Hand.Evaluate(opp7cards | board)
            
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
                opp1cards = Hand.RandomHand(np.uint64(0), pocket | board, 2)
                opp2cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards, 2)
                opp3cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards, 2)
                opp4cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp6cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards, 2)
                opp7cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards, 2)
                opp8cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards | opp7cards, 2)
                opp1rank = Hand.Evaluate(opp1cards | board)
                opp2rank = Hand.Evaluate(opp2cards | board)
                opp3rank = Hand.Evaluate(opp3cards | board)
                opp4rank = Hand.Evaluate(opp4cards | board)
                opp5rank = Hand.Evaluate(opp5cards | board)
                opp6rank = Hand.Evaluate(opp6cards | board)
                opp7rank = Hand.Evaluate(opp7cards | board)
                opp8rank = Hand.Evaluate(opp8cards | board)
            
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
                opp1cards = Hand.RandomHand(np.uint64(0), pocket | board, 2)
                opp2cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards, 2)
                opp3cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards, 2)
                opp4cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp6cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards, 2)
                opp7cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards, 2)
                opp8cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards | opp7cards, 2)
                opp9cards = Hand.RandomHand(np.uint64(0), pocket | board | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards | opp7cards | opp8cards, 2)
                opp1rank = Hand.Evaluate(opp1cards | board)
                opp2rank = Hand.Evaluate(opp2cards | board)
                opp3rank = Hand.Evaluate(opp3cards | board)
                opp4rank = Hand.Evaluate(opp4cards | board)
                opp5rank = Hand.Evaluate(opp5cards | board)
                opp6rank = Hand.Evaluate(opp6cards | board)
                opp7rank = Hand.Evaluate(opp7cards | board)
                opp8rank = Hand.Evaluate(opp8cards | board)
                opp9rank = Hand.Evaluate(opp9cards | board)
            
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
    @dispatch(np.uint64, np.uint64)
    def StraightDrawCount(mask: np.uint64, dead: np.uint64):
        retval = 0

        # Get original mask value
        origType = Hand.EvaluateType(mask)[0]

        # If current mask is better than a straight then return 0 outs
        if origType >= Hand.HandTypes.STRAIGHT:
            return retval
        
        # look ahead one card
        for card in Hand.Hands(np.uint64(0), mask | dead, 1):

            # Get new mask value
            newHandType = Hand.EvaluateType(mask | card)[0]

            # Include straight flush as this will ensure outs is always the maximum
            if newHandType == Hand.HandTypes.STRAIGHT or newHandType == Hand.HandTypes.STRAIGHT_FLUSH:
                retval += 1
            
        return retval
    
    # The method returns the number of straight draws that are possible for the player and board configuration.   
    # This method filters the results so only player hand improvements are counted.
    # player - Two card mask making up the players pocket cards
    # board - The community cards
    # dead - Dead cards
    @staticmethod
    @dispatch(np.uint64, np.uint64, np.uint64)
    def StraightDrawCount(player: np.uint64, board: np.uint64, dead: np.uint64):
        retval = 0
        ncards = Hand.BitCount(player | board)

        if __debug__:
            if Hand.BitCount(player) != 2:
                raise Exception("Player must have exactly 2 cards")
            if Hand.BitCount(board) != 3 and Hand.BitCount(board) != 4:
                raise Exception("Board must contain 3 or 4 cards")
        
        playerOrigHandVal = Hand.Evaluate(player | board, ncards);

        if Hand.HandType(playerOrigHandVal) >= Hand.HandTypes.STRAIGHT:
            return retval
        
        for card in Hand.Hands(np.uint64(0), board | player | dead, 1):
            playerNewHandVal = Hand.Evaluate(player | board | card, ncards + 1)
            playerHandType = Hand.HandType(playerNewHandVal);

            # Include straight flush as this will ensure outs is always the maximum
            if playerHandType == Hand.HandTypes.STRAIGHT or playerHandType == Hand.HandTypes.STRAIGHT_FLUSH:
                boardHandVal = Hand.Evaluate(board | card)

                if (Hand.HandType(playerNewHandVal) > Hand.HandType(boardHandVal)) \
                    or (Hand.HandType(playerNewHandVal) == Hand.HandType(boardHandVal) \
                    and Hand.HandType(playerNewHandVal) > Hand.TopCard(boardHandVal)):
                    retval += 1
        
        return retval

    # Returns true if the mask is an open ended straight draw
    # mask - Players pocket cards mask
    # dead - Community card mask
    # returns true if the combined mask is an open ended straight draw
    @staticmethod
    @dispatch(str, str)
    def IsOpenEndedStraightDraw(mask: str, dead: str):
        return HandAnalysis.IsOpenEndedStraightDraw(Hand.ParseHand(mask)[0], Hand.ParseHand(dead)[0])

    # Returns true if the combined mask is an open ended straight draw. Only straight possibilities that
    # improve the player's mask are considered in this method
    # pocket - Players pocket cards mask
    # board - Community card mask
    # dead - Dead cards
    # Returns true if the combined mask is an open ended straight draw
    @staticmethod
    @dispatch(np.uint64, np.uint64, np.uint64)
    def IsOpenEndedStraightDraw(pocket: np.uint64, board: np.uint64, dead: np.uint64):
        if __debug__:
            if Hand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if Hand.BitCount(board) != 3 and Hand.BitCount(board) != 4:
                raise Exception("Board must have 3 or 4 cards for this calculation")
        return HandAnalysis.IsOpenEndedStraightDraw(pocket | board, np.uint64(0)) and HandAnalysis.StraightDrawCount(pocket, board, dead) > 0
    
    # Returns true if the combined mask is an open ended straight draw
    # mask - Players pocket cards mask
    # dead - Community cards mask
    # Returns true if the combined mask is an open ended straight draw
    @staticmethod
    @dispatch(np.uint64, np.uint64)
    def IsOpenEndedStraightDraw(mask: np.uint64, dead: np.uint64):
        if __debug__:
            if mask and dead != 0:
                raise Exception("Mask and dead cards must not have any cards in common")
            if Hand.BitCount(mask) < 4 or Hand.BitCount(mask) > 6:
                raise Exception("Mask must have 4-6 cards")
        return HandAnalysis.StraightDrawCount(mask, np.uint64(0)) > 4 and HandAnalysis.StraightDrawCount(mask, dead)

    # Returns true if the mask is an open ended straight draw
    # mask - Players pocket cards mask
    # dead - Community card mask
    # Returns true if the combined mask is an open ended straight draw    
    @staticmethod
    @dispatch(str, str)
    def IsOpenEndedStraightDraw(mask: str, dead: str):
        return HandAnalysis.IsOpenEndedStraightDraw(Hand.ParseHand(mask)[0], Hand.ParseHand(dead)[0])

    # Return true if the combined cards contains a gut shot straight draw
    # pocket - Players pocket cards mask
    # board - Communit board mask
    # dead - Dead cards    
    @staticmethod
    @dispatch(np.uint64, np.uint64, np.uint64)
    def IsGutShotStraightDraw(pocket: np.uint64, board: np.uint64, dead: np.uint64):
        if __debug__:
            if Hand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if Hand.BitCount(board) != 3 and Hand.BitCount(board) != 4:
                raise Exception("Board must have 3 or 4 cards for this calculation")
        
        
        return HandAnalysis.IsGutShotStraightDraw(pocket | board, dead) and HandAnalysis.StraightDrawCount(pocket, board, dead) > 0

    # mask - Current mask
    # dead - Dead cards
    @staticmethod
    @dispatch(np.uint64, np.uint64)
    def IsGutShotStraightDraw(mask: np.uint64, dead: np.uint64):
        if __debug__:
            if mask & dead != 0:
                raise Exception("Mask and dead cards must not have any cards in common")
            if Hand.BitCount(mask) < 4 or Hand.BitCount(mask) > 6:
                raise Exception("mask must have 4-6 cards")
        
        return HandAnalysis.StraightDrawCount(mask, np.uint64(0)) <= 4 and HandAnalysis.StraightDrawCount(mask, dead) > 0
    
    # mask - Current mask
    # dead - Dead cards
    @staticmethod
    @dispatch(str, str)
    def IsGutShotStraightDraw(mask: str, dead: str):
        return HandAnalysis.IsGutShotStraightDraw(Hand.ParseHand(mask)[0], Hand.ParseCard(dead)[0])

    # Returns true if the passed mask only needs one card to make a straight.
    # Note that the pocket cards must contains at least one card in the 
    # combined straight.
    # pocket - Players pocket mask
    # board - Community board
    # dead - Dead cards
    @staticmethod
    @dispatch(np.uint64, np.uint64, np.uint64)
    def IsStraightDraw(pocket: np.uint64, board: np.uint64, dead: np.uint64):
        return HandAnalysis.StraightDrawCount(pocket, board, dead) > 0
    
    @staticmethod
    @dispatch(np.uint64, np.uint64)
    def IsStraightDraw(mask: np.uint64, dead: np.uint64):
        return HandAnalysis.StraightDrawCount(mask, dead) > 0

    @staticmethod
    @dispatch(str, str)
    def IsStraightDraw(mask: str, dead: str):
        return HandAnalysis.IsStraightDraw(Hand.ParseHand(mask)[0], Hand.ParseHand(dead)[0])
    
    @staticmethod
    @dispatch(str, str, str)
    def IsStraightDraw(pocket: str, board: str, dead: str):
        if __debug__:
            if not Hand.ValidateHand(pocket):
                raise Exception("Invalid pocket hand")
            if not Hand.ValidateHand(board):
                raise Exception("Invalid board cards")
        pocketMask = Hand.ParseHand(pocket)[0]
        boardMask = Hand.ParseHand(board)[0]
        deadMask = Hand.ParseHand(dead)[0]
        return HandAnalysis.IsStraightDraw(pocketMask, boardMask, deadMask)
    
    # Returns the count of adjacent cards
    # pocket - Players pocket cards mask
    # Community card mask
    @staticmethod
    @dispatch(np.uint64, np.uint64)
    def CountContiguous(pocket: np.uint64, board: np.uint64):
        mask = pocket | board
        bf = Hand.CardMask(mask, Hand.CLUBS) | Hand.CardMask(mask, Hand.DIAMONDS) \
                | Hand.CardMask(mask, Hand.HEARTS) | Hand.CardMask(mask, Hand.SPADES)
        if __debug__: 
            if Hand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if Hand.BitCount(board) != 3 and Hand.BitCount(board) != 4:
                raise Exception("Board must have 3 or 4 cards for this calculation")    

            masks = [0x7f, 0x3f, 0x1f, 0xf, 0x7, 0x3]
            i = 0
            while i < len(masks):
                count = Hand.BitCount(np.uint64(masks[i]))
                contmask = 0
                offset = 13 - count
                while offset >= 0:                    
                    contmask = np.uint64(masks[i] << offset)
                    if bf & contmask == contmask:
                        return count
                    offset -= 1
                
                contmask = np.uint64(0x1000 | (masks[i] >> 1))
                if bf & contmask == contmask:
                    return count
                i += 1
            
            return 0
        else:
            return HandAnalysis.__ContiguousCountTable[bf]

    # Returns the count of adjacent cards
    # mask - current hand    
    @staticmethod
    @dispatch(np.uint64)
    def CountContiguous(mask: np.uint64):
        clubs = Hand.CardMask(mask, Hand.CLUBS)
        diamonds = Hand.CardMask(mask, Hand.DIAMONDS)
        hearts = Hand.CardMask(mask, Hand.Hands)
        spades = Hand.CardMask(mask, Hand.SPADES)
        return HandAnalysis.__ContiguousCountTable[clubs | diamonds | hearts | spades]    

    # Counts the number of hands that are a flush with one more drawn card
    # mask - Hand
    # dead - Cards not allowed to be drawn
    @staticmethod
    @dispatch(np.uint64, np.uint64)
    def FlushDrawCount(mask: np.uint64, dead: np.uint64):
        retval = 0

        # Get original mask value
        handType = Hand.EvaluateType(mask)[0]

        # if current mask is better than a straight then return 0 outs
        if handType >= Hand.HandTypes.FLUSH:
            return retval
        
        # look ahead one card
        shared = np.uint64(0)
        for card in Hand.Hands(shared, mask | dead, 1):
            handType = Hand.EvaluateType(mask | card)[0]

            # include straight flush as this will ensure outs is always the maximum
            if handType == Hand.HandTypes.FLUSH or handType == Hand.HandTypes.STRAIGHT_FLUSH:
                retval += 1
        
        return retval
    
    # Counts the number of hands that are a flush with one more drawn card. However,
    # Flush hands that only improve the board are not considered
    # player - Players two card hand
    # board - Board cards
    # dead - Dead cards
    @staticmethod
    @dispatch(np.uint64, np.uint64, np.uint64)
    def FlushDrawCount(player: np.uint64, board: np.uint64, dead: np.uint64):
        retval = 0
        if __debug__:
            if Hand.BitCount(player) != 2:
                raise Exception("Player must have exactly 2 cards")
            if Hand.BitCount(board) != 3 and Hand.BitCount(board) != 4:
                raise Exception("Board must contain 3 or 4 cards")
        
        # Get original mask value
        playerOrigHandType = Hand.EvaluateType(player | board)[0]

        # if current mask better than a straight then return 0 outs
        if playerOrigHandType == Hand.HandTypes.FLUSH or \
            playerOrigHandType == Hand.HandTypes.STRAIGHT_FLUSH:
            return retval
        
        # look ahead one card
        shared = np.uint64(0)
        for card in Hand.Hands(shared, board | player | dead, 1):
            # get new mask value
            playerNewHandValue = Hand.Evaluate(player | board | card)
            boardNewHandValue = Hand.Evaluate(board | card)

            # include straight flush as this will ensure outs is always the maximum
            if Hand.HandType(playerNewHandValue) == Hand.HandTypes.FLUSH or \
                Hand.HandType(playerNewHandValue) == Hand.HandTypes.STRAIGHT_FLUSH:
                # if the mask improved, increment out
                if Hand.HandType(playerNewHandValue) > Hand.HandType(boardNewHandValue) or \
                    Hand.HandType(playerNewHandValue) == Hand.HandType(boardNewHandValue) and \
                    Hand.TopCard(playerNewHandValue) > Hand.TopCard(boardNewHandValue):
                    retval += 1
            
        return retval

    # Returns true if there are 4 cards of the same suit
    # pocket - Players pocket cards mask
    # board - Communit card mask
    # dead - dead cards
    @staticmethod
    @dispatch(np.uint64, np.uint64, np.uint64)
    def IsFlushDraw(pocket: np.uint64, board: np.uint64, dead: np.uint64):
        if __debug__:
            if Hand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if Hand.BitCount(board) != 3 and Hand.BitCount != 4:
                raise Exception("board must have 3 or 4 cards for this calculation")

        return HandAnalysis.FlushDrawCount(pocket, board, dead) > 0

    # Returns true if the hand is a flush draw
    # mask - cards
    # dead - dead cards
    @staticmethod
    @dispatch(np.uint64, np.uint64)
    def IsFlushDraw(mask: np.uint64, dead: np.uint64):
        return HandAnalysis.FlushDrawCount(mask, dead) > 0    

    # Returns if there are 4 cards of the same suit
    # pocket - Player's pocket cards
    # board community cards
    # dead - Dead cards
    @staticmethod
    @dispatch(str, str, str)
    def IsFlushDraw(pocket: str, board: str, dead: str):
        if __debug__:
            if not Hand.ValidateHand(pocket):
                raise Exception("Invalid pocket cards")
            if not Hand.ValidateHand(board):
                raise Exception("Invalid board")
        
        return HandAnalysis.FlushDrawCount(Hand.ParseHand(pocket)[0], Hand.ParseHand(board)[0], Hand.ParseHand(dead)[0]) > 0

    # Returns true if there are three cards of the same suit. 
    # The pocket cards must have at least one card in that suit.
    # pocket - Players pocket cards mask
    # board - Community card mask
    # dead - Dead cards
    @staticmethod
    @dispatch(np.uint64, np.uint64, np.uint64)
    def IsBackdoorFlushDraw(pocket: np.uint64, board: np.uint64, dead: int):
        if __debug__:
            if Hand.BitCount(pocket) != 2:
                raise Exception("Pocket must have exactly two cards")
            if Hand.BitCount(board) != 3 and Hand.BitCount(board) != 4:
                raise Exception("Board must have 3 or 4 cards for this calculation")
        
        mask = pocket | board
        currentType = Hand.EvaluateType(mask)[0]
        if currentType >= Hand.HandTypes.FLUSH:
            return False
        
        x = np.uint64(0x1FFF)
        ss = (mask >> Hand.GetSpadeOffset()) & x
        sc = (mask >> Hand.GetClubOffset()) & x
        sd = (mask >> Hand.GetDiamondOffset()) & x
        sh = (mask >> Hand.GetHeartOffset()) & x

        if Hand.BitCount(ss) == 3:
            ps = (pocket >> Hand.GetSpadeOffset()) & x
            return ps != 0
        elif Hand.BitCount(sc) == 3:
            pc = (pocket >> Hand.GetClubOffset()) & x
            return pc != 0
        elif Hand.BitCount(sd) == 3:
            pd = (pocket >> Hand.GetDiamondOffset()) & x
            return pd != 0
        elif Hand.BitCount(sh) == 3:
            ph = (pocket >> Hand.GetHeartOffset()) & x
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
            if not Hand.ValidateHand(pocket):
                raise Exception("Invalid pocket cards")
            if not Hand.ValidateHand(board):
                raise Exception("Invalid board")
        
        return HandAnalysis.IsBackdoorFlushDraw(Hand.ParseHand(pocket)[0], Hand.ParseHand(board)[0], Hand.ParseHand(dead)[0])

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
    @dispatch(np.uint64, np.uint64, np.uint64, int)
    def DrawCount(player: np.uint64, board: np.uint64, dead: np.uint64, handType: int):
        retval = 0
        if __debug__:
            if Hand.BitCount(player) != 2:
                raise Exception("Player must have exactly two cards")
            if Hand.BitCount(board) != 3 and Hand.BitCount(board) != 4:
                raise Exception("Board must contain 3 or 4 cards for this calculation")
            if (board | player) & dead != 0: 
                raise Exception("Player and board must not contain dead cards")
        
        # Get original mask value
        playerOrigHandVal = Hand.Evaluate(player | board)

        if Hand.HandType(playerOrigHandVal) > handType:
            return 0
        
        # look ahead one card
        shared = np.uint64(0)
        for card in Hand.Hands(shared, board | player | dead, 1):
            # get new mask value
            playerNewHandVal = Hand.Evaluate(player | board | card)

            # Get new board value
            boardHandVal = Hand.Evaluate(board | card)

            # Is the new mask better than the old one? We don't
            # want to know about supesizing the kickers so this
            # ensures that mask moved up in mask type
            handImproved = Hand.HandType(playerNewHandVal) > Hand.HandType(playerOrigHandVal)

            # if the mask improved and it matches the specified type, return true
            handStrongerThanBoard = playerNewHandVal > boardHandVal

            if handImproved and handStrongerThanBoard and Hand.HandType(playerNewHandVal) == handType:
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
    @dispatch(np.uint64, np.uint64, int)
    def DrawCount(mask: np.uint64, dead: np.uint64, handType: int):
        retval = 0
        if Hand.BitCount(mask) >=7:
            raise Exception("mask must contain less than 7 cards")
        if mask & dead != 0:
            raise Exception("mask must not contain dead cards")

        playerOriginalHandType = Hand.EvaluateType(mask)[0]
        if playerOriginalHandType >= handType:
            return 0

        # Look ahead one card
        for card in Hand.Hands(0, mask | dead, 1):
            # Get new mask value
            playerNewHandType = Hand.EvaluateType(mask | card)[0]

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
            if not Hand.ValidateHand(player):
                raise Exception("Invalid pocket cards")
            if not Hand.ValidateHand(board):
                raise Exception("Invalid board")
        
        return HandAnalysis.DrawCount(Hand.ParseHand(player)[0], Hand.ParseHand(board)[0], Hand.ParseHand(dead)[0], handType)
    
    # This method returns the mask distance from the best possible
    # mask given this board (no draws are considered). The value 0 is the 
    # best possible mask. The value 1 is the next best mask and so on.
    # pocket - The players pocket mask
    # board - The board mask
    @staticmethod
    @dispatch(np.uint64, np.uint64)
    def HandDistance(pocket: np.uint64, board: np.uint64):
        if __debug__:
            if Hand.BitCount(pocket) != 2:
                raise Exception("Player must have exactly two cards")
            if Hand.BitCount(board) != 3 and Hand.BitCount(board) !=4:
                raise Exception("Board must containt 3 or 4 cards")
        hv = 0
        handValues = []
        pocketHandVal = Hand.Evaluate(pocket | board)
        shared = np.uint64(0)
        for p in Hand.Hands(shared, board, 2):
            hv = Hand.Evaluate(p | board)            
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
    def OutsDiscounted(player: np.uint64, board: np.uint64, opponentsList):
        return Hand.BitCount(HandAnalysis.OutsMaskDiscounted(player, board, opponentsList))
    
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
    def OutsMaskDiscounted(player: np.uint64, board: np.uint64, opponentsList):
        retval = np.uint64(0)
        dead = np.uint64(0)
        ncards = Hand.BitCount(player | board)

        if __debug__:
            if Hand.BitCount(player) != 2:
                raise Exception("Player pocket must have exactly two cards")
            if ncards != 5 and ncards != 6:
                raise Exception("Outs only make sense after the flop and before the river")
        if len(opponentsList) > 0:
            for opp in opponentsList:
                if Hand.BitCount(opp) != 2:
                    raise Exception("Opponent hand ust have exactly two cards")
                dead |= opp
            playerOrigHandVal = Hand.Evaluate(player | board, ncards);
            playerOrigHandType = Hand.HandType(playerOrigHandVal)
            playerOrigTopCard = Hand.TopCard(playerOrigHandVal)

            shared = np.uint64(0)
            for card in Hand.Hands(shared, dead | board | player, 1):
                bWinFlag = True
                playerNewHandVal = Hand.Evaluate(player | board | card, ncards + 1)
                playerNewHandType = Hand.HandType(playerNewHandVal)
                playerNewTopCard = Hand.TopCard(playerNewHandVal)
                for oppmask in opponentsList:
                    oppHandVal = Hand.Evaluate(oppmask | board | card, ncards + 1)
                    bWinFlag = oppHandVal < playerNewHandVal and \
                        (playerNewHandType > playerOrigHandType or (playerNewHandType == playerOrigHandType and playerNewTopCard > playerOrigTopCard))
                    if not bWinFlag:
                        break
                if bWinFlag:
                    retval |= card
        else:
            # Look at the cards that improve the hand
            playerOrigHandVal = Hand.Evaluate(player | board, ncards)
            playerOrigHandType = Hand.HandType(playerOrigHandVal)
            playerOrigTopCard = Hand.TopCard(playerOrigHandVal)
            boardOrigHandVal = Hand.Evaluate(board)
            boardOrigHandType = Hand.HandType(boardOrigHandVal)
            boardOrigTopCard = Hand.TopCard(boardOrigHandVal)

            # Look at players pocket cards for special cases
            playerPocketHandVal = Hand.Evaluate(player)
            playerPocketHandType = Hand.HandType(playerPocketHandVal)

            # Separate out by suit
            x = np.uint64(0x1fff)
            sc = (board >> Hand.GetClubOffset()) & x
            sd = (board >> Hand.GetDiamondOffset()) & x
            sh = (board >> Hand.GetHeartOffset()) & x
            ss = (board >> Hand.GetSpadeOffset()) & x

            # Check if board is 3 suited
            discountSuitedBoard = (Hand.nBitsTable[sc] > 2) or (Hand.nBitsTable[sd] > 2) or (Hand.nBitsTable[sh] > 2) or (Hand.nBitsTable[ss] > 2)

            # Check if board is 3 connected on the flop. a dangerous board:
            # 3 possible straights using 2 pocket cards and a higher chance
            # of 2 pair; player often play 2 connected cards which can hit
            countContiguous = 0
            boardCardCount = Hand.BitCount(board)

            if boardCardCount == 3:
                bf = Hand.CardMask(board, Hand.CLUBS) or Hand.CardMask(board, Hand.DIAMONDS) or Hand.CardMask(board, Hand.HEARTS) or Hand.CardMask(board, Hand.SPADES)
                if Hand.BitCount(np.uint64(0x1800) & bf) == 2: countContiguous += 1
                if Hand.BitCount(np.uint64(0xc00) & bf) == 2: countContiguous += 1
                if Hand.BitCount(np.uint64(0x600) & bf) == 2: countContiguous += 1
                if Hand.BitCount(np.uint64(0x300) & bf) == 2: countContiguous += 1
                if Hand.BitCount(np.uint64(0x180) & bf) == 2: countContiguous += 1
                if Hand.BitCount(np.uint64(0xc0) & bf) == 2: countContiguous += 1
                if Hand.BitCount(np.uint64(0x60) & bf) == 2: countContiguous += 1
                if Hand.BitCount(np.uint64(0x30) & bf) == 2: countContiguous += 1
                if Hand.BitCount(np.uint64(0x18) & bf) == 2: countContiguous += 1
                if Hand.BitCount(np.uint64(0xc) & bf) == 2: countContiguous += 1;
                if Hand.BitCount(np.uint64(0x6) & bf) == 2: countContiguous += 1;
                if Hand.BitCount(np.uint64(0x3) & bf) == 2: countContiguous += 1;
                if Hand.BitCount(np.uint64(0x1001) & bf) == 2: countContiguous += 1;
            
            discountStraight = countContiguous > 2

            # Look ahead one card
            shared = np.uint64(0)
            for card in Hand.Hands(shared, dead | board | player, 1):
                boardNewHandVal = Hand.Evaluate(board | card)
                boardNewHandType = Hand.HandType(boardNewHandVal)
                boardNewTopCard = Hand.TopCard(boardNewHandVal)
                playerNewHandVal = Hand.Evaluate(player | board | card, ncards + 1)
                playerNewHandType = Hand.HandType(playerNewHandVal)
                playerNewTopCard = Hand.TopCard(playerNewHandVal)
                playerImproved = Hand.TopCard(playerNewHandVal)
                playerStrongerThanBoard = playerNewHandType > boardNewHandType or (playerNewHandType == boardNewHandType and playerNewTopCard > boardNewTopCard)

                if playerImproved and playerStrongerThanBoard:
                    isOut = False
                    discountSuitedOut = False
                    if not discountSuitedBoard:
                        x = np.uint64(0x1fff)
                        cc = (card >> Hand.GetClubOffset()) & x
                        cd = (card >> Hand.GetDiamondOffset()) & x
                        ch = (card >> Hand.GetHeartOffset()) & x
                        cs = (card >> Hand.GetSpadeOffset()) & x

                        # Check if card will make a 3 suited board
                        discountSuitedOut = (Hand.nBitsTable[sc] > 1 and Hand.nBitsTable[cc] == 1) \
                            or (Hand.nBitsTable[sd] > 1 and Hand.nBitsTable[cd] == 1) \
                            or (Hand.nBitsTable[sh] > 1 and Hand.nBitsTable[ch] == 1) \
                            or (Hand.nBitsTable[ss] > 1 and Hand.nBitsTable[cs] == 1)
                        
                    # Check if board is 4 connected or card + board is 4 connected
                    # Dangerous board: straight using 1 pocket card only
                    if boardCardCount != 4:
                        continue

                    # We need to check for the following:
                    # 9x,8x,7x,6x (4 in a row)
                    # 9x,8x,7x,5x (3 in a row with a 1 gap connected card)
                    # 9x,8x,6x,5x (2 connected with a 1 gap connected in the middle)
                    countContiguous = 0
                    bf = Hand.CardMask(board | card, Hand.CLUBS) | Hand.CardMask(board | card, Hand.DIAMONDS) | Hand.CardMask(board | card, Hand.HEARTS) | Hand.CardMask(board | card, Hand.SPADES)

                    # AxKx
                    if Hand.BitCount(np.uint64(0x1800) & bf) == 2:
                        countContiguous += 1
                    
                    # KxQx
                    if Hand.BitCount(np.uint64(0xc00) & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1 and Hand.BitCount(np.uint64(0x300) & bf) == 2:
                            # 2 connected with a 1 gap connected in the middle
                            discountStraight = True                            
                        countContiguous = 0
                    
                    # QxJx
                    if Hand.BitCount(np.uint64(0x600) & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if Hand.BitCount(np.uint64(0x100) & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for a T
                            if Hand.BitCount(np.uint64(0x100) & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        countContiguous = 0

                    # JxTx
                    if Hand.BitCount(np.uint64(0x300) & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if Hand.BitCount(np.uint64(0xc0) & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 9x
                            if Hand.BitCount(np.uint64(0x00) & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True

                        countContiguous = 0
                    
                    # Tx9x
                    if Hand.BitCount(np.uint64(0x180) & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if Hand.BitCount(np.uint64(0x60) & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 8x or Ax
                            if Hand.BitCount(np.uint64(0x1040) & bf) == 1:
                                discountStraight = True
                        elif countContiguous == 3:
                            discountStraight = True
                        
                        countContiguous = 0
                    
                    # 9x8x
                    if Hand.BitCount(np.uint64(0xc0) & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if Hand.BitCount(np.uint64(0x30) & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 7x or Kx
                            if Hand.BitCount(np.uint64(0x820) & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                        
                        countContiguous = 0
                    
                    # 8x7x
                    if Hand.BitCount(np.uint64(0x60) & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if Hand.BitCount(np.uint64(0x18) & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 6x or Qx
                            if Hand.BitCount(np.uint64(0x410) & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                        
                        countContiguous = 0
                    
                    # 7x6x
                    if Hand.BitCount(np.uint64(0x30) & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if Hand.BitCount(np.uint64(0xc) & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 5x or Jx
                            if Hand.BitCount(np.uint64(0x208) & bf) == 1:
                                # 3 in a row with a gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                        
                        countContiguous = 0
                    
                    # 6x5x
                    if Hand.BitCount(np.uint64(0x18) & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if Hand.BitCount(np.uint64(0x6) & bf) == 2:
                                discountStraight = True
                        elif countContiguous == 2:
                            if Hand.BitCount(np.uint64(0x104) & bf) == 1:
                                discountStraight = True
                        elif countContiguous == 3:
                            discountStraight = True
                        
                        countContiguous = 0
                    
                    # 5x4x
                    if Hand.BitCount(np.uint64(0xc) & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if Hand.BitCount(np.uint64(0x3) & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 3x or 9x
                            if Hand.BitCount(np.uint64(0x82) & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                        
                        countContiguous = 0

                    # 4x3x
                    if Hand.BitCount(np.uint64(0x6) & bf) == 2:
                        countContiguous += 1
                    else:
                        if countContiguous == 1:
                            if Hand.BitCount(np.uint64(0x1001) & bf) == 2:
                                # 2 connected with a 1 gap in the middle
                                discountStraight = True
                        elif countContiguous == 2:
                            # test for 2x or 8x
                            if Hand.BitCount(np.uint64(0x41) & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                        
                        countContiguous = 0
                    
                    # 3x2x
                    if Hand.BitCount(np.uint64(0x3) & bf) == 2:
                        countContiguous += 1
                    else:                            
                        if countContiguous == 2:
                            # test for Ax or 7x
                            if Hand.BitCount(np.uint64(0x1020) & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                        
                        countContiguous = 0

                    # 2xAx
                    if Hand.BitCount(np.uint64(0x1001) & bf) == 2:
                        countContiguous += 1
                        # check one last time
                        if countContiguous == 2:
                            # test for 5x
                            if Hand.BitCount(np.uint64(0x8) & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                    else:                            
                        if countContiguous == 2:
                            # test for 6x
                            if Hand.BitCount(np.uint64(0x10) & bf) == 1:
                                # 3 in a row with a 1 gap connected
                                discountStraight = True
                        elif countContiguous == 3: # 4 in a row
                            discountStraight = True
                    
                    # Hand improving to a pair, must use overcards and not make a 3 suited board
                    if playerNewHandType == Hand.HandTypes.PAIR:
                        newCardVal = Hand.Evaluate(card)
                        newTopCard = Hand.TopCard(newCardVal)
                        if boardOrigTopCard < newTopCard and not (discountSuitedBoard or discountSuitedOut) and not discountStraight:
                            isOut = True
                    
                    # Hand imporving to two pair, must use one of the players pocket cards and 
                    # the player already has a pair, either a pocket pair or a pair using the board. 
                    # ie: not drawing to two pair when trips is out - drawing dead.
                    # And not make a 3 suited board and not discounting for a straight. 
                    elif playerNewHandType == Hand.HandTypes.TWO_PAIR:
                        playerPocketHandNewCardVal = Hand.Evaluate(player | card)
                        playerPocketHandNewCardType = Hand.HandType(playerPocketHandNewCardVal)
                        if (playerPocketHandNewCardType == Hand.HandTypes.PAIR and playerPocketHandType != Hand.HandTypes.PAIR) and (boardOrigHandType != Hand.HandTypes.PAIR or playerOrigHandType == Hand.HandTypes.TWO_PAIR):
                            if not (discountSuitedBoard or discountSuitedOut) and not discountStraight:
                                isOut = True;

                    # New hand better than two pair
                    elif playerNewHandType > Hand.HandTypes.TWO_PAIR:
                        # Hand imporving trips, must not make a 3 suited board and not discounting for a straight. 
                        if playerNewHandType == Hand.HandTypes.TRIPS:
                            if not (discountSuitedBoard or discountSuitedOut) and not discountStraight:
                                isOut = True
                        # Hand imporving to a straight, must not make a 3 suited board.
                        elif playerNewHandType == Hand.HandTypes.STRAIGHT:
                            if not (discountSuitedBoard or discountSuitedOut):
                                isOut = True
                        else:
                            # No discounting for a Flush (should we consider a straight Flush?),
                            # Full house, Four of a kind and straight flush
                            isOut = True
                    
                    if isOut:
                        retval |= card

        return retval

    # Returns the number of outs possible with the next card. Note that cards that only
    # help the board will be ignored.
    # player - Player's pocket cards
    # board - The board (must contain either 3 or 4 card)
    # opponentsList - a list of zero or more opponent cards
    @staticmethod    
    def OutCards(player: str, board: str, opponentsList):
        playerMask = Hand.ParseHand(player)[0]
        boardMask = Hand.ParseHand(board)[0]
        if not Hand.ValidateHand(player) and not Hand.BitCount(player) != 2:
            raise Exception("Invalid player pocket")
        if not Hand.ValidateHand(board) and not Hand.BitCount(board) != 3 and Hand.BitCount(board) != 4:
            raise Exception("Invalid board")
        
        opponentsMask = []
        i = 0
        while i < len(opponentsList):
            oppMask = Hand.ParseHand(opponentsList[i])
            if not Hand.ValidateHand(opponentsList[i]) and not oppMask[1] != 2:
                raise Exception("Invalid opponent pocket cards")
            opponentsMask.append(oppMask[0])
            i += 1
        
        mask = HandAnalysis.OutsMask(playerMask, boardMask, opponentsMask)
        retval = ""
        for s in Hand.Cards(mask):
            if len(retval) == 0:
                retval = s
            else:
                retval += " " + s
        
        return retval
    
    # Creates a Hand mask with the cards that will improve the specified players mask
    # against a list of opponents or if no opponents are list just the cards that improve the 
    # players current had.
    # 
    # Please note that this only looks at single cards that improve the mask and will not specifically
    # look at runner-runner possiblities.
    # player - Player's pocket cards
    # board - The board (must contain either 3 or 4 cards)
    # opponents - A list of zero or more opponent pocket cards
    # Returns a mask of all of the cards that improve the mask
    def OutsMask(player: np.uint64, board: np.uint64, opponentsList):
        retval = np.uint64(0)
        if __debug__:
            if Hand.BitCount(player) != 2:
                raise Exception("Player must have exactly two cards")
            if Hand.BitCount(board) != 3 and Hand.BitCount(board) != 4:
                raise Exception("Board must contain 3 or 4 cards")
        
        # Get original mask value
        playerOrigHandVal = Hand.Evaluate(player | board)

        # Look ahead one card
        shared = np.uint64(0)
        for card in Hand.Hands(shared, board | player, 1):
            # Get new mask value
            playerNewHandVal = Hand.Evaluate(player | board | card)

            # Get new board value
            boardHandVal = Hand.Evaluate(board | card)

            # Is the new mask better than the old one?
            handImproved = playerNewHandVal > playerOrigHandVal

            # This compare ensures we move up in mask type
            handStrongerThanBoard = Hand.HandType(playerNewHandVal) > Hand.HandType(boardHandVal) \
                or (Hand.HandType(playerNewHandVal) == Hand.HandType(boardHandVal) \
                and Hand.TopCard(playerNewHandVal) > Hand.TopCard(boardHandVal))
            
            # Check against opponents cards
            handBeatAllOpponents = True
            if handImproved and handStrongerThanBoard and len(opponentsList) > 0:
                for opponent in opponentsList:
                    opponentHandVal = Hand.Evaluate(opponent | board | card)
                    if opponentHandVal > playerNewHandVal:
                        handBeatAllOpponents = False
                        break
            
            # if the mask improved then we have an out
            if handImproved and handStrongerThanBoard and handBeatAllOpponents:
                retval |= card
        
        # return outs as mask mask
        return retval
    
    # Returns the number of outs possible with the next card
    # player - Player's pocket cards
    # board - The board (must contain either 3 or 4 cards)
    # oponents - A list of zero or more opponent cards.
    # Returns the count of the number of single cards that improve the current mask.
    @staticmethod
    def Outs(player: np.uint64, board: np.uint64, opponentsList):
        return Hand.BitCount(HandAnalysis.OutsMask(player, board, opponentsList))
        
    # Creates a Hand mask with the cards that will improve the specified players mask.
    #
    # Please note that this only looks at single cards that improve the mask and will not specifically
    # look at runner-runner possiblities.
    # 
    # This version of outs contributed by Matt Baker
    # player - Player pocket cards
    # board - The board (must contain either 3 or 4 cards)
    # dead - dead cards
    # Returns a mask of all of the cards that improve the mask
    @staticmethod
    @dispatch(np.uint64, np.uint64, np.uint64)
    def OutsMaskEx(player: np.uint64, board: np.uint64, dead: np.uint64):
        retval = np.uint64(0)
        ncards = Hand.BitCount(player | board)
        if __debug__:
            if Hand.BitCount(player) != 2:
                raise Exception("Player pocket must exactly have two cards.")
            if ncards != 5 and ncards != 6:
                raise Exception("Outs only make sense after the flop and before the River")
        
        # Look at the cards that improve the mask
        playerOrigHandVal = Hand.Evaluate(player | board | np.uint64(ncards))
        playerOrigHandType = Hand.HandType(playerOrigHandVal)
        playerOrigTopCard = Hand.TopCard(playerOrigHandVal)
        boardOrigHandVal = Hand.Evaluate(board)
        boardOrigHandType = Hand.HandType(boardOrigHandVal)
        boardOrigTopCard = Hand.TopCard(boardOrigHandVal)

        # Look at players pocket cards for special cases
        playerPocketHandVal = Hand.Evaluate(player)
        playerPocketHandType = Hand.HandType(playerPocketHandVal)

        # Look ahead one card
        shared = np.uint64(0)
        for card in Hand.Hands(shared, dead | board | player, 1):
            boardNewHandVal = Hand.Evaluate(board | card)
            boardNewHandType = Hand.HandType(boardNewHandVal)
            boardNewTopCard = Hand.TopCard(boardNewHandVal)
            playerNewHandVal = Hand.Evaluate(player | board | card, ncards + 1)
            playerNewHandType = Hand.HandType(playerNewHandVal)
            playerNewTopCard = Hand.TopCard(playerNewHandVal)
            playerImproved = playerNewHandType > playerOrigHandType or (playerNewHandType == playerOrigHandType and playerNewTopCard > playerOrigTopCard) \
                or (playerNewHandType == playerOrigHandType and playerNewHandType == Hand.HandTypes.TWO_PAIR and playerNewHandVal > playerOrigHandVal)
            playerStrongerThanBoard = playerNewHandType > boardNewHandType or (playerNewHandType == boardNewHandType and playerNewTopCard > boardNewTopCard)

            if playerImproved and playerStrongerThanBoard:
                # New mask better than two pair and special case pocket pair improving to full house
                if playerNewHandType > Hand.HandTypes.TWO_PAIR or (playerPocketHandType == Hand.HandTypes.PAIR and playerNewHandType > Hand.HandTypes.TWO_PAIR):
                    retval |= card
                else:
                    # Special case pair improving to two pair must use one of the players cards.
                    playerPocketHandNewCardVal = Hand.Evaluate(player | card)
                    playerPocketHandNewCardType = Hand.Evaluate(playerPocketHandNewCardVal)
                    if playerPocketHandNewCardType == Hand.HandTypes.PAIR and playerPocketHandType != Hand.HandTypes.PAIR:
                        retval |= card

        return retval

    @staticmethod
    @dispatch(str, str, str)
    def OutsMaskEx(pocket: str, board: str, dead: str):
        return HandAnalysis.OutsMaskEx(Hand.ParseHand(pocket), Hand.ParseHand(board), Hand.ParseHand(dead))

    @staticmethod
    @dispatch(np.uint64, np.uint64, np.uint64)
    def OutsEx(pocket: np.uint64, board: np.uint64, dead: np.uint64):
        return Hand.BitCount(HandAnalysis.OutsMaskEx(pocket, board, dead))
    
    @staticmethod
    @dispatch(str, str, str)
    def OutsEx(pocket: str, board: str, dead: str):
        return HandAnalysis.OutsEx(Hand.ParseHand(pocket), Hand.ParseHand(board), Hand.ParseHand(dead))
    
    # This function returns true if the cards in the mask are all one suit. This method
    # calculates the results. Because of the equivelent call in PocketHands is preferred
    # because it uses a lookup table and is faster. This function remains to allow for automated
    # testing.
    # mask - mask to check for "suited-ness"
    # Returns true if all hands are of the same suit, false otherwise
    @staticmethod
    def IsSuited(mask: np.uint64):
        cards = Hand.BitCount(mask)
        sc = Hand.CardMask(mask, Hand.CLUBS)
        sd = Hand.CardMask(mask, Hand.DIAMONDS)
        sh = Hand.CardMask(mask, Hand.HEARTS)
        ss = Hand.CardMask(mask, Hand.SPADES)

        return Hand.BitCount(sc) == cards or Hand.BitCount(sd) == cards \
            or Hand.BitCount(sh) == cards or Hand.BitCount(ss) == cards

    # Returns true if the cards in the two card mask are connected. This method
    # calculates the results. Because of that equivelent call in PocketHands is preferred
    # because it uses a lookup table and is faster. This function remains to allow for automated
    # testing.
    # mask - the mask to check
    # returns true of all the cards are next to each other
    @staticmethod
    def IsConnected(mask: np.uint64):
        return HandAnalysis.GapCount(mask) == 0

    # Counts the number of empty space between adjacent cards. 0 means connected, 1 means a gap
    # of one, 2 means a gap of two and 3 means a gap of three. This method
    # calculates the results. Because of that equivelent call in PocketHands is preferred
    # because it uses a lookup table and is faster. This function remains to allow for automated
    # testing.
    # mask - two card mask mask
    # Returns number of spaces between two cards
    @staticmethod
    def GapCount(mask: np.uint64):
        start = end = 0
        if Hand.BitCount(mask) != 2:
            return -1
        
        bf = Hand.CardMask(mask, Hand.CLUBS) or Hand.CardMask(mask, Hand.DIAMONDS) \
            or Hand.CardMask(mask, Hand.HEARTS) or Hand.CardMask(mask, Hand.SPADES)
        
        i = 12
        leftShiftOne = np.uint64(1)
        while i >= 0:
            start = np.uint64(i)
            if bf & (leftShiftOne << start) != 0:
                break
            i -= 1
        
        i = start - 1
        while i >= 0:
            end = np.uint64(i)
            if bf & (leftShiftOne << end) != 0:
                break
            i -= 1
        
        if start == 12 and end == 0: return 0
        if start == 12 and end == 1: return 1
        if start == 12 and end == 2: return 2
        if start == 12 and end == 3: return 3

        result = start - end - 1
        if result > 3:
            return -1
        else:
            return result

    # Cacluates the approxamate odds that each player and opponent mask
    # type has to win. This method uses Monte Carlo Analysis to determine
    # a results. The quality of the result will depend on the number of trials.
    # pocket - Players Hand
    # board - Current board
    # dead - Dead cards
    # playerCount - The number of players in the mask
    # Returns a Tuple<playerOddsList, opponentOddsList>
    # TODO This one requires a PocketHand query parser
    @staticmethod
    def DetailedOddsWithMultiplePlayers(pocket: str, board: str, dead: str, playerCount: int, trials: int):
        count = 0
        deadMask = 0
        finalBoard = 0
        pocketMask = 0

        # Intermediate results
        opponent = [0] * playerCount
        oppHandVal = [0] * playerCount

        # Storage for results
        podds = [0.0] * 9
        oodds = [0.0] * 9

        if __debug__:
            if not Hand.ValidateHand(board):
                raise Exception("Invalid board")
            if playerCount < 1 or playerCount > 9:
                raise Exception("Invalid player count")
            if Hand.BitCount(Hand.ParseHand(board)) > 5:
                raise Exception("Board must be exactly 5 cards")
            if trials <= 0:
                raise Exception("Trials must be a positive number")
            # require PocketQuery parser
            #if not PocketHands.ValidateQuery(pocket)      

        boardMask = Hand.ParseHand(board)      
        #pocketList = PockatHands.Query(pocket, boardMask | dead)
        
        # while count < trials:
        #     pocketMask = Hand.RandomHand(boardMask)
        pass

    # Cacluates the approxamate odds that each player and opponent mask
    # type has to win. This method uses Monte Carlo Analysis to determine
    # a results. The quality of the result will depend on the amount of time
    # allowed for the simulation.
    # pocket - Players hand
    # board - Current board
    # dead - Dead cards
    # playerCount - the number of players in the mask
    # duration - The time allowed to run the simulation
    # Returns a Tuple<playerOddsList, oppOddsList>
    # TODO: Requires a pocket query parser
    @staticmethod
    def DetailedOddsWithMultiplePlayers(pocket: str, board: str, dead: int, playerCount: int, duration: float):
        pass

    # Returns a Tuple<playerOddsList, oppOddList, isApproximate>
    @staticmethod
    @dispatch(object, object, np.uint64)
    def HandWinOdds(ourCardsList, oppCardsList, board: np.uint64):
        count = ourBest = oppBest = 0
        boardCount = Hand.BitCount(board)
        cards = boardCount + 2
        podds = [0.0] * 9
        oodds = [0.0] * 9

        if __debug__:
            for pocketCards in ourCardsList:
                if Hand.BitCount(pocketCards) != 2:
                    raise Exception(pocketCards + " is invalid. Expecting two cards only.")

            for pocketCards in oppCardsList:
                if Hand.BitCount(pocketCards) != 2:
                    raise Exception(pocketCards +" is invalid. Expecting two cards only.")
            if boardCount > 5: 
                raise Exception("Invalid board. Up to five cards only.")

        player = podds
        opponent = oodds
        if boardCount == 0:
            # calculate monte carlo results
            for pocketCards in ourCardsList:
                if pocketCards & board != 0:
                    continue
                for oppHand in oppCardsList:
                    if oppHand & pocketCards != 0 or oppHand & board != 0: 
                        continue
                    for handMask in Hand.RandomHand(board, pocketCards | oppHand, 5, (5.0 / (len(ourCardsList) * len(oppCardsList)))):
                        ourBest = Hand.Evaluate(pocketCards | handMask, 7)
                        oppBest = Hand.Evaluate(oppHand | handMask, 7)
                        if ourBest > oppBest:
                            player[Hand.HandType(ourBest)] += 1.0
                        elif ourBest == oppBest:
                            player[Hand.HandType(ourBest)] += 0.5
                            opponent[Hand.HandType(oppBest)] += 0.5
                        else:
                            opponent[Hand.HandType(oppBest)] += 1.0
                        count += 1
            
            i = 0
            while i < 9:
                player[i] = player[i] / count
                opponent[i] = opponent[i] / count
                i += 1

            return (player, opponent, True)
        else:
            # calculate results
            for pocketCards in ourCardsList:
                if pocketCards & board != 0: 
                    continue
                
                for oppHand in oppCardsList:
                    if oppHand & pocketCards != 0 or oppHand & board != 0:
                        continue
                
                    for handMask in Hand.Hands(board, pocketCards | oppHand, 5):
                        ourBest = Hand.Evaluate(pocketCards | handMask, 7)
                        oppBest = Hand.Evaluate(oppHand | handMask, 7)
                        if ourBest > oppBest:
                            player[Hand.HandType(ourBest)] += 1.0
                        elif ourBest == oppBest:
                            player[Hand.HandType(ourBest)] += 0.5
                            opponent[Hand.HandType(oppBest)] += 0.5
                        else:
                            opponent[Hand.HandType(oppBest)] += 1.0
                        
                        count += 1
            i = 0
            while i < 9:
                player[i] = player[i] / count
                opponent[i] = opponent[i] / count
                i += 1
            
            return (player, opponent, False)
    
    # Given a set of pocket cards and a set of board cards this function returns the odds of winning or tying for a player and a random opponent.
    # ourCards - Pocket mask for the mask
    # board - Board mask for mask
    # Returns a Tuple<playerOddsList, opponentOddsList>
    @staticmethod
    @dispatch(np.uint64, np.uint64)
    def HandWinOdds(ourCards: np.uint64, board: np.uint64):
        ourBest = oppBest = 0
        count = 0
        cards = Hand.BitCount(ourCards | board)
        boardCount = Hand.BitCount(board)
        podds = [0.0] * 9
        oodds = [0.0] * 9
        if __debug__:
            if Hand.BitCount(ourCards) != 2:
                raise Exception("Player cards must be exactly two cards")
            if boardCount > 5:
                raise Exception("Board must not exceed five cards")
        
        # Use precalculated results for pocket cards
        if boardCount == 0:
            pocketHand = Hand.PocketHand169Type(ourCards)
            player = HandAnalysis.__PreCalcPlayerOdds()[pocketHand.value]
            opponent = HandAnalysis.__PreCalcOppOdds()[pocketHand.value]
            return (player, opponent)

        player = podds
        opponent = oodds

        for oppCards in Hand.Hands(0, ourCards | board, 2):
            for handMask in Hand.Hands(board, ourCards | oppCards, 5):
                ourBest = Hand.Evaluate(ourCards | handMask, 7)
                oppBest = Hand.Evaluate(oppCards | handMask, 7)
                if ourBest > oppBest:
                    player[Hand.HandType(ourBest)] += 1.0
                elif ourBest == oppBest:
                    player[Hand.HandType(ourBest)] += 0.5
                    opponent[Hand.HandType(oppBest)] += 0.5
                else:
                    opponent[Hand.HandType(oppBest)] += 1.0
                
                count += 1
        
        i = 0
        while i < 9:
            player[i] = player[i] / count
            opponent[i] = opponent[i] / count
            i += 1

        return (player, opponent)
    
    # Given a set of pocket cards and a set of board cards this function returns the odds of winning or tying for a player and a random opponent.
    # pocketCards - Pocket cards in ASCII
    # boardCards - Board cards in ASCII
    # Returns a Tuple<playerOddsList, opponentOddsList>
    @staticmethod
    @dispatch(str, str)
    def HandWinOdds(pocketCards: str, boardCards: str):
        return HandAnalysis.HandWinOdds(Hand.ParseHand(pocketCards)[0], Hand.ParseHand(boardCards)[0])
    
    # This method calculates the probablity of a player winning with specific hands and 
    # opponents winning with specific hands.
    # ourCards - pocket card mask
    # board - board cards mask
    # numberOfOpponents - The number of opponents
    # duration - The amount of time in seconds to calculate samples
    # Returns a Tuple<playerOddsList, opponentOddsList>
    @staticmethod
    @dispatch(np.uint64, np.uint64, int, float)
    def HandWinOdds(ourCards: np.uint64, board: np.uint64, numberOfOpponents: int, duration: float):
        count = 0
        podds = [0.0] * 9
        oodds = [0.0] * 9
        player = podds
        opponent = oodds

        if numberOfOpponents == 1:
            shared = np.uint64(0)
            for boardMask in Hand.RandomHand(board, ourCards, 5, duration):
                oppCards = Hand.RandomHand(shared, boardMask | ourCards, 2)
                playerHandVal = Hand.Evaluate(ourCards | boardMask, 7)
                oppHandVal = Hand.Evaluate(oppCards | boardMask, 7)

                if playerHandVal > oppHandVal:
                    player[Hand.HandType(playerHandVal)] += 1.0
                elif playerHandVal == oppHandVal:
                    player[Hand.HandType(playerHandVal)] += 0.5
                    opponent[Hand.HandType(oppHandVal)] += 0.5
                else:
                    opponent[Hand.HandType(oppHandVal)] += 1.0
                
                count += 1

        elif numberOfOpponents == 2:
            shared = np.uint64(0)
            for boardMask in Hand.RandomHand(board, ourCards, 5, duration):
                opp1cards = Hand.RandomHand(shared, boardMask | ourCards, 2)
                opp2cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards, 2)
                playerHandVal = Hand.Evaluate(ourCards | boardMask, 7)
                opp1HandVal = Hand.Evaluate(opp1cards | boardMask, 7)
                opp2HandVal = Hand.Evaluate(opp2cards | boardMask, 7)

                if playerHandVal > opp1HandVal and playerHandVal >= opp2HandVal:
                    player[Hand.HandType(playerHandVal)] += 1.0
                elif playerHandVal >= opp1HandVal and playerHandVal >= opp2HandVal:
                    player[Hand.HandType(playerHandVal)] += 0.5
                    opponent[Hand.HandType(playerHandVal)] += 0.5
                else:
                    if opp1HandVal > opp2HandVal:
                        opponent[Hand.HandType(opp1HandVal)] += 1.0
                    else:
                        opponent[Hand.HandType(opp2HandVal)] += 1.0
                
                count += 1
        elif numberOfOpponents == 3:
            shared = np.uint64(0)
            for boardMask in Hand.RandomHand(board, ourCards, 5, duration):
                opp1cards = Hand.RandomHand(shared, boardMask | ourCards, 2)
                opp2cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards, 2)
                opp3cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards, 2)
                playerHandVal = Hand.Evaluate(ourCards | boardMask, 7)
                opp1HandVal = Hand.Evaluate(opp1cards | boardMask, 7)
                opp2HandVal = Hand.Evaluate(opp2cards | boardMask, 7)
                opp3HandVal = Hand.Evaluate(opp3cards | boardMask, 7)

                if playerHandVal > opp1HandVal and playerHandVal > opp2HandVal and playerHandVal > opp3HandVal:
                    player[Hand.HandType(playerHandVal)] += 1.0
                elif playerHandVal >= opp1HandVal and playerHandVal >= opp2HandVal and playerHandVal >= opp3HandVal:
                    player[Hand.HandType(playerHandVal)] += 0.5
                    opponent[Hand.HandType(playerHandVal)] += 0.5
                else:
                    if opp1HandVal >= opp2HandVal and opp1HandVal >= opp3HandVal:
                        opponent[Hand.HandType(opp1HandVal)] += 1.0
                    elif opp2HandVal >= opp1HandVal and opp2HandVal >= opp3HandVal:
                        opponent[Hand.HandType(opp2HandVal)] += 1.0
                    elif opp3HandVal >= opp1HandVal and opp3HandVal >= opp2HandVal:
                        opponent[Hand.HandType(opp3HandVal)] += 1.0
                
                count += 1

        elif numberOfOpponents == 4:
            shared = np.uint64(0)
            for boardMask in Hand.RandomHand(board, ourCards, 5, duration):
                opp1cards = Hand.RandomHand(shared, boardMask | ourCards, 2)
                opp2cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards, 2)
                opp3cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards, 2)
                opp4cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards, 2)
                playerHandVal = Hand.Evaluate(ourCards | boardMask, 7)
                opp1HandVal = Hand.Evaluate(opp1cards | boardMask, 7)
                opp2HandVal = Hand.Evaluate(opp2cards | boardMask, 7)
                opp3HandVal = Hand.Evaluate(opp3cards | boardMask, 7)
                opp4HandVal = Hand.Evaluate(opp4cards | boardMask, 7)

                if playerHandVal > opp1HandVal and playerHandVal > opp2HandVal and playerHandVal > opp3HandVal \
                    and playerHandVal > opp4HandVal:
                    player[Hand.HandType(playerHandVal)] += 1.0
                elif playerHandVal >= opp1HandVal and playerHandVal >= opp2HandVal and playerHandVal >= opp3HandVal \
                    and playerHandVal >= opp4HandVal:
                    player[Hand.HandType(playerHandVal)] += 0.5
                    opponent[Hand.HandType(playerHandVal)] += 0.5
                else:
                    if opp1HandVal >= opp2HandVal and opp1HandVal >= opp3HandVal \
                        and opp1HandVal >= opp4HandVal:
                        opponent[Hand.HandType(opp1HandVal)] += 1.0
                    elif opp2HandVal >= opp1HandVal and opp2HandVal >= opp3HandVal \
                        and opp2HandVal >= opp4HandVal:
                        opponent[Hand.HandType(opp2HandVal)] += 1.0
                    elif opp3HandVal >= opp1HandVal and opp3HandVal >= opp2HandVal \
                        and opp3HandVal >= opp4HandVal:
                        opponent[Hand.HandType(opp3HandVal)] += 1.0
                    elif opp4HandVal >= opp1HandVal and opp4HandVal >= opp2HandVal \
                        and opp4HandVal >= opp3HandVal:
                        opponent[Hand.HandType(opp4HandVal)] += 1.0
                
                count += 1

        elif numberOfOpponents == 5:
            shared = np.uint64(0)
            for boardMask in Hand.RandomHand(board, ourCards, 5, duration):
                opp1cards = Hand.RandomHand(shared, boardMask | ourCards, 2)
                opp2cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards, 2)
                opp3cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards, 2)
                opp4cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                playerHandVal = Hand.Evaluate(ourCards | boardMask, 7)
                opp1HandVal = Hand.Evaluate(opp1cards | boardMask, 7)
                opp2HandVal = Hand.Evaluate(opp2cards | boardMask, 7)
                opp3HandVal = Hand.Evaluate(opp3cards | boardMask, 7)
                opp4HandVal = Hand.Evaluate(opp4cards | boardMask, 7)
                opp5HandVal = Hand.Evaluate(opp5cards | boardMask, 7)

                if playerHandVal > opp1HandVal and playerHandVal > opp2HandVal and playerHandVal > opp3HandVal \
                    and playerHandVal > opp4HandVal and playerHandVal > opp5HandVal:
                    player[Hand.HandType(playerHandVal)] += 1.0
                elif playerHandVal >= opp1HandVal and playerHandVal >= opp2HandVal and playerHandVal >= opp3HandVal \
                    and playerHandVal >= opp4HandVal and playerHandVal >= opp5HandVal \
                    and playerHandVal >= opp5HandVal:
                    player[Hand.HandType(playerHandVal)] += 0.5
                    opponent[Hand.HandType(playerHandVal)] += 0.5
                else:
                    if opp1HandVal >= opp2HandVal and opp1HandVal >= opp3HandVal \
                        and opp1HandVal >= opp4HandVal and opp1HandVal >= opp5HandVal:
                        opponent[Hand.HandType(opp1HandVal)] += 1.0
                    elif opp2HandVal >= opp1HandVal and opp2HandVal >= opp3HandVal \
                        and opp2HandVal >= opp4HandVal and opp2HandVal >= opp5HandVal:
                        opponent[Hand.HandType(opp2HandVal)] += 1.0
                    elif opp3HandVal >= opp1HandVal and opp3HandVal >= opp2HandVal \
                        and opp3HandVal >= opp4HandVal and opp3HandVal >= opp5HandVal:
                        opponent[Hand.HandType(opp3HandVal)] += 1.0
                    elif opp4HandVal >= opp1HandVal and opp4HandVal >= opp2HandVal \
                        and opp4HandVal >= opp3HandVal and opp4HandVal >= opp5HandVal:
                        opponent[Hand.HandType(opp4HandVal)] += 1.0
                    elif opp5HandVal >= opp1HandVal and opp5HandVal >= opp2HandVal \
                        and opp5HandVal >= opp3HandVal and opp5HandVal >= opp4HandVal:
                        opponent[Hand.HandType(opp5HandVal)] += 1.0
                
                count += 1
        elif numberOfOpponents == 6:
            shared = np.uint64(0)
            for boardMask in Hand.RandomHand(board, ourCards, 5, duration):
                opp1cards = Hand.RandomHand(shared, boardMask | ourCards, 2)
                opp2cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards, 2)
                opp3cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards, 2)
                opp4cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp6cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards, 2)
                playerHandVal = Hand.Evaluate(ourCards | boardMask, 7)
                opp1HandVal = Hand.Evaluate(opp1cards | boardMask, 7)
                opp2HandVal = Hand.Evaluate(opp2cards | boardMask, 7)
                opp3HandVal = Hand.Evaluate(opp3cards | boardMask, 7)
                opp4HandVal = Hand.Evaluate(opp4cards | boardMask, 7)
                opp5HandVal = Hand.Evaluate(opp5cards | boardMask, 7)
                opp6HandVal = Hand.Evaluate(opp6cards | boardMask, 7)

                if playerHandVal > opp1HandVal and playerHandVal > opp2HandVal and playerHandVal > opp3HandVal \
                    and playerHandVal > opp4HandVal and playerHandVal > opp5HandVal \
                    and playerHandVal > opp6HandVal:
                    player[Hand.HandType(playerHandVal)] += 1.0
                elif playerHandVal >= opp1HandVal and playerHandVal >= opp2HandVal and playerHandVal >= opp3HandVal \
                    and playerHandVal >= opp4HandVal and playerHandVal >= opp5HandVal \
                    and playerHandVal >= opp5HandVal and playerHandVal >= opp6HandVal:
                    player[Hand.HandType(playerHandVal)] += 0.5
                    opponent[Hand.HandType(playerHandVal)] += 0.5
                else:
                    if opp1HandVal >= opp2HandVal and opp1HandVal >= opp3HandVal \
                        and opp1HandVal >= opp4HandVal and opp1HandVal >= opp5HandVal \
                        and opp1HandVal >= opp6HandVal:
                        opponent[Hand.HandType(opp1HandVal)] += 1.0
                    elif opp2HandVal >= opp1HandVal and opp2HandVal >= opp3HandVal \
                        and opp2HandVal >= opp4HandVal and opp2HandVal >= opp5HandVal \
                        and opp2HandVal >= opp6HandVal:
                        opponent[Hand.HandType(opp2HandVal)] += 1.0
                    elif opp3HandVal >= opp1HandVal and opp3HandVal >= opp2HandVal \
                        and opp3HandVal >= opp4HandVal and opp3HandVal >= opp5HandVal \
                        and opp3HandVal >= opp6HandVal:
                        opponent[Hand.HandType(opp3HandVal)] += 1.0
                    elif opp4HandVal >= opp1HandVal and opp4HandVal >= opp2HandVal \
                        and opp4HandVal >= opp3HandVal and opp4HandVal >= opp5HandVal \
                        and opp4HandVal >= opp6HandVal:
                        opponent[Hand.HandType(opp4HandVal)] += 1.0
                    elif opp5HandVal >= opp1HandVal and opp5HandVal >= opp2HandVal \
                        and opp5HandVal >= opp3HandVal and opp5HandVal >= opp4HandVal \
                        and opp5HandVal >= opp6HandVal:
                        opponent[Hand.HandType(opp5HandVal)] += 1.0
                    elif opp6HandVal >= opp1HandVal and opp6HandVal >= opp2HandVal \
                        and opp6HandVal >= opp3HandVal and opp6HandVal >= opp4HandVal \
                        and opp6HandVal >= opp5HandVal:
                        opponent[Hand.HandType(opp6HandVal)] += 1.0                    
                
                count += 1
        elif numberOfOpponents == 7:
            shared = np.uint64(0)
            for boardMask in Hand.RandomHand(board, ourCards, 5, duration):
                opp1cards = Hand.RandomHand(shared, boardMask | ourCards, 2)
                opp2cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards, 2)
                opp3cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards, 2)
                opp4cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp6cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards, 2)
                opp7cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards, 2)
                playerHandVal = Hand.Evaluate(ourCards | boardMask, 7)
                opp1HandVal = Hand.Evaluate(opp1cards | boardMask, 7)
                opp2HandVal = Hand.Evaluate(opp2cards | boardMask, 7)
                opp3HandVal = Hand.Evaluate(opp3cards | boardMask, 7)
                opp4HandVal = Hand.Evaluate(opp4cards | boardMask, 7)
                opp5HandVal = Hand.Evaluate(opp5cards | boardMask, 7)
                opp6HandVal = Hand.Evaluate(opp6cards | boardMask, 7)
                opp7HandVal = Hand.Evaluate(opp7cards | boardMask, 7)

                if playerHandVal > opp1HandVal and playerHandVal > opp2HandVal and playerHandVal > opp3HandVal \
                    and playerHandVal > opp4HandVal and playerHandVal > opp5HandVal \
                    and playerHandVal > opp6HandVal and playerHandVal > opp7HandVal:
                    player[Hand.HandType(playerHandVal)] += 1.0
                elif playerHandVal >= opp1HandVal and playerHandVal >= opp2HandVal and playerHandVal >= opp3HandVal \
                    and playerHandVal >= opp4HandVal and playerHandVal >= opp5HandVal \
                    and playerHandVal >= opp5HandVal and playerHandVal >= opp6HandVal \
                    and playerHandVal >= opp7HandVal:
                    player[Hand.HandType(playerHandVal)] += 0.5
                    opponent[Hand.HandType(playerHandVal)] += 0.5
                else:
                    if opp1HandVal >= opp2HandVal and opp1HandVal >= opp3HandVal \
                        and opp1HandVal >= opp4HandVal and opp1HandVal >= opp5HandVal \
                        and opp1HandVal >= opp6HandVal and opp1HandVal >= opp7HandVal:
                        opponent[Hand.HandType(opp1HandVal)] += 1.0
                    elif opp2HandVal >= opp1HandVal and opp2HandVal >= opp3HandVal \
                        and opp2HandVal >= opp4HandVal and opp2HandVal >= opp5HandVal \
                        and opp2HandVal >= opp6HandVal and opp2HandVal >= opp7HandVal:
                        opponent[Hand.HandType(opp2HandVal)] += 1.0
                    elif opp3HandVal >= opp1HandVal and opp3HandVal >= opp2HandVal \
                        and opp3HandVal >= opp4HandVal and opp3HandVal >= opp5HandVal \
                        and opp3HandVal >= opp6HandVal and opp3HandVal >= opp7HandVal:
                        opponent[Hand.HandType(opp3HandVal)] += 1.0
                    elif opp4HandVal >= opp1HandVal and opp4HandVal >= opp2HandVal \
                        and opp4HandVal >= opp3HandVal and opp4HandVal >= opp5HandVal \
                        and opp4HandVal >= opp6HandVal and opp4HandVal >= opp7HandVal:
                        opponent[Hand.HandType(opp4HandVal)] += 1.0
                    elif opp5HandVal >= opp1HandVal and opp5HandVal >= opp2HandVal \
                        and opp5HandVal >= opp3HandVal and opp5HandVal >= opp4HandVal \
                        and opp5HandVal >= opp6HandVal and opp5HandVal >= opp7HandVal:
                        opponent[Hand.HandType(opp5HandVal)] += 1.0
                    elif opp6HandVal >= opp1HandVal and opp6HandVal >= opp2HandVal \
                        and opp6HandVal >= opp3HandVal and opp6HandVal >= opp4HandVal \
                        and opp6HandVal >= opp5HandVal and opp6HandVal >= opp7HandVal:
                        opponent[Hand.HandType(opp6HandVal)] += 1.0
                    elif opp7HandVal >= opp1HandVal and opp7HandVal >= opp2HandVal \
                        and opp7HandVal >= opp3HandVal and opp7HandVal >= opp4HandVal \
                        and opp7HandVal >= opp5HandVal and opp7HandVal >= opp6HandVal:
                        opponent[Hand.HandType(opp7HandVal)] += 1.0                    
                
                count += 1
        elif numberOfOpponents == 8:
            shared = np.uint64(0)
            for boardMask in Hand.RandomHand(board, ourCards, 5, duration):
                opp1cards = Hand.RandomHand(shared, boardMask | ourCards, 2)
                opp2cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards, 2)
                opp3cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards, 2)
                opp4cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp6cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards, 2)
                opp7cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards, 2)
                opp8cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards, 2)
                playerHandVal = Hand.Evaluate(ourCards | boardMask, 7)
                opp1HandVal = Hand.Evaluate(opp1cards | boardMask, 7)
                opp2HandVal = Hand.Evaluate(opp2cards | boardMask, 7)
                opp3HandVal = Hand.Evaluate(opp3cards | boardMask, 7)
                opp4HandVal = Hand.Evaluate(opp4cards | boardMask, 7)
                opp5HandVal = Hand.Evaluate(opp5cards | boardMask, 7)
                opp6HandVal = Hand.Evaluate(opp6cards | boardMask, 7)
                opp7HandVal = Hand.Evaluate(opp7cards | boardMask, 7)
                opp8HandVal = Hand.Evaluate(opp8cards | boardMask, 7)

                if playerHandVal > opp1HandVal and playerHandVal > opp2HandVal and playerHandVal > opp3HandVal \
                    and playerHandVal > opp4HandVal and playerHandVal > opp5HandVal \
                    and playerHandVal > opp6HandVal and playerHandVal > opp7HandVal \
                    and playerHandVal > opp8HandVal:
                    player[Hand.HandType(playerHandVal)] += 1.0
                elif playerHandVal >= opp1HandVal and playerHandVal >= opp2HandVal and playerHandVal >= opp3HandVal \
                    and playerHandVal >= opp4HandVal and playerHandVal >= opp5HandVal \
                    and playerHandVal >= opp5HandVal and playerHandVal >= opp6HandVal \
                    and playerHandVal >= opp7HandVal and playerHandVal >= opp8HandVal:
                    player[Hand.HandType(playerHandVal)] += 0.5
                    opponent[Hand.HandType(playerHandVal)] += 0.5
                else:
                    if opp1HandVal >= opp2HandVal and opp1HandVal >= opp3HandVal \
                        and opp1HandVal >= opp4HandVal and opp1HandVal >= opp5HandVal \
                        and opp1HandVal >= opp6HandVal and opp1HandVal >= opp7HandVal \
                        and opp1HandVal >= opp8HandVal:
                        opponent[Hand.HandType(opp1HandVal)] += 1.0
                    elif opp2HandVal >= opp1HandVal and opp2HandVal >= opp3HandVal \
                        and opp2HandVal >= opp4HandVal and opp2HandVal >= opp5HandVal \
                        and opp2HandVal >= opp6HandVal and opp2HandVal >= opp7HandVal \
                        and opp2HandVal >= opp8HandVal:
                        opponent[Hand.HandType(opp2HandVal)] += 1.0
                    elif opp3HandVal >= opp1HandVal and opp3HandVal >= opp2HandVal \
                        and opp3HandVal >= opp4HandVal and opp3HandVal >= opp5HandVal \
                        and opp3HandVal >= opp6HandVal and opp3HandVal >= opp7HandVal \
                        and opp3HandVal >= opp8HandVal:
                        opponent[Hand.HandType(opp3HandVal)] += 1.0
                    elif opp4HandVal >= opp1HandVal and opp4HandVal >= opp2HandVal \
                        and opp4HandVal >= opp3HandVal and opp4HandVal >= opp5HandVal \
                        and opp4HandVal >= opp6HandVal and opp4HandVal >= opp7HandVal \
                        and opp4HandVal >= opp8HandVal:
                        opponent[Hand.HandType(opp4HandVal)] += 1.0
                    elif opp5HandVal >= opp1HandVal and opp5HandVal >= opp2HandVal \
                        and opp5HandVal >= opp3HandVal and opp5HandVal >= opp4HandVal \
                        and opp5HandVal >= opp6HandVal and opp5HandVal >= opp7HandVal \
                        and opp5HandVal >= opp8HandVal:
                        opponent[Hand.HandType(opp5HandVal)] += 1.0
                    elif opp6HandVal >= opp1HandVal and opp6HandVal >= opp2HandVal \
                        and opp6HandVal >= opp3HandVal and opp6HandVal >= opp4HandVal \
                        and opp6HandVal >= opp5HandVal and opp6HandVal >= opp7HandVal \
                        and opp6HandVal >= opp8HandVal:
                        opponent[Hand.HandType(opp6HandVal)] += 1.0
                    elif opp7HandVal >= opp1HandVal and opp7HandVal >= opp2HandVal \
                        and opp7HandVal >= opp3HandVal and opp7HandVal >= opp4HandVal \
                        and opp7HandVal >= opp5HandVal and opp7HandVal >= opp6HandVal \
                        and opp7HandVal >= opp8HandVal:
                        opponent[Hand.HandType(opp7HandVal)] += 1.0
                    elif opp8HandVal >= opp1HandVal and opp8HandVal >= opp2HandVal \
                        and opp8HandVal >= opp3HandVal and opp8HandVal >= opp4HandVal \
                        and opp8HandVal >= opp5HandVal and opp8HandVal >= opp6HandVal \
                        and opp8HandVal >= opp7HandVal:
                        opponent[Hand.HandType(opp8HandVal)] += 1.0
                
                count += 1
        elif numberOfOpponents == 9:
            shared = np.uint64(0)
            for boardMask in Hand.RandomHand(board, ourCards, 5, duration):
                opp1cards = Hand.RandomHand(shared, boardMask | ourCards, 2)
                opp2cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards, 2)
                opp3cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards, 2)
                opp4cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards, 2)
                opp5cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards, 2)
                opp6cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards, 2)
                opp7cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards, 2)
                opp8cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards | opp7cards, 2)
                opp9cards = Hand.RandomHand(shared, boardMask | ourCards | opp1cards | opp2cards | opp3cards | opp4cards | opp5cards | opp6cards | opp7cards | opp8cards, 2)
                playerHandVal = Hand.Evaluate(ourCards | boardMask, 7)
                opp1HandVal = Hand.Evaluate(opp1cards | boardMask, 7)
                opp2HandVal = Hand.Evaluate(opp2cards | boardMask, 7)
                opp3HandVal = Hand.Evaluate(opp3cards | boardMask, 7)
                opp4HandVal = Hand.Evaluate(opp4cards | boardMask, 7)
                opp5HandVal = Hand.Evaluate(opp5cards | boardMask, 7)
                opp6HandVal = Hand.Evaluate(opp6cards | boardMask, 7)
                opp7HandVal = Hand.Evaluate(opp7cards | boardMask, 7)
                opp8HandVal = Hand.Evaluate(opp8cards | boardMask, 7)
                opp9HandVal = Hand.Evaluate(opp9cards | boardMask, 7)

                if playerHandVal > opp1HandVal and playerHandVal > opp2HandVal and playerHandVal > opp3HandVal \
                    and playerHandVal > opp4HandVal and playerHandVal > opp5HandVal \
                    and playerHandVal > opp6HandVal and playerHandVal > opp7HandVal \
                    and playerHandVal > opp8HandVal and playerHandVal > opp9HandVal:
                    player[Hand.HandType(playerHandVal)] += 1.0
                elif playerHandVal >= opp1HandVal and playerHandVal >= opp2HandVal and playerHandVal >= opp3HandVal \
                    and playerHandVal >= opp4HandVal and playerHandVal >= opp5HandVal \
                    and playerHandVal >= opp6HandVal and playerHandVal >= opp7HandVal \
                    and playerHandVal >= opp8HandVal and playerHandVal >= opp9HandVal:
                    player[Hand.HandType(playerHandVal)] += 0.5
                    opponent[Hand.HandType(playerHandVal)] += 0.5
                else:
                    if opp1HandVal >= opp2HandVal and opp1HandVal >= opp3HandVal \
                        and opp1HandVal >= opp4HandVal and opp1HandVal >= opp5HandVal \
                        and opp1HandVal >= opp6HandVal and opp1HandVal >= opp7HandVal \
                        and opp1HandVal >= opp8HandVal and opp1HandVal > opp9HandVal:
                        opponent[Hand.HandType(opp1HandVal)] += 1.0
                    elif opp2HandVal >= opp1HandVal and opp2HandVal >= opp3HandVal \
                        and opp2HandVal >= opp4HandVal and opp2HandVal >= opp5HandVal \
                        and opp2HandVal >= opp6HandVal and opp2HandVal >= opp7HandVal \
                        and opp2HandVal >= opp8HandVal and opp2HandVal > opp9HandVal:
                        opponent[Hand.HandType(opp2HandVal)] += 1.0
                    elif opp3HandVal >= opp1HandVal and opp3HandVal >= opp2HandVal \
                        and opp3HandVal >= opp4HandVal and opp3HandVal >= opp5HandVal \
                        and opp3HandVal >= opp6HandVal and opp3HandVal >= opp7HandVal \
                        and opp3HandVal >= opp8HandVal and opp3HandVal >= opp9HandVal:
                        opponent[Hand.HandType(opp3HandVal)] += 1.0
                    elif opp4HandVal >= opp1HandVal and opp4HandVal >= opp2HandVal \
                        and opp4HandVal >= opp3HandVal and opp4HandVal >= opp5HandVal \
                        and opp4HandVal >= opp6HandVal and opp4HandVal >= opp7HandVal \
                        and opp4HandVal >= opp8HandVal and opp4HandVal >= opp9HandVal:
                        opponent[Hand.HandType(opp4HandVal)] += 1.0
                    elif opp5HandVal >= opp1HandVal and opp5HandVal >= opp2HandVal \
                        and opp5HandVal >= opp3HandVal and opp5HandVal >= opp4HandVal \
                        and opp5HandVal >= opp6HandVal and opp5HandVal >= opp7HandVal \
                        and opp5HandVal >= opp8HandVal and opp5HandVal >= opp9HandVal:
                        opponent[Hand.HandType(opp5HandVal)] += 1.0
                    elif opp6HandVal >= opp1HandVal and opp6HandVal >= opp2HandVal \
                        and opp6HandVal >= opp3HandVal and opp6HandVal >= opp4HandVal \
                        and opp6HandVal >= opp5HandVal and opp6HandVal >= opp7HandVal \
                        and opp6HandVal >= opp8HandVal and opp6HandVal >= opp9HandVal:
                        opponent[Hand.HandType(opp6HandVal)] += 1.0
                    elif opp7HandVal >= opp1HandVal and opp7HandVal >= opp2HandVal \
                        and opp7HandVal >= opp3HandVal and opp7HandVal >= opp4HandVal \
                        and opp7HandVal >= opp5HandVal and opp7HandVal >= opp6HandVal \
                        and opp7HandVal >= opp8HandVal and opp7HandVal >= opp9HandVal:
                        opponent[Hand.HandType(opp7HandVal)] += 1.0
                    elif opp8HandVal >= opp1HandVal and opp8HandVal >= opp2HandVal \
                        and opp8HandVal >= opp3HandVal and opp8HandVal >= opp4HandVal \
                        and opp8HandVal >= opp5HandVal and opp8HandVal >= opp6HandVal \
                        and opp8HandVal >= opp7HandVal and opp8HandVal >= opp9HandVal:
                        opponent[Hand.HandType(opp8HandVal)] += 1.0
                    elif opp9HandVal >= opp1HandVal and opp9HandVal >= opp2HandVal \
                        and opp9HandVal >= opp3HandVal and opp9HandVal >= opp4HandVal \
                        and opp9HandVal >= opp5HandVal and opp9HandVal >= opp6HandVal \
                        and opp9HandVal >= opp7HandVal and opp9HandVal >= opp8HandVal:
                        opponent[Hand.HandType(opp8HandVal)] += 1.0
                
                count += 1
        else:
            raise Exception("Only up 9 opponents")

        i = 0
        while i < len(player):
            player[i] /= count
            opponent[i] /= count
            i += 1
        
        return (player, opponent)
        

    # This method calculates the probablity of a player winning with specific hands and 
    # opponents winning with specific hands.
    # TODO: requires a PocketHand parser
    @staticmethod
    @dispatch(str, str, int, float)
    def HandWinOdds(ourCards: str, board: str, numberOfOpponents: int, duration: float):
        pass

    # Used to calculate the wining information about each players mask. This function enumerates all 
    # possible remaining hands and tallies win, tie and losses for each player. This function typically takes
    # well less than a second regardless of the number of players.
    # pocketList - Array of pocket mask string, one for each player
    # board - the board cards
    # dead - the dead cards
    # Returns a Tuple<wins, ties, losses, totalHands>
    #   wins - An array of win tallies, one for each player
    #   ties - An array of tie tallies, one for each player
    #   losses - An array of losses tallies, one for each player
    #   totalHands - The total number of hands enumerated
    @staticmethod
    @dispatch(object, str, str)
    def HandWinOdds(pocketList, board: str, dead: str):
        pocketMasks = [0] * len(pocketList)
        pocketHands = [0] * len(pocketList)
        wins = ties = losses = [0] * len(pocketList)        
        count = bestCount = 0
        boardMask = deadCardsMask = np.uint64(0)
        deadCards = Hand.ParseHand(dead)[0]

        totalHands = 0
        deadCardsMask |= deadCards

        # Read pocket cards
        i = 0
        while i < len(pocketList):
            handTuple = Hand.ParseHand(pocketList[i], "")
            pocketMasks[i] = handTuple[0]
            count = handTuple[1]
            if count != 2:
                raise Exception("There must be two pocket cards")
            deadCardsMask |= pocketMasks[i]
            wins[i] = ties[i] = losses[i] = 0
            i += 1
                
        boardMaskTuple = Hand.ParseHand("", board)
        boardMask = boardMaskTuple[0]
        count = boardMaskTuple[1]

        if __debug__:
            # The board must have zero or more cards but no more than a total of 5
            if not (count >= 0 and count <= 5):
                raise Exception("The board must have zero or more cards but no more than a total of 5")

            # Validate the input
            i = 0
            while i < len(pocketList):
                j = i + 1
                while j < len(pocketList):
                    if pocketMasks[i] & pocketMasks[j] != 0:
                        raise Exception("Duplicate pocket cards")                    
                    j += 1
                
                if pocketMasks[i] & boardMask != 0:
                    raise Exception("Duplicate between cards pocket and board")

                if pocketMasks[i] & deadCards != 0:
                    raise Exception("Duplicate between cards pocket and dead cards")

                i += 1
        
        # Iterate through all board possibilities that doesn't include any pocket cards.
        for boardHand in Hand.Hands(boardMask, deadCardsMask, 5):
            # Evaluate all hands and determine the best mask
            bestPocket = Hand.Evaluate(pocketMasks[0] | boardHand, 7)
            pocketHands[0] = bestPocket
            bestCount = 1
            i = 0
            while i < len(pocketList):
                pocketHands[i] = Hand.Evaluate(pocketMasks[i] | boardHand, 7)
                if pocketHands[i] > bestPocket:
                    bestPocket = pocketHands[i]
                    bestCount = 1
                elif pocketHands[i] == bestPocket:
                    bestCount += 1
                i += 1
            
            # Calculate wins/ties/losses for each pocket + board combindation
            i = 0
            while i < len(pocketList):
                if pocketHands[i] == bestPocket:
                    if bestCount > 1:
                        ties[i] += 1
                    else:
                        wins[i] += 1
                elif pocketHands[i] < bestPocket:
                    losses[i] += 1
                i += 1
            
            totalHands += 1

        return (wins, ties, losses, totalHands)
    
    # Returns the normalized, positive and negative potential of the current mask. This funciton
    # is described in Aaron Davidson's masters thesis on page 23.
    # pocket - Hold cards
    # board - Community cards
    # Returns a Tuple<ppot, npot>
    #   ppot - Positive Potential
    #   npot - Negative Potential
    @staticmethod
    @dispatch(np.uint64, np.uint64)
    def HandPotential(pocket: np.uint64, board: np.uint64):
        ahead = 2
        tied = 1
        behind = 0

        if __debug__:
            if Hand.BitCount(pocket) != 2:
                raise Exception("Pocket must contain exactly two cards.")
            if Hand.BitCount(board) != 3 and Hand.BitCount(board) != 4:
                raise Exception("Board must contain only 3 or 4 cards")
        
        hp = [[0] * 3] * 3
        hpTotal = [0] * 3
        ncards = Hand.BitCount(pocket | board)
        if ncards == 5:
            mult = 990.0
        else:
            mult = 45.0
        
        if __debug__:
            if ncards < 5 or ncards >7:
                raise Exception("Invalid number of cards")
        # rank our mask
        ourRank = Hand.Evaluate(pocket | board, ncards)

        # iterate through all possible opponent pocket cards
        for oppPocket in Hand.Hands(0, pocket | board, 2):
            oppRank = Hand.Evaluate(oppPocket | board, ncards)
            if ourRank > oppRank:
                index = ahead
            elif ourRank == oppRank:
                index = tied
            else:
                index = behind
            
            for boardMask in Hand.Hands(board, pocket | oppPocket, 5):
                ourBest = Hand.Evaluate(pocket | boardMask, 7)
                oppBest = Hand.Evaluate(oppPocket | boardMask, 7)
                if ourBest > oppBest:
                    hp[index][ahead] += 1
                elif ourBest == oppBest:
                    hp[index][tied] += 1
                else:
                    hp[index][behind] += 1
            
            hpTotal[index] += 1

        den1 = mult * (hpTotal[behind] + (hpTotal[tied] / 2.0))
        den2 = mult * (hpTotal[ahead] + (hpTotal[tied] / 2.0))
        if den1 > 0:
            ppot = (hp[behind][ahead] + (hp[behind][tied] / 2) + (hp[tied][ahead] / 2)) / den1
        else:
            ppot = 0
        
        if den2 > 0:
            npot = (hp[ahead][behind] + (hp[ahead][tied] / 2) + (hp[tied][behind] / 2)) / den2
        else:
            npot = 0
            
        return (ppot, npot)
    
    # This method is similar to the HandPotential algorithm described in Aaron Davidson's
    # masters thesis, however if differs in several significant ways. First, it makes the calculation
    # while accounting for one or more opponents. Second, it uses the Monte Carlo technique to get 
    # answers in a reasonable amount of time (a duration of 0.1 seems to give reasonable results). And
    # finally, the results are not normalized; the positive and negative potential is the actual odds of improvement
    # or worsening of a mask.
    # pocket - player's pocket card mask
    # board - The current board mask
    # numberOfOpponents - The number of opponents
    # duration - The length of time (in seconds) to spend on this calculation
    # Returns a Tuple<ppot, npot>
    #   ppot - The resultant positive potential
    #   npot - The resultant negative potential
    @staticmethod
    @dispatch(np.uint64, np.uint64, int, float)
    def HandPotential(pocket: np.uint64, board: np.uint64, numberOfOpponents: int, duration: float):
        ahead = 2
        tied = 1
        behind = 0

        if __debug__:
            if Hand.BitCount(pocket) != 2:
                raise Exception("Pocket must contain exactly two cards")
            if Hand.BitCount(board) != 3 and Hand.BitCount(board) != 4:
                raise Exception("Board must contain 3 or 4 cards")
        
        ppot = npot = 0.0
        hp = [[0] * 3] * 3
        count = 0
        ncards = Hand.BitCount(pocket | board)
        ourBest = 0
        ourRank = Hand.Evaluate(pocket | board)
        startTime = timer()

        if numberOfOpponents == 1:
            shared = np.uint64(0)
            while timer() - startTime < duration:
                opp1Pocket = Hand.RandomHand(shared, pocket | board, 2)
                opp1Rank = Hand.Evaluate(opp1Pocket | board, ncards)
                index: int

                if ourRank > opp1Rank:
                    index = ahead
                elif ourRank >= opp1Rank:
                    index = tied
                else:
                    index = behind
                
                boardMask = Hand.RandomHand(board, pocket | opp1Rank, 5)
                ourBest = Hand.Evaluate(pocket | boardMask, 7)
                opp1Best = Hand.Evaluate(opp1Pocket | boardMask, 7)
                if ourBest > opp1Best:
                    hp[index][ahead] += 1
                elif ourBest >= opp1Best:
                    hp[index][tied] += 1
                else:
                    hp[index][behind] += 1
                
                count += 1

        elif numberOfOpponents == 2:
            shared = np.uint64(0)
            while timer() - startTime < duration:
                opp1Pocket = Hand.RandomHand(shared, pocket | board, 2)
                opp2Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket, 2)
                opp1Rank = Hand.Evaluate(opp1Pocket | board)
                opp2Rank = Hand.Evaluate(opp2Pocket | board)
                index: int

                if ourRank > opp1Rank and ourRank > opp2Rank:
                    index = ahead
                elif ourRank >= opp1Rank and ourRank >= opp2Rank:
                    index = tied
                else:
                    index = behind
                
                boardMask = Hand.RandomHand(board, pocket | opp1Rank | opp2Pocket, 5)
                ourBest = Hand.Evaluate(pocket | boardMask, 7)
                opp1Best = Hand.Evaluate(opp1Pocket | boardMask, 7)
                opp2Best = Hand.Evaluate(opp2Pocket | boardMask, 7)
                if ourBest > opp1Best and ourBest > opp2Best:
                    hp[index][ahead] += 1
                elif ourBest >= opp1Best and ourBest >= opp2Best:
                    hp[index][tied] += 1
                else:
                    hp[index][behind] += 1
                
                count += 1
        elif numberOfOpponents == 3:
            shared = np.uint64(0)
            while timer() - startTime < duration:
                opp1Pocket = Hand.RandomHand(shared, pocket | board, 2)
                opp2Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket, 2)
                opp3Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket, 2)
                opp1Rank = Hand.Evaluate(opp1Pocket | board)
                opp2Rank = Hand.Evaluate(opp2Pocket | board)
                opp3Rank = Hand.Evaluate(opp3Pocket | board)

                index: int

                if ourRank > opp1Rank and ourRank > opp2Rank \
                    and ourRank > opp3Rank:
                    index = ahead
                elif ourRank >= opp1Rank and ourRank >= opp2Rank \
                    and ourRank >= opp3Rank:
                    index = tied
                else:
                    index = behind
                
                boardMask = Hand.RandomHand(board, pocket | opp1Rank | opp2Pocket | opp3Pocket, 5)
                ourBest = Hand.Evaluate(pocket | boardMask, 7)
                opp1Best = Hand.Evaluate(opp1Pocket | boardMask, 7)
                opp2Best = Hand.Evaluate(opp2Pocket | boardMask, 7)
                opp3Best = Hand.Evaluate(opp3Pocket | boardMask, 7)
                if ourBest > opp1Best and ourBest > opp2Best \
                    and ourBest > opp3Best:
                    hp[index][ahead] += 1
                elif ourBest >= opp1Best and ourBest >= opp2Best \
                    and ourBest >= opp3Best:
                    hp[index][tied] += 1
                else:
                    hp[index][behind] += 1
                
                count += 1
        elif numberOfOpponents == 4:
            shared = np.uint64(0)
            while timer() - startTime < duration:
                opp1Pocket = Hand.RandomHand(shared, pocket | board, 2)
                opp2Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket, 2)
                opp3Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket, 2)
                opp4Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket, 2)
                opp1Rank = Hand.Evaluate(opp1Pocket | board)
                opp2Rank = Hand.Evaluate(opp2Pocket | board)
                opp3Rank = Hand.Evaluate(opp3Pocket | board)
                opp4Rank = Hand.Evaluate(opp4Pocket | board)

                index: int

                if ourRank > opp1Rank and ourRank > opp2Rank \
                    and ourRank > opp3Rank and ourRank > opp2Rank:
                    index = ahead
                elif ourRank >= opp1Rank and ourRank >= opp2Rank \
                    and ourRank >= opp3Rank and ourRank >= opp4Rank:
                    index = tied
                else:
                    index = behind
                
                boardMask = Hand.RandomHand(board, pocket | opp1Rank | opp2Pocket | opp3Pocket | opp4Pocket, 5)
                ourBest = Hand.Evaluate(pocket | boardMask, 7)
                opp1Best = Hand.Evaluate(opp1Pocket | boardMask, 7)
                opp2Best = Hand.Evaluate(opp2Pocket | boardMask, 7)
                opp3Best = Hand.Evaluate(opp3Pocket | boardMask, 7)
                opp4Best = Hand.Evaluate(opp4Pocket | boardMask, 7)

                if ourBest > opp1Best and ourBest > opp2Best \
                    and ourBest > opp3Best and ourBest > opp4Best:
                    hp[index][ahead] += 1
                elif ourBest >= opp1Best and ourBest >= opp2Best \
                    and ourBest >= opp3Best and ourBest >= opp4Best:
                    hp[index][tied] += 1
                else:
                    hp[index][behind] += 1
                
                count += 1
        elif numberOfOpponents == 5:
            shared = np.uint64(0)
            while timer() - startTime < duration:
                opp1Pocket = Hand.RandomHand(shared, pocket | board, 2)
                opp2Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket, 2)
                opp3Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket, 2)
                opp4Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket, 2)
                opp5Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket, 2)
                opp1Rank = Hand.Evaluate(opp1Pocket | board)
                opp2Rank = Hand.Evaluate(opp2Pocket | board)
                opp3Rank = Hand.Evaluate(opp3Pocket | board)
                opp4Rank = Hand.Evaluate(opp4Pocket | board)
                opp5Rank = Hand.Evaluate(opp5Pocket | board)

                index: int

                if ourRank > opp1Rank and ourRank > opp2Rank \
                    and ourRank > opp3Rank and ourRank > opp2Rank \
                    and ourRank > opp5Rank:
                    index = ahead
                elif ourRank >= opp1Rank and ourRank >= opp2Rank \
                    and ourRank >= opp3Rank and ourRank >= opp4Rank \
                    and ourRank >= opp5Rank:
                    index = tied
                else:
                    index = behind
                
                boardMask = Hand.RandomHand(board, pocket | opp1Rank | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket, 5)
                ourBest = Hand.Evaluate(pocket | boardMask, 7)
                opp1Best = Hand.Evaluate(opp1Pocket | boardMask, 7)
                opp2Best = Hand.Evaluate(opp2Pocket | boardMask, 7)
                opp3Best = Hand.Evaluate(opp3Pocket | boardMask, 7)
                opp4Best = Hand.Evaluate(opp4Pocket | boardMask, 7)
                opp5Best = Hand.Evaluate(opp5Pocket | boardMask, 7)

                if ourBest > opp1Best and ourBest > opp2Best \
                    and ourBest > opp3Best and ourBest > opp4Best \
                    and ourBest > opp5Best:
                    hp[index][ahead] += 1
                elif ourBest >= opp1Best and ourBest >= opp2Best \
                    and ourBest >= opp3Best and ourBest >= opp4Best \
                    and ourBest >= opp5Best:
                    hp[index][tied] += 1
                else:
                    hp[index][behind] += 1
                
                count += 1
        elif numberOfOpponents == 6:
            shared = np.uint64(0)
            while timer() - startTime < duration:
                opp1Pocket = Hand.RandomHand(shared, pocket | board, 2)
                opp2Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket, 2)
                opp3Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket, 2)
                opp4Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket, 2)
                opp5Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket, 2)
                opp6Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket, 2)
                opp1Rank = np.uint64(Hand.Evaluate(opp1Pocket | board))
                opp2Rank = np.uint64(Hand.Evaluate(opp2Pocket | board))
                opp3Rank = np.uint64(Hand.Evaluate(opp3Pocket | board))
                opp4Rank = np.uint64(Hand.Evaluate(opp4Pocket | board))
                opp5Rank = np.uint64(Hand.Evaluate(opp5Pocket | board))
                opp6Rank = np.uint64(Hand.Evaluate(opp5Pocket | board))

                index: int

                if ourRank > opp1Rank and ourRank > opp2Rank \
                    and ourRank > opp3Rank and ourRank > opp2Rank \
                    and ourRank > opp5Rank and ourRank > opp6Rank:
                    index = ahead
                elif ourRank >= opp1Rank and ourRank >= opp2Rank \
                    and ourRank >= opp3Rank and ourRank >= opp4Rank \
                    and ourRank >= opp5Rank and ourRank >= opp6Rank:
                    index = tied
                else:
                    index = behind
                                
                dead = pocket | opp1Rank | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket | opp6Pocket
                boardMask = Hand.RandomHand(board, dead, 5)
                ourBest = Hand.Evaluate(pocket | boardMask, 7)
                opp1Best = Hand.Evaluate(opp1Pocket | boardMask, 7)
                opp2Best = Hand.Evaluate(opp2Pocket | boardMask, 7)
                opp3Best = Hand.Evaluate(opp3Pocket | boardMask, 7)
                opp4Best = Hand.Evaluate(opp4Pocket | boardMask, 7)
                opp5Best = Hand.Evaluate(opp5Pocket | boardMask, 7)
                opp6Best = Hand.Evaluate(opp6Pocket | boardMask, 7)

                if ourBest > opp1Best and ourBest > opp2Best \
                    and ourBest > opp3Best and ourBest > opp4Best \
                    and ourBest > opp5Best and ourBest > opp6Best:
                    hp[index][ahead] += 1
                elif ourBest >= opp1Best and ourBest >= opp2Best \
                    and ourBest >= opp3Best and ourBest >= opp4Best \
                    and ourBest >= opp5Best and ourBest >= opp6Best:
                    hp[index][tied] += 1
                else:
                    hp[index][behind] += 1
                
                count += 1
        elif numberOfOpponents == 7:
            shared = np.uint64(0)
            while timer() - startTime < duration:
                opp1Pocket = Hand.RandomHand(shared, pocket | board, 2)
                opp2Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket, 2)
                opp3Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket, 2)
                opp4Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket, 2)
                opp5Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket, 2)
                opp6Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket, 2)
                opp7Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket | opp6Pocket, 2)
                opp1Rank = Hand.Evaluate(opp1Pocket | board)
                opp2Rank = Hand.Evaluate(opp2Pocket | board)
                opp3Rank = Hand.Evaluate(opp3Pocket | board)
                opp4Rank = Hand.Evaluate(opp4Pocket | board)
                opp5Rank = Hand.Evaluate(opp5Pocket | board)
                opp6Rank = Hand.Evaluate(opp6Pocket | board)
                opp7Rank = Hand.Evaluate(opp7Pocket | board)

                index: int

                if ourRank > opp1Rank and ourRank > opp2Rank \
                    and ourRank > opp3Rank and ourRank > opp2Rank \
                    and ourRank > opp5Rank and ourRank > opp6Rank \
                    and ourRank > opp7Rank:
                    index = ahead
                elif ourRank >= opp1Rank and ourRank >= opp2Rank \
                    and ourRank >= opp3Rank and ourRank >= opp4Rank \
                    and ourRank >= opp5Rank and ourRank >= opp6Rank \
                    and ourRank >= opp7Rank:
                    index = tied
                else:
                    index = behind
                
                boardMask = Hand.RandomHand(board, pocket | opp1Rank | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket | opp6Pocket | opp7Pocket, 5)
                ourBest = Hand.Evaluate(pocket | boardMask, 7)
                opp1Best = Hand.Evaluate(opp1Pocket | boardMask, 7)
                opp2Best = Hand.Evaluate(opp2Pocket | boardMask, 7)
                opp3Best = Hand.Evaluate(opp3Pocket | boardMask, 7)
                opp4Best = Hand.Evaluate(opp4Pocket | boardMask, 7)
                opp5Best = Hand.Evaluate(opp5Pocket | boardMask, 7)
                opp6Best = Hand.Evaluate(opp6Pocket | boardMask, 7)
                opp7Best = Hand.Evaluate(opp7Pocket | boardMask, 7)

                if ourBest > opp1Best and ourBest > opp2Best \
                    and ourBest > opp3Best and ourBest > opp4Best \
                    and ourBest > opp5Best and ourBest > opp6Best \
                    and ourBest > opp7Best:
                    hp[index][ahead] += 1
                elif ourBest >= opp1Best and ourBest >= opp2Best \
                    and ourBest >= opp3Best and ourBest >= opp4Best \
                    and ourBest >= opp5Best and ourBest >= opp6Best \
                    and ourBest >= opp7Best:
                    hp[index][tied] += 1
                else:
                    hp[index][behind] += 1
                
                count += 1
        elif numberOfOpponents == 8:
            shared = np.uint64(0)
            while timer() - startTime < duration:
                opp1Pocket = Hand.RandomHand(shared, pocket | board, 2)
                opp2Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket, 2)
                opp3Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket, 2)
                opp4Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket, 2)
                opp5Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket, 2)
                opp6Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket, 2)
                opp7Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket | opp6Pocket, 2)
                opp8Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket | opp6Pocket | opp7Pocket, 2)
                opp1Rank = Hand.Evaluate(opp1Pocket | board)
                opp2Rank = Hand.Evaluate(opp2Pocket | board)
                opp3Rank = Hand.Evaluate(opp3Pocket | board)
                opp4Rank = Hand.Evaluate(opp4Pocket | board)
                opp5Rank = Hand.Evaluate(opp5Pocket | board)
                opp6Rank = Hand.Evaluate(opp6Pocket | board)
                opp7Rank = Hand.Evaluate(opp7Pocket | board)
                opp8Rank = Hand.Evaluate(opp8Pocket | board)

                index: int

                if ourRank > opp1Rank and ourRank > opp2Rank \
                    and ourRank > opp3Rank and ourRank > opp2Rank \
                    and ourRank > opp5Rank and ourRank > opp6Rank \
                    and ourRank > opp7Rank and ourRank > opp8Rank:
                    index = ahead
                elif ourRank >= opp1Rank and ourRank >= opp2Rank \
                    and ourRank >= opp3Rank and ourRank >= opp4Rank \
                    and ourRank >= opp5Rank and ourRank >= opp6Rank \
                    and ourRank >= opp7Rank and ourRank >= opp8Rank:
                    index = tied
                else:
                    index = behind
                
                boardMask = Hand.RandomHand(board, pocket | opp1Rank | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket | opp6Pocket | opp7Pocket | opp8Pocket, 5)
                ourBest = Hand.Evaluate(pocket | boardMask, 7)
                opp1Best = Hand.Evaluate(opp1Pocket | boardMask, 7)
                opp2Best = Hand.Evaluate(opp2Pocket | boardMask, 7)
                opp3Best = Hand.Evaluate(opp3Pocket | boardMask, 7)
                opp4Best = Hand.Evaluate(opp4Pocket | boardMask, 7)
                opp5Best = Hand.Evaluate(opp5Pocket | boardMask, 7)
                opp6Best = Hand.Evaluate(opp6Pocket | boardMask, 7)
                opp7Best = Hand.Evaluate(opp7Pocket | boardMask, 7)
                opp8Best = Hand.Evaluate(opp8Pocket | boardMask, 7)

                if ourBest > opp1Best and ourBest > opp2Best \
                    and ourBest > opp3Best and ourBest > opp4Best \
                    and ourBest > opp5Best and ourBest > opp6Best \
                    and ourBest > opp7Best and ourBest > opp8Best:
                    hp[index][ahead] += 1
                elif ourBest >= opp1Best and ourBest >= opp2Best \
                    and ourBest >= opp3Best and ourBest >= opp4Best \
                    and ourBest >= opp5Best and ourBest >= opp6Best \
                    and ourBest >= opp7Best and ourBest >= opp8Best:
                    hp[index][tied] += 1
                else:
                    hp[index][behind] += 1
                
                count += 1
        elif numberOfOpponents == 9:
            shared = np.uint64(0)
            while timer() - startTime < duration:
                opp1Pocket = Hand.RandomHand(shared, pocket | board, 2)
                opp2Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket, 2)
                opp3Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket, 2)
                opp4Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket, 2)
                opp5Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket, 2)
                opp6Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket, 2)
                opp7Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket | opp6Pocket, 2)
                opp8Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket | opp6Pocket | opp7Pocket, 2)
                opp9Pocket = Hand.RandomHand(shared, pocket | board | opp1Pocket | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket | opp6Pocket | opp7Pocket | opp8Pocket, 2)
                opp1Rank = Hand.Evaluate(opp1Pocket | board)
                opp2Rank = Hand.Evaluate(opp2Pocket | board)
                opp3Rank = Hand.Evaluate(opp3Pocket | board)
                opp4Rank = Hand.Evaluate(opp4Pocket | board)
                opp5Rank = Hand.Evaluate(opp5Pocket | board)
                opp6Rank = Hand.Evaluate(opp6Pocket | board)
                opp7Rank = Hand.Evaluate(opp7Pocket | board)
                opp8Rank = Hand.Evaluate(opp8Pocket | board)
                opp9Rank = Hand.Evaluate(opp9Pocket | board)

                index: int

                if ourRank > opp1Rank and ourRank > opp2Rank \
                    and ourRank > opp3Rank and ourRank > opp2Rank \
                    and ourRank > opp5Rank and ourRank > opp6Rank \
                    and ourRank > opp7Rank and ourRank > opp8Rank \
                    and ourRank > opp9Rank:
                    index = ahead
                elif ourRank >= opp1Rank and ourRank >= opp2Rank \
                    and ourRank >= opp3Rank and ourRank >= opp4Rank \
                    and ourRank >= opp5Rank and ourRank >= opp6Rank \
                    and ourRank >= opp7Rank and ourRank >= opp8Rank \
                    and ourRank >= opp9Rank:
                    index = tied
                else:
                    index = behind
                
                boardMask = Hand.RandomHand(board, pocket | opp1Rank | opp2Pocket | opp3Pocket | opp4Pocket | opp5Pocket | opp6Pocket | opp7Pocket | opp8Pocket | opp9Pocket, 5)
                ourBest = Hand.Evaluate(pocket | boardMask, 7)
                opp1Best = Hand.Evaluate(opp1Pocket | boardMask, 7)
                opp2Best = Hand.Evaluate(opp2Pocket | boardMask, 7)
                opp3Best = Hand.Evaluate(opp3Pocket | boardMask, 7)
                opp4Best = Hand.Evaluate(opp4Pocket | boardMask, 7)
                opp5Best = Hand.Evaluate(opp5Pocket | boardMask, 7)
                opp6Best = Hand.Evaluate(opp6Pocket | boardMask, 7)
                opp7Best = Hand.Evaluate(opp7Pocket | boardMask, 7)
                opp8Best = Hand.Evaluate(opp8Pocket | boardMask, 7)
                opp9Best = Hand.Evaluate(opp9Pocket | boardMask, 7)

                if ourBest > opp1Best and ourBest > opp2Best \
                    and ourBest > opp3Best and ourBest > opp4Best \
                    and ourBest > opp5Best and ourBest > opp6Best \
                    and ourBest > opp7Best and ourBest > opp8Best \
                    and ourBest > opp9Best:
                    hp[index][ahead] += 1
                elif ourBest >= opp1Best and ourBest >= opp2Best \
                    and ourBest >= opp3Best and ourBest >= opp4Best \
                    and ourBest >= opp5Best and ourBest >= opp6Best \
                    and ourBest >= opp7Best and ourBest >= opp8Best \
                    and ourBest >= opp9Best:
                    hp[index][tied] += 1
                else:
                    hp[index][behind] += 1
                
                count += 1
        
        if count != 0:
            ppot = (hp[behind][ahead] + (hp[behind][tied] / 2.0) + (hp[tied][ahead] / 2.0)) / count
            npot = (hp[ahead][behind] + (hp[ahead][tied] / 2.0) + (hp[tied][behind] / 2.0)) / count
        
        return (ppot, npot)

    # returns a Tuple<playerOddsList, opponentOddsList>
    @staticmethod
    def HandPlayerMultiOpponentOdds(ourCards: int, board: int, numberOfOpponents: int, duration: float):
        pass
    
    # This method returns the approximate odd for the players mask winning against multiple opponents.
    # This uses a default time duration of 0.25S (or 250mS) for the time allotment for Monte Carlo analysis.
    # pocket - The pocket mask of the player
    # board - The current board cards
    # dead - Dead cards
    # numberOfOpponents - The number of oppoents 1-9 are legal values
    # The approximate odds of winning the passed mask against the number of opponents specified.
    @staticmethod
    @dispatch(str, str, np.uint64, int)
    def WinOdds(pocket: str, board: str, dead: np.uint64, numberOfOpponents: int):
        if __debug__:
            if not Hand.ValidateHand(pocket) or Hand.BitCount(Hand.ParseHand(pocket)[0]) != 2:
                raise Exception("pocket must contain exactly two cards")
            if (board != "" and not Hand.ValidateHand(board)) or Hand.BitCount(Hand.ParseHand(board)[0]) > 5:
                raise Exception("Board must have 0-5 cards")

            return HandAnalysis.WinOdds(Hand.ParseHand(pocket)[0], Hand.ParseHand(board)[0], dead, numberOfOpponents)

    # This method returns the approximate odd for the players mask winning against multiple opponents.
    # This uses a default time duration of 0.25S (or 250mS) for the time allotment for Monte Carlo analysis.
    # pocket - The pocket mask of the player
    # board - The current board cards
    # numberOfOpponents - The number of oppoents 1-9 are legal values
    # return The approximate odds of winning the passed mask against the number of opponents specified.
    @staticmethod
    @dispatch(str, str, int)
    def WinOdds(pocket: str, board: str, numberOfOpponents: int):
        if __debug__:
            if not Hand.ValidateHand(pocket) or Hand.BitCount(Hand.ParseHand(pocket)[0]) != 2:
                raise Exception("pocket must contain exactly two cards")
            if (board != "" and not Hand.ValidateHand(board)) or Hand.BitCount(Hand.ParseHand(board)[0]) > 5:
                raise Exception("Board must have 0-5 cards")
            if numberOfOpponents < 0 or numberOfOpponents > 9:
                raise Exception("numberOfOpponents must be 1-9")
        
        return HandAnalysis.WinOdds(Hand.ParseHand(pocket)[0], Hand.ParseHand(board)[0], 0, numberOfOpponents)

    # This method returns the exact odds of the specified mask mask
    # winning against an average player. It's reasonably fast because it
    # uses a lookup table when possible.
    # pocket - The pocket mask
    # board - The board mask
    # dead - Dead cards
    # returns the win odds
    @staticmethod
    @dispatch(np.uint64, np.uint64, np.uint64)
    def WinOdds(pocket: np.uint64, board: np.uint64, dead: np.uint64):
        # For one player we can lookup the value if the board is empty
        # and if it's not empty it's probably just faster to calculate the
        # results exhaustively.
        if board == 0 and dead == 0:
            # Use precalculated values
            retval = 0.0
            index = Hand.PocketHand169Type(pocket)
            for value in HandAnalysis.__PreCalcPlayerOdds()[index]:
                retval += value
            return retval
        else:
            # calculate the results exhaustively
            win = lose = tie = 0
            for mask in Hand.Hands(board, pocket | dead, 5):
                for opp1 in Hand.Hands(0, pocket | board | dead, 2):
                    playerHandVal = Hand.Evaluate(mask | pocket)
                    oppHandVal = Hand.Evaluate(mask | opp1)

                    if playerHandVal == oppHandVal:
                        win += 1
                    elif playerHandVal == oppHandVal:
                        tie += 1
                    else:
                        lose += 1
            
            return (win + tie / 2.0) / (win + tie + lose)
    
    # This method returns the approximate odd for the players mask winning against multiple opponents.
    # This uses a default time duration of 0.1S (or 100mS) for the time allotment for Monte Carlo analysis.
    # pocket - The pocket mask of the player
    # board - The current board cards
    # dead - Dead cards
    # numberOfOpponents - The number of oppoents 1-9 are legal values
    # returns The approximate odds of winning the passed mask against the number of opponents specified.
    @staticmethod
    @dispatch(np.uint64, np.uint64, np.uint64, int)
    def WinOdds(pocket: np.uint64, board: np.uint64, dead: np.uint64, numberOfOpponents: int):
        return HandAnalysis.WinOdds(pocket, board, dead, numberOfOpponents, HandAnalysis.__defaultTimeDuration)
    
    # This method returns the approximate odd for the players mask winning against multiple opponents.
    # pocket - the pocket mask of the player
    # board - The current board cards
    # dead - Dead cards
    # numberOfOpponents - The approximate odds of winning the passed mask against the number of opponents specified.
    # duration - The period of time (in seconds) to run trials. On my 2.8Ghz laptop 0.1 seconds seems adequate.
    # returns The approximate odds of winning the passed mask against the number of opponents specified.
    @staticmethod
    @dispatch(np.uint64, np.uint64, np.uint64, int, float)
    def WinOdds(pocket: np.uint64, board: np.uint64, dead: np.uint64, numberOfOpponents: int, duration: float):
        if __debug__:
            if Hand.BitCount(pocket) != 2:
                raise Exception("Pocket must contain exactly two cards")
            if numberOfOpponents < 1 or numberOfOpponents > 9:
                raise Exception("numberOfOpponents must be 1-9")
            if Hand.BitCount(board) > 5:
                raise Exception("Board must contain 0-5 cards")
            if duration <= 0.0:
                raise Exception("Duration must not be 0.0 or negative")
        
        # keep track of the stats
        win = count = 0.0
        
        # loop through random boards
        for boardMask in Hand.RandomHand(board, dead | pocket, 5, duration):
            deadMask = dead | board | pocket
            playerHandVal = Hand.Evaluate(pocket | boardMask)

            # comparison results
            greaterThan = True
            greaterThanEqual = True

            # Get random component hand values
            i = 0
            while i < numberOfOpponents:
                oppMask = Hand.RandomHand(deadMask, 2)
                oppHandVal = Hand.Evaluate(oppMask | boardMask)
                deadMask |= oppMask
                if playerHandVal < oppHandVal:
                    greaterThan = greaterThanEqual = False
                    break
                elif playerHandVal <= oppHandVal:
                    greaterThan = False                
                i += 1
            
            if greaterThan:
                win += 1.0
            elif greaterThanEqual:
                win += 0.5
            
            count += 1.0
        
        if count == 0.0:
            return 0.0
        else:
            return win / count

    # This method returns the approximate odd for the players mask winning against multiple opponents.
    # pocketQuery - The pocket mask of the player
    # board - The current board cards
    # deadCards - dead cards
    # numberOfOpponents - The approximate odds of winning the passed mask against the number of opponents specified.
    # duration - The period of time (in seconds) to run trials. On my 2.8Ghz laptop 0.1 seconds seems adequate.
    # returns The approximate odds of winning the passed mask against the number of opponents specified.
    # TODO: requires pocket query parser
    @staticmethod
    @dispatch(str, str, str, int, float)
    def WinOdds(pocketQuery: str, board: str, deadCards: str, numberOfOpponents: int, duration: float):
        pass

    __defaultTimeDuration = 0.25;

    # This table is used by HandPlayerOpponentOdds and contains the odds of each type of 
    # mask occuring against a random player when the board is currently empty. This calculation
    # normally takes about 5 minutes, so the values are precalculated to save time.
    @staticmethod
    def __PreCalcPlayerOdds():
        return [
            [0, 0.286740271754148, 0.337632177082422, 0.107630068931113, 0.00871248305898762, 0.0186005527151292, 0.0842236711352609, 0.00840620900618257, 9.16993377677929E-05],
            [0, 0.27207410337779, 0.324989138873109, 0.10751232138638, 0.00934600684105111, 0.0180595349176028, 0.0835212896584642, 0.0083608155789998, 9.35872344620858E-05],
            [0, 0.258379200641656, 0.313030451773679, 0.106138870820383, 0.0129346953649848, 0.0174970341905719, 0.0828132101661902, 0.00832256374082725, 0.000135613912540039],
            [0, 0.244957911345515, 0.300932738245412, 0.104766138227219, 0.0165233838889184, 0.0169436487627316, 0.0821021100392053, 0.00829115791187947, 0.000177640590617992],
            [0, 0.231824795177511, 0.28851389778012, 0.10339412360689, 0.0201120724128521, 0.0163993424017212, 0.0813879892775096, 0.0082659115842676, 0.000219667268695946],
            [0, 0.217844636971768, 0.275105943899719, 0.103675534632321, 0.0189032492990468, 0.0159062342734868, 0.0806736110753555, 0.00824653871303799, 0.000216770586798339],
            [0, 0.204018493950435, 0.261328674519173, 0.103557069114754, 0.0189032492990468, 0.0154180280022754, 0.0799561264250045, 0.00823194279253484, 0.000216770586798339],
            [0, 0.190192350929103, 0.247219242587288, 0.103438603597187, 0.0189032492990468, 0.0149329429582502, 0.0792356211399425, 0.00822144684970111, 0.000216770586798339],
            [0, 0.176338424361419, 0.232896092168261, 0.10332013807962, 0.0189032492990468, 0.0144463480736112, 0.0785120952201697, 0.00821436437664798, 0.000216770586798339],
            [0, 0.162635821295131, 0.218553432053168, 0.102802513991889, 0.0190919245504947, 0.0139528294708683, 0.0777854628522, 0.00820999933065481, 0.000217221584341976],
            [0, 0.148162103963611, 0.203711469029627, 0.10394046946842, 0.015503236026561, 0.0134690902683502, 0.0770585730437719, 0.00820807520159972, 0.000175194906264022],
            [0, 0.133400213503953, 0.188900201490065, 0.105077706972117, 0.0119145475026273, 0.0129687585515523, 0.076328662600633, 0.00820750501865871, 0.000133168228186069],
            [0, 0.118330046676816, 0.174113077574819, 0.10621422650298, 0.00834041866683601, 0.0124479441091044, 0.0755957315227832, 0.00820760227394296, 9.11434570744733E-05],
            [0.0571760455086079, 0.280205634856752, 0.184453924450951, 0.0365310084171588, 0.0266728173482832, 0.0627649090920533, 0.0208664745016668, 0.00123686052505268, 0.000538648391826666],
            [0.0623297388924454, 0.295079403218692, 0.189393299129985, 0.037229782390348, 0.0286287805846416, 0.018343179000639, 0.0208670251382026, 0.00123686624595175, 9.26432861149393E-05],
            [0.0563138631114711, 0.273071728060495, 0.181336609406188, 0.0361693789449175, 0.0298615120507879, 0.0627519903484619, 0.020787031236681, 0.00123684908325453, 0.000559661730865643],
            [0.0613800553439776, 0.287610629316061, 0.186203309597323, 0.0368551455005796, 0.0320692320322293, 0.0180619286371236, 0.0207875818732169, 0.0012368548041536, 0.000113656625153916],
            [0.0555485498378983, 0.265836711524236, 0.178378615679726, 0.0358473867219077, 0.0330502067532925, 0.0627403220980596, 0.020707484995512, 0.00123683764145638, 0.000580675069904619],
            [0.0605358651744274, 0.280022782050336, 0.183176929196818, 0.036522534335406, 0.035509683479817, 0.0177852359232034, 0.0207080356320478, 0.00123684336235545, 0.000134669964192893],
            [0.0548500495143815, 0.258622320259363, 0.175555095976663, 0.0355624373203995, 0.0362389014557972, 0.0627287129636145, 0.0206278357781596, 0.00123682619965823, 0.000601688408943596],
            [0.0597644305388458, 0.272450396944582, 0.180288551184217, 0.0362290483989969, 0.0389501349274047, 0.0175130827426982, 0.0206283864146954, 0.00123683192055731, 0.000155683303231869],
            [0.0574857463799581, 0.254825609833539, 0.174627747533291, 0.0354514275645503, 0.0203041237098657, 0.0631969142042487, 0.0205495381232133, 0.0012368233392087, 0.000134208478334288],
            [0.0626260385577156, 0.268517188727312, 0.17933947071386, 0.0361150332641677, 0.0219231388628111, 0.017266608771168, 0.0205495266814151, 0.0012368233392087, 0.000154234962283066],
            [0.055426437247172, 0.248354728065644, 0.172370931511113, 0.0353384398078464, 0.0229088361860597, 0.0631777978199942, 0.0204698803245123, 0.00123682047875916, 0.000154234962283066],
            [0.0603773891189644, 0.261706200939715, 0.177031322017776, 0.0359976308803453, 0.0247300665283353, 0.0170225056355623, 0.0204698803245123, 0.00123682047875916, 0.000154234962283066],
            [0.0540477577794216, 0.242280815193793, 0.170399055593981, 0.0352441164843702, 0.0229088361860597, 0.0631777978199942, 0.0203901538750224, 0.00123681761830962, 0.000154234962283066],
            [0.0588679728051342, 0.255339080548543, 0.175013417892036, 0.0359002468758647, 0.0247300665283353, 0.0167799631135497, 0.0203901538750224, 0.00123681761830962, 0.000154234962283066],
            [0.053377082478774, 0.236664279621528, 0.168698908795711, 0.035164367151284, 0.0202753890640437, 0.0631969142042487, 0.0203103587747436, 0.00123681475786009, 0.000134165571591236],
            [0.0581277599762468, 0.249478345538871, 0.173272169771113, 0.0358185276465308, 0.0218896573009828, 0.0165366656712302, 0.0203103473329455, 0.00123681475786009, 0.000154234962283066],
            [0.0495020672468802, 0.229125260229397, 0.165634580718167, 0.0350797550539853, 0.0350912190206164, 0.0627287129636145, 0.0202292035307101, 0.00123681189741055, 0.000601645502200544],
            [0.0539093120218401, 0.241543500000286, 0.17013673854595, 0.0357301101978649, 0.0377348243140499, 0.0162898262772718, 0.0202297541672459, 0.00123681761830962, 0.000154460461054884],
            [0.0484983712600337, 0.22563169023391, 0.164477461659965, 0.0351392438230023, 0.0318824225089918, 0.0627403220980596, 0.0201493998490827, 0.00123681761830962, 0.000580630732936799],
            [0.0528171351796963, 0.2378983233189, 0.168950961120579, 0.0357896456875577, 0.0342725333342487, 0.0160479566760127, 0.0201499504856185, 0.0012368233392087, 0.000133447122015908],
            [0.0480691608070358, 0.222398602784819, 0.163345378686333, 0.0352099455542035, 0.0285622543946516, 0.0627519903484619, 0.020069493191272, 0.0012368233392087, 0.00055955684771596],
            [0.0523535278210182, 0.23453412144439, 0.167790650277435, 0.0358607145097828, 0.0306899118237826, 0.0157977908176137, 0.0200700438278078, 0.00123682906010777, 0.000112433782976931],
            [0.0476945134289524, 0.219158324165593, 0.162231942983231, 0.035283424781905, 0.0248923190922993, 0.0627649090920533, 0.0199894835572779, 0.00123682906010777, 0.000537232469305946],
            [0.0519490960121329, 0.231165252746461, 0.166649352842362, 0.0359346380606457, 0.0267315731271064, 0.0155373835963898, 0.0199900341938138, 0.00123683478100684, 9.14213974211331E-05],
            [0.0463257883255901, 0.252002054374857, 0.173669051423445, 0.0347785797524796, 0.0424756597197789, 0.0618434967965826, 0.0207056271335378, 0.00119692864951884, 0.0010068467720113],
            [0.0505172550897409, 0.265106691907273, 0.178202746899225, 0.0354012233379882, 0.0455204745256946, 0.0177913396457734, 0.0207067284066095, 0.00119694009131699, 0.000114600573501062],
            [0.0454199554685216, 0.244720638486662, 0.170730035349435, 0.0344562228221538, 0.0456643544222836, 0.06183133654886, 0.0206260808923687, 0.0011969172077207, 0.00102786011105028],
            [0.049520231101439, 0.257467379433482, 0.175195653079722, 0.0350682903722417, 0.0489609259732823, 0.0175146469318532, 0.0206271821654404, 0.00119692864951884, 0.000135613912540039],
            [0.044662873138491, 0.237657768094203, 0.167925486862813, 0.0341737262561235, 0.0488530491247883, 0.0618204673173617, 0.0205464316750163, 0.00119690576592255, 0.00104887345008926],
            [0.0486851085569204, 0.250054959247175, 0.172326807646783, 0.034777327352324, 0.05240137742087, 0.017242493751348, 0.020547532948088, 0.0011969172077207, 0.000156627251579016],
            [0.0473196229126585, 0.234490950109755, 0.167045325110113, 0.0340896833882826, 0.0324032789046995, 0.0622894642397087, 0.0204681340200701, 0.00119690290547301, 0.000581393519479947],
            [0.0515702151687351, 0.246780948776786, 0.171425909303536, 0.034690563720232, 0.0348348290623961, 0.0169960197798179, 0.0204686732148077, 0.00119690862637209, 0.000155178910630212],
            [0.0482008058458435, 0.229799316581397, 0.165812924025888, 0.0339996392973134, 0.0208593712903545, 0.0627296907606145, 0.020389699063546, 0.00119690004502348, 0.000135152426681434],
            [0.0525199916818127, 0.241900469800232, 0.170165775207569, 0.0345985444888577, 0.0225231810830463, 0.0167519967367992, 0.0203896876217479, 0.00119690004502348, 0.000155178910630212],
            [0.0461820936431086, 0.223813894576416, 0.163618899876829, 0.0339249100531643, 0.0234640837665484, 0.0627114787551552, 0.0203099382886617, 0.00119689718457394, 0.000155178910630212],
            [0.0503143848574667, 0.235614019806897, 0.167922660261929, 0.0345208594468539, 0.0253301087485705, 0.0165094542147866, 0.0203099382886617, 0.00119689718457394, 0.000155178910630212],
            [0.0448215994832884, 0.218273938959151, 0.161690117347082, 0.0338647547994053, 0.0234640837665484, 0.0627106787827681, 0.0202301088629885, 0.0011968943241244, 0.000155178910630212],
            [0.0488249344814034, 0.229820854336184, 0.165949713821559, 0.0344588391799968, 0.0253301087485705, 0.0162661567724671, 0.0202301088629885, 0.0011968943241244, 0.000155178910630212],
            [0.0437027561003377, 0.212843816022751, 0.159720843723916, 0.0338148099202678, 0.0236374842174697, 0.0627069940470231, 0.0201501764611319, 0.00119689146367487, 0.000155404409402031],
            [0.0476003617324484, 0.224155905655509, 0.163935191462283, 0.0344076156799165, 0.0255187840000183, 0.0160193974710956, 0.0201501764611319, 0.00119689146367487, 0.000155404409402031],
            [0.0426523489725551, 0.209250891173053, 0.158500574521289, 0.0338742986892848, 0.020448789514965, 0.0627178017788564, 0.0200703727795045, 0.00119689718457394, 0.000134391070363054],
            [0.0464572688885495, 0.220406914679083, 0.162685864859778, 0.0344671511696092, 0.0220783325524306, 0.0157775278698366, 0.0200703727795045, 0.00119689718457394, 0.000134391070363054],
            [0.0421295231573413, 0.205887041133836, 0.157298748782164, 0.0339450004204861, 0.0172600948124603, 0.0627286095106896, 0.0199904661216938, 0.00119690290547301, 0.000113377731324077],
            [0.045891786619618, 0.216905482738045, 0.161455417224216, 0.0345382199918344, 0.0186378811048429, 0.0155273620114376, 0.0199904661216938, 0.00119690290547301, 0.000113377731324077],
            [0.0415875537836024, 0.202387923296474, 0.156102155520353, 0.0340157021516874, 0.0140848013160356, 0.0627394167657812, 0.0199104564876998, 0.00119690862637209, 9.23653457682796E-05],
            [0.0453054016156963, 0.213263612736323, 0.160230259990072, 0.0346092888140595, 0.0152119893453976, 0.0152669547902137, 0.0199104564876998, 0.00119690862637209, 9.23653457682796E-05],
            [0.0367350371314954, 0.224383730449543, 0.163381827249443, 0.0330285805629403, 0.0609119492132906, 0.0609478056633468, 0.0205443421166297, 0.00116366448185531, 0.00149511454288777],
            [0.040070950590311, 0.23579145206144, 0.167553169559249, 0.0335791274713569, 0.0652525776941001, 0.0172333164757507, 0.0205459940262372, 0.00116368164455253, 0.000156627251579016],
            [0.0358573439467453, 0.217302590365892, 0.160588721991193, 0.0327453746054248, 0.0641006439157952, 0.0609364444345282, 0.0204646928992773, 0.00116365304005716, 0.00151612788192675],
            [0.0391047908525112, 0.228357655735745, 0.164696050539185, 0.0332874808039999, 0.0686930291416878, 0.0169611632952455, 0.0204663448088848, 0.00116367020275438, 0.000177640590617992],
            [0.0384869051480655, 0.214279256820885, 0.159683215225372, 0.0326573104222767, 0.0475316744728335, 0.0614061617134169, 0.020386395244331, 0.00116365017960763, 0.00104864795131744],
            [0.0419606922745551, 0.225235224776985, 0.16376882104284, 0.0331964183929956, 0.0510011644890064, 0.0167146893237154, 0.0203874850756045, 0.00116366162140577, 0.000176192249669189],
            [0.0394664803941928, 0.210109579531081, 0.158495276253635, 0.0325928387501666, 0.0355919736072042, 0.0618471667533383, 0.020307960287807, 0.00116364731915809, 0.000602406858518924],
            [0.0430184722110188, 0.220900556757898, 0.162554356884177, 0.0331302433231864, 0.0382752805099838, 0.0164706662806967, 0.0203084994825447, 0.00116365304005716, 0.000176192249669189],
            [0.0398099131167058, 0.205514361745034, 0.15728853769243, 0.0325306697399336, 0.0240480659928592, 0.0622818511532665, 0.0202294223550996, 0.00116364445870855, 0.000156165765720411],
            [0.0433818637201748, 0.21612625766815, 0.161320363721414, 0.0330670903183127, 0.025963632530634, 0.0162282038512711, 0.0202294109133015, 0.00116364445870855, 0.000176192249669189],
            [0.0379638791013841, 0.200131440516666, 0.15513436318098, 0.0324901085655017, 0.0266527784690531, 0.0622637020776971, 0.020149558604032, 0.00116364159825902, 0.000176192249669189],
            [0.0413644673242268, 0.21048746493804, 0.159118962711371, 0.0330247690139325, 0.0287705601961582, 0.0159849064089516, 0.020149558604032, 0.00116364159825902, 0.000176192249669189],
            [0.0369036177249472, 0.194724169711615, 0.153130219247736, 0.0324401636863643, 0.0268261789199743, 0.0622600769346507, 0.0200696262021754, 0.00116363873780948, 0.000176417748441007],
            [0.0402035824842089, 0.20484706463529, 0.157069570042016, 0.0329735455138521, 0.028959235447606, 0.0157381471075802, 0.0200696262021754, 0.00116363873780948, 0.000176417748441007],
            [0.0358467030744684, 0.191120801360659, 0.151869403172925, 0.0324996524553813, 0.0236374842174697, 0.0622701047172436, 0.019989822520548, 0.00116364445870855, 0.000155404409402031],
            [0.0390532527029818, 0.201086877859377, 0.155779696567327, 0.0330330810035449, 0.0255187840000183, 0.0154962775063211, 0.019989822520548, 0.00116364445870855, 0.000155404409402031],
            [0.0353173697365583, 0.187746507820183, 0.150621353999509, 0.0325703541865825, 0.020448789514965, 0.0622801324998365, 0.0199099158627373, 0.00116365017960763, 0.000134391070363054],
            [0.0384805334967222, 0.197574250118852, 0.154503025497475, 0.03310414982577, 0.0220783325524306, 0.0152461116479221, 0.0199099158627373, 0.00116365017960763, 0.000134391070363054],
            [0.0347688928401232, 0.184236946481561, 0.149372860741303, 0.0326410559177838, 0.0172734960185403, 0.0622901598056878, 0.0198299062287433, 0.0011636559005067, 0.000113378684807256],
            [0.0378869115554724, 0.193921184317643, 0.153225968266936, 0.0331752186479952, 0.0186524407929853, 0.0149857044266982, 0.0198299062287433, 0.0011636559005067, 0.000113378684807256],
            [0.0280928896661684, 0.198748847953949, 0.154065147167268, 0.0314300314496892, 0.0793482387068022, 0.0600907162966103, 0.0203828511473549, 0.00113646637417617, 0.00198338231376424],
            [0.030656295820826, 0.208590982604462, 0.157924536001713, 0.0319159481694172, 0.0849846808625056, 0.0166843904887383, 0.0203850536934983, 0.00113648925777246, 0.000198653929656969],
            [0.0306068171949631, 0.195292900736108, 0.153118814635433, 0.031325592146426, 0.0627637198601583, 0.0605599415781787, 0.0203045534924087, 0.00113646351372663, 0.00151590238315493],
            [0.0333866092059564, 0.205008572767262, 0.156954791643902, 0.0318077983863632, 0.0672764000899325, 0.0164379165172082, 0.020306193960218, 0.00113648067642385, 0.000197205588708166],
            [0.0315532684354542, 0.191281454933332, 0.151908748656304, 0.0312587126909183, 0.0507203691753381, 0.0610016474282366, 0.0202261185358846, 0.00113646065327709, 0.00106966129035641],
            [0.0344087979990583, 0.2008398680303, 0.155717555446477, 0.0317390131563516, 0.0544416159365941, 0.0161938934741895, 0.0202272083671581, 0.00113647209507524, 0.000197205588708166],
            [0.0319924117994688, 0.187160167868342, 0.150747898856793, 0.0312221160995444, 0.0387806683097089, 0.0614370903240336, 0.0201475806031773, 0.00113645779282756, 0.000623420197557901],
            [0.0348774254466735, 0.196560338036484, 0.154530916310684, 0.031701704313043, 0.0417157319575715, 0.0159514310447639, 0.020148119797915, 0.00113646351372663, 0.000197205588708166],
            [0.0320433206501001, 0.182796865319166, 0.149548553127415, 0.031185114754561, 0.0272367606953638, 0.0618658831513992, 0.0200689396942866, 0.00113645493237802, 0.000177179104759388],
            [0.0349224632246305, 0.192036259630418, 0.153304609890939, 0.0316645113179407, 0.0294040839782217, 0.0157082136950315, 0.0200689282524884, 0.00113645493237802, 0.000197205588708166],
            [0.0306152555210967, 0.177597580660386, 0.147317395337582, 0.0311547639547507, 0.030014873622479, 0.0618457699004812, 0.0199889729670356, 0.00113645207192848, 0.000197431087479984],
            [0.0333618591663391, 0.186604898119369, 0.151025140777024, 0.0316329867803371, 0.0323996868951937, 0.01546145439366, 0.0199889729670356, 0.00113645207192848, 0.000197431087479984],
            [0.0295719351570415, 0.173994186565384, 0.146020898015248, 0.0312142527237677, 0.0268261789199743, 0.0618550377569804, 0.0199091692854082, 0.00113645779282756, 0.000176417748441007],
            [0.0322261319799974, 0.182844739947951, 0.149699586054813, 0.0316925222700299, 0.028959235447606, 0.015219584792401, 0.0199091692854082, 0.00113645779282756, 0.000176417748441007],
            [0.0290561961055552, 0.170619867280862, 0.144732301969648, 0.031284954454969, 0.0236374842174697, 0.0618643056134797, 0.0198292626275975, 0.00113646351372663, 0.000155404409402031],
            [0.0316680153686233, 0.179332140811921, 0.148382368112776, 0.031763591092255, 0.0255187840000183, 0.014969418934002, 0.0198292626275975, 0.00113646351372663, 0.000155404409402031],
            [0.0285213134955437, 0.167110280198195, 0.143438396214596, 0.0313556561861703, 0.020462190721045, 0.0618735729932373, 0.0197492529936035, 0.0011364692346257, 0.000134392023846233],
            [0.0310889960222589, 0.175679103615208, 0.147059898385391, 0.0318346599144802, 0.022092892240573, 0.0147090117127781, 0.0197492529936035, 0.0011364692346257, 0.000134392023846233],
            [0.0237410017408696, 0.178033017596913, 0.147263559531962, 0.030154308142117, 0.0780113146511653, 0.0597515866436839, 0.020222608764303, 0.0011147326785955, 0.00198315681499242],
            [0.0259152294337969, 0.186632688816844, 0.150890405975975, 0.0305868903500065, 0.0835680518107504, 0.0161656832441159, 0.0202247998686482, 0.0011147555621918, 0.000218218927747142],
            [0.0245718193088353, 0.17374053691782, 0.146016035966148, 0.0300742806303134, 0.065952414562663, 0.0601928004964215, 0.0201441738077789, 0.00111472981814597, 0.0015369157221939],
            [0.0268118301899853, 0.18216485543002, 0.149614364205021, 0.030504394985365, 0.0707168515375202, 0.0159216602010972, 0.0201458142755883, 0.00111474698084319, 0.000218218927747142],
            [0.0249818575988128, 0.169728582670138, 0.144834249821365, 0.0300366592828929, 0.0539090638778428, 0.0606289246559499, 0.0200656358750716, 0.00111472695769643, 0.00109067462939539],
            [0.0272493788533831, 0.177998729388316, 0.148406375388997, 0.0304659233693197, 0.0578820673841818, 0.0156791977716717, 0.0200667257063451, 0.00111473839949458, 0.000218218927747142],
            [0.0251160341354606, 0.165808167813421, 0.14368333293287, 0.0300252303567686, 0.0419693630122135, 0.0610584759791843, 0.0199869949661809, 0.00111472409724689, 0.000644433536596877],
            [0.0273860296788802, 0.173936593559297, 0.147230188335811, 0.0304545745357824, 0.0451561834051592, 0.0154359804219392, 0.0199875341609186, 0.00111472981814597, 0.000218218927747142],
            [0.0251982005484054, 0.161294301212201, 0.142379219663645, 0.0299908220092904, 0.0305988558487898, 0.0614798001728093, 0.0199082510811069, 0.00111472123679736, 0.000198417942570183],
            [0.0274667801693043, 0.169261923926917, 0.14589665224428, 0.0304202219670701, 0.0330332106772572, 0.0151893012131548, 0.0199082396393088, 0.00111472123679736, 0.000218444426518961],
            [0.0238347458233146, 0.157916549388236, 0.140855708484723, 0.0300699048576345, 0.030014873622479, 0.0614725827818863, 0.0198284130740851, 0.00111472695769643, 0.000197431087479984],
            [0.0259831865636676, 0.165729726420885, 0.144341021077508, 0.0304994564192397, 0.0323996868951937, 0.0149474316118957, 0.0198284130740851, 0.00111472695769643, 0.000197431087479984],
            [0.0233527028673718, 0.154552622116881, 0.139532242129044, 0.0301406065888357, 0.0268261789199743, 0.0614811107354387, 0.0197485064162744, 0.0011147326785955, 0.000176417748441007],
            [0.0254615120793923, 0.162228380293333, 0.142988932825394, 0.0305705252414648, 0.028959235447606, 0.0146972657534968, 0.0197485064162744, 0.0011147326785955, 0.000176417748441007],
            [0.022851516352904, 0.151053427047381, 0.138199411376694, 0.030211308320037, 0.0236508854235496, 0.0614896382122496, 0.0196684967822803, 0.00111473839949458, 0.00015540536288521],
            [0.0249189348601269, 0.158586596105097, 0.141627538100711, 0.03064159406369, 0.0255333436881607, 0.0144368585322728, 0.0196684967822803, 0.00111473839949458, 0.00015540536288521],
            [0.0194458007742665, 0.159299809150807, 0.141398242082133, 0.0291764153170589, 0.0761043366131248, 0.0594424678738145, 0.0200623577999024, 0.0010978531658788, 0.00198027109815137],
            [0.0212338105707341, 0.166773736153279, 0.144835725336584, 0.0295658605157085, 0.0815069734899258, 0.015675026044393, 0.0200645489042476, 0.0010978760494751, 0.000216770586798339],
            [0.0197402053917185, 0.154949099730717, 0.140174160615386, 0.0291270174988954, 0.0646916535515055, 0.0598781000360226, 0.019983819867195, 0.00109785030542927, 0.0015354039746137],
            [0.0215457711972183, 0.162248064476821, 0.14358417044389, 0.0295151661987925, 0.0693522297490184, 0.0154325636149675, 0.0199854603350044, 0.00109786746812649, 0.000216770586798339],
            [0.0198602084009115, 0.151101909521693, 0.139004611473721, 0.0291157163395171, 0.0527998780876407, 0.0603083326229884, 0.0199051789583044, 0.00109784744497973, 0.00108922485822182],
            [0.0216676907076008, 0.158261064075786, 0.142389137318931, 0.0295038607487398, 0.056681455190772, 0.015189346265235, 0.0199062687895779, 0.00109785888677788, 0.000216770586798339],
            [0.0200032451799995, 0.147004435699097, 0.13775258055455, 0.0291068804108979, 0.0410536794820527, 0.0607304339054042, 0.0198264350732304, 0.00109784458453019, 0.000643210694419892],
            [0.0218155330419107, 0.154020401870276, 0.141109567183474, 0.0294953523415926, 0.0441660859954107, 0.0149426670564506, 0.0198269742679681, 0.00109785030542927, 0.000216996085570157],
            [0.0198044725416868, 0.144005095604805, 0.13713300217909, 0.0291756713618085, 0.026321077165203, 0.0611587628632032, 0.0197478199083855, 0.00109785030542927, 0.000175956262582402],
            [0.0215968302214503, 0.150916376474061, 0.140475573095832, 0.0295652498097324, 0.0284139865684732, 0.0147008775477786, 0.0197478084665874, 0.00109785030542927, 0.000195982746531181],
            [0.0190681499241695, 0.140894910230512, 0.13558414384171, 0.0292659671723369, 0.0257370949388922, 0.0611516074486869, 0.0196678789251804, 0.00109785602632834, 0.000174969407492204],
            [0.0207991080546254, 0.147673108685068, 0.138895030274044, 0.0296560175944344, 0.0277804627864097, 0.0144507116893796, 0.0196678789251804, 0.00109785602632834, 0.000174969407492204],
            [0.0186207613143651, 0.137414508314469, 0.134218875591612, 0.0293366689035382, 0.0225618014424675, 0.0611594150456976, 0.0195878692911863, 0.00109786174722741, 0.000153957021936406],
            [0.0203148124946724, 0.144051702339333, 0.137501198051614, 0.0297270864166596, 0.0243545710269643, 0.0141903044681557, 0.0195878692911863, 0.00109786174722741, 0.000153957021936406],
            [0.0150189762222272, 0.141771374852186, 0.135925600708705, 0.0284132764618756, 0.0761043366131248, 0.0591624565616901, 0.0199019008831352, 0.00108520902544294, 0.00198027109815137],
            [0.0164071380801921, 0.148228832530405, 0.139201259036398, 0.0287694446208388, 0.0815069734899258, 0.0151883803867747, 0.0199040919874804, 0.00108523190903923, 0.000216770586798339],
            [0.0149798881793067, 0.13761659478357, 0.134716210510779, 0.0283925038773393, 0.0646916535515055, 0.0595919716525637, 0.0198232599742445, 0.0010852061649934, 0.0015354039746137],
            [0.0163561720205701, 0.143914917072707, 0.137965313616827, 0.0287483287823581, 0.0693522297490184, 0.0149451630370422, 0.0198249004420539, 0.00108522332769062, 0.000216770586798339],
            [0.015118705795328, 0.133590298957023, 0.133448964860522, 0.0283847177337002, 0.052973278538562, 0.0600147913845548, 0.0197445160891705, 0.00108520330454386, 0.00108945035699364],
            [0.0165001813525006, 0.139747336492414, 0.136670482267978, 0.0287408286836726, 0.0568701304422198, 0.0146984838282578, 0.019745605920444, 0.00108521474634201, 0.000216996085570157],
            [0.0149821479344408, 0.130987395715161, 0.132886235774269, 0.0284790811034699, 0.037864984779548, 0.0604431203423539, 0.0196659009243257, 0.00108520902544294, 0.000622197355380916],
            [0.0163495929866354, 0.137056402916057, 0.13609538197585, 0.0288365703133775, 0.040725634547823, 0.0144566943195858, 0.0196664401190634, 0.00108521474634201, 0.000195982746531181],
            [0.0151266006360496, 0.128004763506614, 0.132222871067525, 0.0285542336941504, 0.0231323824626983, 0.0608668492205561, 0.0195871827832975, 0.00108521474634201, 0.000154942923543426],
            [0.0165075613123056, 0.133973080023364, 0.135417045914601, 0.0289129395485944, 0.0249735351208855, 0.0142066085537739, 0.0195871713414993, 0.00108521474634201, 0.000174969407492204],
            [0.0144706852550119, 0.124797801973367, 0.130635454585501, 0.0286445295046788, 0.0225618014424675, 0.0608597553057048, 0.019507138823909, 0.00108522046724108, 0.000153957021936406],
            [0.0157971972743348, 0.130630744855338, 0.133798002872273, 0.0290037073332963, 0.0243545710269643, 0.01394620133255, 0.019507138823909, 0.00108522046724108, 0.000153957021936406],
            [0.0107493405233593, 0.126422920610511, 0.130855868669897, 0.0278780000633113, 0.0761043366131248, 0.0589095008115095, 0.0197412380140013, 0.00107619002805338, 0.00198027109815137],
            [0.0117500330381922, 0.132026187987599, 0.133994633033882, 0.0282106882222516, 0.0815069734899258, 0.0147025404224426, 0.0197434291183465, 0.00107621291164968, 0.000216770586798339],
            [0.0107099235287421, 0.122155096291313, 0.129555400328494, 0.0278639695583332, 0.0648650540024268, 0.0593316118671279, 0.0196624941289273, 0.00107618716760385, 0.00153562947338552],
            [0.0117002540651279, 0.127602710161518, 0.132665868172178, 0.0281967549725578, 0.0695409050004663, 0.0144558612136582, 0.0196641345967367, 0.00107620433030107, 0.000216996085570157],
            [0.0106306032630864, 0.119647420274981, 0.128981987463222, 0.0279600742267585, 0.0497845838360573, 0.059759940824927, 0.0195838789640825, 0.00107619288850292, 0.00106843701795466],
            [0.0116123309974902, 0.125010639442052, 0.132080172774966, 0.0282942286044572, 0.0534296789946321, 0.0142140717049862, 0.019584968795356, 0.00107620433030107, 0.000195982746531181],
            [0.0108248277866356, 0.117049876085326, 0.12838135241482, 0.0280607992362981, 0.0346762900770433, 0.0601836697031292, 0.0195051608230543, 0.00107619860940199, 0.000601184016341939],
            [0.0118247908868366, 0.122328554666337, 0.131466739598595, 0.0283964420012391, 0.0372851831002353, 0.0139639859391743, 0.019505700017792, 0.00107620433030107, 0.000174969407492204],
            [0.0108151737694489, 0.113751960838157, 0.127665662934924, 0.0281324835319153, 0.0199539510531317, 0.06060322899939, 0.0194263397058428, 0.00107620433030107, 0.000133929584504449],
            [0.0118146005353617, 0.11891317219849, 0.130735338622877, 0.0284691970584663, 0.0215440163114274, 0.0137036588105374, 0.0194263282640447, 0.00107620433030107, 0.000153957021936406],
            [0.00715480667079716, 0.11305582682152, 0.126000009582506, 0.0275335502126172, 0.076277737064046, 0.0586808800973926, 0.0195803691925008, 0.00107018594447562, 0.00198049659692319],
            [0.00782691219621311, 0.117967235838915, 0.129019536822662, 0.0278514405509912, 0.0816956487413736, 0.0142124836787517, 0.019582560296846, 0.00107020882807192, 0.000216996085570157],
            [0.00699029506681152, 0.110441574746121, 0.125404233722755, 0.0276261880162039, 0.0616763592999221, 0.059107977631666, 0.019501754027656, 0.0010701916653747, 0.00151461613434654],
            [0.00764622475009683, 0.11526153090115, 0.128411057229777, 0.0279453357605201, 0.0661004535528786, 0.0139706941700797, 0.0195033944954653, 0.00107020882807192, 0.000195982746531181],
            [0.00720442831913692, 0.107935243856183, 0.124798559277382, 0.027729115333516, 0.0465958891335527, 0.0595317065098683, 0.0194230358866278, 0.00107019738627377, 0.00104742367891568],
            [0.00788048126491367, 0.112674148458475, 0.127792776306553, 0.0280497636219851, 0.0499892275470444, 0.0137206084042677, 0.0194241257179013, 0.00107020882807192, 0.000174969407492204],
            [0.00724454612389065, 0.105022416627908, 0.124152593254946, 0.0278263720479922, 0.0314978586674767, 0.059951265806129, 0.0193442147694163, 0.00107020310717284, 0.000580170677302962],
            [0.00792478247711497, 0.109660004107606, 0.127133368555002, 0.0281483628407773, 0.0338556642907773, 0.0134602812756308, 0.019344753964154, 0.00107020882807192, 0.000153957021936406],
            [0.0046199728314503, 0.103372264051529, 0.121754777808861, 0.0274419562347407, 0.0764109338967275, 0.0584674927072839, 0.0194194917896517, 0.00106659512682375, 0.00198071923524547],
            [0.00506002081263083, 0.107812188032222, 0.124678615860888, 0.0277530258311942, 0.0818406449283944, 0.0137238547761212, 0.019421694335795, 0.00106661801042005, 0.000196208245302999],
            [0.00478069433979967, 0.100848382158346, 0.121136827744301, 0.0275426833896174, 0.0618095561326036, 0.0588892669449693, 0.0193407736486235, 0.00106660084772282, 0.00151483877266882],
            [0.00523608148162133, 0.105205131417633, 0.124047839063863, 0.0278552020421321, 0.0662454497398993, 0.0134737690103093, 0.019342425558231, 0.00106661801042005, 0.000175194906264022],
            [0.00484569805552361, 0.0980976094079041, 0.120493131488572, 0.027642723321493, 0.0467290859662341, 0.0593088262412301, 0.019261952531412, 0.0010666065686219, 0.00104764631723797],
            [0.00530762847566072, 0.102359674927073, 0.123391014298243, 0.0279566173734933, 0.0501342237340651, 0.0132134418816724, 0.0192630538044837, 0.00106661801042005, 0.000154182520708224],
            [0.00362257698470861, 0.0972710110030052, 0.119458007742665, 0.0275736522848985, 0.0579746444032158, 0.0587024695786424, 0.0192598629730254, 0.00106480734586325, 0.001492451464369],
            [0.00396843751376591, 0.101451643814535, 0.122333384058638, 0.0278845063941535, 0.0621085417599888, 0.0132318994090502, 0.0192615148826329, 0.00106482450856047, 0.000154181567225045],
            [0.00368758070043256, 0.0943639204062754, 0.11878586646163, 0.0276722977476248, 0.043388816042774, 0.0591192399366048, 0.0191810418558139, 0.00106481306676232, 0.00102657100179236],
            [0.00403998450780531, 0.0984440885091737, 0.121647442062071, 0.0279845143843426, 0.0465297626913855, 0.0129715722804133, 0.0191821431288856, 0.00106482450856047, 0.000133169181669248],
            [0.00368818854595913, 0.0914915070392803, 0.117212702169422, 0.0277525564790994, 0.0395740061225062, 0.0589569284950546, 0.0191000282040324, 0.00106420379101098, 0.0010041851237173],
            [0.00404105717638161, 0.0954661989259584, 0.120045861110682, 0.0280655628382601, 0.0424146942436886, 0.0127214064220143, 0.0191011294771041, 0.00106421523280913, 0.000112155842630271]
        ]
    
    # This table is used by HandPlayerOpponentOdds and contains the odds of each type of 
    # mask occuring for a random player when the board is currently empty. This calculation
    # normally takes about 5 minutes, so the values are precalculated to save time.
    @staticmethod
    def __PreCalcOppOdds():
        return [
            [0, 0.000176203691467336, 0.0326410244528389, 0.0291796688400362, 0.0451538349760895, 0.021233850140286, 0.0176688366036853, 0.0015772518745956, 0.00033219639999077],
            [0, 0.0144409365798291, 0.045186784494304, 0.0292916954856958, 0.0450247457489429, 0.0217730639476378, 0.018371218080482, 0.00162264530177838, 0.000332112493471024],
            [0, 0.0285658649970795, 0.0573239407612343, 0.0293464073039863, 0.0421463011240995, 0.0223154194820641, 0.0190763112634396, 0.00166049477004942, 0.000313619687215564],
            [0, 0.0424026202861937, 0.069600123457002, 0.029400401149443, 0.0392824161873983, 0.0228486578103335, 0.019784425081108, 0.00169149822909569, 0.000295128787926462],
            [0, 0.0559512024471718, 0.0821974330897947, 0.0294536770220661, 0.0364185312506972, 0.0233728170717731, 0.0204955595334874, 0.00171634218680604, 0.00027663788863736],
            [0, 0.0699936898483218, 0.095626857504418, 0.0295849144468148, 0.0371309061846924, 0.0238678664917597, 0.0212100235491276, 0.00173572459286745, 0.00027749793046476],
            [0, 0.0838198328696545, 0.109404126884965, 0.0297033799643817, 0.0371309061846924, 0.0243560727629711, 0.0219275081994786, 0.0017503205133706, 0.00027749793046476],
            [0, 0.0976459758909871, 0.123513558816849, 0.0298218454819486, 0.0371309061846924, 0.0248411578069963, 0.0226480134845405, 0.00176081645620432, 0.00027749793046476],
            [0, 0.111499902458671, 0.137836709235877, 0.0299403109995154, 0.0371309061846924, 0.0253277526916353, 0.0233715394043133, 0.00176789892925746, 0.00027749793046476],
            [0, 0.125140176329551, 0.152157898816746, 0.0300452866370667, 0.0374386791130547, 0.0258193300026259, 0.0240980859587969, 0.00177225444041884, 0.00027908357299133],
            [0, 0.139198427668099, 0.166821392672787, 0.0302260699082425, 0.0403025640497558, 0.0263232163047149, 0.0248279620765414, 0.00177458093937544, 0.000297574472280432],
            [0, 0.153544852134782, 0.181454191044848, 0.030407571152252, 0.0431664489864569, 0.0268436951210838, 0.0255608588289968, 0.00177555349221796, 0.000316065371569534],
            [0, 0.168184993280804, 0.196062845792593, 0.0305897903690952, 0.046030333923158, 0.0273846547561362, 0.026296776216163, 0.00177585860683522, 0.000334556270858636],
            [0.000778585759423608, 0.0857216227673476, 0.120254482753492, 0.0303105118087938, 0.0415814374273803, 0.0263834292442063, 0.0227276245625658, 0.00145477672189051, 0.000341205862548535],
            [0.000863083438740899, 0.0931761058640932, 0.128900488011761, 0.0320056885759938, 0.0442699160229225, 0.0230610004212489, 0.0227356824489109, 0.00145516288257797, 0.000332154446730897],
            [0.001943975807462, 0.0912532888018549, 0.12236401422902, 0.0305207820240198, 0.0408509186619732, 0.0263836695219674, 0.022806681666864, 0.00145477386144097, 0.00033327145227502],
            [0.00213885823440469, 0.0989645801975655, 0.131040601983512, 0.0322232686700111, 0.0433906052539593, 0.0233308843117882, 0.0228147395532092, 0.00145516002212844, 0.000322908043603167],
            [0.00309443430891825, 0.0971088320956168, 0.124351205708084, 0.0306994957599557, 0.0397706327085539, 0.0263839097997285, 0.0228858417473456, 0.00145477100099143, 0.000324086548812332],
            [0.00339828556096562, 0.105110615013813, 0.133056615352109, 0.0324073986671449, 0.042135577298786, 0.0235962095992491, 0.0228938996336908, 0.0014551571616789, 0.000313662593958616],
            [0.00422996126379237, 0.103003240317235, 0.126203923163749, 0.0308411666743899, 0.0385789751524191, 0.0263841500774896, 0.0229651048040106, 0.00145476814054189, 0.000314842529392549],
            [0.0046413654184237, 0.111305110135889, 0.134934626332803, 0.0325524034355143, 0.0407602188129478, 0.0238569953532951, 0.0229731626903558, 0.00145515430122936, 0.000304417144314065],
            [0.00500605843211896, 0.114119995572024, 0.131034367872117, 0.0315056648342627, 0.0393253293664619, 0.0263829272353126, 0.0230527604196165, 0.00145516002212844, 0.000305597079747998],
            [0.00549146241626749, 0.123138150559189, 0.140011536192982, 0.033258019127254, 0.0414562477080648, 0.0241039126945034, 0.0230526059553415, 0.00145515430122936, 0.000304847165227765],
            [0.00629338944391145, 0.119787641656612, 0.132650986683463, 0.0315623746765547, 0.0389923058198134, 0.026382961560707, 0.0231322294286481, 0.0014551571616789, 0.000304847165227765],
            [0.00690074154293792, 0.129060170700187, 0.141642831970901, 0.033313468941525, 0.0411164634889361, 0.0243480387137054, 0.0231322294286481, 0.0014551571616789, 0.000304847165227765],
            [0.00767206891166188, 0.125861554528463, 0.134622862600595, 0.0316566980000309, 0.0389923058198134, 0.026382961560707, 0.023211955878138, 0.00145516002212844, 0.000304847165227765],
            [0.00841015785676814, 0.135427291091359, 0.143660736096642, 0.0334108529460056, 0.0411164634889361, 0.024590581235718, 0.023211955878138, 0.00145516002212844, 0.000304847165227765],
            [0.00911472233330301, 0.132281325784035, 0.136963206609698, 0.031792725247529, 0.0393540640122839, 0.0263829272353126, 0.0232919397680862, 0.00145516860347705, 0.00030563998649105],
            [0.00998974099773624, 0.142176993747629, 0.146078837135729, 0.0335545247448908, 0.0414897292698931, 0.0248338557944412, 0.0232917853038112, 0.00145516288257797, 0.000304847165227765],
            [0.0095779435312936, 0.132500300347201, 0.136124438422245, 0.0313238489408041, 0.0397266575875998, 0.0263841500774896, 0.0233637370514601, 0.00145478244278958, 0.000314885436135601],
            [0.0104964839354294, 0.142212007080185, 0.14508643897107, 0.0330513416366462, 0.0419755294263025, 0.0250802518187215, 0.0233717949378052, 0.00145516860347705, 0.00030563998649105],
            [0.0101446128867828, 0.137313853385943, 0.138252359727845, 0.0314076386588611, 0.0409384169528546, 0.0263839097997285, 0.0234439268937749, 0.00145479102413819, 0.000324130885780152],
            [0.0111170155556967, 0.147235073745249, 0.147282583428348, 0.0331402873149933, 0.0433727274443542, 0.0253334888464398, 0.0234519847801201, 0.00145517718482566, 0.000314885436135601],
            [0.0101886781118974, 0.141926414077531, 0.140355244948875, 0.0314802154147337, 0.0421501763181094, 0.0263836695219674, 0.0235242197122731, 0.0014547996054868, 0.000333376335424703],
            [0.0111653857573641, 0.152041088069237, 0.1494532613034, 0.0332176996608079, 0.044769925462406, 0.0255950221312981, 0.0235322775986183, 0.00145518576617427, 0.000324130885780152],
            [0.0102601178390791, 0.146768933458507, 0.142476464221211, 0.0315580954440476, 0.0433619356833643, 0.0263834292442063, 0.0236046155069546, 0.00145480818683541, 0.000342621785069254],
            [0.0112437263190534, 0.157090256336325, 0.151644434299383, 0.0333008329056961, 0.0461671234804577, 0.0258667958254981, 0.0236126733932998, 0.00145519434752288, 0.000333376335424703],
            [0.00938340435829533, 0.106536486178022, 0.126920558737329, 0.0314315648890117, 0.0401629233393803, 0.026846661883995, 0.022878916599017, 0.00149431099493872, 0.000341140072209188],
            [0.0102295825402737, 0.115235952761392, 0.135750875392907, 0.0331660885698153, 0.0427453951053132, 0.0236011233748118, 0.0228950323717074, 0.00149508331631366, 0.000322866090343294],
            [0.0105070604475917, 0.112156171105226, 0.128851791242104, 0.031602562562322, 0.0395772791918887, 0.0268460821662222, 0.0229580766794986, 0.00149430813448918, 0.000333267161600715],
            [0.0114598904905499, 0.121131043200225, 0.137708093651499, 0.0333419647398107, 0.0420228140873707, 0.0238664486622726, 0.022974192452189, 0.00149508045586412, 0.000313620640698743],
            [0.0116291861963859, 0.117839568255189, 0.130685537481328, 0.0317417806412785, 0.0385170950475893, 0.0268455219948546, 0.0230373397361636, 0.00149430527403965, 0.000324083688362795],
            [0.0126884106598657, 0.127101650937055, 0.139566572052531, 0.0334844465916886, 0.0407896256644109, 0.0241272344163186, 0.0230534555088539, 0.00149507759541459, 0.000304375191054192],
            [0.0124732404945832, 0.129018431020545, 0.13558351096725, 0.0324139762708548, 0.0388480519194475, 0.0268434991802905, 0.0231249953517695, 0.00149469715562619, 0.000314842529392549],
            [0.0136129651591526, 0.138997545448252, 0.144713078795278, 0.034197968565948, 0.0410522621293072, 0.0243741517575269, 0.0231328987738397, 0.00149507759541459, 0.000304805211967892],
            [0.0140899808750344, 0.138915287500922, 0.139821439298114, 0.0329521498280584, 0.0392351565552636, 0.0268492067305996, 0.0232125994792838, 0.00149508331631366, 0.000305597079747998],
            [0.0153791139700351, 0.149504482896514, 0.14915529995532, 0.0347687870034903, 0.0413606400427466, 0.024617622733785, 0.0232124450150088, 0.00149507759541459, 0.000304805211967892],
            [0.0153788350762052, 0.144080950435847, 0.141375266236341, 0.0329706011577956, 0.038876536275935, 0.0268483786304587, 0.0232921714644987, 0.00149508045586412, 0.000304805211967892],
            [0.0167909031411741, 0.154886267096192, 0.150721561982795, 0.0347845194759428, 0.0409910013118022, 0.0248601881393939, 0.0232921714644987, 0.00149508045586412, 0.000304805211967892],
            [0.0167393292360254, 0.149620906053112, 0.143304048766088, 0.0330307564115546, 0.038876536275935, 0.0268491786028458, 0.0233720008901719, 0.00149508331631366, 0.000304805211967892],
            [0.0182803535172374, 0.160679432566904, 0.152694508423166, 0.0348465397427998, 0.0409910013118022, 0.0251034855817134, 0.0233720008901719, 0.00149508331631366, 0.000304805211967892],
            [0.0179919558438126, 0.15433230242732, 0.145104149682748, 0.0330549529541865, 0.0394830002053803, 0.0268518450185557, 0.0234519332920284, 0.0014950861767632, 0.000305598033231177],
            [0.0196486495531692, 0.165587838112286, 0.154532129141287, 0.0348709179239773, 0.0416188928687277, 0.0253492265630497, 0.0234519332920284, 0.0014950861767632, 0.000305598033231177],
            [0.018585234531118, 0.159245210320273, 0.147295221132772, 0.0331387426722434, 0.0406947595706351, 0.0268524047131818, 0.0235321231343433, 0.00149509475811181, 0.000314843482875728],
            [0.0202982576429781, 0.170714719072391, 0.1567918227757, 0.0349598636023243, 0.0430160908867794, 0.0256024635907681, 0.0235321231343433, 0.00149509475811181, 0.000314843482875728],
            [0.0186509319058546, 0.163929043402745, 0.149467849119296, 0.033211319428116, 0.0419065189358899, 0.0268529644078078, 0.0236124159528415, 0.00149510333946042, 0.000324088932520279],
            [0.0203702551578196, 0.175594040997107, 0.15903263744317, 0.0350372759481389, 0.0444132889048311, 0.0258639968756263, 0.0236124159528415, 0.00149510333946042, 0.000324088932520279],
            [0.0187223716330364, 0.168748144283363, 0.151635244628505, 0.0332838961839887, 0.0431182783011447, 0.0268535236256923, 0.023692811747523, 0.00149511192080903, 0.00033333438216483],
            [0.0204485957195089, 0.180613800982507, 0.161268161709222, 0.0351146882939535, 0.0458104869228829, 0.0261357705698263, 0.023692811747523, 0.00149511192080903, 0.00033333438216483],
            [0.0172662526452007, 0.125596476669888, 0.132139757130672, 0.0324108188113078, 0.0378316412344098, 0.0272736855233221, 0.02303026012356, 0.00152716325786895, 0.000331893192339869],
            [0.018810745221476, 0.135424968406335, 0.14107351956004, 0.03417585776777, 0.0401439177975454, 0.0241369647121596, 0.0230544337825955, 0.00152832173993136, 0.000304374237571013],
            [0.0183416672530588, 0.131015885792548, 0.133925078819687, 0.0325426655118078, 0.0372660988960381, 0.0272723053564206, 0.0231095231802249, 0.00152716039741942, 0.000324021711956164],
            [0.0199883493890366, 0.141114542697072, 0.142880763019193, 0.0343104476393759, 0.0394431763118165, 0.0243977504662056, 0.0231336968392605, 0.00152831887948182, 0.000295128787926462],
            [0.0191906987334502, 0.142159968351986, 0.138860754460728, 0.0332216713949898, 0.0376146160676027, 0.0272695016391329, 0.0231971787958308, 0.00152755227900596, 0.000314841099167781],
            [0.0209183530446911, 0.152970112020925, 0.148066266985588, 0.0350310830748917, 0.0397281500271457, 0.0246446678074139, 0.0232131401042462, 0.00152831887948182, 0.000295558808840162],
            [0.02078848863572, 0.152085104666709, 0.14316275757633, 0.0337675424218969, 0.0376260292612546, 0.0272744292402017, 0.0232847829233451, 0.00152793843969343, 0.000305597079747998],
            [0.0226636420273264, 0.163505530965224, 0.152574264182729, 0.0356098077949538, 0.0396441314731258, 0.024888138783672, 0.0232926863454153, 0.00152831887948182, 0.000295558808840162],
            [0.0229429792268434, 0.161885545404774, 0.147375023384175, 0.0342778408983642, 0.0380131338970707, 0.0272856789114883, 0.0233724900270427, 0.0015283246003809, 0.000296351630103447],
            [0.0250161758421306, 0.17390628852668, 0.156990344409566, 0.0361517600059955, 0.0399525093865652, 0.025130049146337, 0.0233723355627677, 0.00152831887948182, 0.000295558808840162],
            [0.0240675792644869, 0.166443421452342, 0.148889000684792, 0.0342621241583842, 0.0376513757046002, 0.0272847888349408, 0.0234521649884409, 0.00152832173993136, 0.000295558808840162],
            [0.0262488651166463, 0.17863493198137, 0.158514892501446, 0.0361321287408244, 0.0395792436056081, 0.0253733694722528, 0.0234521649884409, 0.00152832173993136, 0.000295558808840162],
            [0.0252616238657602, 0.171131965695201, 0.15072397191153, 0.0342863207010161, 0.0382578396340455, 0.027287395657952, 0.0235320973902975, 0.0015283246003809, 0.000296351630103447],
            [0.0275534732436411, 0.183518789148827, 0.160387383529646, 0.0361565069220018, 0.0402071351625336, 0.0256191104535891, 0.0235320973902975, 0.0015283246003809, 0.000296351630103447],
            [0.0258614100757619, 0.176055317089412, 0.152955590233739, 0.034370110419073, 0.0394695989993003, 0.0272887353018184, 0.0236122872326123, 0.00152833318172951, 0.000305597079747998],
            [0.0282103182707782, 0.188656865908419, 0.162687624036243, 0.0362454526003489, 0.0416043331805853, 0.0258723474813074, 0.0236122872326123, 0.00152833318172951, 0.000305597079747998],
            [0.0259336149731947, 0.180749593673143, 0.155174441654553, 0.0344426871749457, 0.0406813583645551, 0.0272900749456848, 0.0236925800511105, 0.00152834176307812, 0.000314842529392549],
            [0.0282895527229477, 0.193547383632622, 0.164974662138003, 0.0363228649461635, 0.0430015311986371, 0.0261338807661657, 0.0236925800511105, 0.00152834176307812, 0.000314842529392549],
            [0.0260115622230727, 0.18557913805502, 0.157393737160157, 0.0345152639308183, 0.0418931177298099, 0.0272914141128096, 0.023772975845792, 0.00152835034442673, 0.0003240879790371],
            [0.0283751302219652, 0.198578339417509, 0.16726208640045, 0.0364002772919781, 0.0443987292166888, 0.0264056544603657, 0.023772975845792, 0.00152835034442673, 0.0003240879790371],
            [0.0241754182120245, 0.142662453510544, 0.136388411432187, 0.0332386226573157, 0.0355360103422413, 0.0276621059659252, 0.0231818096004696, 0.0015539494608148, 0.000322647742695318],
            [0.0263329694841523, 0.153488246698898, 0.145375219944732, 0.0350267104010331, 0.0375806961418829, 0.0246637079130141, 0.0232140411458503, 0.00155549410356467, 0.000285883338281911],
            [0.0249827157336738, 0.153978036467299, 0.141327931517406, 0.0339259228906711, 0.0363636199160515, 0.0276584822531036, 0.0232694652160755, 0.00155434134240134, 0.00031477912276115],
            [0.0272175062944192, 0.165523319242759, 0.15056373024359, 0.0357558575808873, 0.0383817006745512, 0.0249106252542225, 0.0232934844108361, 0.00155549410356467, 0.000286313359195611],
            [0.0265814638865386, 0.163837787196285, 0.145664418782398, 0.0344769906392742, 0.0364028567023479, 0.027662648497854, 0.0233570693435898, 0.00155472750308881, 0.00030559564952323],
            [0.0289637320742779, 0.175987578783931, 0.155107165550043, 0.036340007143496, 0.0383309520090939, 0.0251540962304805, 0.0233730306520051, 0.00155549410356467, 0.000286313359195611],
            [0.0287196856709213, 0.173714533286193, 0.149939332725774, 0.0349949865854452, 0.0364142698959998, 0.0276731382430471, 0.0234447764472874, 0.00155511366377628, 0.000296351630103447],
            [0.0312981735457618, 0.186467859702959, 0.159587337724314, 0.0368898656370574, 0.0382469334550741, 0.0253960065931455, 0.0234526798693575, 0.00155549410356467, 0.000286313359195611],
            [0.0311667001339262, 0.183283058787387, 0.154144205701791, 0.0354801173966629, 0.0368013745318159, 0.0276902794868964, 0.0235325865271683, 0.00155549982446375, 0.000287106180458896],
            [0.0339690610917649, 0.196618396580733, 0.163995731208134, 0.0374058578383278, 0.0385553113685134, 0.0256386718761174, 0.0235324320628933, 0.00155549410356467, 0.000286313359195611],
            [0.0320071145100879, 0.186938571703175, 0.155565993574286, 0.0354284419455557, 0.0370460802687907, 0.0276903352656623, 0.0236123644647498, 0.00155549696401421, 0.000287106180458896],
            [0.0348886813156008, 0.20038306568107, 0.16542144576273, 0.037348584487477, 0.0388099371444819, 0.02588443574105, 0.0236123644647498, 0.00155549696401421, 0.000287106180458896],
            [0.0325933064336659, 0.191861948841432, 0.157833293144017, 0.0355122316636127, 0.0382578396340455, 0.0276924348356224, 0.0236925543070647, 0.00155550554536282, 0.000296351630103447],
            [0.0355309237478525, 0.205521113836166, 0.167757367516849, 0.0374375301658241, 0.0402071351625336, 0.0261376727687683, 0.0236925543070647, 0.00155550554536282, 0.000296351630103447],
            [0.0326519170446751, 0.196556251169209, 0.160092691437015, 0.0355848084194853, 0.0394695989993003, 0.0276945344055824, 0.0237728471255629, 0.00155551412671143, 0.000305597079747998],
            [0.0355955556051367, 0.210411602955874, 0.170084952490794, 0.0375149425116387, 0.0416043331805853, 0.0263992060536266, 0.0237728471255629, 0.00155551412671143, 0.000305597079747998],
            [0.0327162700081294, 0.201385821295131, 0.162357399439466, 0.035657385175358, 0.0406813583645551, 0.0276966334988008, 0.0238532429202444, 0.00155552270806004, 0.000314842529392549],
            [0.0356665305092687, 0.215442530136266, 0.172417789250087, 0.0375923548574533, 0.0430015311986371, 0.0266709797478266, 0.0238532429202444, 0.00155552270806004, 0.000314842529392549],
            [0.0299178278661561, 0.164330744912547, 0.143122944409452, 0.0344778208847523, 0.0346335313622548, 0.0280109096591851, 0.0233418546125035, 0.00157567457504685, 0.000313405153500304],
            [0.0325850111300091, 0.176506234063721, 0.152351058299585, 0.0363214957443185, 0.0365192205046176, 0.0251720431676161, 0.0233739316936092, 0.00157721349689765, 0.00027706790955106],
            [0.0314748420602788, 0.174210417242332, 0.147459907939292, 0.0350339559197098, 0.0351518605507967, 0.0280142559084015, 0.0234294587400177, 0.00157606073573432, 0.000305533673116599],
            [0.0342857700644803, 0.186989146596322, 0.156893790650563, 0.0369107798138458, 0.0369845026564995, 0.0254155141438741, 0.0234534779347783, 0.00157721349689765, 0.00027706790955106],
            [0.0336100031636572, 0.184070676416223, 0.151768115369939, 0.0355557655602257, 0.0351910973370931, 0.0280240038436814, 0.0235171658437153, 0.00157644689642179, 0.000296350199878679],
            [0.0366166359740431, 0.197450827442238, 0.161407978575614, 0.0374646157624881, 0.0369337539910422, 0.0256574245065391, 0.0235331271521307, 0.00157721349689765, 0.00027706790955106],
            [0.0360531917754067, 0.193746550297859, 0.156033096402298, 0.036048593841147, 0.035202510530745, 0.0280403851614371, 0.0236049759235962, 0.00157683305710926, 0.000287106180458896],
            [0.0392830540676451, 0.207713714196468, 0.165877698667278, 0.0379885142462782, 0.0368497354370223, 0.025900089789511, 0.0236128793456664, 0.00157721349689765, 0.00027706790955106],
            [0.0386027319009346, 0.202746913288905, 0.160173564211657, 0.0365053833183541, 0.0361960790960064, 0.0280639767189919, 0.0236928889796605, 0.00157721921779673, 0.00027865355207763],
            [0.0420619521881581, 0.217258299165264, 0.17021642018173, 0.0384748207022556, 0.0377860049073872, 0.0261451986114997, 0.0236927345153855, 0.00157721349689765, 0.000277860730814345],
            [0.03878762420787, 0.206619602975325, 0.162027680427145, 0.036513301042672, 0.0370460802687907, 0.0280635223842572, 0.0237729243577004, 0.00157722207824626, 0.000287106180458896],
            [0.0422673539182724, 0.221258237379554, 0.172105565462246, 0.0384821148485745, 0.0388099371444819, 0.0263984585228143, 0.0237729243577004, 0.00157722207824626, 0.000287106180458896],
            [0.0388125387233356, 0.211303513289935, 0.164321949030222, 0.0365858777985446, 0.0382578396340455, 0.028066361857164, 0.0238532171761985, 0.00157723065959487, 0.000296351630103447],
            [0.0422955436484576, 0.226137473490784, 0.174468020746268, 0.0385595271943891, 0.0402071351625336, 0.0266599918076725, 0.0238532171761985, 0.00157723065959487, 0.000296351630103447],
            [0.0388431955912463, 0.21612269140269, 0.166625582029969, 0.0366584545544173, 0.0394695989993003, 0.0280692008533293, 0.0239336129708801, 0.00157723924094348, 0.000305597079747998],
            [0.0423300764254907, 0.231157147662698, 0.176839782502859, 0.0386369395402037, 0.0416043331805853, 0.0269317655018725, 0.0239336129708801, 0.00157723924094348, 0.000305597079747998],
            [0.0344508394561256, 0.184183918037823, 0.149194415887623, 0.0354895428162575, 0.0349427509629703, 0.0283224841249818, 0.023502105576904, 0.00159255408776355, 0.000313835174414004],
            [0.0375266736919307, 0.197551984379657, 0.158622149109132, 0.0373779465252308, 0.0368814263574406, 0.025663718687374, 0.0235341826580098, 0.00159409300961435, 0.00027749793046476],
            [0.0362848595833927, 0.193780071190868, 0.153470955996561, 0.0360069673876334, 0.0354610801515123, 0.0283300380954669, 0.0235898126806016, 0.00159294024845102, 0.000305963694030299],
            [0.0395300324317769, 0.207726403150614, 0.163100886052849, 0.0379268539193212, 0.0373467085093225, 0.025905629050039, 0.0236138318753622, 0.00159409300961435, 0.00027749793046476],
            [0.038617970945842, 0.20341607612686, 0.157766926424089, 0.0365024568401072, 0.0355003169378087, 0.0283456156269028, 0.0236776227604825, 0.00159332640913849, 0.000296780220792379],
            [0.042076440365062, 0.21794503589006, 0.167602118286835, 0.0384535237019709, 0.0372959598438652, 0.0261482943330109, 0.0236935840688979, 0.00159409300961435, 0.00027749793046476],
            [0.0411659807308677, 0.212550282412183, 0.161963848780619, 0.0369669437870178, 0.0361181940609058, 0.0283684272352172, 0.0237655358165468, 0.00159371256982596, 0.000288329022635881],
            [0.0448535507046145, 0.227629905885489, 0.171998319819616, 0.038947736440468, 0.0378398328467709, 0.0263934031549996, 0.023773439238617, 0.00159409300961435, 0.000278290751728045],
            [0.0434055482423396, 0.222074828501748, 0.166559756650116, 0.0374895607894154, 0.0377170580619768, 0.0283973997750924, 0.0238537063130693, 0.0015941044514125, 0.000288329022635881],
            [0.0472946940949452, 0.23773827973709, 0.17682476800324, 0.039505119346536, 0.039545408778262, 0.0266460080233703, 0.0238535518487943, 0.00159409873051343, 0.000287536201372596],
            [0.0429633084417015, 0.225679951738495, 0.168439220024062, 0.037486265551549, 0.0385670592347611, 0.028396883463951, 0.0239338446672925, 0.00159410731186204, 0.000296781651017147],
            [0.0468142243862476, 0.241449288234342, 0.178738824938772, 0.0395008801603225, 0.0405693410153566, 0.0269075641918248, 0.0239338446672925, 0.00159410731186204, 0.000296781651017147],
            [0.0429401674049487, 0.230480336697794, 0.170775290521557, 0.0375588423074217, 0.0397788186000159, 0.0284004423399164, 0.024014240461974, 0.00159411589321065, 0.000306027100661698],
            [0.0467904755039683, 0.246448584563756, 0.18114302419311, 0.0395782925061371, 0.0419665390334083, 0.0271793378860248, 0.024014240461974, 0.00159411589321065, 0.000306027100661698],
            [0.0388776640081649, 0.201712352336444, 0.154667057261051, 0.0362526816714408, 0.0349427509629703, 0.0286024954371062, 0.0236625624936713, 0.00160519822819942, 0.000313835174414004],
            [0.0423533461824727, 0.216096888002531, 0.164256615409318, 0.0381743624201005, 0.0368814263574406, 0.0261503643449923, 0.023694639574777, 0.00160673715005022, 0.00027749793046476],
            [0.0410451767958045, 0.211112576138016, 0.158928906101167, 0.0367414810091895, 0.0354610801515123, 0.0286161664789258, 0.0237503725735522, 0.00160558438888689, 0.000305963694030299],
            [0.0447196316084251, 0.226059550554727, 0.168719742879912, 0.0386936913357556, 0.0373467085093225, 0.0263930296279642, 0.0237743917683127, 0.00160673715005022, 0.00027749793046476],
            [0.043473154967142, 0.220208960129338, 0.163153400330782, 0.0372077071094185, 0.0361268826763739, 0.0286381371150765, 0.0238382856296164, 0.00160597054957436, 0.000297574472280432],
            [0.0473658334749256, 0.235702220338139, 0.173143871696634, 0.0391897104481352, 0.0379456909330043, 0.0266381384499529, 0.0238542469380318, 0.00160673715005022, 0.000278290751728045],
            [0.0457299495359493, 0.229887305439374, 0.167800995808297, 0.0377380215815197, 0.0373299534261606, 0.0286671082247268, 0.023926456126139, 0.0016063624311609, 0.000297574472280432],
            [0.0498260060057998, 0.245971794823387, 0.178022872059148, 0.0397549996367229, 0.0392370308648226, 0.0268907433183236, 0.0239343595482092, 0.00160674287094929, 0.000287536201372596],
            [0.0476262917074996, 0.239395143643194, 0.172440690009079, 0.0382542769441474, 0.0389288174272316, 0.0287006808441988, 0.0240147295988448, 0.00160675431274744, 0.000297574472280432],
            [0.0518904782499999, 0.256059466171466, 0.182893662216379, 0.0403059107757139, 0.0409426067963137, 0.0271516444438342, 0.0240145751345698, 0.00160674859184837, 0.000296781651017147],
            [0.0470902434643019, 0.243097043038896, 0.174358711527669, 0.038250981706281, 0.0397788186000159, 0.0287001020799091, 0.0240949709292514, 0.00160675717319698, 0.000306027100661698],
            [0.0513080907243059, 0.25986954204775, 0.184846219372452, 0.0403016715895003, 0.0419665390334083, 0.0274234410216305, 0.0240949709292514, 0.00160675717319698, 0.000306027100661698],
            [0.0431472997070328, 0.217060806578119, 0.159736789299859, 0.0367879580700051, 0.0349427509629703, 0.0288554511872868, 0.0238232253628051, 0.00161421722558897, 0.000313835174414004],
            [0.0470104512244726, 0.232299532545337, 0.169463241411834, 0.0387331188186877, 0.0368814263574406, 0.0266362043093244, 0.0238553024439109, 0.00161575614743977, 0.00027749793046476],
            [0.045336737840372, 0.225795857868839, 0.163920543576946, 0.03724426699169, 0.0362392211110329, 0.0288754445376951, 0.0239111384188694, 0.00161460338627644, 0.000306819921924983],
            [0.0493973461893377, 0.241551291864824, 0.173842286683406, 0.0392184198266529, 0.0381604491935535, 0.0268813131313131, 0.0239351576136299, 0.00161575614743977, 0.000278290751728045],
            [0.0475041290589064, 0.235471821854635, 0.16859117997548, 0.037775629103434, 0.0373386420416287, 0.0289043551011636, 0.0239993089153919, 0.00161499526786298, 0.000306819921924983],
            [0.051760199075846, 0.251816807372179, 0.178744548221554, 0.0397847916953903, 0.039342888951056, 0.0271339179996838, 0.0240152702238073, 0.00161576186833885, 0.000287536201372596],
            [0.0494301412432772, 0.245144808112464, 0.173276681415144, 0.0382995819357654, 0.0385417127914154, 0.0289379262904108, 0.0240875823880978, 0.00161538714944953, 0.000306819921924983],
            [0.0538573233515086, 0.262077533056785, 0.183661881468311, 0.040343609116901, 0.0406342288828743, 0.0273948191251944, 0.024095485810168, 0.00161576758923792, 0.000296781651017147],
            [0.051475612951429, 0.254962643244162, 0.177968700389078, 0.0388193055934565, 0.0401405767924864, 0.0289756684918242, 0.024175958836987, 0.00161577903103607, 0.000306819921924983],
            [0.0560845051164861, 0.272491780498256, 0.188585736540012, 0.0408981344338818, 0.0423398048143654, 0.0276659606600468, 0.024175804372712, 0.00161577331013699, 0.000306027100661698],
            [0.0465040229362286, 0.229307935687941, 0.164386494358907, 0.0370985788142521, 0.036367108949374, 0.0290816162054764, 0.0239840941843056, 0.00162022130916673, 0.000316065371569534],
            [0.0506733283675929, 0.245171687041649, 0.174221927452897, 0.0390569455433338, 0.0383916235739944, 0.0271252427329803, 0.0240161712654114, 0.00162176023101753, 0.000278290751728045],
            [0.0485992378618254, 0.238829362457286, 0.169042512430083, 0.0376253270208933, 0.0374509804762877, 0.0291104461996163, 0.0240722646808282, 0.00162061319075327, 0.000316065371569534],
            [0.0529578907502787, 0.25527036110887, 0.179107464657716, 0.0396183202067304, 0.0395576472116052, 0.027377847601351, 0.0240962838755888, 0.00162176595191661, 0.000287536201372596],
            [0.0504731755623787, 0.248503981316688, 0.173745410408718, 0.0381498664837505, 0.0385504014068835, 0.0291439568426816, 0.0241605381535341, 0.00162100507233982, 0.000316065371569534],
            [0.0549985640543325, 0.265531188339435, 0.184042311721874, 0.0401777378459022, 0.0407400869691077, 0.0276387487268616, 0.0241764994619494, 0.00162177167281568, 0.000296781651017147],
            [0.052548317283351, 0.258486964502393, 0.178476242822417, 0.0386772876111452, 0.0397534721566703, 0.0291816976138702, 0.0242489146024233, 0.00162139695392636, 0.000316065371569534],
            [0.0572583978507726, 0.276118490117433, 0.189005619543812, 0.0407401694454027, 0.042031426900926, 0.027909890261714, 0.0242568180244935, 0.00162177739371475, 0.000306027100661698],
            [0.0476483350467426, 0.238039037412964, 0.168698780790594, 0.0372266978722641, 0.0384733151523161, 0.0292853295552516, 0.0241451689581728, 0.00162382070816721, 0.000325310821214085],
            [0.0519292444923474, 0.254267041271138, 0.178621140085558, 0.0391896327392561, 0.0407247320759941, 0.0276242436256312, 0.0241774005035535, 0.00162536535091709, 0.000288329022635881],
            [0.0494183168600045, 0.247470094000093, 0.173376973066579, 0.0377453567276152, 0.0395571866792298, 0.0293194828459795, 0.0242334424308787, 0.00162421258975376, 0.000325310821214085],
            [0.0538570587599265, 0.264267067015184, 0.183528974494516, 0.0397427264012436, 0.0418907557136049, 0.0278851447511418, 0.0242576160899142, 0.00162537107181616, 0.000297574472280432],
            [0.0514463612793532, 0.257399726941487, 0.17811789285557, 0.038272783575909, 0.0406410582061434, 0.0293571630709863, 0.0243218188797679, 0.0016246044713403, 0.000325310821214085],
            [0.0560658907411253, 0.274796935257157, 0.18850236540107, 0.0403051565705193, 0.0430567793512157, 0.0281562862859942, 0.0243379346524582, 0.00162537679271524, 0.000306819921924983],
            [0.0503787127919875, 0.252709196116425, 0.17606357663745, 0.0378657470893496, 0.0407689460444846, 0.0295190216080265, 0.0243147392671643, 0.00162602039386102, 0.000334556270858636],
            [0.0549132582980211, 0.26976477665324, 0.18629330506065, 0.0398704788449734, 0.0432879537316566, 0.0281383817788602, 0.0243389129261998, 0.00162717887592342, 0.000306819921924983],
            [0.0522394352156808, 0.262512889185613, 0.18079596012991, 0.0383864876368511, 0.0418528175713982, 0.0295581787784774, 0.0244031157160535, 0.00162641227544756, 0.000334556270858636],
            [0.0569401370841836, 0.280154334124534, 0.19125630466915, 0.0404257407277098, 0.0444539773692674, 0.0284095233137126, 0.0244192314887438, 0.0016271845968225, 0.000316065371569534],
            [0.0520210041379263, 0.267047033513599, 0.183376907991352, 0.0384575881623919, 0.0430645769366531, 0.029733230185523, 0.0244845155285224, 0.00162703585344658, 0.000343801720503187],
            [0.056705780453633, 0.284876445742707, 0.19390776118145, 0.0405017490695434, 0.0458511753873192, 0.0286710565985708, 0.0245006313012128, 0.00162780817482152, 0.000325310821214085],
        ]

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
                





