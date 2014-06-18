# Cannot access database in setUpClass despite module level django\_db marker

Test classes like the below 

* pass when run with the normal django test runner
* fails when run with py.test

```python
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
```

This repo contains a full environment to run and repro the issue

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ pip install -e .
$ ./run_tests.sh
```
