#!/usr/bin/env python

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/add_mps.py utils/cdep_2015_mp.csv

import sys
import csv
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "godfatherism.settings")

from django.contrib.auth.models import User
from kinship.models import Person

import django
django.setup()

def main():

    if len(sys.argv) != 2:
        print ('Usage: python add_mps.py <file.csv>')
        print (" CSV columns: name, group")
        sys.exit(1)

    csvfile = open(sys.argv[1], 'r')
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        name, group = row
        p, new = Person.objects.get_or_create(name=name)
        if not new:
            continue
        p.affiliation = group
        p.save()


if __name__ == "__main__":
    sys.exit(main())
