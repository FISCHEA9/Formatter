from theme import Theme
import subprocess

skipSecondstanza = False
skipDone = False

#skipDone = True; skipSecondstanza = True;

def Formatstanza(txt, eols = ['. ', ', ', '? ', '! ', ': ']):
	# does the bulk of per-stanza edits and formatting
	txt = capitalizeSentences(txt)
	
	# make new list for end of quotes
	eol2 = eols.copy()
	eol2 = [eol[0] + '"' for eol in eol2]
	eols = eols + eol2 # combined list
	
	# remove double spaces
	txt = " ".join(txt.split())
	txt = spellCheck(txt, "i", "I")
	
	# finally, add linebreaks 
	for eol in eols:
		txt = txt.replace(eol, eol + '\n')
	
	# remove any erroneous spaces at start of line
	txt = txt.replace("\n ", "\n")
	
	return txt
def capitalizeSentences(txt):
	# capitalizes first letter after every ! . and ? 
	if not txt[0].upper() == txt[0]: # if it needs capitalized
		txt = assignStrIdx(txt, 0, txt[0].upper(), clr=Theme.capitalized)
	
	for i in range(len(txt)-2):
		sr = txt[i:i+2]
		if (sr == '. ' or sr == '? ' or sr == '! ') and not txt[i+3] == txt[i+3].upper():
			#txt = txt[0:i+2] + txt[i+2].upper() + txt[i+3:] 
			txt = assignStrIdx(txt, i+2, txt[i+2].upper(), clr=Theme.capitalized)
			# I fucked up the indexing here for a whole hour wth
			
	return txt
def spellCheck(txt, word, changeTo):
	# changes all instances of word to changeTo, but checks to make sure 
	#`word` is not a section of another word (scunthorpe check)
	
	# fixes words before a punctuation
	punctuation = ['.', ',', '?', '!', ':', " "]
	clr = Theme.spellChecked
	for p in punctuation: # fixes misspellings after punctuation
		txt = txt.replace(" " + word + p,     clr + " " + changeTo + Theme.default + p)
	if (txt[-(len(word)+1):] == " " + word):# special case, if last few chars are the misspelling
		txt = assignStrIdx(txt, -len(word), changeTo, clr=clr)
	return txt
def assignStrIdx(txt, idx, assignment, clr=Theme.default):
	if idx == -len(assignment): 
		# prevents txt duplication when `assignment` terminates the string
		finality = ""
	else: finality = txt[idx + len(assignment):]
	
	return txt[:idx] + clr + assignment  + Theme.default + finality
def strInputLoop(inputText,lnBrk='',forceUpper = False, minLen=-1,maxLen=-1,validChars=''):
	# runs until a string meets the requirements specified
	bad = True
	while bad:
		bad = False
		print(lnBrk)
		output = input(inputText)
		if forceUpper:
			output = output.upper()
		
		# restart loop if conditions not met, condition failed
		if not(minLen == -1 or len(output) >= minLen):
			print("Input has too few characters\n\
				   minimum length: " + str(minLen) + "\n\
				   length: " + str(len(output)))
			bad = True
		if not(maxLen == -1 or len(output) <= maxLen):
			print("Input has too many characters")
			bad = True
		if not len(validChars) == 0:
			for i in range(len(output)):
				if not output[i] in validChars:
					bad = True
					"Input has invalid characters"
					break
	return output
def 	boolInputLoop(inputText,trues='',falses='',lnBrk='', forceUpper=True):
	# input trues/falses as strings to check for single chars
	# or as [str] to check for whole strings
	bad = True
	while bad:
		print(lnBrk)
		txt = input(inputText)
		if forceUpper:
			txt = txt.upper()
		for check in trues:
			if txt == check:
				return True
		for check in falses:
			if txt == check:
				return False
		print(lnBrk + "Invalid selection")







lnBrk = "\n\n----------------------------------------------------------------------\n\n"
## program start
print(Theme.default + "poemFormatter 0.2.0.1" )

# cmd setup
colorScheme= strInputLoop(\
			   "Type two characters so that the first is the background color\
				\nand the second is the color of the text (i.e. 7d is white\
				\nbackground and light purple text):\n\
			    \n0 = Black       8 = Gray\
			    \n1 = Blue        9 = Light Blue\
			    \n2 = Green       A = Light Green\
			    \n3 = Aqua        B = Light Aqua\
			    \n4 = Red         C = Light Red\
			    \n5 = Purple      D = Light Purple\
			    \n6 = Yellow      E = Light Yellow\
			    \n7 = White       F = Bright White\n\n",\
				minLen=2,maxLen=2,validChars="0123456789ABCDEF",forceUpper = True,lnBrk=lnBrk)
Theme.setAttr("default", Theme.TwoCharScheme(colorScheme))
deft = Theme.default
print(deft)
subprocess.run("color " + colorScheme, shell=True)

# error color setup
if boolInputLoop("This program changes the color of text that is autocapitalized\
				 \nor autocorrected. Would you like to change the default colors? (y/n):\n",\
				 lnBrk=lnBrk,trues='Y',falses='N',forceUpper=True):
	 Theme.setAttr("capitalized", Theme.TwoCharScheme(\
				    strInputLoop("Type one character from the previous list to change autocapitalize text color\
					\nor two characters to change highlight and color (similar to previous default theme):\n",\
					minLen=1,maxLen=2,validChars="0123456789ABCDEF",forceUpper = True,lnBrk=lnBrk)))
	 Theme.setAttr("spellChecked", Theme.TwoCharScheme(\
					strInputLoop("Type one character from the previous list to change spell check text color\
					\nor two characters to change highlight and color (similar to previous default theme):\n",\
					minLen=1,maxLen=2,validChars="0123456789ABCDEF",forceUpper = True,lnBrk=lnBrk)))

# collect and format individual stanzas
done = False
stanzas = []
while not done:
	curstanza = input(deft + "\nInput unformatted stanza: \n\n")
	
	curstanza = Formatstanza(curstanza)
	stanzas.append(curstanza)
	
	print("\n\n\nformatted stanza:" + lnBrk + curstanza + lnBrk)
	
	if skipSecondstanza:
		break
	done = boolInputLoop("\nWould you like to format another stanza? (y/n)\n",trues='N',falses='Y')
		
	
	
# print final poem
finalString = "\n\n".join(stanzas)
print("\n\n\n\nfinal:" + lnBrk + finalString + lnBrk)

strInputLoop("\n\nScript concluded. Type \"done\" to close program.\n", minLen=4, maxLen=5, validChars='done') # mild typos allowed