"""Queue implementation with simple tests.

Provides a Queue class with:
 - enqueue(item)
 - dequeue() -> removes and returns front item (raises IndexError if empty)
 - peek() -> returns front item without removing it (returns None if empty)

When run as a script this file will execute multiple test scenarios and print results.
"""

from collections import deque
from typing import Any


class Queue:
	"""A simple FIFO queue.

	Methods:
		enqueue(item): add item to the back of the queue.
		dequeue(): remove and return the front item; raises IndexError if empty.
		peek(): return the front item without removing it; returns None if empty.
	"""

	def __init__(self) -> None:
		self._data = deque()

	def enqueue(self, item: Any) -> None:
		"""Add `item` to the back of the queue."""
		self._data.append(item)

	def dequeue(self) -> Any:
		"""Remove and return the front item. Raises IndexError if queue is empty."""
		if not self._data:
			raise IndexError("dequeue from an empty queue")
		return self._data.popleft()

	def peek(self) -> Any:
		"""Return the front item without removing it. Returns None if empty."""
		if not self._data:
			return None
		return self._data[0]

	def __len__(self) -> int:  # helper for tests
		return len(self._data)


def _run_tests() -> None:
	"""Run several test scenarios and print results."""
	tests_passed = 0
	tests_total = 5

	# Scenario 1: Basic FIFO behavior
	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	try:
		assert q.dequeue() == 1
		assert q.dequeue() == 2
		assert q.dequeue() == 3
		tests_passed += 1
		print("Test 1 (FIFO): PASS")
	except AssertionError:
		print("Test 1 (FIFO): FAIL")

	# Scenario 2: peek does not remove
	q = Queue()
	q.enqueue("a")
	q.enqueue("b")
	try:
		assert q.peek() == "a"
		assert len(q) == 2
		assert q.dequeue() == "a"
		tests_passed += 1
		print("Test 2 (peek non-destructive): PASS")
	except AssertionError:
		print("Test 2 (peek non-destructive): FAIL")

	# Scenario 3: dequeue on empty raises IndexError
	q = Queue()
	try:
		try:
			q.dequeue()
			print("Test 3 (dequeue empty): FAIL - no exception")
		except IndexError:
			tests_passed += 1
			print("Test 3 (dequeue empty): PASS")
	except Exception as e:
		print("Test 3 (dequeue empty): FAIL - unexpected error", e)

	# Scenario 4: mixed types and peek/size
	q = Queue()
	q.enqueue(0)
	q.enqueue(None)
	q.enqueue([1, 2, 3])
	try:
		assert q.peek() == 0
		assert len(q) == 3
		assert q.dequeue() is 0
		assert q.dequeue() is None
		assert q.dequeue() == [1, 2, 3]
		tests_passed += 1
		print("Test 4 (mixed types): PASS")
	except AssertionError:
		print("Test 4 (mixed types): FAIL")

	# Scenario 5: enqueue many items and ensure order
	q = Queue()
	n = 1000
	for i in range(n):
		q.enqueue(i)
	ok = True
	try:
		for i in range(n):
			v = q.dequeue()
			if v != i:
				ok = False
				break
		if ok and len(q) == 0:
			tests_passed += 1
			print("Test 5 (large enqueue/dequeue): PASS")
		else:
			print("Test 5 (large enqueue/dequeue): FAIL")
	except Exception as e:
		print("Test 5 (large enqueue/dequeue): FAIL -", e)

	print(f"\nTests passed: {tests_passed}/{tests_total}")


if __name__ == "__main__":
	_run_tests()
