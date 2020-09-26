from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import post_save
# Create your models here.


def validate_number(value):
    print(value)
    if value == 10:
        print('i aa inside')
        raise ValidationError('It must be a number')
    return value


class DummyQuerySet(models.QuerySet):
    def UserName(self):
        return self.filter(UserName='rangooski')

    def UserName1(self):
        return self.filter(UserName__icontains='rangooski')

    def age(self, value):
        return self.filter(number=12)


class DummyManager(models.Manager):
    def get_queryset(self):
        return DummyQuerySet(self.model, using=self._db)
        # 'We have to pass the query like Dummy.modelManager.all().UserName() or age(10) will give the query set'
        # if you didnot create any custom queryset then your get query method looks like this
        # def get_queryset(self):
        #     return super().get_queryset()

    def UserName(self):
        return self.get_queryset().UserName1()
        # 'Dummy.modelManager.UserName()'
        # 'Dummy.modelManager.all() will call the get_queryset and return '
        # def all():
        # super(Dummy,self).all(*args,**kwargs).filter(UserName__icontains='rangooski')


class Dummy(models.Model):
    def custom(self, value):
        newstr = value+'zzzzzzz'
        return newstr

    MEDIA_CHOICES = [
        ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
        ),
        ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
        ),
        ('unknown', 'Unknown'),
    ]
    id = models.BigAutoField(primary_key=True)
    number = models.BigIntegerField(
        verbose_name='Age', validators=[validate_number])
    slug = models.SlugField(null=True, blank=True)
    Active = models.BooleanField(null=True)
    UserName = models.CharField(max_length=50,
                                unique=True,
                                error_messages={
                                    'unique': 'Username already taked try again!!!!'},
                                help_text="Valid username in alphabets only...",
                                )
    Date = models.DateField(default=now)
    options = models.CharField(
        max_length=50, choices=MEDIA_CHOICES, default='unknown')
    # Date = models.DateTimeField(default=now)
    files = models.FileField(upload_to=None, max_length=100, blank=True)
    UpdatedDate = models.DateTimeField(auto_now=True)
    # it will fire datetime.now everytime clicked save
    publishedDate = models.DateTimeField(auto_now_add=True)
    # it will fire datetime.now only on creation means one time only
    modelManager = DummyManager()
    '''to get all the objects we use Dummy.objects.all() if modelManager assigned to same objects method used by django like objects = DummyManager() now objects overriden with modelManager so  Dummy.modelMAnager.all() and all() also to be defined inside the DummyManager() or you can use get_queyset() instead define all()'''

    def __str__(self):
        return self.UserName

    def save(self, *args, **kwargs):
        # self.slug = self.custom(self.UserName)
        super(Dummy, self).save(*args, **kwargs)

    # will make this as instance.property (self.property) instead as instance.method(self.property())
    @property
    def property(self):
        return str(self.UserName)+str(self.slug)


def post_save_receiver(sender, instance, created, *args, **kwargs):
    # post_save.disconnect(post_save_receiver, sender=Dummy) #we can use disconnect to stop maximum recursion and connect after save()
    if created:  # we can use this to stop max recursion becuase one time only object can be created
        # instance.UserName = ''
        print(instance.slug)
        print(not instance.slug)
        if not instance.slug and instance.UserName:
            instance.slug = slugify(instance.UserName)
            instance.save()
    # post_save.connect(post_save_receiver, sender=Dummy)


post_save.connect(post_save_receiver, sender=Dummy)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name
