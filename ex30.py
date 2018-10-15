people = 30
cars = 40
buese = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buese > cars:
    print "That's too many buese."
elif buese < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buese:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

