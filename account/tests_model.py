from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='test1', password=make_password(password='Test@1235'))
        self.user2 = User.objects.create(username='test2', password=make_password(password='Test@1234'), email='test2@gmail.com')

    def test_user_created(self):
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(self.user1.username, 'test1')
        self.assertEqual(self.user2.email, 'test2@gmail.com')

    def test_password_is_hashed(self):
        self.assertTrue(check_password('Test@1235', self.user1.password))

    def test_unique_username(self):
        with self.assertRaises(Exception):
            User.objects.create(username='test1', password=make_password('Test@1235'))
    
    def test_authentication(self):
        user = User.objects.get(username='test1')
        self.assertIsNotNone(self.user1)
        self.assertTrue(user.check_password('Test@1235'))
    
    def test_inactive_user(self):
        self.user2.is_active = False
        self.user2.save()
        self.assertFalse(self.user2.is_active)
    
    def test_super_user(self):
        superuser = User.objects.create_superuser(username='admin', email='admin@nic.in',
                                                   password=make_password('Admin@123'))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

        
    