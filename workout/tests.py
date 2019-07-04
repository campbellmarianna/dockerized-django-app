from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse


from .models import Workout

from . import views

class WebsiteTests(TestCase):

    def test_index_page_status_code(self):
        response = self.client.get('/workouts')
        self.assertEquals(response.status_code, 301) # Permanent Redirect

    def test_admin_page_status_code(self):
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 302) # Found
