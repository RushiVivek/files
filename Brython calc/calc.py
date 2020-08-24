from browser import document as doc
from browser import alert, prompt, html
from math import *
# import math
# alert(dir(math))
# try:
def k(ev):
    l = doc.getElementById("inp")
    l.value += ev.target.text

# def solvefunction(string):
#     stringlist = string.split('=')
#     function = ''
#     function.append('def '+stringlist[1])

def bkspace(ev):
    l = doc.getElementById("inp")
    l.value = l.value[0:-1]

def clear(ev):
    l = doc.getElementById("inp")
    l.value = ''

def showhide(ev): 
    div = doc.getElementById("scientific") 
    if div.style['display'] != "inline-block":  
        div.style['display'] = "inline-block"
        # doc.getElementById('kkk').style['margin-left'] = '0px'
    else:
        div.style['display'] = "none"
        # doc.getElementById('kkk').style['margin-left'] = '0px'

def solve(ev):
    te = doc.getElementById("inp").value
    try:
        doc.getElementById("inp").value = eval(te)
    except Exception as e:
        alert('Syntax Error')
        alert(e)

def p(ev):
    l = doc.getElementById("inp")
    l.value += f'{ev.target.text}('

for i in doc.getElementsByName('common'):
    i.bind('click', k)

for i in doc.getElementsByName('diff'):
    i.bind('click', bkspace)

for i in doc.getElementsByName('clear'):
    i.bind('click', clear)

for i in doc.getElementsByName('sci'):
    i.bind('click', showhide)

for i in doc.getElementsByName('functions'):
    i.bind('click', p)

doc.getElementById('equals').bind('click', solve)
#alert(dir(doc))

# from math import *

# while True:
#     a = input(':')
#     #print(dir(math))
#     alert(eval(a))
# except Exception as e:
#     doc.body.textcontent = f'Syntax Error/n {e}'