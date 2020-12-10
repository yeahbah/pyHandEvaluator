from HandEvaluator import HoldemHand
from multipledispatch import dispatch

class HandAnalysis:
    DEFAULT_TIME_DURATION = 0.25

    # The classic HandStrength Calculation from page 21 of Aaron Davidson's
    # Masters Thesis
    # pocket - Pocket cards
    # board - Current board
    # returns hand strength as a percentage of hands won
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

        
