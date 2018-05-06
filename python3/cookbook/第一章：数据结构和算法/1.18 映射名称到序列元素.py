from collections import namedtuple
Subscriber = namedtuple('Subscriber',['addr','joined'])
sub = Subscriber('json@yahu.com','2018-05-02')
print(sub)
print(sub.addr,sub.joined)


from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

s = Stock('ACME', 100, 123.45)
print(s.shares)
s = s._replace(shares=75)
print(s)


from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)
def dict_to_stocks(s):
    return stock_prototype._replace(**s)

a = {'name':'jack','shares':100,'price':123.5}    
print(dict_to_stocks(a))
