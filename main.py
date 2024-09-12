calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(i):
    count_calls()
    j = len(i)
    upp = i.upper()
    loww = i.lower()
    return (j, upp, loww)
def is_contains(i, list_):
    count_calls()
    iup = i.upper()
    list_upper = [item.upper() for item in list_]
    return iup in list_upper

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
