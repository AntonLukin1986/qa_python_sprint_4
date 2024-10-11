class BooksCollector:
    '''Приложение, позволяющее установить жанр книг и добавить их
    в избранное.'''
    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = [
            'Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'
        ]
        self.genre_age_rating = ['Ужасы', 'Детективы']

    def add_new_book(self, name):
        '''Добавить новую книгу в словарь без указания жанра.
        Максимум 40 символов.'''
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    def set_book_genre(self, name, genre):
        '''Установить жанр книги, если книга есть в books_genre и её жанр
        входит в список genre.'''
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    def get_book_genre(self, name):
        '''Получить жанр книги по её имени.'''
        return self.books_genre.get(name)

    def get_books_with_specific_genre(self, genre):
        '''Получить список книг с определённым жанром.'''
        books_with_specific_genre = []
        if self.books_genre and genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        return books_with_specific_genre

    def get_books_genre(self):
        '''Получить словарь books_genre.'''
        return self.books_genre

    def get_books_for_children(self):
        '''Получить книги, подходящие детям - отсутствует возрастной
        рейтинг.'''
        books_for_children = []
        for name, genre in self.books_genre.items():
            if genre not in self.genre_age_rating and genre in self.genre:
                books_for_children.append(name)
        return books_for_children

    def add_book_in_favorites(self, name):
        '''Добавить книгу в избранное.'''
        if name in self.books_genre:
            if name not in self.favorites:
                self.favorites.append(name)

    def delete_book_from_favorites(self, name):
        '''Удалить книгу из избранного.'''
        if name in self.favorites:
            self.favorites.remove(name)

    def get_list_of_favorites_books(self):
        '''Получить список избранных книг.'''
        return self.favorites
