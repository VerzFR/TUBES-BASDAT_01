# Generated by Django 3.2 on 2021-05-05 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_depan', models.CharField(max_length=25)),
                ('nama_belakang', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=60)),
                ('password', models.TextField()),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=60)),
                ('jenis_barang', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'barang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Laporan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_laporan', models.IntegerField()),
                ('tgl_laporan', models.DateField()),
            ],
            options={
                'db_table': 'laporan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'mahasiswa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prodi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_prodi', models.CharField(max_length=60)),
                ('kaprodi', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'prodi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jabatan', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('nama_depan', models.CharField(max_length=25)),
                ('nama_belakang', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=60)),
                ('password', models.TextField()),
                ('role', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]