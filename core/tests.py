from django.test import TestCase

<<<<<<< HEAD
=======
class TestPage(TestCase):
    def test_base(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

>>>>>>> 93a9b19... Long Time no C
# Create your tests here.
