#Write Python code to create a function called most_frequent that takes a string . Use dictionaries.

def most_frequent(s):
    d = dict()
    for key in s:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
print (most_frequent('Mississippi'))
