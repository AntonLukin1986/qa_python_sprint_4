import random

import pytest

from main import BooksCollector


class TestBooksCollector:
    '''Набор тестов для покрытия приложения BooksCollector.'''
    @pytest.fixture(autouse=True)
    def create_app_object(self):
        '''Создание нового объекта приложения для каждого теста.'''
        self.collector = BooksCollector()

    def test_init_books_genre_empty_dict(self):
        '''Словарь books_genre пустой у созданного объекта приложения.'''
        books_genre = self.collector.books_genre
        assert isinstance(books_genre, dict) and not books_genre

    def test_init_favorites_empty_list(self):
        '''Список favorites пустой у созданного объекта приложения.'''
        favorites = self.collector.favorites
        assert isinstance(favorites, list) and not favorites

    def test_init_genre_list_contains_default_genres(self, default_genres):
        '''Список genre содержит жанры по умолчанию.'''
        genre = self.collector.genre
        assert isinstance(genre, list) and genre == default_genres

    def test_init_genre_age_rating_list_contains_default_genres_age_rating(
            self, default_genres_age_rating):
        '''Список genre_age_rating содержит жанры возрастных ограничений
        по умолчанию.'''
        genre_age_rating = self.collector.genre_age_rating
        assert (
            isinstance(genre_age_rating, list) and
            genre_age_rating == default_genres_age_rating
        )

    def test_add_new_book_add_2_books_added_2(
            self, valid_book_zombies, valid_book_cat):
        '''Успешное добавление двух книг в словарь books_genre.'''
        for title in valid_book_zombies, valid_book_cat:
            self.collector.add_new_book(title)
        assert len(self.collector.get_books_genre()) == 2

    def test_add_new_book_add_invalid_book_not_added_V_1(
            self, invalid_book_titles  # параметризированная фикстура
         ):
        '''Книги с недопустимыми названиями не добавляются.'''
        self.collector.add_new_book(invalid_book_titles)
        assert not self.collector.get_books_genre()

    @pytest.mark.parametrize(  # то же самое ↑, но без создания фикстуры
        'title',
        [pytest.param('', id='empty string'),
         pytest.param('Книга' * 8 + 'К', id='41 chars')]
        # или простым списком ['', 'Книга' * 8 + 'К']
    )
    def test_add_new_book_add_invalid_book_not_added_V_2(self, title):
        '''Книги с недопустимыми названиями не добавляются.'''
        self.collector.add_new_book(title)
        assert not self.collector.get_books_genre()

    def test_add_new_book_add_already_added_book_not_duplicate(
            self, valid_book_zombies):
        '''Невозможно повторно добавить уже имеющуюся книгу.'''
        for _ in range(2):
            self.collector.add_new_book(valid_book_zombies)
        assert len(self.collector.get_books_genre()) == 1

    def test_add_new_book_add_book_new_book_without_genre(
            self, valid_book_zombies):
        '''Добавленная книга не имеет жанра.'''
        self.collector.add_new_book(valid_book_zombies)
        assert not self.collector.get_book_genre(valid_book_zombies)

    def test_set_book_genre_valid_genre_assigned(
            self, valid_book_zombies, default_genres):
        '''Книге можно присвоить один из доступных жанров.'''
        self.collector.add_new_book(valid_book_zombies)
        valid_genre = random.choice(default_genres)
        self.collector.set_book_genre(valid_book_zombies, valid_genre)
        assert self.collector.get_book_genre(valid_book_zombies) == valid_genre

    def test_set_book_genre_invalid_genre_not_assigned(
            self, valid_book_zombies, default_genres, invalid_genre):
        '''Книге невозможно присвоить недоступный жанр.'''
        self.collector.add_new_book(valid_book_zombies)
        assert invalid_genre not in default_genres
        self.collector.set_book_genre(valid_book_zombies, invalid_genre)
        assert self.collector.get_book_genre(valid_book_zombies) == ''

    def test_set_book_genre_missing_book_cant_assign_genre(
            self, valid_book_zombies, default_genres):
        '''Книге, отсутствующей в приложении, невозможно присвоить жанр.'''
        valid_genre = random.choice(default_genres)
        self.collector.set_book_genre(valid_book_zombies, valid_genre)
        assert self.collector.get_book_genre(valid_book_zombies) is None

    def test_get_book_genre_correct_genre_by_book_title(
            self, valid_book_zombies, default_genres):
        '''Получить корректный жанр книги по её названию.'''
        self.collector.add_new_book(valid_book_zombies)
        valid_genre = random.choice(default_genres)
        self.collector.set_book_genre(valid_book_zombies, valid_genre)
        assert self.collector.get_book_genre(valid_book_zombies) == valid_genre

    def test_get_books_with_specific_genre_get_all_books_same_genre(
            self, valid_book_zombies, valid_book_cat, valid_book_john,
            default_genres):
        '''Получить все книги одного жанра.'''
        genre_get, genre_leave = random.sample(default_genres, 2)
        books_genres = (
            (valid_book_zombies, genre_get),
            (valid_book_cat, genre_get),
            (valid_book_john, genre_leave)
        )
        for title, genre in books_genres:
            self.collector.add_new_book(title)
            self.collector.set_book_genre(title, genre)
        assert (
            len(self.collector.get_books_with_specific_genre(genre_get)) == 2
        )

    def test_get_books_with_specific_genre_get_invalid_genre_empty_list(
            self, valid_book_zombies, default_genres, invalid_genre):
        '''Невозможно получить книги несуществующего жанра.'''
        valid_genre = random.choice(default_genres)
        self.collector.add_new_book(valid_book_zombies)
        self.collector.set_book_genre(valid_book_zombies, valid_genre)
        assert not self.collector.get_books_with_specific_genre(invalid_genre)

    def test_get_books_genre_get_all_books(
            self, valid_book_zombies, valid_book_cat):
        '''Получить все книги, содержащиеся в словаре books_genre.'''
        for title in valid_book_zombies, valid_book_cat:
            self.collector.add_new_book(title)
        assert len(self.collector.get_books_genre()) == 2

    def test_get_books_for_children_only_not_in_genre_age_rating_books(
            self, valid_book_zombies, valid_book_cat, default_genres,
            default_genres_age_rating):
        '''Получить все книги без возрастных ограничений.'''
        age_rating = random.choice(default_genres_age_rating)
        while (
            (not_age_rating := random.choice(default_genres)) in
            default_genres_age_rating
        ): pass
        books_genres = (
            (valid_book_zombies, not_age_rating),
            (valid_book_cat, age_rating),
        )
        for title, genre in books_genres:
            self.collector.add_new_book(title)
            self.collector.set_book_genre(title, genre)
        books_for_children = self.collector.get_books_for_children()
        assert (
            len(books_for_children) == 1 and
            self.collector.get_book_genre(books_for_children[0]) not in
            self.collector.genre_age_rating
        )

    def test_add_book_in_favorites_valid_book_added_to_favorites(
            self, valid_book_zombies):
        '''Cуществующая книга добавляется в избранное.'''
        self.collector.add_new_book(valid_book_zombies)
        self.collector.add_book_in_favorites(valid_book_zombies)
        favorites = self.collector.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == valid_book_zombies

    def test_add_book_in_favorites_missing_book_not_added_to_favorites(
            self, valid_book_zombies):
        '''Невозможно добавить в избранное отсутствующую книгу.'''
        self.collector.add_book_in_favorites(valid_book_zombies)
        assert not self.collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_same_book_not_added_to_favorites(
            self, valid_book_zombies):
        '''Невозможно повторно добавить одну и ту же книгу в избранное.'''
        self.collector.add_new_book(valid_book_zombies)
        for _ in range(2):
            self.collector.add_book_in_favorites(valid_book_zombies)
        assert len(self.collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_existing_book_removed(
            self, valid_book_zombies):
        '''Успешное удаление имеющейся книги из избранного.'''
        self.collector.add_new_book(valid_book_zombies)
        self.collector.add_book_in_favorites(valid_book_zombies)
        self.collector.delete_book_from_favorites(valid_book_zombies)
        assert not self.collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_unexisting_book_favorites_not_chenged(
            self, valid_book_zombies, valid_book_cat):
        '''Попытка удалить книгу, отсутствующую в избранном, не изменяет состав
        книг в избранном.'''
        self.collector.add_new_book(valid_book_zombies)
        self.collector.add_book_in_favorites(valid_book_zombies)
        self.collector.delete_book_from_favorites(valid_book_cat)
        assert len(self.collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_got_all_books(
            self, valid_book_zombies, valid_book_cat, valid_book_john):
        '''Получить все книги, находящиеся в избранном.'''
        for title in valid_book_zombies, valid_book_cat, valid_book_john:
            self.collector.add_new_book(title)
        for title in valid_book_zombies, valid_book_cat:
            self.collector.add_book_in_favorites(title)
        favorites = self.collector.get_list_of_favorites_books()
        assert (
            len(favorites) == 2 and favorites[0] == valid_book_zombies and
            favorites[1] == valid_book_cat
        )
