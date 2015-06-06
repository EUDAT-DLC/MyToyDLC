from flask import Flask, request, render_template

app = Flask(__name__)

app.config.update(dict(
    DEBUG=True,
))

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        file = request.files['file']
        # ipdb.set_trace()
        return file.filename
    else:
        return render_template('main.html')

if __name__ == "__main__":
    app.run()
