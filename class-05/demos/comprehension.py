studs = ['tammy','raven','alex']

def capitalize(lst):
    # return [each item capitalized]
    # caps = []
    # for item in lst:
    #     caps.append(item.upper())



    return [ item.upper() for item in lst if len(item) > 4 ]

assert capitalize(studs) == ['TAMMY','RAVEN']

print('############ passed')

print(capitalize(studs))