# 这是一个简单的例子，在装饰器的函数里传递
# 装饰器修饰的函数可以认为是装饰器函数的第一个参数

def print_log(f):
	def wrapper(*args,**kargs):
		f(*args,**kargs)
		print(*args,**kargs)
	return wrapper
	
@print_log
def log_hello(name):
	print("hello "+name)

log_hello("world")

####################################

array = ['a', 'b', 'c']

def decorator(func):
    def newValueOf(pos):
        if pos >= len(array):
            print("Oops! Array index is out of range")
            return
        func(pos)

    return newValueOf


@decorator
def valueOf(index):
    print(array[index])
	
valueOf(7)