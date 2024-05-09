#!/usr/bin/python3
""" commenttttttttttttttttttttttttttttttttt """
import sys
import os


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    elif not os.path.isfile(f"./{sys.argv[1]}"):
        sys.stderr.write(f"Missing {sys.argv[1]}\n")
        sys.exit(1)
    else:
        with open(f"./{sys.argv[1]}", "r") as readme, open(f"./{sys.argv[2]}", "a") as html:
            for line in readme.readlines():
                line = line.rstrip('\n')
                if line.startswith("# "):
                    line = line.replace("# ", "")
                    html.write(f"<h1>{line}</h1>\n")
                elif line.startswith("## "):
                    line = line.replace("## ", "")
                    html.write(f"<h2>{line}</h2>\n")
                elif line.startswith("### "):
                    line = line.replace("### ", "")
                    html.write(f"<h3>{line}</h3>\n")
                elif line.startswith("#### "):
                    line = line.replace("#### ", "")
                    html.write(f"<h4>{line}</h4>\n")
                elif line.startswith("##### "):
                    line = line.replace("##### ", "")
                    html.write(f"<h5>{line}</h5>\n")
                elif line.startswith("###### "):
                    line = line.replace("###### ", "")
                    html.write(f"<h6>{line}</h6>\n")
