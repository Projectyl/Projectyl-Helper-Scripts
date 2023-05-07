#!/bin/python

from multiprocessing import Pool
import csv
import requests as requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import re


header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}

def checkDate(oldDate):
    return datetime.today() < datetime.strptime(oldDate, '%d-%m-%Y')


def check_IITH(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('a', string=re.compile("SURE")):
        year = tag.findNext('h5').text.split()[-1]
        if year.isnumeric() and int(year) > int(oldDate.split('-')[-1]):
            print ("IIT-Hyderabad:", year, tag.text)
            print ("https://www.iith.ac.in/"+tag['href'])
            return


def check_IITRP(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('a', string=re.compile("internship")):
        year = int(oldDate.split('-')[-1]) + 1
        if str(year) in tag.text:
            print ("IIT-Ropar:", year, tag.text)
            print (tag['href'])
            return


def check_IOPB(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('a', string=re.compile("Summer Student Visiting Programme")):
        year = int(oldDate.split('-')[-1]) + 1
        if str(year) in tag.text:
            print ("IOPB:", year, tag.text)
            print (tag['href'])
            return


def check_SINP(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll(string=re.compile("Summer Students' Programme")):
        year = int(oldDate.split('-')[-1]) + 1
        if str(year) in tag.text:
            print ("SINP:", year, tag.text)
            print (url)
            return
    

def check_SNBNCBS(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll(string=re.compile("Summer Research Programme")):
        year = int(oldDate.split('-')[-1]) + 1
        if str(year) in tag.text:
            print ("SINP:", year, tag.text)
            print ("https://www.bose.res.in/" + tag.findNext('a', string="Advertisement")['href'])
            return
    

def check_NISER(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('a', string=re.compile("Summer Project Programme")):
        year = int(oldDate.split('-')[-1]) + 1
        if str(year) in tag.text:
            print ("NISER:", year, tag.text)
            print (tag['href'])
            return


def check_IUAC(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('a', string=re.compile("Summer Programme")):
        year = int(oldDate.split('-')[-1]) + 1
        if str(year) in tag.text:
            print ("IUAC:", year, tag.text.strip())
            print (tag['href'])
            return
    
    
def check_PRL(url, oldDate):
    year = int(oldDate.split('-')[-1]) + 1
    for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('a'):
        if str(year) in tag.text and "Summer Internship Programme" in tag.text:
            print ("PRL:", year, tag.text.strip())
            print (tag['href'])
            return

    
def check_NITM(url, oldDate):
    year = int(oldDate.split('-')[-1]) + 1
    for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('a'):
        if str(year) in tag.text and "Summer Internship Program" in tag.text:
            print ("NIT Meghalaya:", year, tag.text.strip())
            print (tag['href'])
            return


def check_IITBh(url, oldDate):
    year = int(oldDate.split('-')[-1]) + 1
    for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('a'):
        if str(year) in tag.text and "Summer Internship" in tag.text:
            print ("IIT Bhubaneswar:", year, tag.text.strip())
            print (tag['href'])
            return

    
def check_JNC(url, oldDate):
    year = int(oldDate.split('-')[-1]) + 1
    for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('a'):
        if str(year) in tag.text and "SRFP" in tag.text:
            print ("JNCASR:", year, tag.text.strip())
            print (tag['href'])
            return

def check_IISERK(url, oldDate):
    year = int(oldDate.split('-')[-1]) + 1
    for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('big'):
        if str(year) in tag.text:
            print ("IISER Kolkata:", year, tag.text.strip())
            print (url)
            return


def check_IMSC(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('a'):
        if "Summer Research Programme" in tag.text:
            print ("IMSC:", tag.text)
            return


def check_IIITA(url, oldDate):
    year = int(oldDate.split('-')[-1]) + 1
    for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('p'):
        if str(year) in tag.text and "Summer Internship Program" in tag.text:
            print ("IIIT Allahabad:", year, tag.text.strip())
            print (url)
            return


def check_IIPE(url, oldDate):
    year = int(oldDate.split('-')[-1]) + 1
    for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('a'):
        if str(year) in tag.text and "SUMMER INTERNSHIP PROGRAMME" in tag.text:
            print ("IIPE Vishakhapatnam:", year, tag.text.strip())
            print (tag['href'])
            return


def check_IUCAA(url, oldDate):
    year = int(oldDate.split('-')[-1]) + 1
    for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('div', attrs={'class': "bt-caption"}):
        if "Vacation Students' Programme" in tag.text and str(year) in tag.findNext('p').text:
            print ("IUCAA:", year, tag.text.strip())
            print ("https://www.iucaa.in" + tag.findPrevious('a')['href'])
            return


def check_VNIT(url, oldDate):
    year = int(oldDate.split('-')[-1]) + 1
    for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('a'):
        if str(year) in tag.text and "Summer Internship Program" in tag.text:
            print ("VNIT Nagpur:", year, tag.text.strip())
            print (tag['href'])
            return


def check_NITTRC(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('a'):
        if "Summer" in tag.text:
            print ("NIT Trichy:", tag.text)
            print (tag['href'])
            return


def check_IITM(url, oldDate):
    year = int(oldDate.split('-')[-1]) + 1
    for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('a'):
        if str(year) in tag.text and "Summer Fellowship Programme" in tag.text:
            print ("IIT Madras:", year, tag.text.strip())
            print (url + tag['href'])
            return


def check_IITPKD(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('a'):
        if "Summer@IIT Palakkad" in tag.text:
            print ("IIT Palakkad:", tag.text)
            return


def check_IIA(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('i'):
        if "Last updated on" in tag.text and datetime.strptime(tag.next_sibling, '%B %d, %Y') > datetime.strptime(oldDate, '%d-%m-%Y'):
            print ("IIA:", "Last updated on", tag.next_sibling)
            return


def check_IITG(url, oldDate):
    nextYear = str(int(oldDate.split('-')[-1]) + 1)
    testUrl = url + "srip-" + nextYear + "/"
    if requests.get(testUrl).status_code != 404:
        heading = bs(requests.get(testUrl).content,"lxml").find('h2').text
        print ("IIT Gandhinagar:", heading)
        return


def check_IITRRK(url, oldDate):
    print (requests.get(url).content)
    for tag in bs(requests.get(url).content,"lxml").findAll('strong'):
        if "Application Deadline" in tag.text:
            print ("IIT Roorkee:", tag.text)
            return


def check_NCRA(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('h2'):
        if "Visiting Students' Research Programme" in tag.text:
            print ("NCRA:", tag.text.strip())
            return


def check_TIFR(url, oldDate):
    newYear = int(oldDate.split('-')[-1]) + 1
    for tag in bs(requests.get(url).content,"lxml").findAll('strong'):
        if "VSRP-" + str(newYear) in tag.text:
            print ("TIFR:", tag.text.strip())
            return


def check_IITKNP(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('p'):
        if "Opening of Online Registration" in tag.text and datetime.strptime(tag.findNext('strong').text, '%B %d, %Y') > datetime.strptime(oldDate, '%d-%m-%Y'):
            print ("IIT Kanpur:", tag.text.strip())
            return


def check_IAS(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('h1'):
        if "SUMMER RESEARCH FELLOWSHIP" in tag.text:
            print ("IAS:", tag.text.strip(), tag.findNext('a')['href'])
            return


def check_IITMND(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('a'):
        if "Summer Internship" in tag.text:
            print ("IAS:", tag.text.strip(), "https://www.iitmandi.ac.in/" + tag['href'])
            return


def check_IISERTVM(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('h4'):
        if "Summer Visiting Students" in tag.text:
            newYear = tag.text.split()[-1]
            if newYear > oldDate.split('-')[-1]:
                print ("IISER TVM:", tag.text.strip())
            return


def check_bose(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('a'):
        if "Advertisement for summer trainees" in tag.text:
            newYear = tag.text.split()[-1]
            if newYear > oldDate.split('-')[-1]:
                print ("Bose Institute:", tag.text.strip(), tag['href'])
            return


def check_IISERPN(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('h1'):
        if "Summer Student Programme" in tag.text:
            newYear = tag.text.split()[-1]
            if newYear > oldDate.split('-')[-1]:
                print ("IISER Pune:", tag.text.strip(), url)
            return


def check_IITJ(url, oldDate):
    print (requests.get(url).content)
    for tag in bs(requests.get(url).content,"lxml").findAll('h2'):
        if "Research Internship" in tag.text:
            newYear = tag.text.split()[1]
            if newYear > oldDate.split('-')[-1]:
                print ("IIT Jammu:", tag.text.strip(), url)
                return


def check_IISERM(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('a'):
        if "Summer Research" in tag.text:
            print ("IISER Mohali:", tag.text.strip(), tag['href'])
            return


def check_IITD(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('h4'):
        if "SUMMER RESEARCH FELLOWSHIP" in tag.text:
            print ("IIT Delhi:", tag.text.strip(), tag.findNext('a')['href'])
            return


def check_IIITK(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('strong'):
        if "Summer Internship" in tag.text:
            newYear = tag.text.split()[1]
            if newYear > oldDate.split('-')[-1]:
                print ("IIIT Kottayam:", tag.text.strip())
                return


def check_IISERBH(url, oldDate):
    for tag in bs(requests.get(url, headers=header).content,"lxml").findAll('td'):
        if "Summer Internship  Program" in tag.text:
            newYear = tag.text.split()[-1]
            if newYear > oldDate.split('-')[-1]:
                print ("IISER Bhopal:", tag.text.strip(), tag.findNext('a')['href'])
                return


def check_ICTS(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('td'):
        if "Summer Internship  Program" in tag.text:
            newYear = tag.text.split()[-1]
            if newYear > oldDate.split('-')[-1]:
                print ("IISER Bhopal:", tag.text.strip(), tag.findNext('a')['href'])
                return


def check_NITRK(url, oldDate):
    for tag in bs(requests.get(url).content,"lxml").findAll('span'):
        if "Apply Online" in tag.text:
            print ("NIT Rourkela:", url)
            return


def check_IIST(url, oldDate):
    oldYear = int(oldDate.split('-')[-1])
    if str(oldYear + 1) in str(requests.get(url).content):
        print ("IIST:", url)
        return


website_info = csv.reader(open('internship_website_info.csv', 'r'))
for institute,url,oldDate in website_info:
    if checkDate(oldDate):
        continue
    if institute == "IIT Hyderabad":
        check_IITH(url, oldDate)
    if institute == "IIT Ropar":
        check_IITRP(url, oldDate)
    if institute == "IOP Bhubhaneswar":
        check_IOPB(url, oldDate)
    if institute == "SINP Kolkata":
        check_SINP(url, oldDate)
    if institute == "SNBNCB Kolkata":
        check_SNBNCBS(url, oldDate)
    if institute == "NISER Bhubaneswar":
        check_NISER(url, oldDate)
    if institute == "IUAC New Delhi":
        check_IUAC(url, oldDate)
    if institute == "PRL Ahmedabad":
        check_PRL(url, oldDate)
    if institute == "NIT Meghalaya":
        check_NITM(url, oldDate)
    if institute == "IIT Bhubaneswar":
        check_IITBh(url, oldDate)
    if institute == "JNCASR Bangalore":
        check_JNC(url, oldDate)
    if institute == "IISER Kolkata":
        check_IISERK(url, oldDate)
    if institute == "IMSC Chennai":
        check_IMSC(url, oldDate)
    if institute == "IIIT Allahabad":
        check_IIITA(url, oldDate)
    if institute == "IIPE Andhra Pradesh":
        check_IIPE(url, oldDate)
    if institute == "IUCAA Pune":
        check_IUCAA(url, oldDate)
    if institute == "VNIT Nagpur":
        check_VNIT(url, oldDate)
    if institute == "NIT Trichy":
        check_NITTRC(url, oldDate)
    if institute == "IIT Madras":
        check_IITM(url, oldDate)
    if institute == "IIT Palakkad":
        check_IITPKD(url, oldDate)
    if institute == "IIA Bangalore":
        check_IIA(url, oldDate)
    if institute == "IIT Gandhinagar":
        check_IITG(url, oldDate)
    if institute == "NCRA Pune":
        check_NCRA(url, oldDate)
    if institute == "TIFR":
        check_TIFR(url, oldDate)
    if institute == "IIT Kanpur":
        check_IITKNP(url, oldDate)
    if institute == "Science Academies":
        check_IAS(url, oldDate)
    if institute == "IIT Mandi":
        check_IITMND(url, oldDate)
    if institute == "IISER Thiruvananthapuram":
        check_IISERTVM(url, oldDate)
    if institute == "Bose Institute Kolkata":
        check_bose(url, oldDate)
    if institute == "IISER Pune":
        check_IISERPN(url, oldDate)
    if institute == "IISER Mohali":
        check_IISERM(url, oldDate)
    if institute == "IIT Delhi":
        check_IITD(url, oldDate)
    if institute == "IIIT Kottayam":
        check_IIITK(url, oldDate)
    if institute == "NIT Rourkela":
        check_NITRK(url, oldDate)
    if institute == "IIST": 
        check_IIST(url, oldDate)

    # if institute == "IISER Bhopal":
    #     check_IISERBH(url, oldDate)
    # if institute == "NIT Hamirpur":
    #     check_IISERBH(url, oldDate)
    # if institute == "IISER Berhampur":
    #     check_JNC(url, oldDate)
    # if institute == "IIT Jammu":
    #     check_IITJ(url, oldDate)
    # if institute == "IIT KGP":
    #     check_JNC(url, oldDate)
    # if institute == "ICTS Bangalore":
    #     check_ICTS(url, oldDate)
    ##### Website of ICTS was down
    # if institute == "IIT Roorkee":
    #     check_IITRRK(url, oldDate)
