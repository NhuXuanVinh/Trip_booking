# Generated by Django 4.2.1 on 2023-07-20 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qlxk', '0005_alter_chuyenxe_bien_so_alter_ghe_bien_so'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chuyenxe',
            old_name='date',
            new_name='chuyenxe_date',
        ),
        migrations.RenameField(
            model_name='nhanvienxe',
            old_name='name',
            new_name='nhanvien_name',
        ),
    ]