import os
import time
import string
import pprint
pp = pprint.PrettyPrinter(indent=4)
from math import factorial as fac
import itertools
import requests
import json

def getPassList():   
  unsolvedPass = ""
  while unsolvedPass.count("_") == 0:
    print("Enter password with underscores to represent unknown values:")
    unsolvedPass = input()
    if unsolvedPass.count("_") == 0:
      print("Invalid input, enter a password with unknown values")
      print("")
    else:
      passList = list(unsolvedPass)
      return passList

def getPossibleValues():
  print("Chose a choice below to enter the possibilities for unknown values or enter them without spaces.")
  print("Choices: \n{1} - lowercase\n{2} - uppercase\n{3} - numbers 0-9\n{4} - upper + lowercase\n{5} - alphanumeric")
  valueTypes = input("Enter choice or custom values: ")

  if valueTypes == "{1}":
    return string.ascii_lowercase
  elif valueTypes == "{2}":
    return string.ascii_uppercase
  elif valueTypes == "{3}":
    return string.digits
  elif valueTypes == "{4}":
    return string.ascii_letters
  elif valueTypes == "{5}":
    return string.ascii_lowercase + string.ascii_uppercase + string.digits
  else:
    return valueTypes
  
def isRepAllowed():
  allowed = "invalid"
  while allowed == "invalid":
    try:
      allowed = input("Can the unknown values repeat? y/n: ").lower()
    except:
      print("Invalid input, please try again")
      print("")
      time.sleep(0.5)
    else:
      if allowed == "y" or allowed == "yes":
        return True 
      elif allowed == "n" or allowed == "no":
        return False 
      else:
        print("Invalid input, please try again")
        print("")
        allowed = "invalid"
        time.sleep(0.5)

def getNPerms(passList, repAllowed, possibleValues):
  setLength = len(possibleValues)
  nUnknown = passList.count("_")
  if repAllowed:
    nPerms = setLength ** nUnknown
  else: 
    nPerms = int(fac(setLength)/fac(setLength-nUnknown))
  print(f"There will be {nPerms} possible permutations")
  return nPerms
    
def calPossiblePass(passList, repAllowed, possibleValues, nPerms):
  originalPassList = passList.copy()
  underscoreAmount = passList.count("_")
  if repAllowed:
    perms = [p for p in itertools.product(possibleValues, repeat=underscoreAmount)]
  else:
    perms = list(itertools.permutations(possibleValues, underscoreAmount))
  allPerms = []
  for perm in perms:
    permString = ''.join(perm)
    permIndex = 0
    for count, value in enumerate(passList):
      if value == "_":
        passList[count] = permString[permIndex]
        permIndex = permIndex + 1
    allPerms.append(''.join(passList))
    passList = originalPassList.copy()
  return allPerms
  
def createGist(perms):
  gistKey = os.environ['gistKey']
  allPermsAsString = ', '.join(perms)
  gistTitle = input("Enter the name for the gist: ")
  query_url = "https://api.github.com/gists"
  data = {
    "public": False,
    "files": {
        gistTitle: {
            "content": allPermsAsString
        },
    }
}
  headers = {'Authorization': f'token {gistKey}'}
  r = requests.post(query_url, headers=headers, data=json.dumps(data))
  myGist=r.json()
  print("Alright, gist created, thanks.")
  #pp.pprint(myGist)
  #breakpoint()
  print(f"Gist url: {myGist['html_url']}")
  print(f"Gist raw url: {myGist['files'][gistTitle]['raw_url']}")
  time.sleep(0.5)
  print("")

def getGoAgain():
  goAgain = "invalid"
  while goAgain == "invalid":
    goAgain = input("(y/n) Do you want to calculate more passwords?: ").lower()
    if goAgain == "y" or goAgain == "yes":
      print("")
      return True
    elif goAgain == "n" or goAgain == "no":
      print("")
      return False
    else:
      goAgain == "invalid"
      print("Invalid input, try again")
      print("")

def generatePassword():
  generatePassword = "invalid"
  while generatePassword == "invalid":
    generatePassword = input("(y/n) Are you sure you want to calculate the passwords?: ").lower()
    if generatePassword == "y" or generatePassword == "yes":
      print("")
      return True
    elif generatePassword == "n" or generatePassword == "no":
      print("")
      return False
    else:
      generatePassword == "invalid"
      print("Invalid input, try again")
      print("")



my_secret = os.environ['gistKey']
my_secret = os.environ['gistKey']






'''Tp7__m'''
