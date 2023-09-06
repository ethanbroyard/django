
from django.db import models
from datetime import datetime, timedelta, date
from django.utils.html import format_html
from django.utils import formats

class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    schedule_date =models.DateField(default=datetime.now()+timedelta(days=7))
    closed = models.BooleanField(default=False)  # Rectifié 'false' en 'False'

    def __str__(self):
        return self.name
    
    # Getters
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_created_date(self):
        return self.created_date

    def get_due_date(self):
        return self.due_date

    def get_schedule_date(self):
        return self.schedule_date

    def is_closed(self):
        return self.cslosed
    
    # Setters
    def set_name(self, name):
        self.name = name
        self.save()

    def set_description(self, description):
        self.description = description
        self.save()

    def set_due_date(self, due_date):
        self.due_date = due_date
        self.save()

    def set_schedule_date(self, schedule_date):
        self.schedule_date = schedule_date
        self.save()

    def set_closed(self, closed):
        self.closed = closed
        self.save()

def colored_due_date(self):
    due_date = formats.date_format(self.due_date, "SHORT_DATE_FORMAT")
    if self.due_date is None or self.due_date - timedelta(days=7) > date.today():
        color = "green"
    elif self.due_date < date.today():
        color = "red"
    else:
        color = "orange"
    return format_html("<span style='color:{};'>{}</span>", color, due_date)


colored_due_date.allow_tags = True