from colorama import Fore, Back, Style

class Theme:
	# base colors
	default = Fore.GREEN + Back.BLACK # default condition
	capitalized = Fore.LIGHTYELLOW_EX # condition for autocapitalized sentence starters
	spellChecked = Fore.LIGHTMAGENTA_EX 
	error = Fore.RED + Back.BLACK # currently unused, but self explanatory
	
	# reset behavior
	reset = Style.RESET_ALL

	@staticmethod
	def clr(txt, color):
		return color + txt + Theme.default
	def hexToCol(hexChar, target=Fore):
	    hexChar = hexChar.upper()
	
	    mapping = {
	        '0': 'BLACK',
	        '1': 'BLUE',
	        '2': 'GREEN',
	        '3': 'CYAN',
	        '4': 'RED',
	        '5': 'MAGENTA',
	        '6': 'YELLOW',
	        '7': 'WHITE',
	        '8': 'LIGHTBLACK_EX',
	        '9': 'LIGHTBLUE_EX',
	        'A': 'LIGHTGREEN_EX',
	        'B': 'LIGHTCYAN_EX',
	        'C': 'LIGHTRED_EX',
	        'D': 'LIGHTMAGENTA_EX',
	        'E': 'LIGHTYELLOW_EX',
	        'F': 'LIGHTWHITE_EX',
	    }
	    return getattr(target, mapping.get(hexChar, 'WHITE'))
	def TwoCharScheme(chars):
		if not len(chars) == 2:
			return Theme.hexToCol(chars[0], Fore)
		return Theme.hexToCol(chars[0],Back) + Theme.hexToCol(chars[1],Fore)
	@classmethod
	def setAttr(cls, attrName, value):
		if hasattr(cls, attrName):
			setattr(cls, attrName, value)
		else:
			raise AttributeError(f"{attrName} is not a valid Theme attribute")