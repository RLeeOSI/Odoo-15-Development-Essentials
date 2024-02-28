from odoo.tests.common import TransactionCase

class TestBook(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_manager = cls.env["res.users"].create({
            "name": "Library Manager",
            "login": "librarymanager",
            "email": "librarymanager@example.com",
            "groups_id": [(6, 0, cls.env.ref(
                "library_app.library_group_manager"
            ).ids)],
        })

    def setUp(self):
        super().setUp()
        self.Book = self.env["library.book"]
        self.book1 = self.Book.with_user(
            self.user_manager
        ).create({
            "name": "Odoo Development Essentials",
            "isbn": "879-1-78439-279-6"
        })

    def test_book_create(self):
        """New Books are active by default"""
        self.assertEqual(self.book1.with_user(
            self.user_manager
        ).active, True)

    def test_check_isbn(self):
        """Check Valid ISBN"""
        self.assertTrue(self.book1.with_user(
            self.user_manager
        )._check_isbn())
