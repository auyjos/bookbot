def book_text(text):
    count = len(text.split())
    print(f'Found {count} total words')



def character_count(text):
    counts = {}

    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) +1
    
    return counts

def sort_character_counts(dict):
    sorted_pairs = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return [{"char":ch, "num": num} for ch, num in sorted_pairs]