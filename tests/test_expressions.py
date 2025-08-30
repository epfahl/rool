import pytest

from rool.expr import Literal, Variable, Equal, And, Or, evaluate
from rool.store import Store


def test_equal_true():
    assert evaluate(Equal(Literal(1), Literal(1)), Store())
    assert evaluate(Equal(Literal(1), Variable("a")), Store(a=1))
    assert evaluate(Equal(Variable("b"), Variable("a")), Store(a=1, b=1))


def test_equal_false():
    assert not evaluate(Equal(Literal(1), Literal(2)), Store())
    assert not evaluate(Equal(Variable("a"), Literal(2)), Store(a=1))


def test_and_true():
    expr = And(Equal(Literal(1), Variable("a")), Equal(Variable("a"), Variable("b")))
    assert evaluate(expr, Store(a=1, b=1))


def test_and_false():
    expr = And(Equal(Literal(1), Variable("a")), Equal(Variable("a"), Variable("b")))
    assert not evaluate(expr, Store(a=1, b=2))


def test_or_true():
    expr = Or(Equal(Literal(1), Variable("a")), Equal(Variable("a"), Variable("b")))
    assert evaluate(expr, Store(a=1, b=2))


def test_or_false():
    expr = Or(Equal(Literal(1), Variable("a")), Equal(Variable("a"), Variable("b")))
    assert not evaluate(expr, Store(a=2, b=3))


def test_combined():
    expr = Or(
        Equal(Variable("a"), Literal(1)),
        And(Equal(Literal(1), Variable("a")), Equal(Variable("a"), Variable("b"))),
    )
    assert evaluate(expr, Store(a=1, b=2))


@pytest.mark.xfail(raises=KeyError)
def test_expr_xfail():
    expr = And(Equal(Literal(1), Variable("a")), Equal(Variable("a"), Variable("b")))
    evaluate(expr, Store(a=1))
