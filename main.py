import functions
goAgain = True

while goAgain == True:
  
  passList = functions.getPassList() 
  possibleValues = functions.getPossibleValues()
  repAllowed = functions.isRepAllowed()
  nPerms = functions.getNPerms(passList, repAllowed, possibleValues)
  
  if functions.generatePassword():
    passwords = functions.calPossiblePass(passList, repAllowed, possibleValues, nPerms)
    uploadGist = input("(y/n) Create Gist?: ").lower()
    if uploadGist == "y":
      functions.createGist(passwords)
    else:
      print("Alright")
      print("")
  goAgain = functions.getGoAgain()
 




  

  
  

  

  
      
  
 #'''Tp7__m'''
