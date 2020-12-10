from HandEvaluator import HoldemHand

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