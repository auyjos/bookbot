import sys

from stats import book_text, character_count, sort_character_counts


def get_book_text(filepath:str) -> str:
    with open(filepath, encoding='utf-8') as f:
        return f.read()


def main():
    
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    book_text(get_book_text(book_path))

    ch_count = character_count(get_book_text(book_path))
    sorted_chars =sort_character_counts(ch_count)
    

    print("--------- Character Count -------")
    for entry in sorted_chars:
        ch = entry['char']
        if not ch.isalpha():
            continue
        print(f"{ch}: {entry['num']}")
    print("============= END ===============")

if __name__ == '__main__':
    main()
