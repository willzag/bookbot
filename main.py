from stats import get_num_words
from stats import get_char_count
from stats import dict_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(
        "============ BOOKBOT ============"
        f"Analyzing book found at {sys.argv[1]}..."
        "----------- Word Count ----------"
        f"Found {num_words} total words"
        "--------- Character Count -------"
        )
    # python
    sorted_chars = dict_list(text)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()