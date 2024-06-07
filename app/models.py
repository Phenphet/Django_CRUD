from django.db import models

# Create your models here.
class Student(models.Model):

    select = (
        (1, "male"),(2, "female")
    )
    
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.IntegerField(choices=select)
    image = models.ImageField(upload_to='app/upload/image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    def get_gender(self):
        return dict(self.select).get(self.gender, 'Unknown')

    class Meta:
        db_table = 'tblStudent'