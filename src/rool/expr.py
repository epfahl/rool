from dataclasses import dataclass
from .store import Store, Value


class Term:
    pass


class Logical:
    pass


@dataclass
class Literal(Term):
    value: Value


@dataclass
class Variable(Term):
    name: str


@dataclass
class Equal(Logical):
    left: Term
    right: Term


@dataclass
class And(Logical):
    left: Logical
    right: Logical


@dataclass
class Or(Logical):
    left: Logical
    right: Logical


type Expression = Term | Logical


def evaluate(expr: Expression, Store: Store) -> Value | bool:
    match expr:
        case Literal(value):
            return value

        case Variable(name):
            return Store.get(name)

        case Equal(left, right):
            return evaluate(left, Store) == evaluate(right, Store)

        case And(left, right):
            return evaluate(left, Store) and evaluate(right, Store)

        case Or(left, right):
            return evaluate(left, Store) or evaluate(right, Store)

        case _:
            raise ValueError("Invalid expression")
