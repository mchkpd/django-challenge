from django.core.cache import cache

import pytest

from example_app.models import Category


@pytest.mark.django_db
def test_dummy():
    cache.clear()
    assert Category.objects.exists() is False
