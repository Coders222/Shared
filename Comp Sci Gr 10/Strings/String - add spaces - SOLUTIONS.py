sentence = input ("Enter a sentence: ")

while (sentence.lower () != "done"):
   
   #check if there are extra spaces at the beginning - remove if there are
   while (sentence[0] == " "):
      sentence = sentence [1:]



   firstSpace = sentence.find (" ")

   if (firstSpace == -1):
      print (sentence)
   else:
   
      sentence = sentence [0:firstSpace] + " "  + sentence [firstSpace:]

      lastSpace = sentence.rfind (" ")

      if (lastSpace - 1!= firstSpace):
         sentence = sentence [0:lastSpace] + " "  + sentence [lastSpace:]
      
      print (sentence)
   sentence = input ("Enter a sentence: ")
      


#today is cold, very cold.
#0123456789
##firstspace = 5
##
##today  is cold, very cold.
   
   
