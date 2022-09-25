from django.db import models

# Create your models here.
class Goals(models.Model):
    goalID = models.BigAutoField(primary_key=True)
    goalDesc = models.CharField(max_length=300)



class RoadmapItems(models.Model):
    itemID = models.BigAutoField(primary_key=True)
    itemDesc =  models.CharField(max_length=300)
    completionRate = models.FloatField()
    deadline = models.DateTimeField()
    assGoal = models.ForeignKey(Goals, on_delete=models.CASCADE)

class Tasks(models.Model):
    taskID = models.BigAutoField(primary_key=True)
    taskDesc = models.CharField(max_length=300)
    status = models.CharField(max_length=30)
    weight = models.IntegerField()
    assRoadmapItem = models.ForeignKey(RoadmapItems, on_delete=models.CASCADE)