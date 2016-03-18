
def maxElem(l: list):
    if l is None or len(l) == 0:
        return None
    return functools.reduce(lambda mx, x: x if x > mx else mx, l, l[0])