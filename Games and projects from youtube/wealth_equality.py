def redistriuce_wealth(wealth):
    amount = len(wealth)
    single_wealth = float(sum(wealth)/amount)
    wealth = []
    i=0
    while i < amount:
        wealth.append(single_wealth)
        i +=1
    print(wealth)


redistriuce_wealth([5,5,5,5,5])
redistriuce_wealth([0,10])
redistriuce_wealth([2,2,3])