from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class UserProfileCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'content']



class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'



class AssignmentSerializer(serializers.ModelSerializer):
    due_date = serializers.DateTimeField(format='%d-%m-%Y %H-%M')

    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date',]



class AssignmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'



class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'title']




class OptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['variant', 'check_variant', ]




class OptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'



class QuestionListSerializer(serializers.ModelSerializer):
    question_option = OptionListSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['question', 'passing_score', 'question_option']



class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'



class ExamDetailSerializer(serializers.ModelSerializer):
    exam_question = QuestionListSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['title', 'duration', 'exam_question']




class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'




class ReviewCourseSerializer(serializers.ModelSerializer):
    user = UserProfileCourseSerializer()

    class Meta:
        model = Review
        fields = ['user', 'comment', 'stars']




class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']



class CourseCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'



class CourseListSerializer(serializers.ModelSerializer):
    created_by  = UserProfileCourseSerializer(read_only=True)
    avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_image','level','created_by',  'price','avg_rating', 'get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()



class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(many=True, read_only=True)
    created_by  = UserProfileCourseSerializer(read_only=True)
    avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H-%M')
    update_at = serializers.DateTimeField(format='%d-%m-%Y %H-%M')
    course_lesson = LessonSerializer(many=True, read_only=True)
    course_assignment = AssignmentSerializer(many=True, read_only=True)
    reviews = ReviewCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['course_name', 'category', 'description', 'course_image', 'level', 'created_by', 'price',
                  'created_at', 'update_at', 'avg_rating', 'get_count_people', 'course_lesson', 'course_assignment',
                  'reviews']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()



class CategoryDetailSerializer(serializers.ModelSerializer):
    course_category = CourseListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'course_category']


class ReviewListSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(read_only=True)
    user = UserProfileCourseSerializer()

    class Meta:
        model = Review
        fields = ['id', 'comment', 'stars', 'user', 'course',]


class ReviewDetailSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(read_only=True)
    user = UserProfileCourseSerializer()

    class Meta:
        model = Review
        fields = ['id', 'comment', 'stars', 'user', 'course', ]



class ReviewCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



