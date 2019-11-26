def swap(x, y):      # Incorrect version
     print("before swap statement: x:", x, "y:", y)
     (x, y) = (y, x)
     print("after swap statement: x:", x, "y:", y)

a = ["This", "is", "fun"]
b = [2,3,4]
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)