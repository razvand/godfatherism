#!/usr/bin/env python

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/remove_mps.py

import sys
import csv
import os


# Setup Django environment.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "godfatherism.settings")

from django.contrib.auth.models import User
from kinship.models import Person

import django
django.setup()


def main():
    ps = Person.objects.all()
    for p in ps:
        p.delete()

if __name__ == "__main__":
    sys.exit(main())
