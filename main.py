"""One Line to Stop the Scroll: one line that stops a stranger mid-scroll.

The entry is a single line, 114 characters, inside the 1-200 character
gate. It works on the feed itself: concrete scroll contents in threes
(47 ads, 12 arguments, one smug cat), then the twist in the last clause
- the one line that stopped the reader is not selling anything. It
sounds like a person talking to the scroller, not an ad, and it is worth
repeating because everyone recognises their own feed in it.

The program writes it to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing
newline and asserts the gate before writing.
"""

import os


LINE = "You've scrolled past 47 ads, 12 arguments, and one smug cat. This line stopped you \u2014 and it isn't selling a thing."


def main() -> None:
    line = LINE
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line, "line must be a single line"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
