all_books = [ ]

def clear_all_books():
    global all_books
    all_books = []
    
def remove_book(title):
    try:
        all_books.remove(title)
    except ValueError:
        print("there is no such book in the list")

def add_book(title):
    all_books.append(title)       

def show_books():
    if not all_books:
        print("list of books is clear")
    else:
        for book in all_books:
            print(book)

def display_menu():
    print("Welcome to ur Electronic Library")
    print('just write a paragraph of menu')
    print("1 - display a list of books ")
    print("2 - delete book")
    print("3 - add book")
    print("4 - clear full list of books")
    print("5 - exit")

def main():
    while True:
        display_menu()
        choice = input("write a paragraph")

        if choice == '1':
            show_books()
        elif choice == '2':
            title = input("write tittle of book to remove it")
            remove_book(title)
        elif choice == '3':
            title = input("write title of books to add it")
            add_book(title)
        elif choice == '4':
            clear_all_books()
        elif choice == '0':
            break
        else:
            print("uncorect choose")

        
        show_books()

if __name__ == "__main__":
    main()
