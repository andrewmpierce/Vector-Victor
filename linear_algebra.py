import math
class ShapeException(Exception):
    pass


def shape(vector):
    num_rows = len(vector)
    return (num_rows,)

def vector_add(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ShapeException
    addition = [x + y for x, y in zip(vector1, vector2)]
    return addition

def vector_sub(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ShapeException
    subtraction = [x - y for x, y in zip(vector1, vector2)]
    return subtraction

def vector_sum(*args):
    length = len(args[0])
    for arg in args:
        if len(arg) != length:
            raise ShapeException
    #[raise ShapeException for arg in args if len(arg) != length]
    sum_all = [sum(x) for x in zip(*args)]
    return sum_all

def dot(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ShapeException
    multiply = [x*y for x,y in zip(vector1, vector2)]
    return sum(multiply)


def vector_multiply(vector, scalar):
    multiply = [scalar*x for x in vector]
    return multiply


def vector_mean(*args):
    num = len(args)
    vector = vector_sum(*args)
    mean = [x/num for x in vector]
    return mean

def magnitude(vector):
    exp = [x**2 for x in vector]
    sum_exp = sum(exp)
    magnitude = math.sqrt(sum_exp)
    return magnitude
