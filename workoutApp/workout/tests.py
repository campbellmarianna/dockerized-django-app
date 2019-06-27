import datetime

from django.test import TestCase
from django.utils import timezone, reverse

from .models import Workout

# Model check whether idea works
# View checks website functionality
    # 200 if it is there end to end

# create workout with a date
class WorkoutModelTests(TestCase):
    def test_was_posted_recently_with_future_workout(self):
        """
        was_posted_recently() returns False for workouts whose post_date is
        in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_workout = Workout(post_date=time)
        self.assertIs(future_question.was_posted_recently(), False)

    def create_workout(day):
        """
        Create a workout with the given `day`.
        """
        time = timezone.now() + datetime.timedelta(day=day)
        return Workout.objects.create(day=day, post_date=time)

# once the workout is generated there should be three sets
    def test_has_three_sets(self):
        """
        Workout returns true if it has three workout sets otherwise return false.
        """
        # 1. Create a workout with three sets and save
        # 2. assertEqual workout.sets_set.count() == 3
        workout1 = Workout.objects.get(pk=1)
        workout2 = Workout.objects.get(pk=2)
        workout3 = Workout.objects.get(pk=3)
        self.assertEqual(workout.)


# test the workout index view, if there are no workouts post a message
