n, d, r = map(int, input().split(' '))
if n == 1:
    print(2*d + 2*r)
elif n == 2:
    print(d*4 + 2*r + 2*(r - d))
else:
    side_ring = d + r + (r - d)
    ring = 2*d + 2*r
    print(2*side_ring + (n - 2)*ring)

