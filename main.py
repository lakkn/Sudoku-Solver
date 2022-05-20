from flask import Flask, render_template, request, url_for, flash, redirect
from solver import *

app = Flask(__name__)

@app.route('/', methods=('GET','POST'))
def index():
  numbers = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
  if request.method == "POST":
    for i in range(0,81):
      number = request.form[str(i)]
      if (not number) or ((number != '1') and (number != '2') and (number != '3') and (number != '4') and (number != '5') and (number != '6') and (number != '7') and (number != '8') and (number != '9')):
        numbers[i] = '0'
      else:
        numbers[i] = number
    numberstr = [[],[],[],[],[],[],[],[],[]]
    for i in range(0,81):
      numberstr[int(i/9)].append(int(numbers[i]))
    print(numberstr)
    solved = run_solver(numberstr)
    for i in range(0,9):
      for j in range(0,9):
        numbers[i*9+j] = str(solved[i][j])
    return render_template('index.html',values=numbers)
    
      
  return render_template('index.html',values=numbers)

app.run(host='0.0.0.0', port=81)