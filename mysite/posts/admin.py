from django.contrib import admin

# Register your models here.
from .models import Posts
#
# from import_export.admin import  ImportExportModelAdmin
#
# # @admin.register(Posts)
# # class MyPosts(ImportExportModelAdmin):
# #     pass
#
# @admin.register(Posts)
# class edxUserAdmin(ImportExportModelAdmin):
#     pass





admin.site.register(Posts)