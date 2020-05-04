from django.db import models

# Create your models here.
class Si(models.Model):
    si_name = models.CharField(max_length=20) # max_length는 필수 속성
    # content = models.TextField()


class Gu(models.Model):
    gu_name = models.CharField(max_length=20) # max_length는 필수 속성
    si = models.ForeignKey(Si, on_delete=models.CASCADE, related_name='gus')


class Dong(models.Model):
    dong_name = models.CharField(max_length=20) # max_length는 필수 속성
    gu = models.ForeignKey(Gu, on_delete=models.CASCADE, related_name='dongs')


class Road_address(models.Model):
    road_name = models.CharField(max_length=100)
    gu = models.ForeignKey(Gu, on_delete=models.CASCADE, related_name='road_addresses')
    

class Detail_address(models.Model):
    detail_name = models.CharField(max_length=100)
    gu = models.ForeignKey(Gu, on_delete=models.CASCADE, related_name='detail_addresses')


class Category_big(models.Model):
    cate_big_name = models.CharField(max_length=50)


class Category_small(models.Model):
    cate_small_name = models.CharField(max_length=50)
    category_big = models.ForeignKey(Category_big, on_delete=models.CASCADE, related_name='category_smalls')


class Shop(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    d_address = models.ForeignKey(Detail_address, on_delete=models.CASCADE, related_name='shops')
    r_address = models.ForeignKey(Road_address, on_delete=models.CASCADE, related_name='shops')
    s_catetegory = models.ForeignKey(Category_small, on_delete=models.CASCADE, related_name='shops')

# Create your models here.
