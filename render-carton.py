from jinja2 import Template

template = Template(open('plantilla.j2').read())

print(template.render(usuario="Luis", color="rojo"))
print(template.render(usuario="Dagos", color="azul"))