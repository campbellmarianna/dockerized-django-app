from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from workout.models import Workout

from . import views

class APITests(TestCase):
    def test_api_status_code(self):
            response = self.client.get('/api/')
            self.assertEqual(response.status_code, 200)

    def test_workouts_list_status_code(self):
            response = self.client.get('/api/workout/')
            self.assertEqual(response.status_code, 200)
