# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PersonInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, unique=True, )  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=20, blank=True,
                            null=True)  # Field name made lowercase.
    project = models.CharField(db_column='PROJECT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='POSITION', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    contract_place = models.CharField(db_column='CONTRACT_PLACE', max_length=20, blank=True,
                                      null=True)  # Field name made lowercase.
    hire_date = models.DateField(db_column='HIRE_DATE', blank=True, null=True)  # Field name made lowercase.
    st_work_date = models.DateField(db_column='ST_WORK_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PERSON_INFO'


class User(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', unique=True, max_length=20, )
    name = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'user'


class ProjectInfo(models.Model):
    customer = models.CharField(max_length=200)
    projectName = models.CharField(max_length=200)

    def __str__(self):
        return self.projectName


class Dict(models.Model):
    item = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.item


class DicDetail(models.Model):
    dict = models.ForeignKey(Dict, on_delete=models.CASCADE)
    dicDetailName = models.CharField(max_length=300)

    def __str__(self):
        return self.dicDetailName


class InvoiceTracking(models.Model):
    projectName = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    paymentText = models.CharField(max_length=200)
    estAmount = models.DecimalField(max_digits=10, decimal_places=2)
    estPayDate = models.DateField()
    actPayDate = models.DateField()
    invoicePercent = models.DecimalField(max_digits=5, decimal_places=2)
    invoiceStatus = models.BooleanField()

    def __str__(self):
        return self.paymentText


# '项目问题登记
class WorkDaily(models.Model):
    projectName = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.CharField(max_length=100)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    finish = models.BooleanField()
    remark = models.TextField(null=True)


# '项目指标
class ProjectTarget(models.Model):
    projectName = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    year = models.CharField(max_length=10)
    workloadTarget = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    incomeTarget = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    costTarget = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    incomePerPerson = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    marginTarget = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    versionNo = models.IntegerField(null=True)
    remark = models.TextField(null=True)

    def __str__(self):
        return self.projectName + " + " + self.year + "年度"
