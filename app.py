from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Hello")

@app.route("/customise")
def customise():
    if request.method == 'POST':
       focus_time = request.form.get('focus_time')
       break_intervals = request.form.get('break_intervals')
       break_duration = request.form.get('break_duration')
    return render_template("customise.html", title="Customise")

@app.route("/focus")
def focus():
    if request.method == 'POST':
       x = int(request.form.get('focus_time')) * 60
       y = int(request.form.get('break_duration')) * 60
       z = int(request.form.get('creak_intervlas'))

       for i in range(z):
           return (f"Cycle {i+1} - Focus for {x/60} minutes")
           time.sleep(x)
           return (f"Take a break for {y/60} minutes")
           time.sleep(y)

       return "Focus-break cycle completed."
    else:
       return render_template("focus.html",title="Focus")
    
    
@app.route("/about")
def about():
    return render_template("aboutus.html", title="About us")