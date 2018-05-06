record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name, email, *phone_numbers)


*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(*trailing, current)

list = [10, 8, 7, 1, 9, 5, 10, 3]
start,*mid, end = sorted(list)
print(*mid)



line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, fields, homedir, sh)
print(fields)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name,year)


items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(sorted(tail))