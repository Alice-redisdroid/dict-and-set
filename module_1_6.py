my_dict = {'Anya': 1, 'Curly': 5, 'Daiske': 2}
print(my_dict)
print(my_dict ['Anya'])
my_dict['Swansea'] = 3
print(my_dict['Swansea'])
my_dict.update({'Jimbo': 4, 'Polly': 999})
lost = my_dict.pop('Curly')
print(lost)
print(my_dict)

my_set = {4, 'Polly', 5.1, 7, 'Responsibility', 1, 4, 5.1,'Responsibility', 'Responsibility'}
print(my_set)
my_set.add('Safety')
my_set.add(5)
my_set.discard('Responsibility')
print(my_set)