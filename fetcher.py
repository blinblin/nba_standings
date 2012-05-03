import sys
import urllib
import re
from bs4 import BeautifulSoup

url = urllib.urlopen("http://www.nba.com/standings/team_record_comparison/conferenceNew_Std_Div.html")
html = url.read()

records = {}
soup = BeautifulSoup(html)
even = soup('tr','even')
odd = soup.find_all('tr','odd')
teams = even + odd
for team in teams:
	td_info = team('td')
	wins = td_info[1].string		
	loses = td_info[2].string
	record = (wins,loses)
	city = td_info[0].a.string.lower()
	team_name = td_info[0].a['href'][1:]
	records[city] = record
	records[team_name] = record

timestamp = soup.find(id='timestamp')
timestamp = timestamp.string.strip().split()

print("Welcome to my NBA Team Record Lookup")
print("Last updated on "+timestamp[1]+' '+timestamp[2]+' '+timestamp[3]+' '+timestamp[4]+' '+timestamp[5])	
query = "Enter the city or name of a team or q to quit: "
input_var = raw_input(query)
while input_var != "q" :
  input = input_var.replace(' ','').lower()
  if input in records:
    print "That team has "+records[input][0]+" wins and "+records[input][1]+" loses."
  else:
    print "Sorry, team not found"
  input_var = raw_input(query)
url.close()

