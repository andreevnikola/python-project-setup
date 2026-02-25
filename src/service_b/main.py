from shared.types import User, UserId
from shared.utils import slugify


def main() -> int:
    u = User(id=UserId(1), name="Nikola", role="admin")
    print(u)
    print(slugify("Hello World from service B!!"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
