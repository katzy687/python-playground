x = [1, 2, 3, 4, 5]

for i in range(len(x)):
    print(f"=== i={i} ===")
    for j in range(i + 1, len(x)):
        print(f"j={j}")
