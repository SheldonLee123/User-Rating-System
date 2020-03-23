from django.contrib import admin
from .models import module, professor, relation, user_rating

admin.site.register(module)
admin.site.register(professor)
admin.site.register(relation)
admin.site.register(user_rating)