def items_starting_with_vowel(lst):
    result = []
    for item in lst:
        if item != "" and item[0].lower() in "aeiou":
            result.append(item)
    return result

def count_long_items(lst, n):
    count = 0
    for item in lst:
        if len(item) >= n:
            count += 1
    return count

def main():
    text = input("Enter items separated by commas: ")  # e.g. apples,carrots,bread
    items = text.split(",")            # make list
    items.sort()                       # alphabetical
    print("Items (sorted):", items)
    print()

    vowel_items = items_starting_with_vowel(items)
    print("Items starting with a vowel:", vowel_items)
    print()

    n = int(input("Enter a length threshold: "))
    num = count_long_items(items, n)
    print("Number of items with length >=", n, ":", num)

main()
