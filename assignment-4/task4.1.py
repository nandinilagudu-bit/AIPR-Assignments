"""Simple leap year checker.

This module provides is_leap_year(year) which returns True if the
given year is a leap year according to the Gregorian rules:

- Every year evenly divisible by 4 is a leap year,
- except years evenly divisible by 100 are not leap years,
- except years evenly divisible by 400 are leap years.

Includes a small CLI/test runner when executed as a script.
"""
from __future__ import annotations
import sys
from typing import Iterable


def is_leap_year(year: int) -> bool:
	"""Return True if `year` is a leap year.

	Args:
		year: Gregorian calendar year (integer).

	Returns:
		True if leap year, False otherwise.

	Examples:
		>>> is_leap_year(2000)
		True
		>>> is_leap_year(1900)
		False
	"""
	# Years not divisible by 4 are common years
	if year % 4 != 0:
		return False
	# Years divisible by 4 but not by 100 are leap years
	if year % 100 != 0:
		return True
	# Years divisible by 100 are leap years only if divisible by 400
	return year % 400 == 0


def _print_results(years: Iterable[int]) -> None:
	for y in years:
		print(f"{y}: {'Leap year' if is_leap_year(y) else 'Common year'}")
  
if __name__ == "__main__":
	# If a year (or multiple years) are passed as command-line args, use them.
	if len(sys.argv) > 1:
		try:
			years = [int(a) for a in sys.argv[1:]]
		except ValueError:
			print("Usage: python task4.1.py [year1 [year2 ...]]")
			sys.exit(1)
		_print_results(years)
	else:
		# Example years to demonstrate behavior
		sample_years = [1900, 2000, 2004, 2019, 2020]
		print("No years provided on the command line — running sample years:")
		_print_results(sample_years)

