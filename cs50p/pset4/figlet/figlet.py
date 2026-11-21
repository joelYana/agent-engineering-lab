# caso 1: 
# $ python figlet.py 
# Input: hello, world 
# Output: *Frase con una fuente random*

# caso 2: 
# $ python figlet.py -f slant 
# Input: hello, world 
# Output: *Frase con la fuente slant*

# caso 3: 
# $ python figlet.py --font rectangles  
# Input: hello, world 
# Output: *Frase con la fuente rectangles*

# caso 4: 
# $ python figlet.py --a rectangles  
# Invalid usage

# caso 5: 
# $ python figlet.py -f invalid_font
# Invalid usage

import sys
import random
from pyfiglet import Figlet

if len(sys.argv) != 3 and len(sys.argv) != 1:
    sys.exit("Invalid usage")

if len(sys.argv) == 3 and ((sys.argv[1] != '-f' and sys.argv[1] != '--font') or sys.argv[2] not in Figlet().getFonts()):
    sys.exit("Invalid usage")

texto = input("Input: ")

if len(sys.argv) == 3 :
    font_elegido = sys.argv[2]
    f = Figlet(font=font_elegido)
    print(f.renderText(texto))
else:
    fuentes = Figlet().getFonts()
    f = Figlet(font=random.choice(fuentes))
    print(f.renderText(texto))