

from __future__ import annotations
import sys
from typing import Iterable


def count_lines_in_file(path: str, encoding: str = "utf-8") -> int:
	

	# Deterministic implementation following the few-shot guidance above
	line_count = 0
	with open(path, "r", encoding=encoding) as fh:
		for _ in fh:
			line_count += 1
	return line_count


def _print_counts_for(paths: Iterable[str]) -> None:
	for p in paths:
		try:
			print(f"{repr(p)} -> {count_lines_in_file(p)}")
		except Exception as exc:
			print(f"{repr(p)} -> ERROR: {exc}")


if __name__ == "__main__":
	# If file paths are provided as arguments, process them; otherwise prompt.
	if len(sys.argv) > 1:
		_print_counts_for(sys.argv[1:])
	else:
		print("Example: \"Hello\\nWorld\\n\" -> 2")
		prompt = "Enter path to .txt file (blank to exit) : "
		
while True:
			try:
				path = input(prompt)
			except (EOFError, KeyboardInterrupt):
				print()
				break
			if not path:
				break
			if path.strip().lower() == "demo":
				print("Demo expects real files; provide a path or press Enter to exit.")
				continue
			try:
				print(count_lines_in_file(path))
			except Exception as exc:
				print(f"ERROR: {exc}")


