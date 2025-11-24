numbers = []
letters = []
while True:
    s = input("Enter something (or type 'Exit' to stop): ").strip()
    if s.lower() == 'exit':
        break
    digit_str = ""
    letter_str = ""
    for ch in s:
        if ch.isdigit():
            digit_str += ch
        elif ch.isalpha():
            letter_str += ch
    if digit_str:
        num = int(digit_str)
    else:
        num = 0
    numbers.append(num)
    if letter_str:
        letters.append(letter_str)
    else:
        letters.append('-')
print()
print('Numbers list:', numbers)
print('Characters list:', letters)
total = sum(numbers)
print('Sum of numbers:', total)
if numbers:
    avg = total / len(numbers)
else:
    avg = 0
print(f'Average of numbers: {avg:.2f}')