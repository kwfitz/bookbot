def main():
    #Counts the number of words in a text file
    #varibles defined
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    from stats import get_num_words

    #output of the program
    print(f"{num_words} words found in the document")

#functions defined
def get_book_text(path):
    with open(path) as f:
        return f.read()

'''
def get_num_words(text):
    words = text.split()
    return len(words)

'''   
main()
