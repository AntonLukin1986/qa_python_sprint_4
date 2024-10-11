from main import BooksCollector

# pytest -v file_name.py::TestClassName::test_method_name
class TestBooksCollector:
    '''Набор тестов для покрытия приложения BooksCollector.'''

    def test_init_create_object_books_genre_empty_dict(self):
        '''Создание объекта класса: словарь books_genre пустой.'''
        collector = BooksCollector()
        books_genre = collector.books_genre
        assert isinstance(books_genre, dict) and not books_genre

    def test_init_create_object_favorites_empty_list(self):
        '''Создание объекта класса: список favorites пустой.'''
        collector = BooksCollector()
        favorites = collector.favorites
        assert isinstance(favorites, list) and not favorites

    def test_init_create_object_genre_list_has_5_names(self):
        '''Создание объекта класса: список genre содержит пять жанров.'''
        collector = BooksCollector()
        genre = collector.genre
        default_genres = [
            'Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'
        ]
        assert isinstance(genre, list) and genre == default_genres

    def test_init_create_object_genre_age_rating_list_has_2_names(self):
        '''Создание объекта класса: список genre_age_rating содержит два
        жанра.'''
        collector = BooksCollector()
        genre_age_rating = collector.genre_age_rating
        default_genres_age_rating = ['Ужасы', 'Детективы']
        assert (
            isinstance(genre_age_rating, list) and
            genre_age_rating == default_genres_age_rating
        )

    def test_add_new_book_add_2_books_added_2(self):
        '''Корректное добавление двух книг.'''
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_book_with_title_41_chars_not_added(self):
        '''Книга с названием длиной 41 символ не добавляется.'''
        collector = BooksCollector()
        collector.add_new_book('КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаК')
        assert not collector.get_books_genre()

    def test_add_new_book_add_book_which_already_added_not_duplicate(self):
        '''Повторное добавление уже имеющейся книги не приводит к образованию
        дубликата.'''
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_add_book_genre_not_defined(self):
        '''При добавлении книги её жанр не определён.'''
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert (
            collector.get_book_genre('Гордость и предубеждение и зомби') == ''
        )

    def test_set_book_genre_valid_genre_for_book_success(self):
        '''Для книги можно установить один из доступных жанров.'''
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert (
            collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'
        )

    def test_set_book_genre_invalid_genre_for_book_empty_string(self):
        '''Для книги нельзя установить недопустимый жанр.'''
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Мюзикл')
        assert (
            collector.get_book_genre('Гордость и предубеждение и зомби') == ''
        )

    def test_get_book_genre_genre_assigned_to_book_success(self):
        '''Получить жанр, присвоенный книге.'''
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert (
            collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'
        )

    def test_get_books_with_specific_genre_fantastic_genre_got_2_books(self):
        '''Получить две книги в жанре "Фантастика".'''
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        assert (
            len(collector.get_books_with_specific_genre('Фантастика')) == 2
        )

    def test_get_books_with_specific_genre_invalid_genre_got_no_books(self):
        '''Получить пустой список книг в жанре "Мюзикл".'''
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert not collector.get_books_with_specific_genre('Мюзикл')

    def test_get_books_genre_has_2_books_got_2_books(self):
        '''Получить словарь books_genre, содержащий обе имеющиеся книги.'''
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        assert len(collector.get_books_genre()) == 2

    def test_get_books_for_children_fantastic_genre_included_in_result(self):
        '''Книга в жанре "Фантастика" попадает в выборку для детей.'''
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert (
            len(books_for_children) == 1 and
            collector.get_book_genre(books_for_children[0]) not in collector.genre_age_rating
        )

    def test_get_books_for_children_horror_genre_not_included_in_result(self):
        '''Книга в жанре "Ужасы" не попадает в выборку для детей.'''
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert not books_for_children

    def test_add_book_in_favorites_add_valid_book_to_favorites_sucsess(self):
        '''Добавить существующую книгу в избранное, если её ещё нет в избранном.'''
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        favorites = collector.get_list_of_favorites_books()
        assert (
            favorites == 1 and favorites[0] == 'Что делать, если ваш кот хочет вас убить'
        )

    def test_add_book_in_favorites_add_invalid_book_to_favorites_unsucsess(self):
        '''Невозможно добавить несуществующую книгу в избранное.'''
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert not collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_add_same_book_to_favorites_again_unsucsess(self):
        '''Невозможно повторно добавить одну и ту же книгу в избранное.'''
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_remove_existing_book_sucsess(self):
        '''Возможно удалить имеющуюся книгу из избранного.'''
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert not collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_remove_invalid_book_favorites_not_changed(self):
        '''Попытка удалить книгу, отсутствующую в избранном не изменяет список избранного.'''
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_2_books_got_2_books(self):
        '''Получить список из двух книг, имеющихся в избранном.'''
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books()[0] == 'Что делать, если ваш кот хочет вас убить'
