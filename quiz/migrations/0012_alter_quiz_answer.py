# Generated by Django 4.0.3 on 2022-10-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_alter_userinfo_mobile_alter_userinfo_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='answer',
            field=models.CharField(choices=[('a', 'Option A'), ('b', 'Option B'), ('c', 'Option C'), ('d', 'Option D')], max_length=4),
        ),
    ]