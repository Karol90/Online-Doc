from django.contrib import admin
from worktimes.models import Worktime, WorktimeExclusions

admin.site.register(Worktime)
admin.site.register(WorktimeExclusions)