from flask import Flask,render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ninjaskeyisashurikens'
    
@app.route('/', methods=['GET']) 
def counter_page():
    if 'visiting' not in session:
        session['visiting'] = 0
    else:
        session['visiting'] += 1
    return render_template('index.html')

@app.route('/up', methods=['GET'])
def up_the_counter():
    if 'visiting' not in session:
        session['visiting'] = 0
    else:
        session['visiting'] += 1
    return redirect('/')

@app.route('/clear', methods=['GET'])
def full_restart():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)