##!/usr/bin/env python3

import datetime

year = int (input ('What year were you born'))
month = int (input ('What month were you born'))
date = int (input ('What date were you born'))

bday = datetime.datetime(year, month, date)
today = datetime.datetime.now()

age = today.year - bday.year

if today.month < bday.month or (today.month == bday.month and today.day < bday.day):
  age -=1

print('You are ', age, ' years old.')

if age < 0:
  print ('You are not born yet')
else:
  if 1946 > bday.year:
    print ('You are old')
  elif 1946 <= bday.year <= 1965:
    print ('You are a boomer')
  elif 1966 <= bday.year <= 1980:
    print ('You are a Gen X')
  elif 1981 <= bday.year <= 1996:
    print ('You are a millenial')
  elif 1997 <= bday.year <= 2012:
    print ('You are a zoomer')
  else:
    print ('You are generation alpha')
