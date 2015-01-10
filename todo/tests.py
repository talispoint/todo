from list.models import Todo
from django.test import TestCase
from django.core.exceptions import ValidationError

class TodoTests(TestCase):
	def test_todo_should_require_title(self):
		todo = Todo()
		self.assertRaises(ValidationError, todo.save)

	def test_todo_should_not_be_finished_after_creation(self):
		todo = Todo(title='Walk the dog.')
		self.assertEqual(todo.finished, False)