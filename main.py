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
    char_occurance = get_chars_dict(text)
    print(char_occurance.values())

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


if __name__ == "__main__":
    main()