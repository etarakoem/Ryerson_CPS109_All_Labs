'''
    1. Minimize the ammount of remaining cash
    2. List the items to buy minimize remaining cash
    (buy 1 thing at a time.
    ex: minMaxShop(dict,6) --> return ["gobstoppers","gum],1
    return as tuple <[list thing u bought]>, <spare change>
    tip: using power set
'''

'''
    for i in range(x):
        for j in range(x-1):
            
'''
def powerset(s):
    power_set = [[]]
    for elem in s:
        for sub_set in power_set:
            # add a new subset consisting of the subset at hand added elem
            power_set = power_set + [list(sub_set) + [elem]]
    return power_set
def minCondition(num):
    result = 0
    while(num):
        if num > 0:
            result = num
    return result
def minMaxShop(dict, cash):
    # Make a list of key
    keylist = [dict[key] for key in dict]
    # Get the power set of all possibilities
    possible_result = powerset(keylist)
    # All the possible sum
    all_sum = [sum(i) for i in possible_result]
    # All the possible change if use to buy
    all_different = [cash - i for i in all_sum]
    # Find the position at which it has the least change
    position = all_different.index(min([cash-i for i in all_sum if cash-i>0]))
    # Print the result with the corresponding result
    result = [j for j in dict for i in possible_result[position] if dict[j]==i]
    # Get the change
    change = cash - all_sum[position]
    return result, "{:.2f}".format(change)

dict_sample = {
            "gobstoppers": 2,
            "milk way": 12,
            "gum":3,
            "coke":1,
            "candy":0.1,
            "juke":6.05
               }
print(minMaxShop(dict_sample,6.2))
