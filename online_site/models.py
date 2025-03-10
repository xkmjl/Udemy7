from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True, validators=[MinValueValidator(14),
                                                                              MaxValueValidator(70)])
    phone_number =  PhoneNumberField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    STATUS_CHOICES = (
        ('student', 'student'),
        ('teacher', 'teacher')
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='student')
    date_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ManyToManyField(Category, related_name='course_category')
    COURSE_LEVEL = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвиунтый')
    )
    level = models.CharField(max_length=32, choices=COURSE_LEVEL)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    course_image = models.ImageField(upload_to='course_images/')

    def __str__(self):
        return self.course_name

    def get_avg_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(),1)
        return 0

    def get_count_people(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return ratings.count()
        return 0



class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField(null=True, blank=True)
    content = models.FileField(null=True,blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_lesson')

    def __str__(self):
        return f'{self.course}, {self.title}'


class Assignment(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_assignment')
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Exam(models.Model):
    title = models.CharField(max_length=32)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self):
        return self.title



class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam_question')
    question = models.CharField(max_length=100)
    passing_score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                                 MaxValueValidator(10)])

    def __str__(self):
        return f'{self.exam}, {self.question}'


class Option(models.Model):
    question_option = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_option')
    variant = models.CharField(max_length=100)
    check_variant = models.BooleanField()

    def __str__(self):
        return  f'{self.variant}, {self.check}'


class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_url = models.FileField(upload_to='certificates/')

    def __str__(self):
        return f'{self.student}, {self.course}'


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    stars = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 5)])

    def __str__(self):
        return f'{self.user}, {self.course}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.course}'