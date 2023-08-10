from django.test import TestCase
from django.urls import reverse


class Test(TestCase):
    def test_index(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_error_404(self):
        url = reverse('index') + 'error_404'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # def test_error_500(self):
    #     url = reverse('index')
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, 500)
