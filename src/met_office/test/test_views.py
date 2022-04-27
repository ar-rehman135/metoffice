from django.urls import reverse
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from rest_framework import status
from src.users.test.factories import UserFactory

class TestMetOffice(APITestCase):
    """
    Tests /Met Office operations.
    """

    def setUp(self):
        self.url_get_records = reverse('get_records')
        self.user = UserFactory()
        tokens = self.user.get_tokens()
        access_token = tokens['access']
        self.url = reverse('user-detail', kwargs={'pk': self.user.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    def test_get_request_returns_a_given_user(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_metoffice_get_data(self):
        response = self.client.get(self.url_get_records)
        eq_(response.status_code, status.HTTP_200_OK)
        
        
    def test_get_all_data_succeeds(self):
        response = self.client.get(self.url_get_records)
        eq_(response.status_code, status.HTTP_200_OK)
        ok_(response.json()['data'][0]['jan'])
        
