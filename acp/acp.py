vas = int(input("Enter da base: "))
rot = int(input("Enter da exponent: "))

mass = 1

for i in range(rot):
    mass = mass * vas
    print("Step", i + 1, ": total is", mass)

print("Final answer:", mass)