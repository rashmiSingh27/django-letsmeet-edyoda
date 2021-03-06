# Generated by Django 3.2.3 on 2021-08-16 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('seats', models.IntegerField(default=1)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='blog.post')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
