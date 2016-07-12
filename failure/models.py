#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Hala(models.Model):
	symbol = models.CharField(max_length=10, verbose_name="Symbol hali")
	user = models.ForeignKey(User, verbose_name='Opiekun')

	def __str__(self):
		return self.symbol

	class Meta:
         verbose_name = "Hala"
         verbose_name_plural = "Hale"

class Wydzial(models.Model):
	nazwa = models.CharField(max_length=50, verbose_name="Nazwa wydziału")
	user = models.ForeignKey(User, verbose_name='Mistrz')

	def __str__(self):
		return self.nazwa

	class Meta:
         verbose_name = "Wydział"
         verbose_name_plural = "Wydziały"

class Maszyna(models.Model):
	nazwa = models.CharField(max_length=50, verbose_name="Nazwa")
	wydzial = models.ForeignKey(Wydzial, verbose_name='Wydział')
	hala = models.ForeignKey(Hala, verbose_name='Hala')
	opiekun = models.ForeignKey(User, verbose_name='Opiekun', default=1)

	def __str__(self):
		return self.nazwa

	class Meta:
         verbose_name = "Maszyna"
         verbose_name_plural = "Maszyny"

class Status(models.Model):
    nazwa = models.CharField(max_length = 50, verbose_name = 'Nazwa')

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statusy'

class Awaria(models.Model):
	maszyna = models.ForeignKey(Maszyna, on_delete=models.PROTECT, verbose_name='Maszyna')
	wydzial = models.ForeignKey(Wydzial, verbose_name='Wydział')
	description = models.TextField(verbose_name="Opis awarii", blank=True)
	add_date = models.DateTimeField(auto_now_add=True, verbose_name="Data zgłoszenia")
	user = models.ForeignKey(User, verbose_name='Zgłaszający')
	sur = models.CharField(max_length = 50, verbose_name='Przyjęte przez',blank=True, null=True)
	status = models.ForeignKey(Status, default=1, verbose_name='Status')
	update_date = models.DateTimeField(auto_now=True, verbose_name="Data ostaniej modyfikacji")

	def __str__(self):
		return str(self.status)

	class Meta:
         verbose_name = "Awaria"
         verbose_name_plural = "Awarie"
