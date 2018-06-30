import base64

from django.test import TestCase
from django.contrib.auth.models import User

from mixer.backend.django import mixer

from apps.child.models import Parent, Child


class ChildTest(TestCase):
    """
    Тесты для апи детей.
    Проверяет:
        1) создание детей, используя разный набор
           корректных и некорректных входных данных
    """

    def setUp(self):
        User.objects._create_user(username='jack', password='secret', email='jack@jack.com')
        mixer.cycle(3).blend(Parent)
        child = mixer.blend(Child)
        picture = base64.b64encode(child.photo.file.read()).decode()
        self.child_base = {'first_name': 1, 'last_name': 1, 'photo': picture}
        self.child_data = [
            ({'gender': 1, 'date_of_birth': '2005-12-19', 'parents': [1, 2]}, 201),
            ({'gender': 41, 'date_of_birth': '2005-12-20'}, 400),
            ({'gender': 2, 'date_of_birth': '2005-12-21', 'parents': [1, 250]}, 400),
            ({'gender': 2, 'date_of_birth': '2005.12-22'}, 400),
            ({'gender': 1, 'date_of_birth': '2005-12-23'}, 201),
            ({'gender': 1, 'date_of_birth': '2005-12-24', 'is_studying': 1}, 201),
            ({'gender': 1, 'date_of_birth': '2005-12-25', 'is_studying': 32}, 400),
            ({'gender': 1, 'date_of_birth': '2005-12-26', 'is_studying': 'da'}, 400),
        ]

    def test_create_api(self):
        self.client.login(username='jack', password='secret')

        for data, status_code in self.child_data:
            data.update(**self.child_base)
            response = self.client.post(path='/api/v1/child/child/', data=data)
            self.assertEqual(response.status_code, status_code, response.data)

        data, _ = self.child_data[0]
        data.update(**self.child_base)
        data['photo'] = 'da1231daw12'
        response = self.client.post(path='/api/v1/child/child/', data=data)
        self.assertEqual(response.status_code, 400, response.data)
