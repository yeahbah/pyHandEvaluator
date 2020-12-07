from HandEvaluator import HoldemHand

#print(HoldemHand.ValidateHand("As Ks"))
#print(HoldemHand.ValidateHand("2d 3c", "Ad 5d 4c"))

mask = HoldemHand.ParseHand("As Ks", "Js Qs Ts")
print(mask)

#print(HoldemHand.DescriptionFromHandValueInternal(mask))

card = HoldemHand.ParseCard("Ac") 
print(card)
print(HoldemHand.CardRank(card))



