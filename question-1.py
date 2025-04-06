'''
Question 1: By default are django signals executed synchronously or asynchronously?
Answer: By default, Django signals are executed synchronously. This means that when a signal is sent,
the receiver function is executed immediately in the same thread and process as the sender.

'''

# Example code to demonstrate synchronous execution of Django signals

# models.py
# Created Model Book
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)

# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book
import time

@receiver(post_save, sender=Book)
def book_saved(sender, instance, **kwargs):
    print("Signal START")
    time.sleep(5) # Wait for 5 seconds
    print("Signal END")
    
'''
# Output:

Signal START  
Signal END

'''