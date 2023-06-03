# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1
leek_price = 2      #create leek price

print('Leek is ' + str(leek_price) + ' euro per kilo.')       # 2. Cast into string and use +- indicator

# Part 2

amount_leeks = 'leek 4'     #amount of leeks stored as a string
leeks = amount_leeks[amount_leeks.find(" ") + 1:]       #zoekt naar de spatie en begint "capture" bij de eerste letter na de spatie t/m het einde
#print(int(leeks))           #print de uitkomst van "leeks" als een integer

sum_total =  int(leeks) * leek_price    #maakt van "leeks" een integer en vermenigvuldigd dit met de prijs
print(sum_total)                        #berekent de totale prijs

# Part 3
broccoli_price = 2.34
order = 'broccoli 1.6'
order_amount = float(order[order.find(" ") + 1:])
sum_order = round(broccoli_price * order_amount, 2)

print(str(order_amount) + 'kg broccoli costs ' + str(sum_order) + 'e')