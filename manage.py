from jobplus.app import create_app
from jobplus.config import DeployType

app = create_app(DeployType.Development)


@app.route('/')
def index():
    return "Yoo"


if __name__ == '__main__':
    app.run()
