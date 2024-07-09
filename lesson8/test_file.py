from random import randint
HEADS = 1
TAILS = 2

print("\nTen coin flips:")
print("-" * 30)
for _ in range(10):
    if randint(1,2) == HEADS:
        print("HEADS")
    else:
        print("TAILS")

print("-" * 30)
print()
