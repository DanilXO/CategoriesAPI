from django.db import models
from django.utils.functional import cached_property
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.translation import ugettext_lazy as _


class Category(MPTTModel):
    name = models.CharField(max_length=60, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    @cached_property
    def parents(self):
        return self.get_ancestors(ascending=False, include_self=False).all()

    @cached_property
    def children(self):
        return self.get_children().all()

    @cached_property
    def siblings(self):
        return self.get_siblings(include_self=False).all()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    class MPTTMeta:
        order_insertion_by = ('name',)

    def __str__(self):
        return self.name
