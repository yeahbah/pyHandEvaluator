from inspect import Parameter
from HandEvaluator import Hand
from HandAnalysis import HandAnalysis
import numpy as np

#print(HoldemHand.ValidateHand("As Ks"))
#print(HoldemHand.ValidateHand("2d 3c", "Ad 5d 4c"))
mask = Hand.ParseHand("As Ks Ts Js Qs")
print(mask)
description = Hand.DescriptionFromMask(mask[0])
print(description)
print(Hand.EvaluateType(mask[0]))

mask = Hand.ParseHand("As Ks Ts Js 9s")
print(mask)
description = Hand.DescriptionFromMask(mask[0])
print(description)
print(Hand.EvaluateType(mask[0]))


handValue = Hand.Evaluate("As Ks Ts Js Qs")
print(handValue)

handValue = Hand.Evaluate("As Ks Ts Js 9s")
print(handValue)

print(Hand.DescriptionFromHand("Jd Qd"))

hand = Hand("3s 3c", "Ad Th 7s")
print(hand.ToString())
print(hand.HandTypeDescription())
print(hand.Description())
print(hand.HandValue())


for s in Hand.Cards(mask[0]):
    print(s)

print(Hand.MaskToString(mask[0]))

board = "2h 3d 4c"
player1 = Hand("AsKs", board)
player2 = Hand("AcKh", board)

print(player1 == player2)
print("Player1: " + player1.Description())
print(player1.HandValue())
print("Player2: " + player2.Description())
print(player2.HandValue())


board = "Qs Jh 7c"
pocket = "QdQh"
handValue = Hand.Evaluate(pocket + board)
print(handValue)
print(Hand.DescriptionFromHand(pocket + board))


player1 = Hand("QdQh", board)
player2 = Hand("JdJs", board)
print("Player1: " + player1.Description())
print(player1.HandValue())
print("Player2: " + player2.Description())
print(player2.HandValue())

mask = Hand.ParseHand("AsAc")
pocketAA = Hand.PocketHand169Type(mask[0])

print(pocketAA.value)

hands = Hand.Hands(2)
x = []
for hand in hands:
    x.append(hand)
print(len(x))

hands = Hand.Hands(Hand.ParseHand("5s 6c 7s")[0], np.uint64(0), 5)
y = []
for hand in hands:
    y.append(hand)
print(len(y))


hand = Hand.RandomHand(np.uint64(0), 2)
print(hand)
print(Hand.DescriptionFromMask(hand))
print(Hand.MaskToString(hand))
print(Hand.PocketHand169Type(hand))

# generate random hands within 1 second
# randomHands = HoldemHand.RandomHand(5, 1.0)
# for hand in randomHands:
#     print(HoldemHand.DescriptionFromMask(hand) + " " + HoldemHand.MaskToString(hand))

hand = Hand.ParseHand("QsTs")
board = Hand.ParseHand("Ks Js 2c")
handStrength = HandAnalysis.HandStrength(hand[0], board[0])
print(handStrength)
print(HandAnalysis.StraightDrawCount(Hand.ParseHand("AsKsQsTs")[0], np.uint64(0)))

# strength vs 9 opponents
handStrength = HandAnalysis.HandStrength(hand[0], board[0], 9, 1.0)
print(handStrength)

# opponent = HoldemHand.ParseHand("Js Jc")
print(HandAnalysis.StraightDrawCount(hand[0], board[0], np.uint64(0)))

print(HandAnalysis.CountContiguous(hand[0], board[0]))

pocket = Hand.ParseHand("As Ks")[0]
board = Hand.ParseHand("Qs Ts 2c")[0]
# expected distance is 46
print(HandAnalysis.HandDistance(pocket, board))

# the nuts, expected distance is 0
board = Hand.ParseHand("Qs Ts 2c Js")[0]
print(HandAnalysis.HandDistance(pocket, board))

pocket = Hand.ParseHand("Qs Js")[0]
board = Hand.ParseHand("9c Ts 7d 3c")[0]
opponents = []
outs = HandAnalysis.OutsMaskDiscounted(pocket, board, opponents)

# should print out Ks 8s Kh 8h Kd 8d
print(Hand.MaskToString(outs))

pocket = Hand.ParseHand("Qs Js")[0]
board = Hand.ParseHand("9c Ts 7d")[0]
opponents = []
outs = HandAnalysis.OutsMaskDiscounted(pocket, board, opponents)

pocket = Hand.ParseHand("As Ks")[0]
board = Hand.ParseHand("2s 3s 5c 6d")[0]
opponents = [Hand.ParseHand("5s 6c")[0]]

# 6s murders our hero
print(HandAnalysis.Outs(pocket, board, opponents))
cards =  HandAnalysis.OutCards("As Ks", "2s 3s 5c 6d", ["5s 6c"])
print(cards)

board = Hand.ParseHand("2s 3s 5c")[0]
print(HandAnalysis.OutsEx(pocket, board, np.uint64(0)))

mask = HandAnalysis.OutsMaskEx(pocket, board, np.uint64(0))
print(Hand.MaskToString(mask))

ourCards = [Hand.ParseHand("Ad Kd")[0]]
oppCards = [Hand.ParseHand("Jc Jh")[0]]
board = Hand.ParseHand("Jd Qd 2c")[0]
result = HandAnalysis.HandWinOdds(ourCards, oppCards, board)
print("Player odds: " + str(result[0]))
print("Opponent odds: " + str(result[1]))
print("Is approximate: " + str(result[2]))

# versus random opponent - no board
result = HandAnalysis.HandWinOdds(Hand.ParseHand("As Ks")[0], np.uint64(0))
print("Player Odds: " + str(result[0]))
print("Opponent Odds: " + str(result[1]))

# versus random opponent with board
# result = HandAnalysis.HandWinOdds(Hand.ParseHand("As Ks")[0], board)
# print("Player Odds: " + str(result[0]))
# print("Opponent Odds: " + str(result[1]))

# versus specific number of opponents and duration
result = HandAnalysis.HandWinOdds(Hand.ParseHand("QsQc")[0], board, 6, 0.5)
print("Player Odds: " + str(result[0]))
print("Opponent Odds: " + str(result[1]))

result = HandAnalysis.HandWinOdds(["As Ks", "QcQh"], "2s 3c 5d", "7h 7d")
print(result)

result = HandAnalysis.HandPotential(Hand.ParseHand("As Ks")[0], board, 6, 0.5)
print(result)

result = HandAnalysis.WinOdds("As Ks", "2s 3c 5d", np.uint64(0), 6)
print(result)

hand = Hand.ParseHand("2c")[0]
print(hand)

outs = HandAnalysis.Outs(Hand.ParseHand("As Kd")[0], Hand.ParseHand("2s 3s 4s")[0], [Hand.ParseHand("6s 5d")[0]])
print(outs)

pocket = Hand.ParseHand("Qs Js")[0]
board = Hand.ParseHand("9c Ts 7d 3c")[0]
opponents = [Hand.ParseHand("8s 9s")[0], Hand.ParseHand("Ac Kc")[0]]
outs = HandAnalysis.OutsMaskDiscounted(pocket, board, opponents)
print(outs)
expected = "Ks Kh Qh 8h Kd Qd 8d"
print(Hand.MaskToString(outs))

pocket = Hand.ParseHand("As Ks")[0]
board = Hand.ParseHand("2s 3s 4d")[0]
opponents = [Hand.ParseHand("2d 6c")[0]]
outs = HandAnalysis.Outs(pocket, board, opponents)
print(outs)


pocket = "As Ks"
board = "2s 3s 5c 6d"
opponents = [Hand.ParseHand("5s 6c")[0]]
expectedOuts = 7 # because 6s does not improve our heroe's hand
print(HandAnalysis.Outs(Hand.ParseHand(pocket)[0], Hand.ParseHand(board)[0], opponents))
expectedOuts = "Qs Js Ts 9s 8s 7s 4s"
print(HandAnalysis.OutCards(pocket, board, ["5s 6c"]))

opponents = [Hand.ParseHand("6s 7s")[0]]
expectedOuts = 15 # opponent out is not discounted
print(HandAnalysis.Outs(Hand.ParseHand(pocket)[0], Hand.ParseHand(board)[0], opponents))


board = "2d Kh Qh 3h Qc"
h1 = Hand("Ad Kd", board)
h2 = Hand("2h 3d", board)

print(h1 > h2)
print(h1 >= h2)
print(h2 <= h1)
print(h2 < h1)
print(h1 != h2)

# handValue = HoldemHand.Evaluate(mask[0], 5)
# print(handValue)

# mask = HoldemHand.ParseHand("As Ks Js Qs 9s")
# handValue = HoldemHand.Evaluate(mask[0], 5)
# print(handValue)