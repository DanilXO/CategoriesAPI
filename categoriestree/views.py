from rest_framework import viewsets

from categoriestree.models import Category
from categoriestree.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
        Category List:\n
            GET /categories/ - вывод всех текущих категорий в древовидном виде, согласно заданию.\n
            POST /categories/ - cоздать новый "узел" категорий \n
        Category Instance:\n
            PUT, PATCH /categories/<pk>/ - обновить текущий узел\n
            DELETE /categories/<pk>/ - удалить текущий узел\n
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
