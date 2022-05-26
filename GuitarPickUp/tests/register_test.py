from django.test import TestCase

# Create your tests here.



from django.contrib.auth.models import User
from ..models import *

class register_test(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

    def test_user(self):
        self.assertEqual(self.user.username ,"testuser")


