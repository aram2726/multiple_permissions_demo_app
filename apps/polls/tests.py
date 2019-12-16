import pytest

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory

from multiple_permissions.middlewares import PermissionMiddleware

from .views import PollsListView, PollsCreateView

pytestmark = pytest.mark.django_db


class SimpleTest:
    def __init__(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret', is_superuser=True, is_staff=True)

    @pytestmark
    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/polls')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user
        PermissionMiddleware(object).process_view(request, PollsListView, [], {})
        response = PollsListView.as_view()(request)
        assert response.status_code == 200

    @pytestmark
    @pytest.mark.xfail
    def test_to_fail(self):
        request = object
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Use this syntax for class-based views.
        response = PollsCreateView.as_view()(request)
        PermissionMiddleware(object).process_view(request, PollsCreateView, [], {})
        assert response.status_code == 200
