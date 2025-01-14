from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User

class RegistrationTest(TestCase):
    def setUp(self):
        self.registration_url = reverse('account:register')
        return super().setUp()
    
    def test_render_registration_form(self):
        response = self.client.get(self.registration_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'account/registration.html')
        self.assertIn('form', response.context)
    
    def test_valid_post_request(self):

        valid_data = {
            'username': 'test1',
            'password1': 'Best@1234',
            'password2': 'Best@1234'
        }

        response = self.client.post(self.registration_url, data=valid_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'test1')
        self.assertIn(f'User with username : {User.objects.first().username} created', response.content.decode())
    
    def test_invalid_post_request(self):
        invalid_data = {
            'username': 'test1',
            'password1': 'Test123',
            'password2': 'Test123'
        }

        response = self.client.post(self.registration_url, data=invalid_data)
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 400)
        # Check password if matches strong password condition and password1 = password2
        self.assertEqual()

# class ProfileViewTest()
        