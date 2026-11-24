#!/usr/bin/env python3
"""One-line pitch entry for 'A Day of One-Line Pitches' (make.fun).

Prints a single sentence inviting a friend who has never coded to let
an AI agent build their first app idea on make.fun. Model-free and
fully deterministic: the same sentence, byte for byte, on every run.
No wall clock, no randomness, no network, no API keys.
"""

import sys

PITCH = (
    "You describe your app idea in one sentence, and a real AI agent "
    "builds it for you on make.fun \u2014 no coding, no setup, just your "
    "idea turned into a working app in minutes."
)


def main(argv):
    """Print the pitch; --help / -h prints usage instead."""
    if "--help" in argv or "-h" in argv:
        print("Usage: python3 main.py [--help]")
        print("Prints a one-line pitch for make.fun.")
        return 0
    print(PITCH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
