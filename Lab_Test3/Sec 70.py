def items_starting_with_vowel(lst):
    # return items that start with a vowel (a, e, i, o, u), case-insensitive
    result = []
    vowels = "aeiouAEIOU"
    for item in lst:
        if item != "" and item[0] in vowels:
            result.append(item)
    return result


def count_long_items(lst, n):
    # return how many items have length >= n
    count = 0
    for item in lst:
        if len(item) >= n:
            count += 1
    return count


def main():
    # take input
    text = input("Enter items separated by commas: ")

    # split into list (no spaces before/after commas as the paper says)
    items = text.split(",")

    # sort alphabetically
    items.sort()
    print("Items (sorted):", items)
    print()

    # items starting with vowel
    vowel_items = items_starting_with_vowel(items)
    print("Items starting with a vowel:", vowel_items)
    print()

    # ask for n and count long items
    n = int(input("Enter a length threshold: "))
    num = count_long_items(items, n)
    print("Number of items with length >=", n, ":", num)


# do not forget to call main
main()
