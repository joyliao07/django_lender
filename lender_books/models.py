"""To set up models for lender_books app."""
from django.db import models
import datetime


class Book(models.Model):
    """To set up Book class."""
    cover_imgage = models.CharField(max_length=400)
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=50)
    year = models.CharField(max_length=4)

    STATES = [
        ('available', 'Available'),
        ('checked-out', 'Checked-out'),
    ]
    status = models.CharField(max_length=11, default='available', choices=STATES)
    date_added = models.DateField(max_length=30, default=datetime.date.today)
    last_borrowed = models.DateField(max_length=30, default=datetime.date.today)

    # def __repr__(self):
    #     return ''

    def __str__(self):
        return f'{self.title} ({self.status})'
