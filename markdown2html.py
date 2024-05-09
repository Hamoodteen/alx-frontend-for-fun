#!/usr/bin/python3
""" commenttttttttttttttttttttttttttttttttt """
import sys
import os


if len(sys.argv) < 2:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)
elif not os.path.isfile(f"./{sys.argv[1]}"):
    sys.stderr.write(f"Missing {sys.argv[1]}")
    sys.exit(1)
else:
    sys.exit(0)
