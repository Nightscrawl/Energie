from django.test import TestCase
from django.test import Client
from .models import *
from .forms import *
from .views import *
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
# Use information from models


class ExerciseTypeTest(TestCase):
   def test_string(self):
       type = ExerciseType(exerciseTypeName = "Running")
       self.assertEqual(str(type), type.exerciseTypeName)

   def test_table(self):
       self.assertEqual(str(ExerciseType._meta.db_table), "exercisetype")


class ExerciseTest(TestCase):
    def setup(self):
        self.test_user = User.objects.create_user(username="testuser1", password="P@ssw0rd1")
        type = ExerciseType(exerciseTypeName = "Running")
        exer = Exercise(exerciseName = "training hard", exerciseType = type, user = self.test_user, exerciseDate = "2020-06-18", exerciseDurationMinutes = 20, exerciseNotes = "exercise notes placeholder")
        return exer

    def test_type(self):
        exer = self.setup()
        self.assertEqual(str(exer.exerciseType), "Running")

    def test_string(self):
        exer = self.setup()
        self.assertEqual(str(exer.exerciseNotes), "exercise notes placeholder")
        # self.assertEqual(str(exer.exerciseNotes), "fake excercise notes")   # uncomment to see test failure

    def test_table(self):
        self.assertEqual(str(Exercise._meta.db_table), "exercise")


# testing basic views ----------

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
  
class getExerciseTypesTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse("extypes"))
       self.assertEqual(response.status_code, 200)

class getExercisesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("exercises"))
        self.assertEqual(response.status_code, 200)


class New_Exercise_test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username="testuser1", password="P@ssw0rd1")
        type = ExerciseType.objects.create(exerciseTypeName = "Running")
        self.exer = Exercise.objects.create(exerciseName = "training hard", exerciseType = type, user = self.test_user, exerciseDate = "2020-06-18", exerciseDurationMinutes = "20", exerciseNotes = "exercise notes placeholder")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse("newexercise"))
        self.assertRedirects(response, "/accounts/login/?next=/eapp/newexercise/")

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username="testuser1", password="P@ssw0rd1")
        response=self.client.get(reverse("newexercise"))
        self.assertEqual(str(response.context["user"]), "testuser1")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "eapp/newexercise.html")


class New_Exercise_Form_test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username="testuser1", password="P@ssw0rd1")
        self.type = ExerciseType.objects.create(exerciseTypeName = "Running")

    def test_UserForm_valid(self):
        form = ExerciseForm(data={'exerciseName': "training hard", 'exerciseType': self.type, 'user': self.test_user, 'exerciseDate': "2020-06-18", 'exerciseDurationMinutes': "20", 'exerciseNotes': "exercise notes placeholder"})
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid(self):
        form = ExerciseForm(data={'exerciseName': "", 'exerciseType': "", 'user': "", 'exerciseDate': "", 'exerciseDurationMinutes': "", 'exerciseNotes': ""})
        self.assertFalse(form.is_valid())
