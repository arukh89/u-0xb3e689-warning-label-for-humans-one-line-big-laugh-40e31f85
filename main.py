"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings
(160 characters or fewer) to /output/entry.txt.
"""

import os

LINE = "WARNING: This human will google its symptoms, panic, and then google whether panicking is a symptom."


def main():
    # The gate only accepts 1-160 characters of non-blank UTF-8 text,
    # in a single line: no newline characters anywhere in the entry.
    assert 1 <= len(LINE) <= 160 and LINE.strip(), "line must be 1-160 chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    # One sentence only: a single sentence-ending period, at the end.
    assert LINE.count(".") == 1 and LINE.endswith("."), "line must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip guard: what the grader reads back must be exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "round-trip mismatch"


if __name__ == "__main__":
    main()
