# QA-Python. Спринт 4

## Для покрытия класса _BooksCollector_ реализованы следующие тесты

<ol>
  <li><strong>test_init_books_genre_empty_dict:</strong> проверяет, что словарь books_genre пустой у созданного объекта приложения</li>
  <li><strong>test_init_favorites_empty_list:</strong> проверяет, что список favorites пустой у созданного объекта приложения</li>
  <li><strong>test_init_genre_list_contains_default_genres:</strong> проверяет, что список genre содержит жанры по умолчанию</li>
  <li><strong>test_init_genre_age_rating_list_contains_default_genres_age_rating:</strong> проверяет, что список genre_age_rating содержит жанры возрастных ограничений по умолчанию</li>
  <li><strong>test_add_new_book_add_2_books_added_2:</strong> проверяет успешное добавление двух книг</li>
  <li><strong>test_add_new_book_add_invalid_book_not_added:</strong> проверяет, что книги с недопустимыми названиями не добавляются</li>
  <li><strong>test_add_new_book_add_already_added_book_not_duplicate:</strong> проверяет, что невозможно повторно добавить уже имеющуюся книгу</li>
  <li><strong>test_add_new_book_add_book_new_book_without_genre:</strong> проверяет, что добавленная книга не имеет жанра</li>
  <li><strong>test_set_book_genre_valid_genre_assigned:</strong> проверяет, что книге можно присвоить один из доступных жанров</li>
  <li><strong>test_set_book_genre_invalid_genre_not_assigned:</strong> проверяет, что книге невозможно присвоить недоступный жанр</li>
  <li><strong>test_set_book_genre_missing_book_cant_assign_genre:</strong> проверяет, что книге, отсутствующей в приложении, невозможно присвоить жанр</li>
  <li><strong>test_get_book_genre_correct_genre_by_book_title:</strong> проверяет, что можно получить корректный жанр книги по её названию</li>
  <li><strong>test_get_books_with_specific_genre_get_all_books_same_genre:</strong> проверяет корректное получение всех книг одного жанра</li>
  <li><strong>test_get_books_with_specific_genre_get_invalid_genre_empty_list:</strong> проверяет, что невозможно получить книги несуществующего жанра</li>
  <li><strong>test_get_books_genre_get_all_books:</strong> проверяет, что можно получить все книги, содержащиеся в словаре books_genre</li>
  <li><strong>test_get_books_for_children_only_not_in_genre_age_rating_books:</strong> проверяет, что в выборку "для детей" попадают только книги без возрастных ограничений</li>
  <li><strong>test_add_book_in_favorites_valid_book_added_to_favorites:</strong> проверяет, что существующая книга добавляется в избранное</li>
  <li><strong>test_add_book_in_favorites_missing_book_not_added_to_favorites:</strong> проверяет, что невозможно добавить в избранное отсутствующую книгу</li>
  <li><strong>test_add_book_in_favorites_same_book_not_added_to_favorites:</strong> проверяет, что невозможно повторно добавить одну и ту же книгу в избранное</li>
  <li><strong>test_delete_book_from_favorites_existing_book_removed:</strong> проверяет успешное удаление имеющейся книги из избранного</li>
  <li><strong>test_delete_book_from_favorites_unexisting_book_favorites_not_chenged:</strong> проверяет, что попытка удалить книгу, отсутствующую в избранном, не изменяет состав книг в избранном</li>
  <li><strong>test_get_list_of_favorites_got_all_books:</strong> проверяет корректное получение всех книг, находящихся в избранном</li>
</ol>
