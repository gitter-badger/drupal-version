#!/usr/bin/python
import urllib2
import fileinput
import sys

lines = iter(fileinput.input(["file.dat"]))
print "Prints url drupalversion\n"
for line in lines:
  urlline =  line.strip()
  url = (urlline  + '/CHANGELOG.txt')
  try:
    response = urllib2.urlopen(url)

  except urllib2.HTTPError, err:
     if err.code == 404:
         print "404: Does not exist"
     else:
         print ''
  else:
    lines = response.readlines()
    if 'Drupal' in lines[0]:
      drupal_string = lines[0]
    elif 'Drupal' in lines[1]:
      drupal_string = lines[1]
    else:
      drupal_string = lines[2]

    responses = (urlline + "\t" + drupal_string)
    print responses.strip()
    response.close()
print "\nFinished"
