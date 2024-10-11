# qa_python_sprint_4
setUp: создаёт новый экземпляр BooksCollector перед каждым тестом.
test_add_new_book: проверяет добавление новой книги.
test_add_new_book_invalid_length: проверяет, что книги не добавляются, если имя пустое или превышает 40 символов.
test_set_book_genre: проверяет корректную установку жанра книги.
test_set_book_genre_invalid_book: проверяет, что нельзя установить жанр несуществующим книгам.
test_set_book_genre_invalid_genre: проверяет, что нельзя установить несуществующий жанр.
test_get_book_genre: проверяет, что правильно возвращается жанр для указанной книги.
test_get_books_genre: проверяет возврат всего словаря книг.
test_get_books_for_children: проверяет, что возвращаются только доступные детям книги.
test_add_book_in_favorites: проверяет добавление книги в избранное.
test_add_book_in_favorites_not_exist: проверяет, что нельзя добавить несуществующую книгу в избранное.
test_delete_book_from_favorites: проверяет возможность удаления книги из избранного.
