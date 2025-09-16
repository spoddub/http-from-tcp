#!/usr/bin/env python3
import sys
from pathlib import Path
from typing import IO, Iterable

CHUNK_SIZE = 8


def iter_lines(f: IO[bytes]) -> Iterable[bytes]:
    buf = b""
    try:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:  # EOF
                break
            buf += chunk
            parts = buf.split(b"\n")
            for line in parts[:-1]:
                if line.endswith(b"\r"):
                    line = line[:-1]
                yield line
            buf = parts[-1]
        if buf:
            if buf.endswith(b"\r"):
                buf = buf[:-1]
            yield buf
    finally:
        try:
            f.close()
        except Exception:
            pass


def main() -> None:
    path = Path(__file__).resolve().parent / "messages.txt"
    for line in iter_lines(path.open("rb")):
        sys.stdout.buffer.write(b"read: " + line + b"\n")
        sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
