"""def nb_year(p0, percent, aug, p):
        population_sum=p0
        year=0
        while population_sum < p:
            population_sum = population_sum * (1 + (percent/100)) + aug
            year += 1
        print(year)

nb_year(1500, 5, 100,5000)
nb_year(1500000, 2.5, 10000, 2000000)
nb_year(1500000,0.25,1000,2000000)

def alternate(n, first_value, second_value):
    array_n =[]
    i=1
    while i<= n:
        if i % 2 == 0:
            array_n.append(second_value)
        else:
            array_n.append(first_value)
        i += 1
    return array_n

print(alternate(5,True, False))


def robber_encode(sentence):
    consonants_upper = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X",
                        "Y", "Z"]
    consonants_lower= []
    position = 0
    sentence_robber =""
    for consonant_lower in consonants_upper:
        consonants_lower.append(consonant_lower.lower())
    for letter in sentence:
        if letter in consonants_upper and letter.isupper():
            sentence_robber = sentence_robber + letter + "O" + letter
        elif letter in consonants_lower and letter.islower():
            sentence_robber = sentence_robber + letter + "o" + letter
        else:
            sentence_robber = sentence_robber + letter
        sencence_robber = sentence_robber + letter
    return sentence_robber

x = robber_encode("coDing is Fun")
print (x)
"cocododinongog isos fofunon"
"""
def evens_and_odds(n):
    if n % 2:
        return(hex(n).replace("0x",""))
    else:
     # even - bin
        return( format(n, "b"))

evens_and_odds(8172381723)
