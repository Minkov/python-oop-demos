class Printer:
    def print(self, message):
        print(message)


class FilePrinter(Printer):
    # # LSP Violation - different number of params
    # def print(self, message, file_name):
    #     print(f'Print in {file_name} - {message}')

    # LSP violation - different behavior than parent
    def print(self, message):
        raise NotImplemented

    def print_to_file(self, file_name, message):
        print(f'Print in {file_name} - {message}')


pr = FilePrinter()

pr.print('Message 1')
