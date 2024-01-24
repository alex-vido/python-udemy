class MyList:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, value):
        self.__items.append(value)

    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, value):
        if index >= len(self.__items):
            self.__items.append(value)

        self.__items[index] = value

    def __delitem__(self, index):
        del self.__items[index]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.__items})'

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    li = MyList()
    li.add('Alex')
    li.add('Kelly')

    # li = list(li)

    for value in li:
        print(value)

print(li[0])

li[0] = 'Yuri'
print(li[0])
li[2] = 'Guilherme'
print(li[2])

del li[2]
print(li)
