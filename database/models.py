from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table = "provinces"

class Regency(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    class Meta:
        db_table = "regencies"

class District(models.Model):
    name = models.CharField(max_length=50)
    regency = models.ForeignKey(Regency, on_delete=models.CASCADE)
    class Meta:
        db_table = "districts"

class SubDistrict(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    class Meta:
        db_table = "sub_districts"

class Village(models.Model):
    name = models.CharField(max_length=50)
    sub_district = models.ForeignKey(SubDistrict, on_delete=models.CASCADE)
    class Meta:
        db_table = "villages"