from django.contrib import admin
from apps.clientes.models import Usuario
'''
from .models import Project
from .models import ProjectStatus
from .models import ProjecPermission
from .models import ProjectUser

class ProjectStatusInLine(admin.TabularInline):
    model = ProjectStatus
    extra = 0
    can_delete = False


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectStatusInLine, ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjecPermission)
admin.site.register(ProjectUser)
'''
admin.site.register(Usuario)
