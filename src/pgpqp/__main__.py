# PGPQP - Pretty Good Post-Quantum Privacy: Post-quantum cryptography for public key encryption and digital signatures.
# Copyright (C) 2024  CyberThing

import argparse
from . import __version__
from sys import argv
from .utils import LICENSE_HEADER


def main():
    print(LICENSE_HEADER)

    parser = argparse.ArgumentParser(
        description="Pretty Good Post-Quantum Privacy (PGPQP)"
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"PGPQP v{__version__}"
    )
    args = parser.parse_args(argv[1:])


if __name__ == "__main__":
    main()
