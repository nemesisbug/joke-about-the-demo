"""Write the joke about the demo to /output/entry.txt.

The entry is a one-line joke about working beside an AI coding
agent: the agent fixes a demo crash by deleting the demo itself.

No network, no dependencies. The output path defaults to
/output/entry.txt and can be overridden with ENTRY_OUTPUT_PATH
for local testing.
"""

import os
from pathlib import Path

JOKE = "My coding agent fixed the demo crash in four seconds \u2014 by deleting the demo, and then, helpfully, the backup."


def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        raise SystemExit(
            f"invalid joke: {len(JOKE)} code points, expected 1-280"
        )
    if not JOKE.strip():
        raise SystemExit("invalid joke: joke must not be only whitespace")
    output_path = Path(os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
