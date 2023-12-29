import django
django.setup()

from django.test import TestCase
from django.utils import timezone
from .models import Question
import datetime

class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        old_time = timezone.now() - datetime.timedelta(days=2)
        old_question = Question(pub_date=old_time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        recent_time = timezone.now() - datetime.timedelta(hours=23)
        recent_question = Question(pub_date=recent_time)
        self.assertIs(recent_question.was_published_recently(), True)
