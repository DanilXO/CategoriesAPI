from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from categoriestree.models import Category

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)