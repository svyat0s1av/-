class book:
    def __init__(self, title, author, year):
        self.title= title
        self.author= author
        self.year=year
    def get_info(self):
        return (f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}")
kniga=book("Преступление и наказание","Фёдор Достоевский","1866")
print(kniga.get_info())
