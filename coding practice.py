import cmath as np
a, b, c = (input('Enter coefficient a: ')), (input('Enter coefficient b: ')), (input('Enter coefficient c: '))
a, b, c = complex(a), complex(b), complex(c)
ans, ans2 = (-b-np.sqrt(b*b-4*a*c))/(2*a), (-b+np.sqrt(b*b-4*a*c))/(2*a)
print(ans), print(ans2)


