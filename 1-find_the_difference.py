import collections
import operator
from functools import reduce

"""
问题描述：
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.
"""
s = "abcd"
t = "abecd"

# solution1:
# collections就是将元素t转换为collections，就是每种元素只有一个，因此相减得到的就是不一样的元素，因为结果只有一个，
# 因此下标是0的就是所要求的
print("The solution1 is:" + list((collections.Counter(t) - collections.Counter(s)))[0])

# solution2:
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00141861202544241651579c69d4399a9aa135afef28c44000
# reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 其结果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 而map函数的ord就是将后面的映射成ascii码值
print("The solution2 is:" + chr(reduce(operator.xor, map(ord, s + t))))

# solution3:
# using sorted()
# zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），
# 然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。
# 利用*号操作符，可以将list unzip（解压）
# zip还可以用于 二维矩阵变换（矩阵的行列互换）
s, t = sorted(s), sorted(t)
print("The solution3 is:" + t[-1] if s == t[:-1] else [x[1] for x in zip(s, t) if x[0] != x[1]][0])

# solution4：
print("The solution4 is:" + next((c for c, d in zip(sorted(t), sorted(s)) if c != d), max(t)))

