# class Human(object):
#     species = 'this_is_species'
#     def __init__(self, name):
#         self.name = name

#     def say(self, msg):
#         return '{name}: {message}'.format(name = self.name, message = msg)

#     @classmethod
#     def get_species(cls):
#         return cls.species

#     @staticmethod
#     def grunt(info):
#         return info

# i = Human(name = 'barara')
# j = Human(name = 'gupbpb')

# Human.species = 'other'
# print(i.say('infooooo'))
# print(j.get_species())

test_dic = { 'a': 1, 'b': 2, 'c': 3 }
test_dic2 = { 'a': 9, 'b': 8, 'c': 7 }

SELECTED_NAME = 'test_dic'

print(SELECTED_NAME.get('a'))