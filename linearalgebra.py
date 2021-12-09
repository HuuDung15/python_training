# Build support functions for Linear Algebra operations

import math

# =============================================================================


__author__ = 'Huu Dung'
__email__ = 'nhuudung10@gmail.com'
__date__ = '2021/12/01'
__status__ = 'development'

# ============================================================================
def calc_addition(vector1, vector2):
    add_val = []
    for i in range(len(vector1)):
        add = vector1[i]+vector2[i]
        add_val.append(add)
    return add_val


# =============================================================================


def calc_subtraction(vector1, vector2):
    sub_val = []
    for i in range(len(vector1)):
        sub = vector2[i] - vector1[i]
        sub_val.append(sub)
    return sub_val

# =============================================================================


def calc_multiplication(vector1, num):
    mul_val = []
    for i in range(len(vector1)):
        mul = vector1[i] * num
        mul_val.append(mul)
    return mul_val


# =============================================================================


def calc_dotproduct(vector1, vector2):
    dot_val = 0.
    for i in range(len(vector1)):
        add = vector1[i] * vector2[i]
        dot_val += add
    return dot_val


# =============================================================================


def calc_magnitude(vector1, vector2):
    sum = 0
    for i in range(len(vector1)):
       sub = (vector2[i] - vector1[i])**2
       sum += sub
    dist_val = math.sqrt(sub)
    return dist_val 
def test_mean_median():
    # input
    vector1 = [2.3, 4.2, 5.6, 6.2]
    vector2 = [5.9, 7.1, 5.3, 9.1]
    num = 1.5
# ==================================================================
    # 1. Calculate sum value for 2 vectors
  
    add_val = calc_addition(vector1, vector2)
    print('sum value of 2 vectors:', add_val)


    # 2. Calculate sub value for 2 vectors
    
    sub_val = calc_subtraction(vector1, vector2)
    print('sub value of 2 vectors:', sub_val)


    # 3. Calculate scale a vector by a factor
    
    mul_val = calc_multiplication(vector1, num)
    print('scale value  :', mul_val)


    # 4. Calculate dot product for 2 vectors

    dot_val = calc_dotproduct(vector1, vector2)
    print('dot product of 2 vectors:', dot_val)


    # 5. Calculate distance value for 2 vectors
    
    dist_val = calc_magnitude(vector1, vector2)
    print('distance value of 2 vectors:', dist_val)


# =============================================================================

if __name__ == '__main__':
    test_mean_median()

