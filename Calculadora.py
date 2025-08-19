print('Current Principal:')
current = float(input())

print('Annual Adittion:')
years = float(input())

print('Interest Rate:')
interesRate = float(input())

total = current 
for i in range(years):
    total = total + 1000
    total = total +(interesRate * total /100)

    print('Result: ' + total)
