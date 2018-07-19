from functools import reduce

def largest_product(series, size):

    if 0 == size: return 1
    if "" == series: raise ValueError("Value Error!")
    if len(''.join(filter(str.isdigit, series))) != len(series): raise ValueError("Value Error!")

    data = []
    series = list(series)

    for x,y in enumerate(series):
        if len(series[x:x+size]) == size:        
            result = list(map(int, series[x:x+size]))
            data.append( reduce(lambda x, y: x*y, result) )
            
    return max(data)