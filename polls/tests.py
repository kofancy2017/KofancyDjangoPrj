from django.test import TestCase
import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question

# Create your tests here.
#我们在这里做的是创建一个django.test.TestCase子类，它具有一个方法，该方法创建一个pub_date在未来的Question实例。然后我们检查was_published_recently()的输出 —— 它应该是 False.
class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """

        time = timezone.now()+datetime.timedelta(days=30)
        future_question =Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)


    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)


