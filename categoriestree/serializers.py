from django.db import transaction, IntegrityError
from rest_framework import serializers

from categoriestree.models import Category


class ItemSerializer(serializers.ModelSerializer):
    """
        Serializer для вывода вложенных элементов
    """
    class Meta:
        model = Category
        fields = ('id', 'name', 'children')

    def get_fields(self):
        fields = super().get_fields()
        fields['children'] = ItemSerializer(many=True, write_only=True, required=False)
        return fields


class CategorySerializer(serializers.ModelSerializer):
    """
        Serializer для Category model
    """
    children = ItemSerializer(many=True)
    parents = ItemSerializer(many=True, read_only=True)
    siblings = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'parents', 'children', 'siblings')

    def recursive_instance(self, parent, children):
        """
        Метод рекурсивно создающий или обновляющий дерево категорий
        :param parent: Родитель узла
        :param children: Потомки
        """
        for child in children:
            if child.get('children', None):
                new_parent, created = Category.objects.update_or_create(name=child.get('name'), parent=parent)
                self.recursive_instance(new_parent, child.get('children'))
            else:
                Category.objects.update_or_create(name=child.get('name'), parent=parent)

    def create(self, validated_data):
        """ Переопределенный метод создания """
        node, created = Category.objects.get_or_create(name=validated_data.get('name'))
        children = validated_data.get('children')
        try:
            with transaction.atomic():
                self.recursive_instance(parent=node, children=children)
        except IntegrityError as ex:
            print(ex)
        return node

    def update(self, instance, validated_data):
        """ Переопределенный метод обновления """
        instance.name = validated_data.get('name')
        instance.save()
        children = validated_data.get('children', None)
        if children:
            try:
                with transaction.atomic():
                    self.recursive_instanse(parent=instance, children=children)
            except IntegrityError as ex:
                print(ex)
        return instance
