'''

Question 3: By default do django signals run in the same database transaction as the caller?
Answer: By default, Django signals run in the same database transaction as the caller. This means that if the caller's transaction is 
rolled back, the changes made by the signal will also be rolled back.This behavior is important for maintaining data integrity
and consistency in the database.

'''

# Example code to demonstrate that Django signals run in the same database transaction as the caller

# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)

# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

@receiver(post_save, sender=Book)
def book_saved(sender, instance, **kwargs):
    print(f"Signal: Book ID is {instance.id}")


# view or shell
from django.db import transaction
from myapp.models import Book

try:
    with transaction.atomic():
        book = Book.objects.create(title="Rollback Test")
        print(f"Book created: {book.id}")
        raise Exception("Force rollback!")
except:
    print("Rolled back transaction")
    

'''

# Output:

Signal: Book ID is 1    
Book created: 1
Rolled back transaction

'''
