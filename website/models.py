from django.db import models



class Film(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    release_year = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre =  models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    duration_mins = models.IntegerField()
    production_company = models.CharField(max_length=100)
    status_choices =( 
    ("TO WATCH", "TO WATCH"), 
    ("WATCHING", "WATCHING"), 
    ("WATCHED", "WATCHED"), 
    ("REWATCHED", "REWATCHED"), 
)
    status = models.CharField(max_length=50, choices=status_choices)
    rating_choices =(
          ("1", "1"),
          ("2", "2"),
          ("3", "3"),
          ("4", "4"),
          ("5", "5"),
    )
    rating = models.CharField(max_length=50, choices=rating_choices)
    sypnosis = models.CharField(max_length=1000)

    def __str__(self):
            return self.title + " " + "(" + self.release_year + ")"


    
