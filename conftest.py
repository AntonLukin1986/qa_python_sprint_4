import pytest


@pytest.fixture(scope='session')
def default_genres():
    '''Жанры книг, доступные по умолчанию.'''
    return ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']


@pytest.fixture(scope='session')
def default_genres_age_rating():
    '''Жанры книг, имеющие возрастное ограничение.'''
    return ['Ужасы', 'Детективы']


@pytest.fixture(scope='session')
def invalid_genre():
    '''Несуществующий жанр книг.'''
    return 'Мюзикл'


@pytest.fixture(scope='session')
def valid_book_zombies():
    '''Книга с допустимым названием про зомби.'''
    return 'Гордость и предубеждение и зомби'


@pytest.fixture(scope='session')
def valid_book_cat():
    '''Книга с допустимым названием про кота.'''
    return 'Что делать, если ваш кот хочет вас убить'


@pytest.fixture(scope='session')
def valid_book_john():
    '''Книга с допустимым названием про Джона.'''
    return 'В финале Джон умрёт'


@pytest.fixture(  # параметризированная фикстура
    scope='session',
    params=['', 'Книга' * 8 + 'К'],
    ids=['empty string', '41 chars']
)
def invalid_book_titles(request):
    return request.param
