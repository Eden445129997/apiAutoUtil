#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

# 元祖容器的基本使用
# Person = collections.namedtuple('Person', ['age', 'height', 'name'])
# tom = Person(30, 178, 'Tom')

# print(tom)
# >>> Person(age=30, height=178, name='Tom')

# print(tom.name)
# >>> Tom

# print(tom.age)
# >>> 30

# 总结：使用容器，好处是在可以使用属性而不是索引的方式获取元祖中的元素

# 创建元组容器
Card = collections.namedtuple('Card', ['rank', 'suit'])


# python编程风格的纸牌类
class FrenchDeck:
    # 等级（A 2 3 4 5 6 7 8 9 10 J Q K）
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 套件（黑桃 方块 梅花 红心）
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


print(Card)
# >>> <class '__main__.Card'>

beer_card = Card('7', 'diamods')
print(beer_card)
# >>> Card(rank='7', suit='diamods')


deck = FrenchDeck()
# 52
print(len(deck))
for i in deck:
    print(i)