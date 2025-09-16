import sys

CHUNK_SIZE = 8


def main() -> None:
    with open("messages.txt", "rb") as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            sys.stdout.buffer.write(b"read: " + chunk + b"\n")
            sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
