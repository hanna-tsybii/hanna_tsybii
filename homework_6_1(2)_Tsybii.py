def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return x + (5 - x % 5)


cases = [
    # expected, input
    [5, 5],
    [15, 13],
    [0, 0],
    [0, -1],
    [-15, -16]
]

for i in cases:
    expected, inp = i
    res = closest_mod_5(inp)
    assert expected == res, 'Fail. Expected: {}\nActual: {}'.format(expected, res)
