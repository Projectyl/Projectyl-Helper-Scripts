#!/bin/python

from multiprocessing import Pool
import csv
import requests as requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}

def checkDate(oldDate):
    return datetime.today() < datetime.strptime(oldDate, '%d-%m-%Y')


website_info = csv.reader(open('summerschools_info.csv', 'r'))
for institute,url,oldDate in website_info:
    flag = False
    if checkDate(oldDate):
        continue
    if institute == "IUCAA":
        for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('div'):
            if "Introductory Summer School" in tag.text:
                print ("IUCAA:", tag.text)
                flag = True
                break
        if flag: print (url)
    if institute == "VVidushi":
        for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('a'):
            if "Apply Now" in tag.text:
                print ("Vigyan Vidushi:", tag.findNext('a').text)
                flag = True
                break
        if flag: print (url)
    if institute == "NCRA":
        for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('span', attrs={'class': 'summary'}):
            if "Radio Astronomy" in tag.text and 'School' in tag.text:
                print ("NCRA:", tag.text)
                flag = True
                break
        if flag: print (url)
    if institute == "ARIES":
        for tag in bs(requests.get(url, headers=header, verify=False).content,"lxml").findAll('a'):
            if "ARIES Training School" in tag.text:
                print ("ARIES:", tag.text)
                flag = True
                break
        if flag: print (url)
    if institute == "NCBS":
        for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('a'):
            if "Annual Monsoon School" in tag.text:
                print ("NCBS:", tag.text)
                flag = True
                break
        if flag: print (url)
    if institute == "KAAS":
        for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('h4'):
            if "Summer School in Theoretical Physics" in tag.text and int(tag.text.split(' ')[-1]) > int(oldDate.split('-')[-1]):
                print ("KAAS:", tag.text)
                flag = True
                break
        if flag: print (url)
    if institute == "IIAP":
        for tag in bs(requests.get(url, headers=header, verify=False).content,"lxml").findAll('a'):
            if "Summer School" in tag.text:
                print ("IIAP:", tag.text.strip())
                flag = True
                break
        if flag: print (url)
    if institute == "NASA":
        for tag in bs(requests.get(url, headers=header, verify=False).content,"lxml").findAll('h3'):
            if "Heliophysics Summer School" in tag.text:
                print ("NASA:", tag.text.strip() + ":", tag.findNext('a').text.strip())
                flag = True
                break
        if flag: print (url)
    if institute == "Boulder":
        for tag in bs(requests.get(url, headers=header, verify=False).content,"lxml").findAll('h2'):
            if str(int(oldDate.split('-')[-1]) + 1) in tag.text and "School" in tag.text:
                print ("Boulder:", tag.text.strip())
                flag = True
                break
        if flag: print (url)
    if institute == "Perimeter":
        newYear = bs(requests.get(url, headers=header, verify=False).content,"lxml").find('h3').text.split(' ')[0]
        assert newYear.isnumeric()
        if int(newYear) > int(oldDate.split('-')[-1]):
            print ("Perimeter:", bs(requests.get(url, headers=header, verify=False).content,"lxml").find('h3').text.strip())
            print (url)
    if institute == "CAPSS":
        newYear = bs(requests.get(url, headers=header, verify=False).content,"lxml").find('h1').text.split(' ')[1]
        print (newYear)
        assert newYear.isnumeric()
        if int(newYear) > int(oldDate.split('-')[-1]):
            print ("CAPSS:", bs(requests.get(url, headers=header, verify=False).content,"lxml").find('h1').text.strip())
            print (url)
    if institute == "SantaFe":
        for tag in bs(requests.get(url, headers=header, verify=False).content,"lxml").findAll('h3'):
            if "Complex Systems Summer School" in tag.text:
                assert tag.findNext('p').text.split()[-1].isnumeric()
                if int(tag.findNext('p').text.split()[-1]) > int(oldDate.split('-')[-1]):
                    print ("SantaFe:", tag.findNext('p').text.strip())
                flag = True
                break
        if flag: print (url)
    if institute == "ICTP":
        for tag in bs(requests.get(url, headers=header, verify=False).content,"lxml").findAll('a'):
            if "Summer School on Particle Physics" in tag.text:
                assert tag.findNext('small').text.split()[-1].isnumeric()
                if int(tag.findNext('small').text.split()[-1]) > int(oldDate.split('-')[-1]):
                    print ("ICTP:", tag.text.strip(), tag.findNext('small').text.strip())
                flag = True
                break
        if flag: print (url)
    if institute == "Fermi":
        for tag in bs(requests.get(url, headers=header, verify=False).content,"lxml").findAll('a'):
            if tag.text.split(' ')[0] == "Courses" and tag.text.split(' ')[1].isnumeric() and int(tag.text.split(' ')[1]) > int(oldDate.split('-')[-1]):
                print ("Italian Physical Society:", tag.text.strip())
                flag = True
                break
        if flag: print (url)
    if institute == "DKFZ":
        for tag in bs(requests.get(url, headers=header, verify=False).content,"lxml").findAll('a'):
            if "Summer School in Medical Physics" in tag.text:
                print ("DKFZ:", tag.text.strip())
                flag = True
                break
        if flag: print (url)
