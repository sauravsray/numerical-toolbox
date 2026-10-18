def f(x):
    return x**2 - 2

#def bisection(a, b, tol=1e-8):
#    # Implementation will come later
#    pass

def bisection(f, a, b, tol=1e-8):
    while b - a > tol:
        m = (a + b) / 2

        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m

    return (a + b) / 2
