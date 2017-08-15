import re

#FILES TO MANIPULATE

inputFile = open("input_words.txt","r") #setting up our input file to retrieve strings from
outputFile = open("extracted_words.txt","w") #output file to place the words that match out regexs

inputText = inputFile.read() #all the text that was inside the input file
inputFile.close() #closing inputfile to save resources, we're done with it


#REGULAR EXPRESSIONS

alphaNum = re.findall(r'\s[0-9|a-z|A-Z]+\s', inputText)#retrieves all alphanumeric words with no symbols

techEmail = re.findall(r'[\s|\n][a-z|0-9]+@[a-z|0-9]*[\.]?latech\.edu', inputText)#retrieves all valid Tech email addresses

cIdents = re.findall(r'\s[_|a-z|A-Z]+\s', inputText)#retrieves all valid c identifiers


#PRINTING RESULTS TO OUTPUT FILE

outputFile.write("All alphanumeric words with no symbols.\n ")
outputFile.write("----------------------------------------\n")
outputFile.write(repr(alphaNum) + "\n\n") #using repr to give the string represenation of the value alphaNum

outputFile.write("All valid LaTech e-mail addresses.\n")
outputFile.write("----------------------------------------\n")
outputFile.write(repr(techEmail) + "\n\n")

outputFile.write("All valid identifier names in C.\n")
outputFile.write("----------------------------------------\n")
outputFile.write(repr(cIdents))

outputFile.close() #closing outputFile for good measure


#note: can't seem to rid of the words with the "|" symbol in them