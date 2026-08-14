from django.db import models
from django.db.models.functions import Cast, Coalesce
from datetime import datetime, date


class Project(models.Model):
    name = models.CharField(max_length=22)
    def __str__(self):
        return self.name

class Reader(models.Model):
    name = models.CharField(max_length=22)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Account(models.Model):
    name = models.CharField(max_length=55)
    #def __str__(self):
    #    return f"{self.id} {self.name}"
    readonly_fields=('id',)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['id']

class Transaction_type(models.Model):
    name = models.CharField(max_length=55)
    def __str__(self):
        return(self.name)
    class Meta:
        ordering = ['name']

class Payment_type(models.Model):
    name = models.CharField(max_length=22)
    def __str__(self):
        return(self.name)

class Vendor(models.Model):
    name = models.CharField(max_length=155)
    notes = models.CharField(155, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Branch(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)

    class Meta:
        verbose_name_plural = "branches"
        ordering = ['name']

    def __str__(self):
        return self.name

class Transaction(models.Model):
    class Frequency(models.TextChoices):
        Weekly = "D", "Daily"
        Monthly = "M", "Monthly"
        Quarterly = "Q", "Quarterly"
        Yearly = "Y", "Yearly"
    frequency = models.CharField(null=True, blank=True,
            max_length = 1,
            choices = Frequency.choices)

    vendor = models.ForeignKey(Vendor, on_delete=models.SET_DEFAULT, null=False, blank=False, default=0)
    branch = models.ForeignKey(Branch, on_delete=models.SET_DEFAULT, null=True, blank=True, default=0)
    vendor_name = models.CharField("non recurring vendor", null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.SET_DEFAULT, default=3)
    transaction_type = models.ForeignKey(Transaction_type, on_delete=models.SET_DEFAULT, default=5)
    payment_type = models.ForeignKey(Payment_type, on_delete=models.SET_NULL, null=True, blank=True, default=2)
    receipt_date = models.DateField("date on receipt", null=True, blank=True)
    statement_date = models.DateField("date on statement", null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    cr_dr = models.SmallIntegerField(default='-1')
    cheque_no = models.CharField("cheque no", max_length=22, null=True, blank=True)
    booking = models.CharField("booking ref", max_length=22, null=True, blank=True)
    date_created = models.DateTimeField("date created", auto_now_add=True)
    user_created = models.CharField("user created", max_length=22, default='sysgen')
    date_amended = models.DateTimeField("date amended", null=True, blank=True)
    user_amended = models.CharField("user amended", max_length=22, null=True, blank=True)
    project_name = models.CharField(max_length=55, null=True, blank=True)
    transaction_date = models.DateField("date of transaction", null=True, blank=True)
    reader = models.ForeignKey(Reader, on_delete=models.SET_NULL,null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,null=True, blank=True)

    @property
    def signed_amount(self):
        return self.amount * self.cr_dr

    @property
#    def best_date(self):
#        best_date = Coalesce(self.statement_date,self.transaction_date,self.receipt_date,date.today())
##        return f"Coalesce(self.receipt_date, self.transaction_date, self.statement_date, datetime.now())"
##        return self.receipt_date
#        return best_date

    def get_sort_date(self):
        return Coalesce(self.receipt_date, self.transaction_date, self.statement_date, datetime.now())

    def oldest_date(self):
        from datetime import date
        if self.receipt_date:
            return self.receipt_date
        elif self.transaction_date:
            return self.transaction_date
        elif self.statement_date:
            return self.statement_date
        else:
            return date.today()

    def best_date(self):
        from datetime import date
        if self.statement_date:
            return self.statement_date
        elif self.transaction_date:
            return self.transaction_date
        elif self.receipt_date:
            return self.receipt_date
        else:
            return date.today()

    def vendor_text(self):
        if self.vendor_single:
            return self.vendor_single
        elif self.branch_id:
            return self.branch__name
        else:
            return self.vendor__name

    def __str__(self):
        return f"{self.best_date} {self.vendor} {str(self.amount)}"

    class Meta:
        ordering = ['-statement_date']
#        ordering = ['-oldest_date']

