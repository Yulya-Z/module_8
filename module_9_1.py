def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results.update({function.__name__: function(int_list)})
    return results

def min(int_list):
    i = 0
    for i in range(len(int_list) - 1):
        if int_list[i] < int_list[i + 1]:
            result = int_list[i]
    return result

def max(int_list):
    i = 0
    for i in range(len(int_list) - 1):
        if int_list[i] > int_list[i + 1]:
            result = int_list[i]
    return result

def len_(int_list):
    result = len(int_list)
    return result

def sum(int_list):
    result = 0
    for i in int_list:
        result += i
    return result

def sorted_(int_list):
    result = sorted(int_list)
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))