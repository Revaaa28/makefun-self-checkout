"""The Self-Checkout Is Judging You — make.fun entry.

Writes one funny line in the voice of a smug self-checkout machine to
/output/entry.txt: the till verifies whether twelve yogurts counts as a meal,
denies it, and reclassifies it as a personality trait.

Deterministic: stdlib only, no network, no randomness, no environment reads.
The line is a fixed literal; the program writes it byte-for-byte every run.
"""

LINE = (
    "Please wait. I am verifying that twelve yogurts counts as a meal. "
    "It does not. It counts as a personality trait."
)


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip() == text and "\n" not in text, "entry must be one line"
    assert text.endswith("."), "entry must end with a full stop"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Re-read the written output and verify it matches byte for byte.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == text.encode("utf-8"), "written output differs from entry"


if __name__ == "__main__":
    main()
