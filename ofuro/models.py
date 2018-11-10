from django.db import models


class OfuroResult(models.Model):
    result_id = models.CharField(max_length=20, primary_key=True)
    staff_name = models.CharField(max_length=20)
    image_url_L = models.CharField(max_length=200)
    image_url_S = models.CharField(max_length=200)
    share_text = models.CharField(max_length=100)

    def __str__(self):
        return self.staff_name


class GuestIntroduce(models.Model):
    result = models.ForeignKey(OfuroResult, on_delete=models.CASCADE)
    introduce_url = models.CharField(max_length=500, null=True)
    introduce_text = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.introduce_text
