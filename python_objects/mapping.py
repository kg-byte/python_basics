# Name Mangling

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
    
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    # _Mapping__update
    __update = update

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.item_list.append(item)

    def print_something(self):
        print('something')
    
    # _MappingSubclass__update
    __update = print_something
