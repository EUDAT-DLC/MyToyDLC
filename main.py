from flask import Flask, render_template

app = Flask(__name__)

app.config.update(dict(
    DEBUG=True,
))

@app.route('/', methods=['GET'])
def root():
    return render_template('main.html')

if __name__ == "__main__":
    app.run()
