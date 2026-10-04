from datetime import date


class Book:
    """A printed book with a title, author, and publication year."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

    def get_age(self):
        """Return the number of years since publication."""
        current_year = date.today().year
        return current_year - self.year


class EBook(Book):
    """A Book that also tracks its download size in megabytes."""

    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} - {self.file_size} MB"
