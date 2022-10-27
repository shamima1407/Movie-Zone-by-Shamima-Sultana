from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 64)
    year = models.IntegerField()
    language = models.CharField(max_length = 10)
    gener1 = models.CharField(max_length = 16)
    gener2 = models.CharField(max_length = 16, null = True)
    duration = models.FloatField(null = True)
    rating = models.FloatField()
    cast1 = models.CharField(max_length = 64)
    cast2 = models.CharField(max_length = 64, null = True)
    cast3 = models.CharField(max_length = 64, null = True)
    director = models.CharField(max_length = 64, null = True)
    video = models.CharField(max_length = 200, null = True)
    img = models.ImageField(upload_to="media")
#    img = models.CharField(max_length = 20, null = True)
    category = models.CharField(max_length = 20, null = True)
    imdb_link = models.CharField(max_length = 200, null = True)
    story = models.TextField()
    


    class Meta:
        db_table = 'Movie'

    def __str__(self):
        return f"{self.name}: ({self.year})"

class Banner_Movie(models.Model):
    banner_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to="media")
#    icon = models.ImageField()
    story = models.CharField(max_length = 150, null = True)

    class Meta:
        db_table = 'Banner_Movie'

    def __str__(self):
        return f"{self.poster}"
