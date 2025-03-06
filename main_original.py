def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)

    # Counting words
    num_words = len(file_contents.split())
    print(f"{num_words} words found in the document")

main()
