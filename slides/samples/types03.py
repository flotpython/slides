import math

from typing import Iterable

RealVector = Iterable[float]

def norm(v: RealVector) -> float:
    return math.sqrt(sum(x**2 for x in v))

print(norm([0.7, 0.7]))
print(norm((1, 1)))
