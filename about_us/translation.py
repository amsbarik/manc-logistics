from modeltranslation.translator import register, TranslationOptions

from .models import About, WorkingProcess, ExpertTeam


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('heading', 'short_description', 'mission', 'vision',
              
               'feature_01', 
               'feature_02',
               'feature_03',
               'feature_04',
               'feature_05',
               'feature_06',
               'feature_07',
               )



@register(WorkingProcess)
class WorkingProcessTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description')



@register(ExpertTeam)
class ExpertTeamTranslationOptions(TranslationOptions):
    fields = ('name', 'designation')


