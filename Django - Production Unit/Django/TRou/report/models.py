from django.db import models

class Reports(models.Model):
    __tableName__ = 'Reports'

    id = models.IntegerField(primary_key=True)
    U_Id = models.IntegerField()
    Message = models.CharField(max_length=100)

    def __init(self, Message):
        self.Message = Message

    def __repr__(self):
        return f'{self.Message}'
