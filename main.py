def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)

main ()