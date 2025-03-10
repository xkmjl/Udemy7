from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user')
router.register(r'lesson', LessonViewSet, basename='lessons')
router.register(r'assignment', AssignmentViewSet, basename='assignments')
router.register(r'certificate', CertificateViewSet, basename='certificates')

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('course/', CourseListAPIVew.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('course/create/', CourseCreateAPIView.as_view(), name='course_create'),
    path('exam/', ExamListAPIView.as_view(), name='exam_list'),
    path('exam/<int:pk>', ExamDetailAPIView.as_view(), name='exam_detail'),
    path('question/', QuestionListAPIView.as_view(), name='question_list'),
    path('question/<int:pk>', QuestionDetailAPIView.as_view(), name='question_detail'),
    path('option/', OptionListAPIView.as_view(), name='option_list'),
    path('option/<int:pk>', OptionDetailAPIView.as_view(), name='option_detail'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('assignment/create/', AssignmentCreateAPIView.as_view(), name='assignment_create'),
    path('review/', ReviewListAPIView.as_view(), name='review_list'),
    path('review/<int:pk>', ReviewDetailAPIView.as_view(), name='review_detail'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review_create'),
]
