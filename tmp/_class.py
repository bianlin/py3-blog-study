# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score

#     def print_score(self):
#         print("%s: %s" % (self.__name, self.__score))

#     def get_grade(self):
#         if self.__score >= 90:
#             return "A"
#         elif self.__score >= 60:
#             return "B"
#         else:
#             return "C"

#     def get_name(self):
#         return self.__name

#     def get_score(self):
#         return self.__score

#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError("bad score")


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


class Student(object):
    def __init__(self):
        self.name = "Bianlin"

    def __getattr__(self, attr):
        if attr == "age":
            return lambda: 25
        raise AttributeError("'Student' object has no attribute '%s'" % attr)


class Chain(object):
    def __init__(self, path=""):
        self._path = path

    def __getattr__(self, path):
        return Chain("%s/%s" % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)