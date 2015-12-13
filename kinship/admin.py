from django.contrib import admin

# Register your models here.
from .models import Person
from .models import Kinship
from .models import Relationship

admin.site.register(Person)
admin.site.register(Kinship)
admin.site.register(Relationship)
