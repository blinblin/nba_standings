import sys
import urllib
import string
import re

def find_exact_str(str,list):
  """returns the index of the str in a list"""
  for i in range(len(list)):
    if list[i] == str:
      return i
  return -1

def find_exact_str_back(item,list):
  """returns the index of the str in a list starting from the back"""
  for i in range(len(list)-1,-1,-1):
    if list[i] == item:
      return i
  return -1
  
def find_team(name,list):
  """looks for the name of a team in a list"""
  if len(name) < 4:
    return -1
  for i in range(len(list)):
    if name in list[i]:
      return i
  return -1
  
def clean_str(x,y):
  """given a string x, removes chars in string y from x"""
  return string.translate(x,None,y)
  
def conv_date(x):
  """converts a string into useful date information"""
  return x.split('y')

def remove_space(x):
  """removes spaces in string x"""
  return x.replace(" ","")
  
url = urllib.urlopen("http://www.nba.com/standings/team_record_comparison/conferenceNew_Std_Div.html")
html = url.read()


timestamp = re.findall('<div id="timestamp">(.*)</div>2',html,re.DOTALL)
time = re.findall('created: (.*)',timestamp[0])

#cleans up html string into usable list
c = html.replace("\n","`")
c = c.replace("\t","`")
c = clean_str(c,'/')
c = c.replace('<td>','')
c = c.lower()
d = c.split('`')

d = map(remove_space,d)
#removes the bottom half of the list we don't use
f = d[:find_exact_str_back('<tr>',d)]
#removes the top half of the list we don't use
e = f[find_exact_str('<divid="timestamp">',f):]	

print("Welcome to my NBA Team Record Lookup")
print("Updated on"+time[0])
query = "Enter the city or name of a team or q to quit:"
input_var = raw_input(query)
while input_var != "q" :
  input = input_var.replace(' ','').lower()
  index = find_team(input,e)
  if index != -1:
    print "That team has "+str(e[index+1])+" wins and "+str(e[index+2])+" loses."
  else:
    print "Sorry, team not found"
  input_var = raw_input(query)
url.close()

