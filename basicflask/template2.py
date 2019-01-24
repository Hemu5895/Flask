from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    name="hemu"
    sname=['maths','java']
    v=[70,60]
    return render_template('tmp2.html',name=name,sname=sname,v=v)
if __name__=='__main__':
    app.run(debug=True)
