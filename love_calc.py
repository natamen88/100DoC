def calculate_love_score(name1, name2):
    both_names=name1+name2
    #print(both_names)

    t=0
    r=0
    u=0
    e=0

    for letter in both_names:
        if letter == "t":
            t += 1
        elif letter == "r":
            r += 1
        elif letter == "u":
            u += 1
        elif letter == "e":
            e += 1

    true_total = t+r+u+e
    
    l=0
    o=0
    v=0
    e=0

    for letter in both_names:
        if letter == "l":
            l += 1
        elif letter == "o":
            o += 1
        elif letter == "v":
            v += 1
        elif letter == "e":
            e += 1

    love_total = l+o+v+e

    final_score = (str(true_total)+str(love_total))
    print(int(final_score))

calculate_love_score("Nataniel", "Natalia")


