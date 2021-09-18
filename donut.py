from math import sin, cos
from numpy import arange, asarray, ubyte, single
A, B = 0., 0.
z = asarray([0 for _ in range(1760)], dtype=single)
b = asarray([32 for _ in range(1760)], dtype=ubyte)
print("\x1b[2J", end='')
while True:
    b.fill(32)
    z.fill(0)
    for j in arange(0., 6.28, 0.07):
        for i in arange(0., 6.28, 0.02):
            c, d, e, f, g = sin(i), cos(j), sin(A), sin(j), cos(A)
            l, m, n = cos(i), cos(B), sin(B)
            h = d + 2.
            D = 1. / (c * h * e + f * g + 5.)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x+80*y)
            N = int(8 * ((f * e - c * d * g) * m -
                    c * d * e - f * g - l * d * n))
            if 0 < y < 22 and 0 < x < 80 and z[o] < D:
                z[o] = D
                b[o] = ord('.,-~:;=!*#$@'[N if N > 0 else 0])
    print("\x1b[H", end='')
    for k in range(1761):
        print('%c' % (b[k] if k % 80 else 10), end='')
        A += 0.00004
        B += 0.00002
