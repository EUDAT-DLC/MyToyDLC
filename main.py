from flask import Flask, request, render_template
import ipdb

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


# b2drop: manipulate files
# select services to be used
#     shuffling, b2note
# call services on files
# semantic annots via b2note
# visualize version info (registry)
# visualize provenance info
#     triple store @bsc
# push to b2share
# geolocalization for the data/services
