from inspect import Parameter
from HandEvaluator import Hand
from HandAnalysis import HandAnalysis
import numpy

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

hands = Hand.Hands(3, 0, 5)
y = []
for hand in hands:
    y.append(hand)
print(len(y))


hand = Hand.RandomHand(0, 2)
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
print(HandAnalysis.StraightDrawCount(Hand.ParseHand("AsKsQsTs")[0], 0))

# strength vs 9 opponents
handStrength = HandAnalysis.HandStrength(hand[0], board[0], 9, 1.0)
print(handStrength)

# opponent = HoldemHand.ParseHand("Js Jc")
print(HandAnalysis.StraightDrawCount(hand[0], board[0], 0))

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

pocket = Hand.ParseHand("As Ks")[0]
board = Hand.ParseHand("2s 3s 5c 6d")[0]
opponents = [Hand.ParseHand("5s 6c")[0]]

# 6s murders our hero
print(HandAnalysis.Outs(pocket, board, opponents))
cards =  HandAnalysis.OutCards("As Ks", "2s 3s 5c 6d", ["5s 6c"])
print(cards)

board = Hand.ParseHand("2s 3s 5c")[0]
print(HandAnalysis.OutsEx(pocket, board, 0))

mask = HandAnalysis.OutsMaskEx(pocket, board, 0)
print(Hand.MaskToString(mask))


# handValue = HoldemHand.Evaluate(mask[0], 5)
# print(handValue)

# mask = HoldemHand.ParseHand("As Ks Js Qs 9s")
# handValue = HoldemHand.Evaluate(mask[0], 5)
# print(handValue)