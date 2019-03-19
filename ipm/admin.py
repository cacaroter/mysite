from django.contrib import admin
from .models import User
from .models import ProjectInfo
from .models import Dict
from .models import InvoiceTracking
from .models import WorkDaily
from .models import DicDetail


class WorkDailyAdmin(admin.ModelAdmin):
    list_filter = ['startDate']
    list_display = ('projectName', 'description', 'finish', 'remark')


class DictInLine(admin.TabularInline):
    model = DicDetail
    extra = 1


class DictAdmin(admin.ModelAdmin):
    inlines = [DictInLine]
    search_fields = ['item']


# Register your models here.
# admin.site.register(User)
admin.site.register(ProjectInfo)
admin.site.register(Dict, DictAdmin)
admin.site.register(DicDetail)
admin.site.register(InvoiceTracking)
admin.site.register(WorkDaily, WorkDailyAdmin)

