from django.db import models

class Editor(models.Model) :
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length= 10,blank = True)
    
