from django.test import TestCase, Client


class TestClient(TestCase):
    c = Client()
    response = c.post('/signup/', {username='Mike', email='mike@mike.com', password='mike1'})
    self.asserEqual(response.status_code, 200)
