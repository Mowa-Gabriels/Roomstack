from django.db import models
from authentication.models import User
import uuid
from django.utils.text import slugify

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=225)


    def __str__(self):
        return self.name

class Amenity(models.Model):
    name = models.CharField(max_length=225)


    def __str__(self):
        return self.name





class Room(models.Model):

    TYPE = (
        ('A Room', 'A Room'),
        ('A Room Selfcon', 'A Room Selfcon'),
        ('Two Bedroom', 'Two Bedroom'),
    )

    RENT = (
        ('1', '10k -50k'),
        ('2', '50k -100k'),
        ('3', '> 100k'),
    )

    BILLS = (
        ('1', 'Split bills evenly'),
        ('2', 'Negotiatory'),
        
    )
    ROOM_COMPOSITION= (
        ('1', 'One person'),
        ('2', 'Two'),
        ('3', 'More Than Two'),
    )
    STAY_DURATION = (
        ('1', 'One Semester'),
        ('2', 'One Session'),
        ('3', 'ShortTerm'),
        ('4', 'LongTerm'),
        ('5', 'Negotiatory'),
    )

    VISIT_RATE= (
        ('1', 'One or more occasionally'),
        ('2', 'One or more frequently'),
    )
    HOME_FUNISHING = (
        ('1', 'Completely furnished'),
        ('2', 'Partially'),
        ('3', 'Nothing dey for this room'),
    )
   


 
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='owner_room')
    uuid = models.UUIDField(default=uuid.uuid4, editable = False)
    slug = models.SlugField(max_length = 50, unique=True, blank=True, null=True)
    
    type = models.CharField(max_length=225, null=True, choices=TYPE)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=225)
    room_display_image_one = models.ImageField(upload_to='room/', null=True)
    room_display_image_two = models.ImageField(upload_to='room/', blank=True, null=True)
    room_display_image_three = models.ImageField(upload_to='room/', blank=True, null=True)
    room_display_image_four = models.ImageField(upload_to='room/', blank=True, null=True)
    display_video = models.FileField(upload_to='room_videos/', blank=True, null=True)
    description = models.TextField(max_length=225)
    rent_range = models.CharField(max_length=14, null=True, choices=RENT)
    bills = models.CharField(max_length=14, null=True, choices=BILLS)
    room_composition = models.CharField(max_length=14, null=True, choices=ROOM_COMPOSITION)
    stay_duration = models.CharField(max_length=14, null=True, choices=STAY_DURATION)
    #visit_rate = models.CharField(max_length=14, null=True, choices=VISIT_RATE)
    home_furnishing = models.CharField(max_length=14, null=True, choices=HOME_FUNISHING)
    additional_amenity = models.ManyToManyField(Amenity)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.type + "-" + str(self.uuid))
        super(Room, self).save(*args, **kwargs)
    
    
    

    def __str__(self):
        return self.type

    @property
    def VideoURL(self):
        try:
            url = self.room_display_video.url
        except:
            url = ''
        return url


    @property
    def imageURLOne(self):
        try:
            url = self.room_display_image_one.url
        except:
            url = ''
        return url

    @property
    def imageURLTwo(self):
        try:
            url = self.room_display_image_two.url
        except:
            url = ''
        return url
    
    @property
    def imageURLThree(self):
        try:
            url = self.room_display_image_three.url
        except:
            url = ''
        return url


    @property
    def imageURLFour(self):
        try:
            url = self.room_display_image_four.url
        except:
            url = ''
        return url


class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='reviewer')
    Room = models.ForeignKey(Room, on_delete=models.CASCADE,  null=True, related_name='reviews')
    title = models.CharField(max_length=225)
    experience = models.TextField(max_length=225)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

