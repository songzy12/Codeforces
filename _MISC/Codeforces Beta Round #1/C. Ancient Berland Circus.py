from math import degrees, acos, sin, radians

x0, y0 = map(float, raw_input().split())
x1, y1 = map(float, raw_input().split())
x2, y2 = map(float, raw_input().split())

a2, b2, c2 = (x1-x2)**2+(y1-y2)**2, \
             (x0-x2)**2+(y0-y2)**2, \
             (x1-x0)**2+(y1-y0)**2
R2 = 0
def alpha(a2, b2, c2):
    cosA2 = (b2+c2-a2)**2/(4.0*b2*c2)
    global R2
    R2 = a2/(4.0*(1-cosA2))
    degree = 2*degrees(acos(cosA2**0.5)) # geometry
    return degree

A, B, C = alpha(a2, b2, c2), alpha(b2, c2, a2), alpha(c2, a2, b2)
# print A, B, C
degrees = [360.0/(i+1) for i in range(100)]
degree, eps = 0, 10**(-4)
for x in degrees:
    # print x, A/x-round(A/x), B/x-round(B/x), C/x-round(C/x)
    if abs(A/x-round(A/x)) < eps and \
       abs(B/x-round(B/x)) < eps and \
       abs(C/x-round(C/x)) < eps:
        degree = x
        break
area = round(360.0/degree)*0.5*sin(radians(degree))*R2
print area
