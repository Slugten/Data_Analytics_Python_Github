# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    return f'Hello, {name}!'

def add(a, b, c):
    return a + b + c

def positive(x):
    return x > 0

def negative(y):
    return y < 0
    

print(greet('Bob'))

add_abc = add(5,3,2)
print(add_abc)

result = positive(0)
result1 = positive(50)
result3 = positive(-50)
print(result)
print(result1)
print(result3)

result4 = negative(50)
result5 = negative(-50)
result6 = negative(0)
print(result4)
print(result5)
print(result6)