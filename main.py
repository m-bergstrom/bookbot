import sys
from stats import get_word_count
from stats import get_character_counts
from stats import get_sorted_character_counts

def get_book_text(book_path):
    with open(book_path) as book_file:
        return book_file.read()

def main():
    #book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)


    #print(f"{get_word_count(book_text)} words found in the document")
    character_counts = get_character_counts(book_text)
    sorted_character_counts = get_sorted_character_counts(character_counts)
    #print(character_counts)
    #print(sorted_character_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
    for character_count in sorted_character_counts:
        if character_count["char"].isalpha():
            print(f"{character_count["char"]}: {character_count["num"]}")

    print("============= END ===============")

main()