from django.db import models

# Create your models here.
class EventModel(models.Model):
    name = models.CharField(max_length=255, help_text="Enter name:")
    contact = models.CharField(max_length=10, help_text='Enter Contact:')
    email = models.EmailField(max_length=255, help_text='Enter email:')
    date = models.CharField(max_length=255, help_text='Enter date:', default="01/01/2019")
    EVENT = (('Event', '--Event--'), ('wedding', 'Wedding'), ('birthday', 'Birthday'),('corporate','Corporate Event'),('theme party','Theme Party'),('anniversary','Anniversary'),)
    event = models.CharField(max_length=255, help_text="enter event", default='Event', choices=EVENT)
    dec = models.CharField(max_length=255, help_text="choose decoration", default='no decoration')
    venue = models.CharField(max_length=255, help_text="choose venue", default='no venue')
    photo = models.CharField(max_length=255, help_text="choose photographer",default='no photographer')
    catering = models.CharField(max_length=255, help_text="choose catering", default='no catering')
    sound = models.CharField(max_length=255, help_text="choose sound", default='no sound setup')


    def __str__(self):
        return self.name+''+self.contact+''+self.email+''+self.date+''+self.event+''+self.dec+''+self.venue+''+self.photo+''+self.catering+''+self.sound

    class Meta:
        db_table = "Users"
        ordering = ('id',)
        verbose_name = "User"
        verbose_name_plural = "Users"

class EnquiryModel(models.Model):
    email = models.EmailField(max_length=255, help_text="enter email")
    query = models.TextField(max_length=255, help_text="enter query")

    def __str__(self):
        return self.email+''+self.query

    class Meta:
        db_table = "Users1"
        ordering = ('email',)
        verbose_name = "User1"
        verbose_name_plural = "Users1"

class SignUpModel(models.Model):
    username=models.CharField(max_length=255,help_text="enter username")
    password=models.CharField(max_length=255,help_text="enter password")


    def __str__(self):
        return self.username +''+self.password

    class Meta:
        db_table="Users2"
        ordering = ('username',)
        verbose_name = "User2"
        verbose_name_plural = "Users2"

