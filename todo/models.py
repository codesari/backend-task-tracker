from django.db import models

# Create your models here.
class Todo(models.Model):
    PRIORİTY=(
        (1,'High')
        (2,'Medium')
        (3,'Low')
    )
    task=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    priority=models.SmallIntegerField(choices=PRIORİTY,default=3)
    # kullanıcı front-end'te hicbirşey seçmezse default olarak az öneme sahip bir task olarak 3 default olarak seçilir
    is_done=models.BooleanField(default=False)
    updated_date=models.DateTimeField(auto_now=True)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task