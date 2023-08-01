from django.db import models
from django.urls import reverse

class dog_pictures(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='KurzFinalApp/templates/dog_images')
    url = models.URLField(blank=True)
    # make.migrations --> Tvoří pro nás sql příkazy, pak je pomocí migrate django zkusí

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])
    
