from HandEvaluator import HoldemHand
import numpy

#print(HoldemHand.ValidateHand("As Ks"))
#print(HoldemHand.ValidateHand("2d 3c", "Ad 5d 4c"))
mask = HoldemHand.ParseHand("As Ks Ts Js Qs")
print(mask)
description = HoldemHand.DescriptionFromMask(mask[0])
print(description)

mask = HoldemHand.ParseHand("As Ks Ts Js 9s")
print(mask)
description = HoldemHand.DescriptionFromMask(mask[0])
print(description)


handValue = HoldemHand.Evaluate("As Ks Ts Js Qs")
print(handValue)

handValue = HoldemHand.Evaluate("As Ks Ts Js 9s")
print(handValue)

# handValue = HoldemHand.Evaluate(mask[0], 5)
# print(handValue)

# mask = HoldemHand.ParseHand("As Ks Js Qs 9s")
# handValue = HoldemHand.Evaluate(mask[0], 5)
# print(handValue)



# class TestClass:
#     rankTable = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace",
#                     "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace",
#                     "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace",
#                     "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

# testClass = TestClass()
# print(testClass.rankTable[numpy.uint32(12)])


#print(HoldemHand.DescriptionFromHandValueInternal(mask))

# card = HoldemHand.ParseHand("2") 
# print(card)
#print(HoldemHand.CardRank(card))

# x = 1 << 1
# x |= 1 << 2
# print(x)


# something = mask[0] & 0x1FFF
# print(something)


# 0001
# 1 << 1
# result = 0010

# 0010 | 1 << 2
# result = 0110
