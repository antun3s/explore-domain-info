#!/usr/bin/env python
# coding: utf-8

import whois
import pydig
import requests
import sys

from datetime import datetime 
from datetime import timedelta

if len(sys.argv) <= 1:
    print('fromdomain2data.py domain.com')
    exit(1)

domain = sys.argv[1] 
print ('Checking info about domain ' + domain + ' ...')
print ('')

# Domain info
w = whois.query( domain )

if w == None:
    print ( 'domains doesn\'t exit') 
    exit()

def get_lefttime(expiration_date):
    today = datetime.now().date()
    timeleft = expiration_date.date() - today
    return timeleft.days

# DNS info
def get_isp(ip):
    ispname = requests.get('http://ip-api.com/json/' + ip).json()['isp']
    # requests.get('http://ip-api.com/json/[ip address]').json()['ip']
    return ispname
def clean_query(query):
    splited = query[0].split()
    util = splited[-1]
    return util

def get_ip(host):
    query = (pydig.query(host,'A'))
    ip = clean_query(query)
    return ip

def get_mx(domain):
    query = pydig.query(domain,'MX')
    mx = clean_query(query)
    if mx == '.':
        mx = domainmx
    return mx

# prepare Domain info
domainowner = w.owner
domainexpirationdate = w.expiration_date.date()
domainlefttime = get_lefttime(w.expiration_date)

# prepare DNS info
domainnsip =  get_ip(w.name_servers[0])
domainnsisp = get_isp(domainnsip)

# prepare Mail info
domainmx = get_mx(domain)
domainmxip = get_ip(domainmx)
domainmxisp = get_isp(domainmxip)

# prepare web info
domainwebip = get_ip(domain)
domainwebisp = get_isp(domainwebip)


# Print datas
print ('# Domain info')
print ('Domains owner:', domainowner )
print ('Expiration date: ', domainexpirationdate )
print ('Days to expires: ', domainlefttime )
print ('')
print ('# DNS info')
print ('DNS Servers:', w.name_servers )
print ('DNS Server IP: ', domainnsip )
print ('DNS Server hosted on: ', domainnsisp)
print ('')
print ('# Mail Server info')
print ('Mail server: ', domainmx)
print ('Mail server IP: ', domainmxip)
print ('Mail server hosted on: ',domainmxisp)
print ('')
print ('# Web Server info')
print ('Web server IP: ', domainwebip)
print ('Web server hosted on: ',domainwebisp)
