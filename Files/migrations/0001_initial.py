# Generated by Django 4.0.4 on 2022-04-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advance_math5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Name_of_the_book', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Advanced_math1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Year_Of_the_paper', models.IntegerField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Advanced_math2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Year_Of_the_paper', models.IntegerField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Advanced_math6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Name_of_the_book', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Chemistry1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Year_Of_the_paper', models.IntegerField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Chemistry2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Year_Of_the_paper', models.IntegerField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Chemistry_form5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Name_of_the_book', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Chemistry_form6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Name_of_the_book', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ChemistryPracticals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Name_of_the_practical', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=100)),
                ('Message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Physics1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Year_Of_the_paper', models.IntegerField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Physics2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Year_Of_the_paper', models.IntegerField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='physics_form5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Name_of_the_book', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='physics_form6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Name_of_the_book', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='physics_practicals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('Name_of_the_practical', models.CharField(max_length=20)),
            ],
        ),
    ]