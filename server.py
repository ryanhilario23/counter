from flask import Flask,render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ninjaskeyisashurikens'
    
@app.route('/', methods=['POST']) 
def counter_page():
    number = 0
    viewing = number + 1 
    print(viewing)
    return render_template('index.html', numbers = viewing)

@app.route('/up')
def up_the_counter():
    print('up')
    return redirect('/')

app.route('/destroy_session')
def full_restart():
    return redirect('/')

# if 'key_name' in session:
#     print('key exist!')
# else:
#     print('key "key_name" does NOT exist')

if __name__=="__main__":
    app.run(debug=True)