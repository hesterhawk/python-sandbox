letters = {
    1: ('a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'),
    2: ('d','g'),
    3: ('b','c','m','p'),
    4: ('f','h','v','w','y'),
    5: ('k'),
    8: ('j','x'),
    10: ('q','z')
}

def score(word):
    return sum([
        score for letter in list(word) 
            for score,data in letters.items() 
                if letter.lower() in data
    ])
