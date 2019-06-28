from jobplus.app import create_app
from jobplus.config import DeployType
from flask import render_template
app = create_app(DeployType.Development)


@app.route('/')
def index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
