dict = {
    'Name': 'Reky Rolen Kencana',
    'Age': '23',
    'Class': 'Ipa 3'
}

print('Print the dictionary: ')
print(dict)

#update value dictionary
dict['Class'] = '12 Ipa 3'
print("\nPrint dict with key Class that updated to 12 Ipa 3 from Ipa 3")
print(dict['Class'])

#delete dict
del dict['Age'] #delete entry with key 'Age'
dict.clear() #clear the dict
del dict #delete the dictionary

print(dict)
print("Value in key 'Name", dict['Name'])
print("Value in key 'Age'", dict['Age'])