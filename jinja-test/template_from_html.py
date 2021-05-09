from jinja2 import Template  # pip install jinja2

with open('template.html') as file_:
    template = Template(file_.read())

text = template.render(name='John')
pass