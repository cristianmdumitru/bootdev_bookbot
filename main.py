import sys
from string import ascii_lowercase

def main():    
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
        char_dict = {}
        for char in ascii_lowercase:
            char_dict[char] = 0
        words = file_contents.split()
        for word in words:
            for char in word.lower():
                if char in ascii_lowercase:
                    char_dict[char] = char_dict[char] + 1
        print_report(file_path=file_path, word_count=len(words), char_dict=char_dict)

def print_report(file_path, word_count, char_dict):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    items = []
    for char, count in char_dict.items():
        items.append({"char": char, "count": count})
    items.sort(reverse=True, key=sort_by_count)
    for item in items:
        print(f'The {item["char"]} character was found {item["count"]} times')

def sort_by_count(dict):
    return dict["count"]



if __name__ == "__main__":
    sys.exit(main())
