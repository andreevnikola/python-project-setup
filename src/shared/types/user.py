from dataclasses import dataclass
from typing import Literal, NewType

UserId = NewType("UserId", int)


@dataclass(frozen=True, slots=True)
class User:
    id: UserId
    name: str
    role: Literal["admin", "user"]
