"""考古作业面保护移交的本地请求入口。"""
import sys

from .api import handle


def main() -> int:
    payload = sys.stdin.read().strip() or '{"action":"health"}'
    print(handle(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
