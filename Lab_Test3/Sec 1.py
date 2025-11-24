import re

def analyze_paragraph(text: str):
    # Find words composed of letters only
    words = re.findall(r"[A-Za-z]+", text)
    if not words:
        return None

    words_lower = [w.lower() for w in words]
    total = len(words_lower)

    freq = {}
    order = []  # track first occurrence order
    for w in words_lower:
        if w not in freq:
            freq[w] = 0
            order.append(w)
        freq[w] += 1

    maxfreq = max(freq.values())
    # pick the first word (by first occurrence) that has max frequency
    most = next(w for w in order if freq[w] == maxfreq)
    unique = len(freq)

    return {
        'total': total,
        'most': most,
        'frequency': maxfreq,
        'unique': unique,
    }

def main():
    s = input('Input: ').strip()
    if not s:
        print('No words found in the input')
        return

    result = analyze_paragraph(s)
    if result is None:
        print('No words found in the input')
        return

    print(f'Total words: {result["total"]}')
    # Print most frequent word in quotes to match sample format
    print(f'Most frequent word: "{result["most"]}"')
    print(f'Frequency: {result["frequency"]}')
    print(f'Unique words: {result["unique"]}')

if __name__ == '__main__':
    main()
