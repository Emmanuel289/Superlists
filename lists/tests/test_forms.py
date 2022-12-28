from django.test import TestCase

from lists.forms import EMPTY_ITEM_ERROR, ItemForm


class ItemFormTest(TestCase):

    def test_form_item_input_has_placeholder_and_css_classes(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        # Check form validation using the form API is_valid
        self.assertFalse(form.is_valid())
        # calling is_valid returns True or False and also populates the errors attributes.
        # It's a dictionary mapping the names of fields to lists of errors for those fields.
        self.assertEqual(
            form.errors['text'],
            [EMPTY_ITEM_ERROR]
        )