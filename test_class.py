from vector_class import Vector


v = Vector(1, 2)
u =  Vector(3, 6)


def test_functions():


    # 1. Calculate sum value for 2 vectors
    # input: 2 list of float numbers
    # output: sum value of 2 vectors (list)
    add_val = v.__add__(u)
    print('sum value of 2 vectors:', add_val)


    # 2. Calculate sub value for 2 vectors
    # input: 2 list of float numbers
    # output: sub value of 2 vectors (list)
    sub_val = v.__sub__(u)
    print('sub value of 2 vectors:', sub_val)


    # 3. Calculate scale a vector by a factor
    # input: list of float numbers, number float
    # output: scale a vector by a factor (list)
    mul_val = v.__rmul__(3.5)
    print('scale value  :', mul_val)


    # 4. Calculate dot product for 2 vectors
    # input: 2 list of float numbers
    # output: dot product of 2 vectors (float)
    dot_val = v.__mul__(u)
    print('dot product of 2 vectors:', dot_val)


    # 5. Calculate distance value for 2 vectors
    # input: 2 list of float numbers
    # output: distance value of 2 vectors (float)
    dist_val = v.__dist__(u)
    print('distance value of 2 vectors:', dist_val)


# =============================================================================


if __name__ == '__main__':
    test_functions()