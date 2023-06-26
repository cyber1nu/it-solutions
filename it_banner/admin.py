from django.contrib import admin

from it_banner.models import QueryModel


@admin.register(QueryModel)
class QueryModelAdmin(admin.ModelAdmin):
    """ for admin management of query model """
    pass
