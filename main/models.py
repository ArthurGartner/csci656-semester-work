from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    # def __lt__(self, other):

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        return self.first_name == other.first_name


class Task(models.Model):
    name = models.CharField(max_length=300)

    # Defines a 1 ro many relationship between 'Person' and 'Task'
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    duration_in_minutes = models.IntegerField()

class CourseOffering(models.Model):
    course_num = models.CharField(max_length=20)

    class Meta:
        db_table = 'course_offerings'


class Shopping_item(models.Model):
    item = models.CharField(max_length=200)
    store = models.CharField(max_length=200)
    buy_date = models.DateField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item

    def simple_description(self):
        return f"{self.item} (quantity: {self.quantity}) from {self.store}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)

# Bridge table used to connect many to many
