# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    nama_depan = models.CharField(max_length=25)
    nama_belakang = models.CharField(max_length=25)
    email = models.CharField(max_length=60)
    password = models.TextField()

    class Meta:
        #managed = False
        db_table = 'admin'


class Barang(models.Model):
    nama_barang = models.CharField(max_length=60)
    jenis_barang = models.CharField(max_length=50)
    status = models.CharField(max_length=25)
    id_admin = models.ForeignKey(Admin, models.DO_NOTHING, db_column='id_admin')
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')

    class Meta:
        #managed = False
        db_table = 'barang'


class Laporan(models.Model):
    no_laporan = models.IntegerField()
    tgl_laporan = models.DateField()
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')

    class Meta:
        #managed = False
        db_table = 'laporan'


class Mahasiswa(models.Model):
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    nim = models.CharField(max_length=10)
    id_prodi = models.ForeignKey('Prodi', models.DO_NOTHING, db_column='id_prodi')

    class Meta:
        #managed = False
        db_table = 'mahasiswa'


class Prodi(models.Model):
    nama_prodi = models.CharField(max_length=60)
    kaprodi = models.CharField(max_length=60)

    class Meta:
        #managed = False
        db_table = 'prodi'


class Staff(models.Model):
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    jabatan = models.CharField(max_length=50)

    class Meta:
        #managed = False
        db_table = 'staff'


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    nama_depan = models.CharField(max_length=25)
    nama_belakang = models.CharField(max_length=25)
    email = models.CharField(max_length=60)
    password = models.TextField()
    role = models.CharField(max_length=10)

    class Meta:
        #managed = False
        db_table = 'user'
