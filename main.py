from stats import count_words, count_characters, sorted_count
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    num_characters = count_characters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_count(num_characters):
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    #print(f"{num_words} words found in the document")
    #print(num_characters)

def get_book_text(filepath):
    with open(filepath) as f:
        book_string = f.read()
    return book_string

main()