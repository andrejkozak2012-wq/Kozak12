result = []


def divider(a, b):
  if a < b:
    raise ValueError("a is less than b")
  if b > 100:
    raise IndexError("b is greater than 100")
  return a / b


# Using a list of tuples to safely handle different data types (including list [])
data = [(10, 2), (2, 5), ("123", 4), (18, 0), ([], 15), (8, 4)]

for item in data:
  try:
    key = item[0]
    val = item[1]
    res = divider(key, val)
    result.append(res)
  except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
    print(f"Caught exception: {type(e).__name__} -> {e}")
  except Exception as e:
    print(f"Caught unexpected error: {type(e).__name__} -> {e}")

print("Final result list:", result)