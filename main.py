"""Write a single short text to /output/entry.txt."""

import os

# The entry is this one text; it is written verbatim and must stay exactly 265 characters.
TEXT = (
    "Each Wednesday at 03:14 a request arrives from an IP that cannot exist, "
    "and the reply is always three words. No human wrote the file that answers; "
    "I checked the commits. Eleven weeks so far. The twelfth breaks the pattern, "
    "and it is addressed to whoever reads this."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {len(TEXT)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
