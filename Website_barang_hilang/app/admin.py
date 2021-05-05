from django.contrib import admin
from .models import Admin, User, Staff, Prodi, Mahasiswa, Laporan, Barang

# Register your models here.
admin.site.register((
    Admin,
    User,
    Staff,
    Prodi,
    Mahasiswa,
    Laporan,
    Barang
))