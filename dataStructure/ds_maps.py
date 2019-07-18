import collections

dict1 = {
    'day1' : 'Mon',
    'day2' : 'Tue'
}

dict2 = {
    'day3' : 'Wed',
    'day4' : 'Thu'
}

res = collections.ChainMap(dict1, dict2)

#gabung jadi 1 dict

print(res.maps, "\n")

print('keys = {}'.format(list(res.keys())))
print('values = {}'.format(list(res.values())))
print()

#print semua element
print("element: ")
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

#print spesifik value
print('day3 in res: {}'.format(('day1' in res)))
print('day4 in res. {}'.format(('day5' in res)))

res2 = collections.ChainMap(dict2,dict1)
print(res2)

#update maps
dict1['day1'] = 'Sun'
print(res.maps,'\n')