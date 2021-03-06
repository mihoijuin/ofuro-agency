from django.db import models


class OfuroResult(models.Model):
    result_id = models.CharField(max_length=20, primary_key=True)
    staff_name = models.CharField(max_length=20)
    image_L = models.ImageField(upload_to='images/', null=True, blank=True)
    image_S = models.ImageField(upload_to='images/', null=True, blank=True)
    share_text = models.CharField(max_length=100)

    def __str__(self):
        return self.staff_name


class GuestIntroduce(models.Model):
    result = models.ForeignKey(OfuroResult, on_delete=models.CASCADE)
    introduce_url = models.CharField(max_length=500)
    introduce_text = models.CharField(max_length=50)

    def __str__(self):
        return self.introduce_text
