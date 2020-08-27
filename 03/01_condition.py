# if ~ else

a = 2
if a > 5:
    print('big')
else:
    print('small')


# if ~ elif ~ else
n = -1000
if n > 0:
    print('양수')
elif n == 0:
    print('0')
else:
    print('음수')

price = 0
order = 'nuddle'

if order == 'spam':
    price = 1000
elif order == 'egg':
    price = 200
elif order == 'spacetti':
    price = 2000
else:
    price = 0

print('order: %s, price: %d' % (order, price))
