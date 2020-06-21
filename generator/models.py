from django.db import models

# Create your models here.

class Choice(models.Model):
    sentance_type       = models.CharField(max_length=200)

    # Simple
    grammar_type        = models.CharField(max_length=200)

    # Interrogative
    interrogative_type  = models.CharField(max_length=200)
    #grammer_type

    # Exclamatory
    exclamatory_type    = models.CharField(max_length=200)

    # Reult
    sentance            = models.CharField(max_length=200)


    def __str__(self):
        return self.name
