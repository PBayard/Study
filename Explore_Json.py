import json
import urllib.request

stagedata = urllib.request.urlopen("https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json")
print(type(stagedata))
data = json.load(stagedata)
# print(json.dumps(data, sort_keys=True, indent=4)) # Pretty print

print('type(data): ', end=''), print(type(data))
print('data.keys(): ', end=''), print(data.keys())
print('type(data[''members'']): ', end=''), print(type(data['members']))
print(data['members'])
print('type(data[''members''][0]): ', end=''), print(type(data['members'][0]))
print(data['members'][0])
print(data['members'][0].keys())
# etc... where [0] is row, ['column / header']
print(data['members'][0]['powers'][2])

print([test['powers'] for test in data['members']]) # return all tuples at that level
print([test['name'] for test in data['members']].index('Eternal Flame')) # find where is record
Etflame = data['members'][2] # stores the whole record
print(Etflame['age'])
print(Etflame['powers'][2]), print('\n')

# Rewrite data
members = data['members']
print(members)
member_from_name = dict([(member['name'], member) for member in members])
print(member_from_name)
print(member_from_name['Eternal Flame']['age'])