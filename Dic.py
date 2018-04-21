birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
        print('_________________________')
        print('Values')
        for v in birthdays.values():
            print(v)
        print('_________________________')
        print('Keys')
        for k in birthdays.keys():
            print(k)
        print('_________________________')
        print('Items')
        for i in birthdays.items():
            print(i)
        print('_________________________')
        print('Multiple assignment trick')
        for k, v in birthdays.items(): # multiple assignment trick
            print('Key: ' + k + ' Value: ' + str(v))
