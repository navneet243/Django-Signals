'''

Question 2: Do django signals run in the same thread as the caller?
Answer: Yes, Django signals run in the same thread as the caller. When a signal is sent, the receiver function is executed
in the same thread and process as the sender. This means that if the sender is running in a specific thread,the receiver will also 
run in that same thread.

'''

# Example code to demonstrate that Django signals run in the same thread as the caller

# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)


# signals.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

@receiver(post_save, sender=Book)
def book_saved(sender, instance, **kwargs):
    print(f"[SIGNAL] Running in thread: {threading.current_thread().name}")


# shell or view
import threading
from myapp.models import Book

print(f"[CALLER] Running in thread: {threading.current_thread().name}")
Book.objects.create(title="Thread Check")

'''
# Output:

[CALLER] Running in thread: MainThread
[SIGNAL] Running in thread: MainThread

'''