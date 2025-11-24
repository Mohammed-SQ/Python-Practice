def strip_non_alnum(s):
    """Remove non-alphanumeric characters from the start and end of a string."""
    while s and not s[0].isalnum():
        s = s[1:]
    while s and not s[-1].isalnum():
        s = s[:-1]
    return s
def update_words(words):
    """Normalize each word, skip short ones, and replace if same start/end letter."""
    updated_list = []
    for w in words:
        norm = strip_non_alnum(w).lower()
        if len(norm) < 4:
            continue
        if norm[0] == norm[-1]:
            updated_list.append('xxxxx')
        else:
            updated_list.append(norm)
    return updated_list

sentence = input("Enter a sentence: ").strip()
words_raw = sentence.split()
total = len(words_raw)

# List of words that start and end with the same letter (normalized, lowercase)
same_letter_words = []
for w in words_raw:
    norm = strip_non_alnum(w).lower()
    if norm and norm[0] == norm[-1]:
        same_letter_words.append(norm)

updated = update_words(words_raw)

print()
print("Words starting and ending with the same letter:", same_letter_words)
print("Updated word list:", updated)
print("Total number of words in the sentence:", total)
