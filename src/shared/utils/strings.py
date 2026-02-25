import re


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


# def _debug_only_internal(x: str) -> str:
#     return f"DEBUG:{x}"
