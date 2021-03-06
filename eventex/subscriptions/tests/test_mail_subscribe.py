from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase


class SubscribePostValidEmail(TestCase):

    def setUp(self):
        data = dict(name="Henrique Bastos", cpf='12345678901', email='henrique@bastos.net', phone='21-99618-6180')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expected = 'Confirmação de inscrição'

        self.assertEqual(expected, self.email.subject)

    def test_subscription_email_from(self):
        expected = 'contato@eventex.com.br'

        self.assertEqual(expected, self.email.from_email)

    def test_subscription_email_to(self):
        expected = ['contato@eventex.com.br', 'henrique@bastos.net']

        self.assertEqual(expected, self.email.to)

    def test_subscription_email_body(self):

        contents = [
            'Henrique Bastos',
            '12345678901',
            'henrique@bastos.net',
            '21-99618-6180',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
