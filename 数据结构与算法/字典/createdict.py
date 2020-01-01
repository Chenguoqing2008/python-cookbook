#! /usr/bin/python


empty_dict = dict()
print(empty_dict)

empty_dict['one'] = 'hello'
print(empty_dict)

# create dict from **args
map_dict = dict(one='test', two='test2', three='test3')
print(map_dict)

# create dict from zip
map_zip = dict(zip(['one', 'two', 'three'], ['test', 'test2', 'test3']))
print(map_zip)

# create map from tuple
map_tuple = dict([('one', 'test'), ('two', 'test2'), ('three', 'test3')])
print(map_tuple)

# create dict from map
dict_map = dict({'one': 'test', 'two': 'test2', 'three': 'test3'})
print(dict_map)

print(map_dict == map_zip == map_tuple == dict_map)
