from stats import count_words, count_char_occurrence, dict_to_sorted_list
import sys
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def print_report(book_path, num_words, char_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    #print(charDict)
    print("--------- Character Count -------")
    for pair in dict_to_sorted_list(char_dict):
        for key, value in pair.items():
            print(f"{key}: {value}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    char_dict = count_char_occurrence(text)
    word_count = count_words(text)
    print_report(book_path, word_count, char_dict)
main()