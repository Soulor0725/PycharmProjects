p = (4,5)
x,y = p
print(x,y)

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print(name, shares, price, date)


name, shares, price, (y,m,d) = data
print(name, shares, price, (y,m,d))


s = 'Hello' 
a, b, c, d, e = s
print(a, b, c, d, e)