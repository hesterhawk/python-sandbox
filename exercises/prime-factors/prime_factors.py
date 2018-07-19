def prime_factors(natural_number):
    result = []

    divider = 2
    while natural_number > 1:
        if (natural_number % divider) == 0:
            natural_number = natural_number / divider

            result.append(divider)
        else:
            divider += 1

    return result
