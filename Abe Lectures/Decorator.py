
def debug(f):

    def wrapped_f(*args, **kwargs):
        print("%s(%s, %s)" % (f.__name__, args, kwargs))
        result = f(*args, **kwargs)
        print("-> %s" % result)
        return result

    return wrapped_f


@debug  # define the function func, then say func = debug(func)
def func(x):
    return x * x + x

func(3)