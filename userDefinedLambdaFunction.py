def A(x):
    return (lambda y:x+y)

t = A(4)(5)
print(t)

u = A(4)
print(u(5))