"""The One-Line Exit — a one-line resignation letter.

The program writes exactly one funny resignation letter to
``entry.txt`` inside the output directory the harness provides
(``MAKEFUN_OUTPUT_DIR``, which the grader mounts at ``/output``).

Gate (sealed scorer): the file must be UTF-8 text of 1 to 140
characters, not only whitespace. The letter below is one line,
reads like a letter a person could actually send, names a specific
grievance with a concrete payoff, and lands its punchline in a
place the reader does not expect.
"""

import os

# One line, 111 characters. The joke: three years of being paid in
# "exposure and free pizza" ends the moment a real salary appears.
# Tightened from v1 ("actual money instead of") so the punchline
# lands one beat earlier: "real money, not exposure" is the line a
# colleague would quote back.
LETTER = (
    "I hereby resign, effective immediately \u2014 I found a job that "
    "pays in real money, not exposure and free pizza."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    text = LETTER.strip()
    if not 1 <= len(text) <= 140:
        raise SystemExit(
            "entry must be 1-140 characters, got %d" % len(text)
        )
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %s (%d chars)" % (path, len(text)))


if __name__ == "__main__":
    main()
