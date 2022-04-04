from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    q_id = models.AutoField(primary_key=True)
    question = models.TextField(null=False)
    option1 = models.CharField(max_length=100, null=False)
    option2 = models.CharField(max_length=100, null=False)
    option3 = models.CharField(max_length=100, null=False)
    option4 = models.CharField(max_length=100, null=False)
    answer = models.CharField(max_length=4, choices= (('A', 'Option A'), ('B', 'Option B'),
                                                        ('C', 'Option C'), ('D', 'Option D')), null=False)

    class Meta:
        db_table = "quiz"

    def __str__(self):
        return self.question

class Submission(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    q_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    sub_answer = models.CharField(max_length=4, choices= (('A', 'Option A'), ('B', 'Option B'),
                                                        ('C', 'Option C'), ('D', 'Option D')), null=True)
    class Meta:
        db_table = "submission"

    def __str__(self):
        return f"{self.user_id} - {self.q_id}"
