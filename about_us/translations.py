from modeltranslation.translator import register, TranslationOptions

from .models import WorkingProcess, ExpertTeam



@register(ExpertTeam)
class WorkingProcessTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'order')

@register(ExpertTeam)
class ExpertTeamTranslationOptions(TranslationOptions):
    fields = ('name', 'designation')


