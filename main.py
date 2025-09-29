# Working with Strings
from pyscript import display, document

def generate_message(e):
    name = document.getElementById('name').value
    age = document.getElementById('age').value
    school = document.getElementById('school').value

    display(f'{name} is currently {age} years old and is studying at {school}')