letters = "abcdefghijklmnopqrstuvwxyz"

# Step 1: validate input
n = input("Enter the length of random string: ")

if not n.isdigit():
    print("Error! You should enter an integer.")
else:
    n = int(n)

    # Step 2: generate random-looking string
    rand_str = ""
    pos = n % 26

    for i in range(n):
        rand_str += letters[pos]
        pos = (pos + i + 4) % 26

    print("Generated string:", rand_str)

    # Step 3: counting frequencies WITHOUT ord()
    counts = [0] * 26

    for ch in rand_str:
        idx = letters.index(ch)   # works like ord but allowed
        counts[idx] += 1

    # Step 4: print frequencies in sorted (alphabet) order
    print("Character frequencies:")
    for i in range(26):
        if counts[i] > 0:
            print(letters[i], "-", counts[i])
