

from __future__ import annotations
import sys


def convert_cm_to_inches(cm: float, ndigits: int = 3) -> float:
	
	inches = float(cm) / 2.54
	return round(inches, ndigits) if ndigits is not None else inches


if __name__ == "__main__":
	if len(sys.argv) > 1:
		try:
			values = [float(a) for a in sys.argv[1:]]
		except ValueError:
			print("Usage: python task4.2.py [cm1 [cm2 ...]]")
			sys.exit(1)
		for v in values:
			print(f"{v} cm -> {convert_cm_to_inches(v)} in")
	else:
		# show the sample from your request
		print(f"10 cm -> {convert_cm_to_inches(10)} in")


  