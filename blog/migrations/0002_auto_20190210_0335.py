

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-post_date']},
        ),
        migrations.AlterModelOptions(
            name='blogauthor',
            options={'ordering': ['user', 'bio']},
        ),
        migrations.AlterField(
            model_name='blogauthor',
            name='bio',
            field=models.TextField(help_text='Enter your bio details here.', max_length=400),
        ),
    ]
