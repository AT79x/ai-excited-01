#!/usr/bin/env python3
"""Make the AI judge excited - entry program.
Deterministic, no network, stdlib only.
Copies the bundled image to /output/entry.png (JPEG data, 1024x1024, <1 MiB).
Runs twice and writes identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)

if __name__ == "__main__":
    main()
