from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    image = models.ImageField(upload_to='images/',null=True,blank=True)


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    link = models.URLField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    technology = models.ManyToManyField(Technology)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=False)
    message = models.TextField(null=False)

    def __str__(self):
        return f"{self.email}, Message: {self.message}"
        
