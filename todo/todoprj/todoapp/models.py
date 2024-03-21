from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.(rem that this is what will determine the number of rows and and tables we will have in our db)


#Now lets create our models and give it a name todo and there after are the tables
class todo(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE)#rem the foreignkeys used above is used to connect two models together and then the on_delete will delete all the users task if she/he deleted his/her account
    
    task= models.CharField(max_length=1000)#The maximum length of the task description is 1000 characters.
    # date = models.DateTimeField(default=timezone.now)#The maximum length of the task description is 1000 characters.
    status = models.BooleanField(default=False) # True for completed, False for not yet completed
    description = models.TextField(max_length= 1000)
    completed = models.BooleanField(default=False)
    
    def  __str__(self):
        return self.task
   
    def  __str__(self):
        return self.description
    #NOTE: Remember to do migrations after this or anytime  you add fields here! or new models
