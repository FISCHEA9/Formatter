#text = input("Paste or otherwise input text to be formatted: \n\n")

text = "You like to say \"I'm not involved.\" You refused to come to ANY of our court hearings. Your build your own life while ours was being decided by strangers in rooms we were too young to understand."


texLen = len(text)
texLen = 5
for i in range(texLen-1): # loop over each char
	# reverse order loop, take one off for texLen - 1, take one off because indexing starts at zero
	i = texLen - i - 2 
	
	if (text[i] == "." ) or (text[i] == ","):
		if text[i+1] == "\"":
			#text[i:i+1] = text[i:i+1] + "\n"
			continue
		#else:
			#text.replace(" ", pattern+'\n')


eols = ['. ', '? ', '! ']
eol2 = eols.copy()
eol2 = [eol + '"' for eol in eol2]
eols.append(eol2)
print(eols)
for eol in eols:
	text.replace(eol, eol + '\n')

#text.replace(bsPeriod,".\"\n")
#text.replace(bsCommas,",\"\n")