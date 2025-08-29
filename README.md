## `rool` is a simple rules language.

Example:

```python
from rool.expr import *
from rool.store import Store

expr = Or(
    Equal(Variable("a"), Literal(1)),
    And(
        Equal(Literal(1), Variable("a")),
        Equal(Variable("a"), Variable("b"))
    ),
)

store = Store(dict(a = 1, b = 2))

evaluate(expr, store)

# returns True
```
