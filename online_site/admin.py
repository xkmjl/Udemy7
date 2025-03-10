from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin
from .models import *
import nested_admin

class LessonInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Lesson
    extra = 1

class OptionInline(nested_admin.NestedStackedInline, TranslationInlineModelAdmin):
    model = Option
    extra = 1

class QuestionInline(nested_admin.NestedStackedInline, TranslationInlineModelAdmin):
    model = Question
    extra = 1
    inlines = [OptionInline]

@admin.register(Category, Assignment)
class AllAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    inlines = [LessonInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Exam)
class ExamAdmin(TranslationAdmin, nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(Certificate)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)
