# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-19 11:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.folder
import image_cropping.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Titolo:')),
                ('code', models.CharField(blank=True, max_length=250, null=True, verbose_name='Codice')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Prezzo')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='sconto percentuale')),
                ('price_offer', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Prezzo Scontato')),
                ('image', models.ImageField(blank=True, null=True, upload_to='accessory', verbose_name='Immagine')),
                ('slider', image_cropping.fields.ImageRatioField('image', '1170x600', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Slider')),
                ('thumb', image_cropping.fields.ImageRatioField('image', '800x578', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Miniatura')),
                ('thumbdue', image_cropping.fields.ImageRatioField('image', '745x558', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Miniatura pagina dettaglio')),
                ('croplibero', image_cropping.fields.ImageRatioField('image', '595x335', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Ritaglio Libero')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Quantita')),
                ('size', models.CharField(blank=True, max_length=250, null=True, verbose_name='Misure')),
                ('width', models.IntegerField(blank=True, null=True, verbose_name='larghezza')),
                ('lenght', models.IntegerField(blank=True, null=True, verbose_name='lunghezza')),
                ('depth', models.IntegerField(blank=True, null=True, verbose_name='Profondita')),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='altezza')),
                ('volume', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Volume')),
                ('descrizione', models.TextField(blank=True, null=True, verbose_name='Descrizione')),
                ('allegato', models.FileField(blank=True, null=True, upload_to='allegato')),
                ('prompt_delivery', models.BooleanField(default=False, verbose_name='Pronta Consegna')),
                ('delivery', models.BooleanField(default=False, verbose_name='Consegna 40gg')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('active', models.BooleanField(default=False, verbose_name='attiva')),
                ('slide', models.BooleanField(default=False, verbose_name='Mostra in Slide')),
                ('promo', models.BooleanField(default=False, verbose_name='Mostra in Promo')),
                ('album', filer.fields.folder.FilerFolderField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Folder')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Accessori',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='titolo')),
                ('title_uk', models.CharField(blank=True, max_length=250, null=True, verbose_name='Titolo Inglese')),
                ('subtitle', models.CharField(blank=True, max_length=250, null=True, verbose_name='sottotitolo')),
            ],
            options={
                'verbose_name_plural': 'Categorie',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome colore')),
                ('code', models.CharField(blank=True, max_length=250, null=True, verbose_name='codice colore')),
                ('css_color', models.CharField(blank=True, max_length=250, null=True, verbose_name='css colore')),
                ('image', models.ImageField(blank=True, null=True, upload_to='color', verbose_name='immagine colore')),
                ('thumb', image_cropping.fields.ImageRatioField('image', '300x150', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Miniatura: 300x150px')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='Seleziona Categoria')),
            ],
            options={
                'verbose_name_plural': 'Colori',
            },
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=100, null=True, verbose_name='Titolo:')),
                ('code', models.CharField(blank=True, editable=False, max_length=250, null=True, verbose_name='Codice')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='maggiorazione di prezzo', max_digits=10, null=True, verbose_name='Prezzo')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Immagine')),
                ('slider', image_cropping.fields.ImageRatioField('image', '1000x556', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Slider')),
                ('thumb', image_cropping.fields.ImageRatioField('image', '800x578', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Miniatura')),
                ('thumbdue', image_cropping.fields.ImageRatioField('image', '745x558', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Miniatura pagina dettaglio')),
                ('croplibero', image_cropping.fields.ImageRatioField('image', '595x335', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Ritaglio Libero')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='quantita')),
                ('allegato', models.FileField(blank=True, null=True, upload_to='allegato')),
                ('pub_date', models.DateTimeField(editable=False, verbose_name='date published')),
                ('active', models.BooleanField(default=False, verbose_name='attiva')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Color', verbose_name='Colori')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Componente',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome colore')),
                ('image', models.ImageField(blank=True, null=True, upload_to='color', verbose_name='immagine colore')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descrizione')),
                ('thumb', image_cropping.fields.ImageRatioField('image', '300x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Miniatura')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Prezzo')),
            ],
            options={
                'verbose_name_plural': 'Materiali',
            },
        ),
        migrations.CreateModel(
            name='Moduli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Titolo:')),
                ('name_uk', models.CharField(blank=True, max_length=250, null=True, verbose_name='Titolo Inglese')),
                ('code', models.CharField(blank=True, max_length=250, null=True, verbose_name='Codice')),
                ('quantity', models.IntegerField(blank=True, help_text='quantita quando non e composizione', null=True, verbose_name='quantita')),
                ('price', models.DecimalField(blank=True, decimal_places=2, help_text='prezzo base', max_digits=10, null=True, verbose_name='Prezzo')),
                ('discount', models.IntegerField(blank=True, default=0, null=True, verbose_name='sconto percentuale')),
                ('price_offer', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Prezzo Scontato')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Immagine')),
                ('slider', image_cropping.fields.ImageRatioField('image', '1000x556', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Slider')),
                ('thumb', image_cropping.fields.ImageRatioField('image', '800x578', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Miniatura')),
                ('thumbdue', image_cropping.fields.ImageRatioField('image', '745x558', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Miniatura pagina dettaglio')),
                ('croplibero', image_cropping.fields.ImageRatioField('image', '595x335', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Ritaglio Libero')),
                ('size', models.CharField(blank=True, max_length=250, null=True, verbose_name='Misure')),
                ('width', models.IntegerField(blank=True, null=True, verbose_name='larghezza')),
                ('lenght', models.IntegerField(blank=True, null=True, verbose_name='lunghezza')),
                ('depth', models.IntegerField(blank=True, null=True, verbose_name='Profondita')),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='altezza')),
                ('volume', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Volume')),
                ('descrizione', models.TextField(blank=True, null=True, verbose_name='Descrizione')),
                ('descrizione_uk', models.TextField(blank=True, null=True, verbose_name='Descrizione Inglese')),
                ('allegato', models.FileField(blank=True, null=True, upload_to='allegato')),
                ('pub_date', models.DateTimeField(editable=False, verbose_name='date published')),
                ('active', models.BooleanField(default=False, verbose_name='attiva')),
                ('slide', models.BooleanField(default=False, verbose_name='Mostra in Slide')),
                ('promo', models.BooleanField(default=False, verbose_name='Mostra in Promo')),
                ('album', filer.fields.folder.FilerFolderField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Folder')),
                ('category', models.ManyToManyField(blank=True, null=True, to='product.Category', verbose_name='Seleziona Categorie')),
                ('color', models.ManyToManyField(blank=True, help_text='solo se a 40 giorni', null=True, to='product.Color', verbose_name='Seleziona Colori')),
                ('material', models.ManyToManyField(blank=True, null=True, to='product.Material', verbose_name='Seleziona Materiale')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Parole chiave')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Moduli',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Titolo:')),
                ('name_uk', models.CharField(blank=True, max_length=250, null=True, verbose_name='Titolo Inglese')),
                ('code', models.CharField(blank=True, max_length=250, null=True, verbose_name='Codice')),
                ('quantity', models.IntegerField(blank=True, help_text='quantita quando non e composizione', null=True, verbose_name='quantita')),
                ('price', models.DecimalField(blank=True, decimal_places=2, help_text='prezzo base', max_digits=10, null=True, verbose_name='Prezzo')),
                ('discount', models.IntegerField(blank=True, default=0, null=True, verbose_name='sconto percentuale')),
                ('price_offer', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Prezzo Scontato')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Immagine')),
                ('slider', image_cropping.fields.ImageRatioField('image', '1000x556', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Slider')),
                ('thumb', image_cropping.fields.ImageRatioField('image', '800x578', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Miniatura')),
                ('thumbdue', image_cropping.fields.ImageRatioField('image', '745x558', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Miniatura pagina dettaglio')),
                ('croplibero', image_cropping.fields.ImageRatioField('image', '595x335', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Ritaglio Libero')),
                ('size', models.CharField(blank=True, max_length=250, null=True, verbose_name='Misure')),
                ('width', models.IntegerField(blank=True, null=True, verbose_name='larghezza')),
                ('lenght', models.IntegerField(blank=True, null=True, verbose_name='lunghezza')),
                ('depth', models.IntegerField(blank=True, null=True, verbose_name='Profondita')),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='altezza')),
                ('volume', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Volume')),
                ('descrizione', models.TextField(blank=True, null=True, verbose_name='Descrizione')),
                ('descrizione_uk', models.TextField(blank=True, null=True, verbose_name='Descrizione Inglese')),
                ('allegato', models.FileField(blank=True, null=True, upload_to='allegato')),
                ('pub_date', models.DateTimeField(editable=False, verbose_name='date published')),
                ('active', models.BooleanField(default=False, verbose_name='attiva')),
                ('slide', models.BooleanField(default=False, verbose_name='Mostra in Slide')),
                ('promo', models.BooleanField(default=False, verbose_name='Mostra in Promo')),
                ('album', filer.fields.folder.FilerFolderField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Folder')),
                ('category', models.ManyToManyField(blank=True, null=True, to='product.Category', verbose_name='Seleziona Categorie')),
                ('color', models.ManyToManyField(blank=True, help_text='solo se a 40 giorni', null=True, to='product.Color', verbose_name='Seleziona Colori')),
                ('material', models.ManyToManyField(blank=True, null=True, to='product.Material', verbose_name='Seleziona Materiale')),
                ('moduli', models.ManyToManyField(blank=True, null=True, to='product.Moduli', verbose_name='Seleziona Moduli')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Parole chiave')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Prodotti',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='titolo')),
                ('code', models.CharField(blank=True, max_length=250, null=True, verbose_name='codice youtube')),
                ('url', models.CharField(blank=True, max_length=250, null=True, verbose_name='url youtube')),
                ('frame', models.TextField(blank=True, null=True, verbose_name='Frame embedded youtube')),
                ('image', models.ImageField(blank=True, null=True, upload_to='color', verbose_name='immagine colore')),
                ('thumb', image_cropping.fields.ImageRatioField('image', '300x150', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Miniatura: 300x150px')),
                ('active', models.BooleanField(default=False, verbose_name='attiva')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='Seleziona Categoria')),
            ],
            options={
                'verbose_name_plural': 'Video',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.ManyToManyField(blank=True, null=True, to='product.Video', verbose_name='Video'),
        ),
        migrations.AddField(
            model_name='moduli',
            name='video',
            field=models.ManyToManyField(blank=True, null=True, to='product.Video', verbose_name='Video'),
        ),
        migrations.AddField(
            model_name='composition',
            name='material',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Material', verbose_name='Metallo'),
        ),
        migrations.AddField(
            model_name='composition',
            name='modulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Moduli', verbose_name='Modulo'),
        ),
        migrations.AddField(
            model_name='composition',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Prodotto'),
        ),
        migrations.AddField(
            model_name='composition',
            name='video',
            field=models.ManyToManyField(blank=True, null=True, to='product.Video', verbose_name='Video'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='product.Category', verbose_name='Seleziona Categorie'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, to='product.Color', verbose_name='Seleziona Colori'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='material',
            field=models.ManyToManyField(blank=True, null=True, to='product.Material', verbose_name='Seleziona Materiali'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Parole chiave'),
        ),
    ]