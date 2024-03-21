from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Tag)
admin.site.register(PostTag)
admin.site.register(PostLike)
admin.site.register(ReplyLike)

