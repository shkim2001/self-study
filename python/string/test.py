# Given an incoming stream of characters containing values like $300 and £400, write a function that takes symbol and data stream and returns array of values.

# Example getValues("$", "abc $300 £400 $30 abvv cvc") returns [300, 30]
# getValues("£", "abc $300 £400 $30 abvv cvc") returns [400]

# Follow up : How will you handle tokens like $$300 and $200$300. Incoming data is a stream and you have no ability to peek next value.

def getValues(symbol, data):
    data = data.split()
    res = []

    for item in data:
        if symbol in item:
            temp = item.split(symbol)
            res += temp
    
    while "" in res:
        res.remove("")
    
    return res

print(getValues("$", "abc $$300 £400 $30 abvv cvc"))
print(getValues("$", "abc $200$300 £400 $30 abvv cvc"))
