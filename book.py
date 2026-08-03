# ===============================
# Book Class
# ===============================

class Book:

    def __init__(self, book_id, title, author, publisher, version):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.version = version
        self.available = True
        self.issued_to = None

    # --------------------------
    # Display Book Details
    # --------------------------
    def display(self):

        print("\n----------------------------")
        print("Book ID      :", self.book_id)
        print("Title        :", self.title)
        print("Author       :", self.author)
        print("Publisher    :", self.publisher)
        print("Version      :", self.version)
        print("Available    :", "Yes" if self.available else "No")

        if self.issued_to is not None:
            print("Issued To ID :", self.issued_to)

        print("----------------------------\n")