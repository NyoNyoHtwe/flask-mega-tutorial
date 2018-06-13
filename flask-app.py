from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

     <html>
     <head><title>This is my flask app</title></head>
     <body><h1>Hello!</h1>
     <p>Good enening</p>
     </body></html>

if __name__ == "__main__":
    
  app.run(debug=True)
