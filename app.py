from flask import Flask ,render_template,jsonify    

app = Flask(__name__)
JOBS=[
  {
    'id':1,
    'job_role':'Data Scientist',
    'location':'Delhi, India',
    'salary':'Rs.1200000 LPA'
  },
  {
    'id':2,
    'job_role':'Data Analyst',
    'location':'Delhi, India',
    'salary':'Rs.1000000 LPA'
  },
  {
    'id':3,
    'job_role':'Fullstack Developer',
    'location':'Delhi, India',
    'salary':'Rs.1300000 LPA'
  },
]

@app.route("/")
def hello():
  return render_template('home.html',jobs=JOBS)
@app.route("/jobs")
def to_list_jobs():
  return jsonify(JOBS)
print(__name__)
if __name__ == '__main__':
  app.run(host='localhost', debug=True)
