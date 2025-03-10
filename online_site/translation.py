from .models import *
from modeltranslation.translator import register,TranslationOptions

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('question', )

@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('variant', )

