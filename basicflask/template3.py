from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    dic={"hemu":100,"raju":100}
    print(dic)
    return render_template('tmp3.html',index=dic)
if __name__=='__main__':
    app.run(debug=True)
