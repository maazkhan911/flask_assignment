from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/" , methods = ['GET' , 'POST'])
def hello_world():
    c = ''
    n1 = ''
    n2 = ''
    data = {}
    if request.method == 'POST':
        try :
            if request.method == 'POST':
                n1 = float(request.form['val1'])
                n2 = float(request.form['val2'])
                opr = request.form.get('opr')
                if opr == '+':
                   c = n1 + n2 
                elif opr == '-':
                   c = n1 - n2 
                elif opr == '*':
                   c = n1 * n2 
                elif opr == '/':
                   c = n1 / n2 

        except:
            pass
    return render_template('index.html' , n1 = n1 , n2 = n2 , c = c)

if __name__ == '__main__':
    app.run(debug = True , port = 1000)