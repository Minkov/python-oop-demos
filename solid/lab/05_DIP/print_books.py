class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class UpperCaseFormatter(Formatter):
    def format(self, book: Book) -> str:
        return super().format(book).upper()


class TrimCountCharactersFormatter(Formatter):
    def __init__(self, trim_count):
        self.trim_count = trim_count

    def format(self, book: Book) -> str:
        return super().format(book)[self.trim_count:]


class CompositeFormatter(Formatter):
    def __init__(self, formatters):
        self.formatters = formatters

    def format(self, book: Book) -> str:
        result = super().format(book)
        for formatter in self.formatters:
            new_book = Book(result)
            result = formatter.format(new_book)
        return result


class Printer:
    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        formatted_book = self.formatter.format(book)
        return formatted_book


uppercase_formatter = UpperCaseFormatter()
regular_formatter = Formatter()
trim_formatter = TrimCountCharactersFormatter(3)
composite_formatter = CompositeFormatter([
    uppercase_formatter,
    regular_formatter,
    trim_formatter,
    trim_formatter])

b = Book('Hello world!')
regular_printer = Printer(regular_formatter)
uppercase_printer = Printer(uppercase_formatter)
trim_printer = Printer(trim_formatter)
composite_printer = Printer(composite_formatter)

print(regular_printer.get_book(b))
print(uppercase_printer.get_book(b))
print(trim_printer.get_book(b))
print(composite_printer.get_book(b))
