def verify(isbn):
    isbn = list(''.join([s for s in isbn if s.isdigit() or s == 'X']))

    if len(isbn) == 0: return False
    if isbn[-1] == 'X': isbn[-1] = 10
    if isbn.count('X') > 0: return False

    result = 0
    for counter,item in enumerate(isbn):

        item = 10 if 'X' == item else item

        result += int(item) * (len(isbn) - counter)

    return True if 0 == (result % 11) else False