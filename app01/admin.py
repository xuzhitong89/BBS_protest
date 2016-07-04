#!coding=utf-8
from django.contrib import admin
from models import BBS,BBS_user,Category
# Register your models here.

class BBS_admin(admin.ModelAdmin):
    list_display = ('category','title','summary','author','signature','view_count','created_at')
#   Take care here.Though the 'category' is a foreign key,
#   you don't need to like the follow item "author__user__username".
#   The reason is simple, as you are not searching data from the foreign key table.
    list_filter = ('created_at',)
    search_fields = ('title','author__user__username')

    def signature(self,obj):
        return obj.author.signature
    signature.short_description = '描述'

    def category(self,obj):
        return obj.author.category
    category.short_description = '类别'

admin.site.register(BBS,BBS_admin)
admin.site.register(BBS_user)
admin.site.register(Category)