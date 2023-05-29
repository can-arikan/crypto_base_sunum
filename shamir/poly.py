def evaluate(poly, x) -> int:
    summation = 0
    for degree in range(len(poly)):
        value = poly[degree] * pow(x, degree)
        summation += value
    return summation