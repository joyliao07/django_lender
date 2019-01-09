from django.test import TestCase, RequestFactory
from .models import Book


class TestBookModel(TestCase):
    """
    """
    def setUp(self):
        """
        """
        Book.objects.create(title='Test Book 1', author='author 1')
        Book.objects.create(title='Test Book 2', author='author 2')

    # def setUpClass(cls):
    #     """
    #     """
    #     pass

    def test_book_titles(self):
        """
        """
        one = Book.objects.get(title='Test Book 1')
        self.assertEqual(one.title, 'Test Book 1')

    def test_book_descriptions(self):
        """
        """
        books = Book.objects.all()
        self.assertEqual(books[1].author, 'author 2')

    def test_book_status(self):
        """
        """
        one = Book.objects.get(title='Test Book 1')
        two = Book.objects.get(title='Test Book 2')
        self.assertEqual(one.status, 'available')
        self.assertEqual(two.status, 'available')

    def test_create_new_book(self):
        """
        """
        new_book = Book.objects.create(title='new', author='')
        self.assertEqual(new_book.title, 'new')


class TestBookViews(TestCase):
    """
    """
    def setUp(self):
        """
        """
        self.request = RequestFactory()

        self.book = Book.objects.create(title='Test Book 1', author='author 1')
        Book.objects.create(title='Test Book 2', author='author 2')

    def test_list_view_context(self):
        """
        """
        from .views import book_list_view
        request = self.request.get('')
        response = book_list_view(request)
        self.assertIn(b'Test Book 1', response.content)

    def test_list_view_status(self):
        """
        """
        from .views import book_list_view
        request = self.request.get('')
        response = book_list_view(request)
        self.assertEqual(200, response.status_code)

    def test_detail_view_context(self):
        """
        """
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, self.book.id)
        self.assertIn(b'author 1', response.content)

    def test_detail_view_status_code_failure(self):
        """
        """
        from .views import book_detail_view
        from django.http import Http404
        request = self.request.get('')

        with self.assertRaises(Http404):
            book_detail_view(request, '0')
