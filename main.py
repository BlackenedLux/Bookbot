#def main():
#    f = open("books/frankenstein.txt", "r")
 #   print(f.read())
 #   words = f.read()
  #  word_count = len(words.split())
   # print (word_count)
    #return (word_count)

def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = count_words(text)
    char_occurance = get_chars_dict(text) #dictionary
    char_sorted_list = sort_list (char_occurance)
 #   print(char_occurance.items())
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def count_words(text):
    #whole_text = text.read()
    words = text.split()
    return len(words)

#def get_text(path):
 #   f = open(path)
  #  return f
def get_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
   # whole_text = text.read()
  #  words = whole_text.split()
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def sort_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

#def sort_on(dict)
#    return dict[]


if __name__ == "__main__":
    main()