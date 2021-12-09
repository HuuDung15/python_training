import random

from vector_class import Vector


# ==========================================================================


def vector_rand():
    return Vector(random.randrange(0, 5), random.randrange(0, 5), random.randrange(0, 5))


# ==========================================================================


e = vector_rand()
f = vector_rand()
n = random.random()


# ==========================================================================


def calc_add(e, f):
    add = tuple(a + b for a, b in zip(f, e))
    return Vector(add)

# ==========================================================================


def calc_radd(e, n):
    radd = tuple(a + n for a in e)
    return Vector(*radd)


# ==========================================================================



def calc_mul(e, f):
    return sum(a * b for a, b in zip(f, e))


# ==========================================================================


def calc_rmul(e, n):
    rmul = tuple(a * n for a in e)
    return Vector(*rmul)


# ==========================================================================


def calc_truediv(e, f):
    div = tuple(a / b for a, b in zip(e, f))
    return Vector(*div)




def calc_sub(e, f):
    sub = tuple(a - b for a, b in zip(e, f))
    return Vector(*sub)


# ==========================================================================


def calc_rsub(f, n):
    rsub = tuple(a - n for a in f)
    return Vector(*rsub)


# ==========================================================================


def test_mul():
    assert e * f == calc_mul(e, f)


# ==========================================================================


def test_rmul():
    assert e * n == calc_rmul(e, n)


# ==========================================================================


def test_truediv():
    assert e / f  == calc_truediv(e, f)


# ==========================================================================


def test_add():
    assert e + f == calc_add(e, f)


# ==========================================================================


def test_radd():
    assert e + n == calc_radd(e, n)


# ==========================================================================


def test_sub():
    assert e - f == calc_add(e, f)


# ==========================================================================


def test_rsub():
    assert e - n == calc_radd(e, n)