from django.contrib import admin
from .models import Project,Skill,Contact,Category,Technology
# Register your models here.
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Technology)