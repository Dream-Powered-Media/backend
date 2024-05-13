from django.contrib import admin

from .models import User
from .models import Media
from .models import MediaLink
from .models import Directory
from .models import Community
from .models import Role
from .models import Action
from .models import RoleRequest
from .models import AuthorRequest

admin.site.register(User)
admin.site.register(Media)
admin.site.register(MediaLink)
admin.site.register(Directory)
admin.site.register(Community)
admin.site.register(Role)
admin.site.register(Action)
admin.site.register(RoleRequest)
admin.site.register(AuthorRequest)
