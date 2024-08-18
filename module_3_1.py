
def count_calls():
    global calls
    calls += 1

def string_info(str1):
    list = [len(str1), str1.upper(), str1.lower()]
    list = tuple(list)
    count_calls()
    return list

def is_contains(string, list_to_search):
    count_calls()
    check = False
    for i in range(0, len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            check = True
    return check

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)