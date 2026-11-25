#!/usr/bin/env python3
"""Entrypoint: copy the rendered letter to $MAKEFUN_OUTPUT_DIR/entry.png.

draw.py renders entry.png beside this file; this program validates it
against the competition gate (whole PNG, at most 1024x1024, at most
1 MiB), copies it byte-for-byte to the output directory (env
MAKEFUN_OUTPUT_DIR, default /output), and checks the copy matches the
source in both size and SHA-256.
"""

import hashlib
import os
import shutil
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAX_BYTES = 1_048_576
MAX_DIM = 1024


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def png_dimensions(path):
    """Return (width, height) for a PNG, raising ValueError if not one."""
    data = Path(path).read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n" or len(data) < 24:
        raise ValueError("entry.png is not a whole PNG file")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main():
    src = HERE / "entry.png"
    if not src.is_file():
        raise SystemExit("entry.png missing: run draw.py first")
    if src.stat().st_size > MAX_BYTES:
        raise SystemExit(f"entry.png exceeds 1 MiB: {src.stat().st_size} bytes")
    width, height = png_dimensions(src)
    if width > MAX_DIM or height > MAX_DIM:
        raise SystemExit(f"entry.png too large: {width}x{height}")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    if dst.stat().st_size != src.stat().st_size or sha256(src) != sha256(dst):
        raise SystemExit("copy mismatch: entry.png did not copy byte-for-byte")
    print(dst, dst.stat().st_size, "bytes", f"{width}x{height}")


if __name__ == "__main__":
    main()
