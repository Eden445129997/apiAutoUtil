import collections

import re

class case(object):

    def __init__(self):
        self.id = 1



class suit(object):
    def __init__(self):
        self._suit = collections.deque()

    def __len__(self):
        return len(self._suit)

    def __getitem__(self, position):
        return self._suit[position]

    def append(self, case):
        self._suit.append(case)


first = case()

print(first.__dict__)

a = "aaaa"
b = "aaaa"

print(a>b)

test = re.findall('/^\d*\*[^\d]*[\w]{6}$/','123*ABCabcd-89')

print(test)