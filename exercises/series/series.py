def slices(series, length):

    if length > len(series) or 0 == length:
        raise ValueError("Meaningful message indicating the source of the error")

    series = list(map(int, series))

    return [ series[index:index+length] for index, val in enumerate(series) if index + length <= len(series) ]