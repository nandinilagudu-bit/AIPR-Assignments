from __future__ import annotations
import sys


def format_full_name(full_name: str) -> str:
	
	if not full_name:
		return ""
	parts = full_name.strip().split()
	if len(parts) == 0:
		return ""
	if len(parts) == 1:
		return parts[0]
	last = parts[-1]
	firsts = " ".join(parts[:-1])
	return f"{last}, {firsts}"


def _demo_examples() -> None:
	examples = [
		"John Doe",
		"Alice Johnson",
		"Michael Clark",
		"John A. Doe",
		"  Mary   Ann   Smith  ",
		"SingleName",
		"",
	]
	for name in examples:
		print(f"Input: {repr(name)} -> Output: {format_full_name(name)}")


if __name__ == "__main__":
	# If command-line arguments are provided, format and print each.
	# Otherwise prompt the user interactively for names (blank to exit).
	if len(sys.argv) > 1:
		for arg in sys.argv[1:]:
			print(format_full_name(arg))
	else:
		prompt = "Enter full name : "
		while True:
			try:
				s = input(prompt)
			except (EOFError, KeyboardInterrupt):
				print()  # newline on ^D/^C
				break
			if not s:
				break
			if s.strip().lower() == "demo":
				_demo_examples()
				continue
			print(format_full_name(s))

