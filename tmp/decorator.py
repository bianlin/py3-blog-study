import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('call %s():', func.__name__)
#         return func(*args, **kwargs)
#     return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2019-12-09')

now()
print(now.__name__)