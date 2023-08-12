from django.db import models

class UserProfile(models.Model):
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    group_size = models.CharField(max_length=10000, choices=[('1', '소개팅'), ('2', '2명이서'), ('3', '3명이서'), ('4', '4명이서')])
    #extra = models.TextField()

    def __str__(self):
        #return f"{self.age}세 {self.get_gender_display()} {self.get_group_size_display()}"
        return f"{self.get_group_size_display()}"

    class Meta:
        verbose_name = "사용자 프로필"
        verbose_name_plural = "사용자 프로필"
