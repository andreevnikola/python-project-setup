import re

from hypothesis import given
from hypothesis import strategies as st

from shared.utils.strings import slugify

_slug_re = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def test_slugify_basic() -> None:
    assert slugify("Hello World") == "hello-world"


@given(st.text())
def test_slugify_never_crashes(s: str) -> None:
    slugify(s)


@given(st.text())
def test_slugify_is_safe_charset(s: str) -> None:
    out = slugify(s)
    assert out == "" or _slug_re.fullmatch(out) is not None
