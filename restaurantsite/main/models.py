from django.db import models
import uuid
import os
from django.core.validators import RegexValidator


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Categories'


class Dish(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('dishes', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=500, blank=True)
    ingredients = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    special = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('position', 'price',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return f'{self.name}'


class Events(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('events', new_filename)

    name = models.CharField(unique=True, max_length=100, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    first_text_field = models.TextField(max_length=200, blank=True, db_index=True)
    second_text_field = models.TextField(max_length=200, blank=True, db_index=True)
    selected_text_1 = models.CharField(max_length=100, blank=True, db_index=True)
    selected_text_2 = models.CharField(max_length=100, blank=True, db_index=True)
    selected_text_3 = models.CharField(max_length=100, blank=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Events'

    def __str__(self):
        return f'{self.name}'


class About(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('events', new_filename)

    title_simple = models.CharField(max_length=50, blank=True, db_index=True)
    title_selected = models.CharField(max_length=50, blank=True, db_index=True)
    paragraph_1 = models.TextField(max_length=500, blank=True, db_index=True)
    paragraph_2 = models.TextField(max_length=500, blank=True, db_index=True)
    paragraph_3 = models.TextField(max_length=500, blank=True, db_index=True)
    selected_text_1 = models.CharField(max_length=200, blank=True, db_index=True)
    selected_text_2 = models.CharField(max_length=200, blank=True, db_index=True)
    selected_text_3 = models.CharField(max_length=200, blank=True, db_index=True)
    video_link = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True, unique=True)
    photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        verbose_name_plural = 'About section'

    def __str__(self):
        return f'{self.__class__.__name__}'


class WhyUs(models.Model):
    slogan_1 = models.CharField(max_length=50, db_index=True)
    text_1 = models.TextField(max_length=200, db_index=True)
    slogan_2 = models.CharField(max_length=50, db_index=True)
    text_2 = models.TextField(max_length=200, db_index=True)
    slogan_3 = models.CharField(max_length=50, db_index=True)
    text_3 = models.TextField(max_length=200, db_index=True)

    class Meta:
        verbose_name_plural = '"Why us" section'


class Gallery(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('gallery', new_filename)

    photo = models.ImageField(upload_to=get_file_name)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return f'{self.position}'


class Chefs(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('gallery', new_filename)

    name = models.CharField(max_length=50, db_index=True)
    job_position = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    position = models.SmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Chefs'

    def __str__(self):
        return f'{self.name}'


class Titles(models.Model):
    gallery_title = models.CharField(max_length=300, blank=True, db_index=True)
    book_a_table_title = models.CharField(max_length=300, blank=True, db_index=True)
    chefs_title = models.CharField(max_length=300, blank=True, db_index=True)
    contact_us_title = models.CharField(max_length=300, blank=True, db_index=True)
    why_us_title = models.CharField(max_length=300, blank=True, db_index=True)
    special_title = models.CharField(max_length=300, blank=True, db_index=True)

    class Meta:
        verbose_name_plural = 'Titles'

    def __str__(self):
        return f'{self.__class__.__name__}'


class Testimonials(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('gallery', new_filename)

    name = models.CharField(max_length=100, unique=True)
    profession = models.CharField(max_length=50)
    review = models.TextField(max_length=300)
    position = models.SmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f'{self.name}'


class OurInformation(models.Model):
    main_name = models.CharField(max_length=100)
    bottom_site_slogan = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    google_coordinates = models.CharField(max_length=500, blank=True)
    open_hours = models.CharField(max_length=200)
    open_days = models.CharField(max_length=200, default='Monday-Sunday:')
    email_1 = models.EmailField()
    email_2 = models.EmailField(blank=True)
    phone_re = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone number in format xxx xxx xxxx')
    phone_number_1 = models.CharField(max_length=15, validators=[phone_re])
    phone_number_2 = models.CharField(max_length=15, blank=True, validators=[phone_re])
    twitter = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    skype = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Our information'


class TopSitePresentation(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('presentation', new_filename)

    title = models.CharField(max_length=100, unique=True, db_index=True)
    text = models.TextField(max_length=300, db_index=True)
    position = models.SmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        ordering = ('position', )
        verbose_name_plural = 'Top site presentation'

    def __str__(self):
        return f'{self.title}'


class UserReservation(models.Model):
    name = models.CharField(max_length=50)
    phone_re = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone number in format xxx xxx xxxx')
    phone = models.CharField(max_length=15, validators=[phone_re])
    email = models.EmailField(blank=True)
    req_date = models.DateField()
    req_time = models.TimeField()
    persons = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-is_processed')
        verbose_name_plural = 'User reservations'

    def __str__(self):
        return f'{self.name}, {self.phone}: {self.message[:50]}'


class UserMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField(max_length=300)
    message = models.TextField(max_length=1500)
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-is_processed')
        verbose_name_plural = 'User messages'

    def __str__(self):
        return f'{self.name}, {self.email}: {self.subject[:100]}'
