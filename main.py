from flask import Flask,render_template
#create the flask app
app=Flask(__name__)
#get the location
def map():
    #latitude and longtitude
    lat=7.23
    long=3.55
    return render_template('index,html',lat=lat,long=long)
if __name__=='__main__':
    app.run(Debug=True)