from django.db import models

# Create your models here.
class Task(models.Model):
	Date1=models.CharField(max_length=80,null=True)
	Open=models.FloatField( null = True)
	High=models.FloatField( null = True)
	Low=models.FloatField( null = True)
	Close=models.FloatField( null = True)
	WAP=models.FloatField( null = True)
	No_Of_Shares=models.IntegerField()
	No_Of_Trades=models.IntegerField()
	Total_Turnover=models.FloatField( null = True)
	Deliverable=models.IntegerField()
	Per_Of_Del_Qty_To_Trd_Qty=models.FloatField( null = True)
	Spread_H_L=models.FloatField( null = True)
	Spread_C_O=models.FloatField( null = True)

	def __str__(self):
		return self.name
		#,self.author,self.email,self.describe,self.date2,self.clos
