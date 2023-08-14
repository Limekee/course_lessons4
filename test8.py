# t=set([i for i in [i for i in range(1, 10)]])
# for i in t:
#     print(i)
# for i in t: print(i)
# print(t, t, t)
def ff(s):
    for i in sorted(list(set(s))): print('{}-{} шт'.format(i, s.count(i)))


