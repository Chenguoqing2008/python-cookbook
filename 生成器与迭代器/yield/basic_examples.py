# 可以（）将推导式定义为迭代器
yield_list  = (i for i in range(10) if i%2 == 0)

print(yield_list)


def generator():
    for i in range(10):
        b = yield i
        if b is None:
            i += 1
            print(i)


a = generator()
print(a)
print(a.__next__())
# 执行到第9行返回0
print(a.send(2))
# 由于第9行yield返回值为None，所以执行第11号，i = 1, print(1)
# 现次执行到第9行，yield返回值为2
print(a.__next__())
# 进入下一次循环，i 的值为2，把握 yield 2
print(a.__next__())
#  yield没有返回值 再次执行b is None的逻辑，此时print(3)
#  再循环到第9号 yield 3