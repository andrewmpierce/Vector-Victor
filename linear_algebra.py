
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

# def vector_sum(*args):
#     length = len(args)
#     for arg in args:
#         if len(arg) != length:
#             raise ShapeException
#     sum_all = zip(args)
#     #vector_sum = [sum(row) for row in sum_all]
#     print(sum_all)

def dot(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ShapeException
    multiply = [x*y for x,y in zip(vector1, vector2)]
    return sum(multiply)
