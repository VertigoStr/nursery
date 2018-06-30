from django.test import TestCase
from django.contrib.auth.models import User

from mixer.backend.django import mixer

from apps.child.models import Parent, Child


class JournalTest(TestCase):
    """
    Тесты для апи журналов.
    Проверяет:
        1) наличие корректной связи между ребенок и родителем,
           т.е. родитель не может привести или забрать чужого ребенка.

        2) корректную фильтрацию журнала для детей, которые учатся и нет
    """

    def setUp(self):
        User.objects._create_user(username='tom', password='secret', email='tom@tom.com')
        mixer.cycle(3).blend(Parent)
        children = mixer.cycle(4).blend(
            Child,
            is_studying=mixer.sequence(*[True, False])
        )
        for child, parents in zip(children, [[1, 2], [], [3], [3]]):
            child.parents.set(parents)
            child.save()

        self.base = {'time': '12:19', 'date': '2012-02-03'}
        self.data = [
            ({'child': 1, 'action': 1, 'parent': 4}, 400),
            ({'child': 3, 'action': 32, 'parent': 3}, 400),
            ({'child': 2, 'action': 1, 'parent': 1}, 400),
            ({'child': 3, 'action': 1, 'parent': 3}, 201),
            ({'child': 1, 'action': 1, 'parent': 2}, 201),
            ({'child': 1, 'action': 1, 'parent': 2}, 201),
            ({'child': 4, 'action': 1, 'parent': 3}, 201),
            ({'child': 1, 'action': 1, 'parent': 3}, 400),
        ]

    def test_api(self):
        self.client.login(username='tom', password='secret')

        for data, status_code in self.data:
            data.update(**self.base)
            response = self.client.post(
                path='/api/v1/journal/journal/',
                data=data
            )
            self.assertEqual(response.status_code, status_code, response.data)

        for flag in [True, False]:
            response = self.client.get(
                path='/api/v1/journal/journal/',
                data={'is_studying': flag}
            )
            children_ids = [i['child'] for i in response.data.get('results')]
            count = Child.objects.filter(
                id__in=children_ids,
                is_studying=flag
            ).count()
            self.assertEqual(count, len(set(children_ids)), response.data)
