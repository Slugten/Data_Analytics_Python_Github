# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10

discount_percentage = 30

sum_one_each = broccoli + leek + potato + brussel_sprout
avg_price = (broccoli + leek + potato + brussel_sprout)/4
sum_total = (num_broccolis * broccoli) + (num_brussel_sprouts * brussel_sprout) + (num_potatoes * potato) + (num_leeks * leek)
discounted_sum_total = sum_total - (sum_total / 100 * discount_percentage)

print(sum_one_each)
print(avg_price)
print(sum_total)
print(discounted_sum_total)