calls = 0
def count_calls():
    global calls
    if calls == 0 or calls > 0:
        calls += 1
    return calls
def string_info(info = str()):
    count_calls()
    info = [len(info), info.upper(), info.lower()]
    my_info = tuple(info)
    return my_info
def is_contains(string = str(), list_to_search = list(str())):
    count_calls()
    lower_list = [item.lower() for item in list_to_search]
    string = string.lower()
    return string in lower_list
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
