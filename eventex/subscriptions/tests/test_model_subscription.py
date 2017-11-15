from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Henrique Bastos',
            cpf='1234568901',
            email='henrique@bastos.net',
            phone='61-99618-6180'
        )
        self.obj.save()


    def test_create(self):
        self.assertTrue(Subscription.objects.exists())


    def test_created_at(self):
        """Subscription must heave an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)