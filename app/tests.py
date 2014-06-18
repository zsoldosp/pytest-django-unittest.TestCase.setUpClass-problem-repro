from django.utils.unittest import TestCase
from django.utils.decorators import classonlymethod
from django.contrib.auth.models import Group
import pytest

pytestmark = pytest.mark.django_db


class SimpleTest(TestCase):

    @classonlymethod
    def setUpClass(cls):
        Group.objects.create(name='foo')

    @classonlymethod
    def tearDownClass(cls):
        Group.objects.all().delete()

    def test_needs_db(self):
        self.assertEqual(1, Group.objects.count())
