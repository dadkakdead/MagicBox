import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings

def create_seed_reports(apps, schema_editor):
    Report = apps.get_model('webrequest', 'Report')

    r = Report.objects.create(key="garmin",
                                name = "Daily heart rate",
                                description = "Convert and merge *_data.csv and from Garmin device.",
                                maxDocuments = -1,
                                allowedExtentions = "CSV",
                                pathToScript = settings.BASE_DIR + "/webrequest/scripts/garmin_script.py")
    r.save()

    r = Report.objects.create(key = "telegram",
                                name = "Telegram channels",
                                description = "Show correlation between inten.to, tlgrm.ru, tchannels.me and tsear.ch databases.",
                                maxDocuments = 4,
                                allowedExtentions = "XLS,XLSX,XLSM",
                                pathToScript = settings.BASE_DIR + "/webrequest/scripts/telegram_script.py")
    r.save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(code='nomatch', message='Key should be at least 5 characters long', regex='^[0-9a-zA-Z]{5,}$')])),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('pathToScript', models.CharField(editable=False, max_length=500)),
                ('maxDocuments', models.IntegerField(default=-1, validators=[django.core.validators.MinValueValidator(-1)])),
                ('allowedExtentions', models.CharField(default='XLS,XLSX,XLSM', max_length=100, validators=[django.core.validators.RegexValidator(code='nomatch', message='Write the extension in upper case one by one. Example: XLS,XLSX,XLSM', regex='^[,A-Z]{1,}$')])),
                ('timeCreated', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('timeModified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestZip', models.FileField(upload_to='requests/')),
                ('timeCreated', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webrequest.Report')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responseFile', models.FileField(upload_to='responses/')),
                ('timeCreated', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webrequest.Request')),
            ],
        ),

        migrations.RunPython(create_seed_reports),
    ]
