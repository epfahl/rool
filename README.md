## `rool` is a simple rules language.

`rool` is an embedded domain-specific language that evaluates logical expressions in the context of a key-value data store. Evaluation of a logical expression uses a centralized interpreter so that logging and error handling can be controlled in one place.

Example:

```python
from rool.expr import *
from rool.store import Store

expr = Or(
    Equal(Variable("a"), Literal(1)),
    And(
        Equal(Literal(1), Variable("a")),
        Equal(Variable("a"), Variable("b"))
    )
)

store = Store(a = 1, b = 2)

evaluate(expr, store)

# returns True
```
