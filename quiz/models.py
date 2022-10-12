from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length=12, null=True)
    profile_pic = models.ImageField(upload_to='profiles/', null=True)
    
    class Meta:
        db_table = "user_info"

    def __str__(self):
        return self.user_id.username
    
class Quiz(models.Model):
    q_id = models.AutoField(primary_key=True)
    question = models.TextField(null=False)
    option1 = models.CharField(max_length=100, null=False)
    option2 = models.CharField(max_length=100, null=False)
    option3 = models.CharField(max_length=100, null=False)
    option4 = models.CharField(max_length=100, null=False)
    answer = models.CharField(max_length=4, choices= (('a', 'Option A'), ('b', 'Option B'),
                                                        ('c', 'Option C'), ('d', 'Option D')), null=False)

    class Meta:
        db_table = "quiz"

    def __str__(self):
        return self.question

class Submission(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    q_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    sub_answer = models.CharField(max_length=4, choices= (('a', 'Option A'), ('b', 'Option B'),
                                                        ('c', 'Option C'), ('d', 'Option D')), null=True)
    is_correct = models.BooleanField(null=False, default=False)

    class Meta:
        db_table = "submission"

    def __str__(self):
        return f"{self.user_id} - {self.q_id}"
