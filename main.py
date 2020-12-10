from HandEvaluator import HoldemHand
import numpy

#print(HoldemHand.ValidateHand("As Ks"))
#print(HoldemHand.ValidateHand("2d 3c", "Ad 5d 4c"))
mask = HoldemHand.ParseHand("As Ks Ts Js Qs")
print(mask)
description = HoldemHand.DescriptionFromMask(mask[0])
print(description)
print(HoldemHand.EvaluateType(mask[0]))

mask = HoldemHand.ParseHand("As Ks Ts Js 9s")
print(mask)
description = HoldemHand.DescriptionFromMask(mask[0])
print(description)
print(HoldemHand.EvaluateType(mask[0]))


handValue = HoldemHand.Evaluate("As Ks Ts Js Qs")
print(handValue)

handValue = HoldemHand.Evaluate("As Ks Ts Js 9s")
print(handValue)

print(HoldemHand.DescriptionFromHand("Jd Qd"))

hand = HoldemHand("3s 3c", "Ad Th 7s")
print(hand.ToString())
print(hand.HandTypeDescription())
print(hand.Description())
print(hand.HandValue())


for s in HoldemHand.Cards(mask[0]):
    print(s)

print(HoldemHand.MaskToString(mask[0]))

board = "2h 3d 4c"
player1 = HoldemHand("AsKs", board)
player2 = HoldemHand("AcKh", board)

print(player1 == player2)
print("Player1: " + player1.Description())
print(player1.HandValue())
print("Player2: " + player2.Description())
print(player2.HandValue())


board = "Qs Jh 7c"
pocket = "QdQh"
handValue = HoldemHand.Evaluate(pocket + board)
print(handValue)
print(HoldemHand.DescriptionFromHand(pocket + board))


player1 = HoldemHand("QdQh", board)
player2 = HoldemHand("JdJs", board)
print("Player1: " + player1.Description())
print(player1.HandValue())
print("Player2: " + player2.Description())
print(player2.HandValue())

mask = HoldemHand.ParseHand("AsAc")
pocketAA = HoldemHand.PocketHand169Type(mask[0])

print(pocketAA.value)

hands = HoldemHand.Hands(2)
x = []
for hand in hands:
    x.append(hand)
print(len(x))

hands = HoldemHand.Hands(3, 0, 5)
y = []
for hand in hands:
    y.append(hand)
print(len(y))


hand = HoldemHand.RandomHand(0, 2)
print(hand)
print(HoldemHand.DescriptionFromMask(hand))
print(HoldemHand.MaskToString(hand))
print(HoldemHand.PocketHand169Type(hand))

# generat random hands within 1 second
randomHands = HoldemHand.RandomHand(5, 1.0)
for hand in randomHands:
    print(HoldemHand.DescriptionFromMask(hand) + " " + HoldemHand.MaskToString(hand))

# handValue = HoldemHand.Evaluate(mask[0], 5)
# print(handValue)

# mask = HoldemHand.ParseHand("As Ks Js Qs 9s")
# handValue = HoldemHand.Evaluate(mask[0], 5)
# print(handValue)