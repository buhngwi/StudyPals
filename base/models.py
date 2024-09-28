from django.db import models

class UserGender(models.Model):
    choice = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.choice

class UserCountry(models.Model):
    country_name = models.CharField(max_length=200, null=True)
    country_code = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.country_name

class User(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, unique=True, null=True)
    gender = models.ForeignKey(UserGender,on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(UserCountry, on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(null=True, input_formats=['%d/%m/%Y'])
    phone_number = models.CharField(max_length=11, null=True)
    password = models.CharField(max_length=200, null=True, blank=False)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'username'
    EMAIL_FIELD ='email'
    REQUIRED_FIELDS = ['username','password','email']


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
