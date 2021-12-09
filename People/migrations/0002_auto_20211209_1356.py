# Generated by Django 3.2.10 on 2021-12-09 13:56

from django.db import migrations

import os
from sys import path
from django.core import serializers
from django.db import migrations


fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'initial_data.json'
def load_fixture(apps, schema_editor):
    fixture_file = os.path.join(fixture_dir, fixture_filename)
    fixture = open(fixture_file, 'rb')
    objects = serializers.deserialize('json', fixture, ignorenonexistent=True)
    for obj in objects:
        obj.save()

    fixture.close()

def unload_fixture(apps, schema_editor):
    fixture_file = os.path.join(fixture_dir, fixture_filename)

    fixture = open(fixture_file, 'rb')
    objects = serializers.deserialize('json', fixture, ignorenonexistent=True)
    for obj in objects:
        print("Delete manually")
        print(obj)

class Migration(migrations.Migration):

    dependencies = [
        ('People', '0001_initial'),
    ]

    operations = [
         migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]