import amino
import asyncio
import pyfiglet

from reportconfigs import aminoreportfxckfunctions
from colored import fore, back, style, attr
attr(0)
print(fore.TURQUOISE_2 + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("AminoReportFxck", font="small"))
print("Report Community C or report User U")

select = input("Select >> ")

if select == "C":
	asyncio.get_event_loop().run_until_complete(aminoreportfxckfunctions.report_community())
	
elif select == "U":
	asyncio.get_event_loop().run_until_complete(aminoreportfxckfunctions.report_user())
