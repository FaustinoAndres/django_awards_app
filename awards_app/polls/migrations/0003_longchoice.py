# Generated by Django 4.1 on 2022-09-06 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_choices_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='LongChoice',
            fields=[
                ('choice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='polls.choice')),
                ('long_choice_text', models.CharField(max_length=1000)),
            ],
            bases=('polls.choice',),
        ),
    ]
