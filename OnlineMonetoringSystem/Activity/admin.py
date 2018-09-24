from django.contrib import admin
from Activity.models import Pending_Activity,Comments_Activity
from .forms import Dashboard_Comment_Form

# Register your models here.

# class Pending_ActivityAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         obj.Assigned_By = request.user.username
#         obj.Assigned_By.save()
#         super().save_model(request, obj, form, change)

# class Comments_ActivityAdmin(admin.ModelAdmin):
#     list_display = ('to','comment','commented_by')
#     actions = None
#
#     def save_model(self, request, obj, form, change):
#         if not obj.commented_by:
#             obj.commented_by = request.user
#         obj.save()
admin.site.register(Pending_Activity)
admin.site.register(Comments_Activity)
