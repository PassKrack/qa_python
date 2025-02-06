from main import BooksCollector
import pytest



class TestBooksCollector:

    @pytest.mark.parametrize('title',['Я', 'ВыходВыходВыходВыход', 'ВыходВыходВыходВыходВыходВыходВыходВыход' ])
    def test_add_new_book_add_new_book_with_valid_name(self, title):
        collector = BooksCollector()
        collector.add_new_book(title)
        assert collector.get_book_genre(name=title) == ''

    def test_set_book_genre_book_have_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    @pytest.mark.parametrize('title,genre', [('Гордость и предубеждение и зомби', 'Фантастика'), ('Что делать, если ваш кот хочет вас убить', 'Ужасы')])
    def test_get_book_genre_get_genre_by_book_name(self, title, genre):
        collector = BooksCollector()
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert collector.get_book_genre(title) == genre

    @pytest.mark.parametrize('title,genre', [('Гордость и предубеждение и зомби', 'Фантастика'),('Гарри Поттер и Тайная комната', 'Фантастика'),('Гарри Поттер и Кубок огня', 'Фантастика')])
    def test_get_books_with_specific_genre_all_books_with_fantasy_genre(self, title, genre):
        collector = BooksCollector()
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert collector.get_books_with_specific_genre(genre) == [title]

    def test_get_books_genre_books_genre_have_dict_format(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert type(collector.get_books_genre()) == dict

    @pytest.mark.parametrize('title,genre',[('Сказка о царе Салтане', 'Мультфильм'),('Алеша Попович и Тугарин змей', 'Мультфильм'),('Гордость и предубеждение и зомби', 'Ужасы')])
    def test_get_books_for_children_list_with_children_books(self, title, genre):
        collector = BooksCollector()
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        for i in collector.get_books_for_children():
            assert collector.get_book_genre(i) not in ['Ужасы', 'Детективы']

    def test_add_book_in_favorites_book_dont_add_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Сказка о царе Салтане')
        collector.add_new_book('Алеша Попович и Тугарин змей')
        collector.add_book_in_favorites('Гарри Поттер и Кубок огня')
        assert 'Гарри Поттер и Кубок огня' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_successfully_deletion_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Сказка о царе Салтане')
        collector.add_new_book('Гарри Поттер и Кубок огня')
        collector.add_book_in_favorites('Гарри Поттер и Кубок огня')
        collector.delete_book_from_favorites('Гарри Поттер и Кубок огня')
        assert 'Гарри Поттер и Кубок огня' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_two_books_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок')
        collector.add_new_book('Шрек')
        collector.add_new_book('Гарри Поттер и Кубок огня')
        collector.add_book_in_favorites('Гарри Поттер и Кубок огня')
        collector.add_book_in_favorites('Шерлок')
        assert len(collector.get_list_of_favorites_books()) == 2
