from rest_framework.serializers import ModelSerializer

from drf_extra_fields.fields import Base64ImageField

from apps.child.models import Child, Parent


class ParentSerializer(ModelSerializer):

    class Meta:
        model = Parent
        fields = ['id', 'first_name', 'last_name']


class ChildSerializer(ModelSerializer):
    photo = Base64ImageField()

    class Meta:
        model = Child
        fields = [
            'id', 'first_name', 'last_name', 'gender',
            'grade', 'photo', 'is_studying', 'parents',
            'date_of_birth'
        ]
