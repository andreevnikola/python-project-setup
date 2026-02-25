from shared.utils.strings import slugify


def test_slugify_basic() -> None:
    assert slugify("Hello World") == "hello-world"


def test_slugify_strips_and_collapses() -> None:
    assert slugify("  Hello   World!! ") == "hello-world"
