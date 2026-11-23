from book import *

class Student:
    def __init__(self, studentID, name):
        self.name = name
        self.borrowedBooks = []


    def showInfo(self):
        print(f"""
 
ID: {self.studentID}
Title: {self.name}
Author: {(self.borrowedBooks)}

        """)


    def borrowedBook(self, book):
        if book.isAvailable:
            book.borrow()
            self.borrowedBooks.append(book)
        else:
            print("Book is not available")

    def returnBook(self, book):
        if book in self.borrowedBooks:
            book.returnBook()
            self.borrowedBooks.remove(book)
        else:
            print("This book is not borrowed.")


student1 = Student(1, "Taleh")
student2 = Student(2, "Ramiz")
student3 = Student(3, "Ramal")


book1 = Book(1, "Clean Code", "Robert Martin", 464)
student.borrowedBook(book1)
print("Reading...")
student1.returnedBook(book1)