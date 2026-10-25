#Logical Operator

#AND(All Operations are True Then True)
print(123>100 and 34==34)
print(123>100 and 34==34 and 45<67) #True
print(123>100 and 34==34 and 45>67) #False

#OR(Any One Operation is True Then True)
print(123>100 or 34==34)
print(123>100 or 34==34 or 45<67) #True
print(123>100 or 34==34 or 45>67) #True
print(100>200 or 34!=34 or 45>67) #False

#NOT(Reverse the Result, IF False Then True, If True Then False)
print(not 123>100) #False
print(not 100>200) #True


