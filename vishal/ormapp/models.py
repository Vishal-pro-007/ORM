from django.db import models
from django.contrib import admin
class Product(models.Model):
    ItmID=models.CharField(primary_key=True,max_length=7)
    Name=models.CharField(max_length=30)
    MerchID=models.CharField(max_length=7)
    Cost=models.FloatField()
    WarrantyTime=models.IntegerField()
    Ratings=models.FloatField()
    DelvDate=models.DateField()

class ProductAdmin(admin.ModelAdmin):
    list_display=["ItmID","Name","MerchID","Cost","WarrantyTime","Ratings","DelvDate"]
    actions_on_bottom=True
    actions_on_top=False
    list_display_links=["ItmID"]
    list_filter=["Name"]
