from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Person(models.Model):
    first_name=models.CharField(_("First Name"), max_length=150)
    last_name=models.CharField(_("Last Name"), max_length=150)
    address=models.CharField(_("Address"),max_length=150)
    mobile = models.CharField(_("Mobile Phone"),max_length=15,unique=True)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()


class Job(models.Model):
    title_ar=models.CharField(_("Title Arabic"), max_length=150)
    title_en=models.CharField(_("Title English"), max_length=150)
    min_salary = models.DecimalField(_("Min Salary"),max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __str__(self):
        return self.title_en
    
class PersonJobDetail(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE,related_name="rel_person")
    job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name="rel_job")
    salary=models.DecimalField(_("Salary"),max_digits=10, decimal_places=2)
    years_of_experince=models.PositiveIntegerField(_("Years Of Experince"))

    class Meta:
        verbose_name = "PersonJobDetail"
        verbose_name_plural = "PersonJobDetails"

    def __str__(self):
        return f"{self.person} - {self.job}"