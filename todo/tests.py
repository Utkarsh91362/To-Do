from django.test import TestCase
from django.urls import reverse
from .models import Todo
from .forms import TodoForm

class TodoAppTests(TestCase):

    def test_todo_addition(self):
        """Test that a new todo can be added."""
        response = self.client.post(reverse('add'), {'text': 'Test Todo'})
        self.assertEqual(response.status_code, 302)  # Should redirect after adding
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.first().text, 'Test Todo')

    def test_todo_complete(self):
        """Test that a todo can be marked as completed."""
        todo = Todo.objects.create(text='Incomplete Todo')
        response = self.client.get(reverse('complete', args=[todo.id]))
        todo.refresh_from_db()
        self.assertTrue(todo.complete)
        self.assertEqual(response.status_code, 302)  # Should redirect after completion

    def test_delete_completed(self):
        """Test that completed todos can be deleted."""
        todo = Todo.objects.create(text='Completed Todo', complete=True)
        response = self.client.get(reverse('deletecomplete'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 0)

    def test_delete_all(self):
        """Test that all todos can be deleted."""
        Todo.objects.create(text='Todo 1')
        Todo.objects.create(text='Todo 2')
        response = self.client.get(reverse('deleteall'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 0)

    def test_form_validation(self):
        """Test that the form properly validates input."""
        form = TodoForm(data={'text': ''})
        self.assertFalse(form.is_valid())  # Should be invalid because text is required

    def test_index_page_load(self):
        """Test that the index page loads successfully."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Anything to Add?')
