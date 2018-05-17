
# GITHUB!! :)

song = [
    "{} bottle{} of beer on the wall, {} bottle{} of beer.",
    "Take {} down and pass it around, {} bottle{} of beer on the wall."
]

nomore = [
    "No more bottles of beer on the wall, no more bottles of beer.",
    "Go to the store and buy some more, 99 bottles of beer on the wall."
]

def recite(start, take=1):
    result = []

    for item in range(take):        
        result += _getRow(start)
        start = _calculateStart(start)
    
    return result[1:]

def _calculateStart(start):
    return start - 1 if start - 1 >= 0 else 99

def _getRow(start):
    
    if start > 2:
        return [
            "",
            song[0].format(start, 's', start, 's'),
            song[1].format('one', start - 1, 's')
        ]
    elif 2 == start:
        return [
            "",
            song[0].format(start, 's', start, 's'),
            song[1].format('one', 1, '')
        ]
    elif 1 == start:
        return [
            "",
            song[0].format(1, '', 1, ''),
            song[1].format('it', 'no more', 's')
        ]        
    elif 0 == start:
        return ["",nomore[0], nomore[1]]