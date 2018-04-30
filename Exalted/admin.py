# -'- coding: utf-8 -'-
from __future__ import unicode_literals

from django.contrib import admin

from .models.charm import Charm, Charm_type
from .models.requirement import Requirement, RequirementSet
from .models.artifact import Artifact
from .models.character import Character
from .models.exalted_type import Exalted_type, Exalted_subtype, HealthLevels, FavoredItems, KungfuCircle, MagicCircle
from .models.tag import Tag, Tag_category
from .models.healthlevel import HealthLevel, HealthLevelSet

from .views import *

admin.site.register(Charm)
admin.site.register(Requirement)
admin.site.register(RequirementSet)
admin.site.register(RequirementType)
admin.site.register(Artifact)
admin.site.register(Character)
admin.site.register(Exalted_type)
admin.site.register(Exalted_subtype)
admin.site.register(Charm_type)
admin.site.register(Tag)
admin.site.register(Tag_category)
admin.site.register(HealthLevels)
admin.site.register(FavoredItems)
admin.site.register(KungfuCircle)
admin.site.register(MagicCircle)
admin.site.register(HealthLevel)
admin.site.register(HealthLevelSet)
