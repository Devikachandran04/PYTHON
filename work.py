book = {'xyz': 10, 'abc': 35, 'lmn': 110}

choice = 1
while(choice != 4):
    print("Enter the choice:")
    print("1: Add book to stock")
    print("2: Sell")
    print("3: Display")
    print("4: Exit")
    print("5: Sort by book name")
    choice = int(input("Enter your choice: "))

    if(choice == 1):
        book_name = input("Enter the book to be added: ")
        count = int(input("Enter the count: "))
        if book_name in book:
            book[book_name] += count
        else:
            book[book_name] = count

    elif(choice == 2):
        book_name = input("Enter the book to be sold: ")
        count = int(input("Enter the count: "))
        if book_name in book:
            if book[book_name] >= count:
                book[book_name] -= count
            else:
                print("Insufficient number of books")
        else:
            print("No such book exists")

    elif(choice == 3):
        print("The stock is:")
        print(book)

    elif(choice == 5):
        sorted_books = dict(sorted(book.items()))  # Sort by book name
        print("Books sorted by name:")
        print(sorted_books)
        for name, count in sorted_books.items():
            print(f"{name}: {count}")


    elif(choice == 4):
        print("Exiting...")

    else:
        print("Wrong choice")
