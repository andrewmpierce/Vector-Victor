
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
