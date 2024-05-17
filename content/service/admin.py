from django.contrib import admin

from .models import Profile
from .models import Media
from .models import MediaLink
from .models import Directory
from .models import Community
from .models import Role
from .models import Action
from .models import RoleRequest
from .models import AuthorRequest
from .models import Grade
from .models import UserAction
from .models import Relation

admin.site.register(Profile)
admin.site.register(Media)
admin.site.register(MediaLink)
admin.site.register(Directory)
admin.site.register(Community)
admin.site.register(Role)
admin.site.register(Action)
admin.site.register(RoleRequest)
admin.site.register(AuthorRequest)
admin.site.register(Grade)
admin.site.register(UserAction)
admin.site.register(Relation)
