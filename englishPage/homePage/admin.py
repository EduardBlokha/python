from django.contrib import admin
from .models import PostModel
from .models import DictionaryModel
# Register your models here.

class PanelAdminDictionary(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(DictionaryModel, PanelAdminDictionary)


@admin.register(PostModel)
class PanelAdmin(admin.ModelAdmin):
    list_display = ('title_book', 'mark_of_translate')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        is_staff = request.user.is_staff

        if not is_superuser and not is_staff:
            form.base_fields['mark_of_translate'].disabled = True
        return form




