"""
Module to calculate cube root using Newton's Method
"""
def cube_root(x, debug=False):
    from numpy import nan
    if x == 0:
        return 0
    elif x < 0:
        return nan
    s = 1.0
    kmax = 100
    tol = 1.0e-14
    for k in range(kmax):
        if debug:
            print(f"At iteration {k} the value of s={s:20.15f}")
        s0 = s
        s = (2 * s + x / (s ** 2)) / 3
        delta_s = s - s0
        if abs(delta_s / x) < tol:
            break
    if debug:
        print(f"Finally, the value of s={s:20.15f}")
    return s
