from jinja2 import Template
from src.bingo import comprobarCarton

template = Template(open('plantilla.j2').read())

file = open("carton.html", "w")
file.write(template.render(carton = comprobarCarton()))
file.close()
print("Generado \"carton.html\".")