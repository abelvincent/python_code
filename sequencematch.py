import difflib
text1=input("enter a string: ")
text2=input("enter 2nd string: ")
rv=difflib.SequenceMatcher(isjunk=None,a=text1,b=text2)
print("similarity: ",rv.ratio()*100,"%")
